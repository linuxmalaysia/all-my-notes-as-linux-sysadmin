"""Infrastructure tests for Ansible Playbooks, Podman configurations, and Bash scripts.

This module provides test scaffolds that will automatically discover and lint
Ansible YAML files, Podman deployment scripts, and Bash shell scripts when
they are introduced to the repository.
"""

import glob
import os
import re
import subprocess

import pytest


def get_bash_scripts():
    """Retrieve all bash scripts in the repository."""
    scripts = glob.glob("**/*.sh", recursive=True)
    return [s for s in scripts if "node_modules" not in s and ".venv" not in s]

def get_playbooks():
    """Retrieve all Ansible playbooks."""
    return glob.glob("playbooks/**/*.yml", recursive=True)

def get_podman_files():
    """Retrieve all Podman YAMLs (if any)."""
    return glob.glob("**/*podman*.yml", recursive=True)

@pytest.mark.parametrize("filepath", get_bash_scripts())
def test_bash_syntax(filepath):
    """Verify Bash script syntax using bash -n."""
    if not os.path.exists(filepath):
        pytest.skip(f"File {filepath} not found.")
        
    # Check syntax (bash -n)
    result = subprocess.run(["bash", "-n", filepath], capture_output=True, text=True, check=False)
    assert result.returncode == 0, f"Syntax error in Bash script {filepath}:\n{result.stderr}"

@pytest.mark.parametrize("filepath", get_playbooks())
def test_ansible_playbook_syntax(filepath):
    """Verify Ansible playbook syntax."""
    if not os.path.exists(filepath):
        pytest.skip(f"File {filepath} not found.")
        
    result = subprocess.run(["ansible-playbook", "--syntax-check", filepath], capture_output=True, text=True, check=False)
    assert result.returncode == 0, f"Ansible syntax error in {filepath}:\n{result.stderr}"

@pytest.mark.parametrize("filepath", get_podman_files())
def test_podman_yaml_syntax(filepath):
    """Verify Podman YAML structure using yamllint."""
    if not os.path.exists(filepath):
        pytest.skip(f"File {filepath} not found.")
        
    result = subprocess.run(["yamllint", filepath], capture_output=True, text=True, check=False)
    assert result.returncode == 0, f"YAML lint error in {filepath}:\n{result.stdout}"

def test_infrastructure_scaffold_exists():
    """Dummy test to ensure the infrastructure test suite runs even if no files exist."""
    assert True

def test_github_pages_workflow_configuration():
    """Pengesahan konfigurasi Direktori Punca (Document Root) html/ dan alur kerja pembinaan semula bagi .github/workflows/static.yml."""
    workflow_path = ".github/workflows/static.yml"
    assert os.path.exists(workflow_path), f"Fail alur kerja {workflow_path} tidak wujud."

    with open(workflow_path, "r", encoding="utf-8") as f:
        content = f.read()

    build_idx = content.find("serve_mkdocs.py --build-only")
    upload_idx = content.find("upload-pages-artifact")

    assert build_idx != -1, "static.yml mesti mengandungi langkah pembinaan semula laman web statik."
    assert upload_idx != -1, "static.yml mesti menggunakan tindakan actions/upload-pages-artifact."
    assert build_idx < upload_idx, \
        "Langkah pembinaan semula (serve_mkdocs.py) MESTI dilaksanakan sebelum langkah muat naik artifak (upload-pages-artifact)."

    upload_section = content[upload_idx:]
    assert "path: 'html'" in upload_section or 'path: "html"' in upload_section or "path: html" in upload_section, \
        "Langkah actions/upload-pages-artifact mesti menetapkan Direktori Punca (Document Root) sasaran ke 'html'."


def _read_static_workflow():
    """Helper: return the raw text content of .github/workflows/static.yml."""
    workflow_path = ".github/workflows/static.yml"
    assert os.path.exists(workflow_path), f"Fail alur kerja {workflow_path} tidak wujud."
    with open(workflow_path, "r", encoding="utf-8") as f:
        return f.read()


def _get_workflow_action_pins(content):
    """Extract (action_ref, commit_sha, version_comment) tuples for every
    'uses:' step in a workflow that is pinned to a full-length commit SHA
    with a trailing version comment, e.g.:
        uses: owner/repo@<40-char-sha> # v1.2.3
    """
    pattern = re.compile(
        r"uses:\s*([\w.\-]+/[\w.\-]+)@([0-9a-fA-F]{40})\s*#\s*(v[\w.\-]+)"
    )
    return pattern.findall(content)


def test_static_workflow_actions_pinned_to_full_commit_sha():
    """Semua langkah 'uses:' dalam static.yml mesti dipaku (pinned) kepada SHA
    komit penuh (40 aksara heksadesimal) berserta anotasi versi, bagi
    mengelakkan serangan rantaian bekalan (supply-chain) menerusi tag terapung."""
    content = _read_static_workflow()

    uses_lines = [line.strip() for line in content.splitlines() if "uses:" in line]
    assert uses_lines, "static.yml mesti mengandungi sekurang-kurangnya satu langkah 'uses:'."

    pins = _get_workflow_action_pins(content)
    assert len(pins) == len(uses_lines), (
        "Setiap langkah 'uses:' dalam static.yml mesti dipaku kepada SHA komit penuh "
        f"(40 hex) dengan komen versi. Dijumpai {len(pins)} daripada {len(uses_lines)} "
        "baris 'uses:' yang sepadan dengan corak tersebut."
    )


def test_setup_uv_action_pinned_to_expected_sha():
    """Regression: astral-sh/setup-uv mesti dipaku kepada SHA komit baharu yang
    dikemas kini dalam PR ini, sementara anotasi versi (v5.3.0) kekal sama."""
    content = _read_static_workflow()
    pins = {action: (sha, version) for action, sha, version in _get_workflow_action_pins(content)}

    assert "astral-sh/setup-uv" in pins, "static.yml mesti menggunakan tindakan astral-sh/setup-uv."
    sha, version = pins["astral-sh/setup-uv"]
    assert sha == "1edb52594c857e2b5b13128931090f0640537287", (
        f"SHA astral-sh/setup-uv tidak sepadan dengan yang dijangka selepas kemas kini PR. Dijumpai: {sha}"
    )
    assert version == "v5.3.0", f"Komen versi astral-sh/setup-uv dijangka 'v5.3.0', dijumpai '{version}'."

    # The SHA that existed prior to this PR must no longer be referenced anywhere.
    old_sha = "f94383a0937a0cbf73cf3ea5a6c965610f135bdf"
    assert old_sha not in content, (
        f"SHA lama astral-sh/setup-uv ({old_sha}) sepatutnya telah digantikan dan "
        "tidak boleh wujud lagi dalam static.yml."
    )


def test_deploy_pages_action_pinned_to_expected_sha():
    """Regression: actions/deploy-pages mesti dipaku kepada SHA komit baharu yang
    dikemas kini dalam PR ini, sementara anotasi versi (v5.0.0) kekal sama."""
    content = _read_static_workflow()
    pins = {action: (sha, version) for action, sha, version in _get_workflow_action_pins(content)}

    assert "actions/deploy-pages" in pins, "static.yml mesti menggunakan tindakan actions/deploy-pages."
    sha, version = pins["actions/deploy-pages"]
    assert sha == "cd2ce8fcbc39b97be8ca5fce6e763baed58fa128", (
        f"SHA actions/deploy-pages tidak sepadan dengan yang dijangka selepas kemas kini PR. Dijumpai: {sha}"
    )
    assert version == "v5.0.0", f"Komen versi actions/deploy-pages dijangka 'v5.0.0', dijumpai '{version}'."

    # The SHA that existed prior to this PR must no longer be referenced anywhere.
    old_sha = "d6db5d410170edc4cdd23101967262f2cc3514a4"
    assert old_sha not in content, (
        f"SHA lama actions/deploy-pages ({old_sha}) sepatutnya telah digantikan dan "
        "tidak boleh wujud lagi dalam static.yml."
    )


def test_static_workflow_action_shas_are_forty_hex_characters():
    """Setiap SHA yang dipaku dalam static.yml mesti tepat 40 aksara heksadesimal
    (panjang penuh SHA-1 Git), bukan bentuk pendek (short SHA) yang tidak selamat."""
    content = _read_static_workflow()
    pins = _get_workflow_action_pins(content)

    for action, sha, _version in pins:
        assert len(sha) == 40, f"SHA bagi {action} sepatutnya 40 aksara, dijumpai {len(sha)} aksara: {sha}"
        assert re.fullmatch(r"[0-9a-fA-F]{40}", sha), f"SHA bagi {action} mengandungi aksara tidak sah: {sha}"


def test_static_workflow_action_pins_are_unique_per_action():
    """Tiada tindakan (action) yang dirujuk lebih daripada sekali dengan SHA yang
    berbeza dalam static.yml, bagi mengelakkan percanggahan pin dalam fail yang sama."""
    content = _read_static_workflow()
    pins = _get_workflow_action_pins(content)

    seen = {}
    for action, sha, _version in pins:
        if action in seen:
            assert seen[action] == sha, f"Tindakan {action} dirujuk dengan SHA yang berbeza dalam static.yml."
        seen[action] = sha
