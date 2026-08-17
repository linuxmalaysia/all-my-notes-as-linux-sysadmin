"""Unit tests for Containerfile / Dockerfile security and structure.

Validates Dockerfile/Containerfile files, Podman Quadlet files, and container orchestration
manifests (docker-compose, podman kube) for structural validity and security best practices.
"""

import glob
import os
import pytest

try:
    import yaml
except ImportError:
    yaml = None


def get_container_files():
    """Collect container configuration file paths from the repository.
    
    Returns:
    	list[str]: Sorted, duplicate-free paths excluding files under ``node_modules`` and ``.venv``.
    """
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
    # Filter out node_modules or venv
    files = [f for f in files if "node_modules" not in f and ".venv" not in f]
    return sorted(list(set(files)))


@pytest.mark.parametrize("filepath", get_container_files())
def test_containerfile_security_and_structure(filepath):
    """Verify security standards and structure for container configuration files."""
    assert os.path.exists(filepath), f"Container file missing: {filepath}"

    filename = os.path.basename(filepath).lower()

    if "dockerfile" in filename or "containerfile" in filename:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        assert len(lines) > 0, f"Containerfile {filepath} is empty."
        has_from = any(line.strip().startswith("FROM") for line in lines)
        assert has_from, f"Containerfile {filepath} must contain a FROM instruction."

        for line in lines:
            line_str = line.strip()
            # Security check: forbid chmod 777
            assert "chmod 777" not in line_str, f"Insecure chmod 777 found in {filepath}: {line_str}"
            # Security check: avoid latest tag without pinned image when possible
            if line_str.startswith("FROM"):
                assert not line_str.endswith(":latest"), f"Avoid using ':latest' image tag in {filepath}: {line_str}"

    elif filepath.endswith(".container") or filepath.endswith(".pod"):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        assert len(content.strip()) > 0, f"Quadlet file {filepath} is empty."
        has_valid_header = "[Container]" in content or "[Pod]" in content
        assert has_valid_header, f"Quadlet file {filepath} missing [Container] or [Pod] section header."

        if "[Container]" in content:
            assert "Image=" in content, f"Quadlet container file {filepath} must specify an Image= directive."

    elif filepath.endswith((".yml", ".yaml")):
        if yaml is None:
            pytest.skip("PyYAML not installed, skipping YAML container manifest check.")

        with open(filepath, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        assert data is not None, f"Container manifest {filepath} is empty or invalid YAML."
        if "version" in data or "services" in data:
            assert "services" in data, f"Docker compose file {filepath} must define 'services'."
        elif "kind" in data:
            assert data.get("kind") in ["Pod", "Deployment", "Service"], f"Podman/Kube file {filepath} has invalid kind."
