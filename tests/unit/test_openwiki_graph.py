"""Ujian unit untuk scripts/generate_openwiki_graph.py (penjana OpenWiki Master Graph)."""

import importlib.util
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def _import_openwiki_graph_script():
    """Muat naik skrip generate_openwiki_graph.py secara dinamik untuk ujian terasing.

    Returns:
        module: Instans modul generate_openwiki_graph yang dimuatkan.
    """
    script_path = REPO_ROOT / "scripts" / "generate_openwiki_graph.py"
    spec = importlib.util.spec_from_file_location("openwiki_graph_mod", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


openwiki_mod = _import_openwiki_graph_script()


def test_extract_metadata_from_topic_file(tmp_path):
    """Mengesahkan ekstraksi tajuk, penerangan, dan CU daripada fail topik OpenWiki."""
    topic_file = tmp_path / "topic-01-test.md"
    topic_file.write_text(
        '---\ntitle: "Topik 1: Test"\ndescription: "Penerangan Ujian"\n---\n\nKandungan merujuk CU01.\n',
        encoding="utf-8",
    )

    meta = openwiki_mod.extract_metadata(str(topic_file))
    assert meta["title"] == "Topik 1: Test"
    assert meta["desc"] == "Penerangan Ujian"
    assert meta["cu"] == "CU01"


def test_generate_graph_execution(tmp_path, monkeypatch):
    """Mengesahkan fungsi generate_graph menghasilkan diagram Mermaid dan jadual perincian modul."""
    openwiki_dir = tmp_path / "openwiki"
    openwiki_dir.mkdir(parents=True, exist_ok=True)
    topic_file = openwiki_dir / "topic-01-sample.md"
    topic_file.write_text(
        '---\ntitle: "Topik Sample"\ndescription: "Sampel"\n---\n\nKandungan CU01.\n',
        encoding="utf-8",
    )

    monkeypatch.setattr(openwiki_mod, "OPENWIKI_DIR", str(openwiki_dir))
    output_file = openwiki_dir / "index.md"
    monkeypatch.setattr(openwiki_mod, "OUTPUT_FILE", str(output_file))

    openwiki_mod.generate_graph()

    assert output_file.exists()
    content = output_file.read_text(encoding="utf-8")
    assert "OpenWiki Master Graph" in content
    assert "mermaid" in content
    assert "Topik Sample" in content
