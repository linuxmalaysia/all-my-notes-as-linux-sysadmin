"""Unit tests for Ansible playbook compliance.

Validates that all Ansible playbooks in the repository are well-formed YAML,
follow expected play/task structures, and comply with standards.
"""

import glob
import os
import shutil
import subprocess
import pytest

try:
    import yaml
except ImportError:
    yaml = None


def get_playbook_files():
    """Retrieve all Ansible playbooks in deploy/ansible, playbooks, and docs/playbooks."""
    patterns = [
        "deploy/ansible/**/*.yml",
        "deploy/ansible/**/*.yaml",
        "playbooks/**/*.yml",
        "playbooks/**/*.yaml",
        "docs/playbooks/**/*.yml",
        "docs/playbooks/**/*.yaml",
    ]
    files = []
    for pattern in patterns:
        files.extend(glob.glob(pattern, recursive=True))
    return sorted(list(set(files)))


@pytest.mark.parametrize("filepath", get_playbook_files())
def test_ansible_playbook_compliance(filepath):
    """Verify Ansible playbook YAML structure, syntax, and compliance."""
    assert os.path.exists(filepath), f"Playbook file does not exist: {filepath}"

    if yaml is None:
        pytest.skip("PyYAML not installed, skipping YAML parsing.")

    with open(filepath, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    assert data is not None, f"Playbook {filepath} is empty or invalid YAML."
    assert isinstance(data, list), f"Playbook {filepath} must be a top-level YAML list of plays."

    for item in data:
        assert isinstance(item, dict), f"Play item in {filepath} must be a dictionary."
        has_hosts_or_import = "hosts" in item or "import_playbook" in item or "include_playbook" in item
        assert has_hosts_or_import, (
            f"Playbook item in {filepath} must specify 'hosts', 'import_playbook', or 'include_playbook'."
        )

    # If ansible-playbook binary is installed, perform syntax check
    if shutil.which("ansible-playbook"):
        res = subprocess.run(
            ["ansible-playbook", "--syntax-check", filepath],
            capture_output=True,
            text=True,
            check=False,
        )
        assert res.returncode == 0, f"Ansible syntax error in {filepath}:\n{res.stderr}"
