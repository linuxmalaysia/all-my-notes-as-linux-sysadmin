"""Ujian unit untuk tests/unit/ansible.py (pengesah pematuhan buku main Ansible).

Memuatkan modul terus dari cakera supaya ujian ini kekal bebas daripada
penyelesaian laluan modul pytest, dan nama modul tidak berlanggar dengan
pakej 'ansible' pihak ketiga.
"""

import importlib.util
import shutil
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def _load_ansible_module():
    """Muat naik modul tests/unit/ansible.py secara dinamik untuk ujian terasing.

    Returns:
        module: Instans modul ujian ansible yang dimuatkan.
    """
    module_path = REPO_ROOT / "tests" / "unit" / "ansible.py"
    spec = importlib.util.spec_from_file_location("unit_test_target_ansible", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ansible_mod = _load_ansible_module()

pytestmark = pytest.mark.skipif(ansible_mod.yaml is None, reason="PyYAML tidak dipasang")


@pytest.fixture(autouse=True)
def _disable_ansible_playbook_binary(monkeypatch):
    """Memaksa cawangan subproses 'ansible-playbook --syntax-check' dilangkau,
    supaya ujian unit kekal deterministik tanpa bergantung pada binari ansible-playbook."""
    monkeypatch.setattr(shutil, "which", lambda _cmd: None)


def test_get_playbook_files_discovers_expected_patterns(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    expected = [
        "deploy/ansible/site.yml",
        "playbooks/sub/deploy.yaml",
        "docs/playbooks/backup.yml",
    ]
    for rel in expected:
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("- hosts: all\n  tasks: []\n", encoding="utf-8")

    unrelated = tmp_path / "unrelated" / "notes.yml"
    unrelated.parent.mkdir(parents=True, exist_ok=True)
    unrelated.write_text("- hosts: all\n", encoding="utf-8")

    found = ansible_mod.get_playbook_files()

    assert sorted(found) == sorted(expected)
    assert "unrelated/notes.yml" not in found


def test_get_playbook_files_returns_empty_list_when_nothing_matches(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert ansible_mod.get_playbook_files() == []


def test_get_playbook_files_deduplicates_overlapping_glob_matches(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    path = tmp_path / "deploy" / "ansible" / "site.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("- hosts: all\n", encoding="utf-8")

    found = ansible_mod.get_playbook_files()
    assert found == ["deploy/ansible/site.yml"]


def test_ansible_playbook_compliance_accepts_valid_playbook(tmp_path):
    playbook = tmp_path / "valid.yml"
    playbook.write_text(
        "- hosts: all\n  tasks:\n    - name: noop\n      debug:\n        msg: hi\n",
        encoding="utf-8",
    )
    ansible_mod.test_ansible_playbook_compliance(str(playbook))


def test_ansible_playbook_compliance_accepts_import_playbook_directive(tmp_path):
    playbook = tmp_path / "import.yml"
    playbook.write_text("- import_playbook: other.yml\n", encoding="utf-8")
    ansible_mod.test_ansible_playbook_compliance(str(playbook))


def test_ansible_playbook_compliance_rejects_include_playbook_directive(tmp_path):
    playbook = tmp_path / "include.yml"
    playbook.write_text("- include_playbook: other.yml\n", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(hosts|import_playbook)"):
        ansible_mod.test_ansible_playbook_compliance(str(playbook))


def test_ansible_playbook_compliance_rejects_missing_file():
    with pytest.raises(AssertionError, match=r"(does not exist|tidak wujud)"):
        ansible_mod.test_ansible_playbook_compliance("does/not/exist.yml")


def test_ansible_playbook_compliance_rejects_empty_yaml(tmp_path):
    playbook = tmp_path / "empty.yml"
    playbook.write_text("", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(empty or invalid YAML|kosong atau YAML tidak sah)"):
        ansible_mod.test_ansible_playbook_compliance(str(playbook))


def test_ansible_playbook_compliance_rejects_non_list_top_level(tmp_path):
    playbook = tmp_path / "dict.yml"
    playbook.write_text("hosts: all\ntasks: []\n", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(top-level YAML list|senarai play YAML)"):
        ansible_mod.test_ansible_playbook_compliance(str(playbook))


def test_ansible_playbook_compliance_rejects_play_missing_hosts_and_imports(tmp_path):
    playbook = tmp_path / "missing_hosts.yml"
    playbook.write_text(
        "- tasks:\n    - name: noop\n      debug:\n        msg: hi\n",
        encoding="utf-8",
    )
    with pytest.raises(AssertionError) as excinfo:
        ansible_mod.test_ansible_playbook_compliance(str(playbook))
    assert "hosts" in str(excinfo.value)


def test_ansible_playbook_compliance_rejects_non_dict_play_item(tmp_path):
    playbook = tmp_path / "list_of_strings.yml"
    playbook.write_text("- just_a_string\n", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(must be a dictionary|kamus \(dictionary\))"):
        ansible_mod.test_ansible_playbook_compliance(str(playbook))


def test_get_playbook_files_helper_is_used_by_the_parametrized_test_signature():
    """Semakan kewarasan bahawa fungsi get_playbook_files() disambung dengan betul."""
    assert callable(ansible_mod.get_playbook_files)
    assert callable(ansible_mod.test_ansible_playbook_compliance)
