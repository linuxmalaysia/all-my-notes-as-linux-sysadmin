"""Ujian unit untuk tests/unit/containers.py (pengesah keselamatan dan struktur fail kontena)."""

import importlib.util
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def _load_containers_module():
    """Muatkan modul tests/unit/containers.py secara dinamik untuk ujian terasing.

    Returns:
        module: Instans modul ujian kontena yang dimuatkan.
    """
    module_path = REPO_ROOT / "tests" / "unit" / "containers.py"
    spec = importlib.util.spec_from_file_location("unit_test_target_containers", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


containers_mod = _load_containers_module()


# ---------------------------------------------------------------------------
# get_container_files()
# ---------------------------------------------------------------------------

def test_get_container_files_discovers_expected_patterns(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    expected = [
        "Dockerfile",
        "sub/Containerfile.prod",
        "deploy/app.container",
        "deploy/app.pod",
        "docker-compose.yml",
        "deploy/podman/config.yml",
    ]
    for rel in expected:
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("placeholder\n", encoding="utf-8")

    found = containers_mod.get_container_files()

    assert sorted(found) == sorted(expected)


def test_get_container_files_excludes_node_modules_and_venv(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    excluded = [
        "node_modules/pkg/Dockerfile",
        ".venv/lib/Dockerfile",
    ]
    for rel in excluded:
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("FROM scratch\n", encoding="utf-8")

    included = tmp_path / "Dockerfile"
    included.write_text("FROM scratch\n", encoding="utf-8")

    found = containers_mod.get_container_files()

    assert found == ["Dockerfile"]


def test_get_container_files_returns_empty_list_when_nothing_matches(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert containers_mod.get_container_files() == []


# ---------------------------------------------------------------------------
# test_containerfile_security_and_structure() - Dockerfile / Containerfile
# ---------------------------------------------------------------------------

def test_containerfile_compliance_accepts_valid_dockerfile(tmp_path):
    dockerfile = tmp_path / "Dockerfile"
    dockerfile.write_text("FROM python:3.12-slim\nRUN pip install foo\n", encoding="utf-8")
    containers_mod.test_containerfile_security_and_structure(str(dockerfile))


def test_containerfile_compliance_rejects_missing_file():
    with pytest.raises(AssertionError, match=r"(Container file missing|tidak wujud)"):
        containers_mod.test_containerfile_security_and_structure("no/such/Dockerfile")


def test_containerfile_compliance_rejects_empty_dockerfile(tmp_path):
    dockerfile = tmp_path / "Dockerfile"
    dockerfile.write_text("", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(is empty|adalah kosong)"):
        containers_mod.test_containerfile_security_and_structure(str(dockerfile))


def test_containerfile_compliance_rejects_missing_from_instruction(tmp_path):
    dockerfile = tmp_path / "Dockerfile"
    dockerfile.write_text("RUN echo hello\n", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(FROM instruction|arahan FROM)"):
        containers_mod.test_containerfile_security_and_structure(str(dockerfile))


def test_containerfile_compliance_rejects_fromm_instruction(tmp_path):
    dockerfile = tmp_path / "Dockerfile"
    dockerfile.write_text("FROMM python:3.12-slim\n", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(FROM instruction|arahan FROM)"):
        containers_mod.test_containerfile_security_and_structure(str(dockerfile))


def test_containerfile_compliance_rejects_chmod_777(tmp_path):
    dockerfile = tmp_path / "Dockerfile"
    dockerfile.write_text("FROM python:3.12-slim\nRUN chmod 777 /app\n", encoding="utf-8")
    with pytest.raises(AssertionError, match="chmod 777"):
        containers_mod.test_containerfile_security_and_structure(str(dockerfile))


def test_containerfile_compliance_rejects_latest_tag(tmp_path):
    dockerfile = tmp_path / "Dockerfile"
    dockerfile.write_text("FROM ubuntu:latest\n", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(latest|implisit)"):
        containers_mod.test_containerfile_security_and_structure(str(dockerfile))


def test_containerfile_compliance_rejects_registry_port_without_tag(tmp_path):
    dockerfile = tmp_path / "Dockerfile"
    dockerfile.write_text("FROM localhost:5000/myimage\n", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(latest|implisit)"):
        containers_mod.test_containerfile_security_and_structure(str(dockerfile))


def test_containerfile_compliance_accepts_pinned_from_tag(tmp_path):
    dockerfile = tmp_path / "Containerfile"
    dockerfile.write_text("FROM registry.access.redhat.com/ubi9:9.3\n", encoding="utf-8")
    containers_mod.test_containerfile_security_and_structure(str(dockerfile))


def test_containerfile_compliance_accepts_registry_port_with_tag(tmp_path):
    dockerfile = tmp_path / "Containerfile"
    dockerfile.write_text("FROM localhost:5000/myimage:v1.0\n", encoding="utf-8")
    containers_mod.test_containerfile_security_and_structure(str(dockerfile))


# ---------------------------------------------------------------------------
# test_containerfile_security_and_structure() - Podman Quadlet (.container/.pod)
# ---------------------------------------------------------------------------

def test_quadlet_compliance_accepts_valid_container_unit(tmp_path):
    quadlet = tmp_path / "app.container"
    quadlet.write_text("[Container]\nImage=docker.io/library/nginx:1.25\n", encoding="utf-8")
    containers_mod.test_containerfile_security_and_structure(str(quadlet))


def test_quadlet_compliance_accepts_valid_pod_unit_without_image(tmp_path):
    quadlet = tmp_path / "app.pod"
    quadlet.write_text("[Pod]\nPodName=my-app\n", encoding="utf-8")
    containers_mod.test_containerfile_security_and_structure(str(quadlet))


def test_quadlet_compliance_rejects_empty_file(tmp_path):
    quadlet = tmp_path / "app.container"
    quadlet.write_text("   \n", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(is empty|adalah kosong)"):
        containers_mod.test_containerfile_security_and_structure(str(quadlet))


def test_quadlet_compliance_rejects_missing_section_header(tmp_path):
    quadlet = tmp_path / "app.container"
    quadlet.write_text("Image=docker.io/library/nginx:1.25\n", encoding="utf-8")
    with pytest.raises(AssertionError) as excinfo:
        containers_mod.test_containerfile_security_and_structure(str(quadlet))
    assert "[Container]" in str(excinfo.value) and "[Pod]" in str(excinfo.value)


def test_quadlet_compliance_rejects_container_unit_missing_image(tmp_path):
    quadlet = tmp_path / "app.container"
    quadlet.write_text("[Container]\nExec=/bin/true\n", encoding="utf-8")
    with pytest.raises(AssertionError, match="Image="):
        containers_mod.test_containerfile_security_and_structure(str(quadlet))


# ---------------------------------------------------------------------------
# test_containerfile_security_and_structure() - YAML manifests (compose / kube)
# ---------------------------------------------------------------------------

@pytest.mark.skipif(containers_mod.yaml is None, reason="PyYAML tidak dipasang")
def test_yaml_manifest_compliance_accepts_valid_docker_compose(tmp_path):
    manifest = tmp_path / "docker-compose.yml"
    manifest.write_text(
        "version: '3'\nservices:\n  web:\n    image: nginx:1.25\n",
        encoding="utf-8",
    )
    containers_mod.test_containerfile_security_and_structure(str(manifest))


@pytest.mark.skipif(containers_mod.yaml is None, reason="PyYAML tidak dipasang")
def test_yaml_manifest_compliance_rejects_compose_missing_services(tmp_path):
    manifest = tmp_path / "docker-compose.yml"
    manifest.write_text("version: '3'\n", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(must define 'services'|mesti mentakrifkan 'services')"):
        containers_mod.test_containerfile_security_and_structure(str(manifest))


@pytest.mark.skipif(containers_mod.yaml is None, reason="PyYAML tidak dipasang")
def test_yaml_manifest_compliance_rejects_arbitrary_yaml_mapping(tmp_path):
    manifest = tmp_path / "docker-compose.yml"
    manifest.write_text("foo: bar\n", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(services|kind)"):
        containers_mod.test_containerfile_security_and_structure(str(manifest))


@pytest.mark.skipif(containers_mod.yaml is None, reason="PyYAML tidak dipasang")
def test_yaml_manifest_compliance_accepts_valid_kube_pod(tmp_path):
    manifest = tmp_path / "pod.yml"
    manifest.write_text("kind: Pod\napiVersion: v1\n", encoding="utf-8")
    containers_mod.test_containerfile_security_and_structure(str(manifest))


@pytest.mark.skipif(containers_mod.yaml is None, reason="PyYAML tidak dipasang")
def test_yaml_manifest_compliance_rejects_invalid_kube_kind(tmp_path):
    manifest = tmp_path / "configmap.yml"
    manifest.write_text("kind: ConfigMap\napiVersion: v1\n", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(invalid kind|jenis tidak sah)"):
        containers_mod.test_containerfile_security_and_structure(str(manifest))


@pytest.mark.skipif(containers_mod.yaml is None, reason="PyYAML tidak dipasang")
def test_yaml_manifest_compliance_rejects_empty_manifest(tmp_path):
    manifest = tmp_path / "empty.yml"
    manifest.write_text("", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(empty or invalid YAML|kosong atau YAML tidak sah)"):
        containers_mod.test_containerfile_security_and_structure(str(manifest))
