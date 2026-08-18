"""Ujian unit untuk pematuhan buku main (playbook) Ansible.

Mengesahkan bahawa semua buku main Ansible dalam repositori mempunyai struktur YAML
yang sah, mengikut struktur permainan/tugasan yang dijangkakan, dan mematuhi piawaian.
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
    """Mendapatkan semua fail buku main Ansible dalam deploy/ansible, playbooks, dan docs/playbooks."""
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
    """Mengesahkan struktur YAML, sintaks, dan pematuhan buku main Ansible."""
    assert os.path.exists(filepath), f"Fail buku main tidak wujud: {filepath}"
    assert yaml is not None, "Modul PyYAML diperlukan tetapi tidak dipasang."

    with open(filepath, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    assert data is not None, f"Buku main {filepath} adalah kosong atau YAML tidak sah."
    assert isinstance(data, list), f"Buku main {filepath} mestilah senarai play YAML peringkat atasan."

    for item in data:
        assert isinstance(item, dict), f"Item play dalam {filepath} mestilah kamus (dictionary)."
        has_hosts_or_import = "hosts" in item or "import_playbook" in item or "include_playbook" in item
        assert has_hosts_or_import, (
            f"Item buku main dalam {filepath} mesti menetapkan 'hosts', 'import_playbook', atau 'include_playbook'."
        )

    # Jika binari ansible-playbook dipasang, jalankan semakan sintaks
    if shutil.which("ansible-playbook"):
        res = subprocess.run(
            ["ansible-playbook", "--syntax-check", filepath],
            capture_output=True,
            text=True,
            check=False,
        )
        assert res.returncode == 0, f"Ralat sintaks Ansible dalam {filepath}:\n{res.stderr}"
