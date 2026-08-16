"""Infrastructure tests for Ansible Playbooks, Podman configurations, and Bash scripts.

This module provides test scaffolds that will automatically discover and lint
Ansible YAML files, Podman deployment scripts, and Bash shell scripts when
they are introduced to the repository.
"""

import glob
import os
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
