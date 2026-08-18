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
        has_from = False

        for line in lines:
            line_str = line.strip()
            if not line_str or line_str.startswith("#"):
                continue

            tokens = line_str.split()
            if tokens and tokens[0].upper() == "FROM":
                has_from = True
                parts = [p for p in tokens if not p.startswith("--")]
                if len(parts) >= 2:
                    img_ref = parts[1]
                    if "@sha256:" not in img_ref:
                        image_component = img_ref.split("/")[-1]
                        if ":" not in image_component or image_component.endswith(":latest") or ":latest" in image_component:
                            assert False, f"Elakkan penggunaan tag imej ':latest' atau implisit dalam {filepath}: {line_str}"

            # Semakan keselamatan: larang chmod 777
            assert "chmod 777" not in line_str, f"chmod 777 tidak selamat ditemui dalam {filepath}: {line_str}"

        assert has_from, f"Containerfile {filepath} mesti mengandungi arahan FROM."

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
        assert isinstance(data, dict), f"Manifes kontena {filepath} mestilah kamus (mapping) YAML."

        has_valid_keys = "services" in data or "kind" in data
        assert has_valid_keys, f"Manifes kontena {filepath} mesti mentakrifkan 'services' atau 'kind' yang sah."

        if "version" in data or "services" in data:
            assert "services" in data, f"Fail Docker compose {filepath} mesti mentakrifkan 'services'."
        elif "kind" in data:
            assert data.get("kind") in ["Pod", "Deployment", "Service"], f"Fail Podman/Kube {filepath} mempunyai jenis tidak sah."
