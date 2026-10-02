"""Ujian unit pengesah OKF v0.2 dengan dokumen sintetik terasing."""

import importlib.util
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture
def compliance(tmp_path, monkeypatch):
    """Elakkan imbasan repositori semasa memuatkan pengesah berparameter."""
    monkeypatch.chdir(tmp_path)
    spec = importlib.util.spec_from_file_location(
        "okf_v02_compliance_target", REPO_ROOT / "tests/test_okf_compliance.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def valid_metadata():
    """Sediakan metadata minimum dengan kedua-dua jenis sumber."""
    return {
        "okf_version": "0.2", "type": "documentation", "title": "Contoh",
        "description": "Penerangan", "status": "stable", "stale_after": "2027-12-31",
        "generated": {"by": "test", "at": "2026-10-02T00:00:00Z"},
        "sources": [{"url": "docs/legal-notice.md"}, {"url": "https://example.org/spec"}],
    }


def write_metadata(tmp_path, metadata):
    """Tulis frontmatter yang boleh dibaca oleh pengesah sebenar."""
    path = tmp_path / "note.md"
    path.write_text("---\n" + yaml.safe_dump(metadata) + "---\n\n# Contoh\n", encoding="utf-8")
    return str(path)


@pytest.mark.parametrize("version_key", ["okf_version", "spec_version"])
@pytest.mark.parametrize("version", ["0.2", 0.2])
@pytest.mark.parametrize("title_key", ["title", "name"])
def test_accepts_version_and_title_alternatives(compliance, tmp_path, valid_metadata, version_key, version, title_key):
    """Terima versi rentetan atau angka dan kedua-dua nama medan yang disokong."""
    valid_metadata.pop("okf_version")
    valid_metadata[version_key] = version
    valid_metadata[title_key] = valid_metadata.pop("title")
    compliance.test_okf_v02_frontmatter(write_metadata(tmp_path, valid_metadata))


@pytest.mark.parametrize("field", ["type", "title", "description", "status", "stale_after", "generated", "sources"])
def test_rejects_missing_required_metadata(compliance, tmp_path, valid_metadata, field):
    """Setiap medan wajib diuji dengan mengeluarkannya secara berasingan."""
    del valid_metadata[field]
    with pytest.raises(AssertionError, match=field):
        compliance.test_okf_v02_frontmatter(write_metadata(tmp_path, valid_metadata))


@pytest.mark.parametrize("version_fields", [{}, {"okf_version": "0.1"}, {"spec_version": "0.3"}, {"okf_version": "0.1", "spec_version": "0.2"}])
def test_rejects_missing_old_or_conflicting_versions(compliance, tmp_path, valid_metadata, version_fields):
    """Versi lama tidak boleh disembunyikan oleh spec_version yang sah."""
    del valid_metadata["okf_version"]
    valid_metadata.update(version_fields)
    with pytest.raises(AssertionError, match="must specify okf_version or spec_version"):
        compliance.test_okf_v02_frontmatter(write_metadata(tmp_path, valid_metadata))


@pytest.mark.parametrize(
    "content,message",
    [
        ("# No frontmatter", "must start with YAML frontmatter"),
        ("---\ntitle: Unclosed\n", "malformed or missing YAML closure"),
        ("---\n- sequence\n---\n", "valid YAML object"),
        ("---\nscalar\n---\n", "valid YAML object"),
        ("---\n\n---\n", "valid YAML object"),
    ],
)
def test_rejects_invalid_frontmatter_structure(compliance, tmp_path, content, message):
    """Dokumen tanpa pemetaan YAML yang lengkap mesti ditolak."""
    path = tmp_path / "note.md"
    path.write_text(content, encoding="utf-8")
    with pytest.raises(AssertionError, match=message):
        compliance.test_okf_v02_frontmatter(str(path))


def test_malformed_yaml_raises_parser_error(compliance, tmp_path):
    """Jangan menerima metadata yang gagal dihuraikan sebagai YAML."""
    path = tmp_path / "note.md"
    path.write_text("---\nbroken: [\n---\n", encoding="utf-8")
    with pytest.raises(yaml.YAMLError):
        compliance.test_okf_v02_frontmatter(str(path))


@pytest.mark.parametrize("sources", [None, "source", {"url": "docs/reference.md"}, []])
def test_rejects_invalid_or_empty_sources(compliance, tmp_path, valid_metadata, sources):
    """Sumber mestilah senarai yang tidak kosong."""
    valid_metadata["sources"] = sources
    with pytest.raises(AssertionError, match="sources"):
        compliance.test_okf_v02_frontmatter(write_metadata(tmp_path, valid_metadata))


@pytest.mark.parametrize(
    "sources,message",
    [
        ([{"url": "https://example.org/spec.md"}], "internal document reference"),
        ([{"url": "docs/spec.md"}], "public internet URL"),
        (["docs/spec.md", "https://example.org/spec"], "internal document reference"),
        ([{}, None, 42], "internal document reference"),
    ],
)
def test_requires_internal_and_public_sources(compliance, tmp_path, valid_metadata, sources, message):
    """Sumber awam berakhiran .md tidak dikira sebagai rujukan dalaman."""
    valid_metadata["sources"] = sources
    with pytest.raises(AssertionError, match=message):
        compliance.test_okf_v02_frontmatter(write_metadata(tmp_path, valid_metadata))


@pytest.mark.parametrize("internal", ["note.md", "docs/note", "file:note"])
@pytest.mark.parametrize("scheme", ["http", "https"])
def test_accepts_resource_fallback_and_ignores_non_mapping_sources(compliance, tmp_path, valid_metadata, internal, scheme):
    """Resource digunakan apabila URL tiada atau kosong."""
    valid_metadata["sources"] = [
        None, "legacy", {"resource": internal},
        {"url": "", "resource": f"{scheme}://example.org/spec"},
    ]
    compliance.test_okf_v02_frontmatter(write_metadata(tmp_path, valid_metadata))


def test_discovery_includes_root_and_hidden_documents_but_prunes_exclusions(compliance, tmp_path):
    """Regresi skop baharu: README, AGENTS dan dokumen otak turut ditemui."""
    included = ["README.md", "AGENTS.md", "CHANGELOG.md", "HISTORY.md", "SUMMARY.md", "docs/nested/note.md", ".agents/brain/note.md", "html-notes/kept.md"]
    excluded = ["plain.txt", "upper.MD"]
    for directory in ["html", "node_modules", ".git", ".pytest_cache", "scratch"]:
        excluded.extend([f"{directory}/ignored.md", f"docs/{directory}/deep/ignored.md"])
    for relative in included + excluded:
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("content", encoding="utf-8")
    found = compliance.get_markdown_files()
    assert found == sorted(found)
    assert {Path(path).as_posix() for path in found} == set(included)


def test_discovery_empty_tree(compliance):
    """Pokok tanpa Markdown menghasilkan senarai kosong."""
    assert compliance.get_markdown_files() == []
