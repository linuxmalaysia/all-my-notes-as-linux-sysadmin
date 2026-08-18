"""Ujian unit untuk keselamatan dan struktur Containerfile / Dockerfile.

Mengesahkan fail Dockerfile/Containerfile, fail Quadlet Podman, dan manifes
orkestratan kontena (docker-compose, podman kube) untuk kesahan struktur dan amalan terbaik keselamatan.
"""

import glob
import os
import pytest

try:
    import yaml
except ImportError:
    yaml = None


def get_container_files():
    """Mendapatkan semua konfigurasi kontena di seluruh repositori."""
    patterns = [
        "**/Dockerfile*",
        "**/Containerfile*",
        "deploy/**/*.container",
        "deploy/**/*.pod",
        "**/docker-compose*.yml",
        "**/docker-compose*.yaml",
        "deploy/podman/*.yml",
    ]
    files = []
    for pattern in patterns:
        files.extend(glob.glob(pattern, recursive=True))
    files = [f for f in files if "node_modules" not in f and ".venv" not in f]
    return sorted(list(set(files)))


@pytest.mark.parametrize("filepath", get_container_files())
def test_containerfile_security_and_structure(filepath):
    """Mengesahkan piawaian keselamatan dan struktur untuk fail konfigurasi kontena."""
    assert os.path.exists(filepath), f"Fail kontena tidak wujud: {filepath}"

    filename = os.path.basename(filepath).lower()

    if "dockerfile" in filename or "containerfile" in filename:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        assert len(lines) > 0, f"Containerfile {filepath} adalah kosong."
        has_from = any(line.strip().startswith("FROM") for line in lines)
        assert has_from, f"Containerfile {filepath} mesti mengandungi arahan FROM."

        for line in lines:
            line_str = line.strip()
            # Semakan keselamatan: larang chmod 777
            assert "chmod 777" not in line_str, f"Insecure chmod 777 found in {filepath}: {line_str}"

            # Semakan arahan FROM: semak tag imej dan elakkan penggunaan implicit/explicit latest
            if line_str.startswith("FROM"):
                parts = [p for p in line_str.split() if not p.startswith("--")]
                if len(parts) >= 2:
                    img_ref = parts[1]
                    if "@sha256:" not in img_ref:
                        if ":" not in img_ref or img_ref.endswith(":latest") or ":latest" in img_ref:
                            assert False, f"Avoid using ':latest' image tag in {filepath}: {line_str}"

    elif filepath.endswith(".container") or filepath.endswith(".pod"):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        assert len(content.strip()) > 0, f"Fail Quadlet {filepath} adalah kosong."
        has_valid_header = "[Container]" in content or "[Pod]" in content
        assert has_valid_header, f"Fail Quadlet {filepath} kehilangan pengepala seksyen [Container] atau [Pod]."

        if "[Container]" in content:
            assert "Image=" in content, f"Fail kontena Quadlet {filepath} mesti menetapkan arahan Image=."

    elif filepath.endswith((".yml", ".yaml")):
        assert yaml is not None, "Modul PyYAML diperlukan tetapi tidak dipasang."

        with open(filepath, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        assert data is not None, f"Manifes kontena {filepath} adalah kosong atau YAML tidak sah."
        if "version" in data or "services" in data:
            assert "services" in data, f"Fail Docker compose {filepath} mesti mentakrifkan 'services'."
        elif "kind" in data:
            assert data.get("kind") in ["Pod", "Deployment", "Service"], f"Fail Podman/Kube {filepath} mempunyai jenis tidak sah."
