"""Ujian regresi pengecualian direktori build daripada imbasan pematuhan OKF."""

import importlib.util
from pathlib import Path


def test_markdown_discovery_prunes_build_directories_without_hiding_sources(tmp_path, monkeypatch):
    included = {
        "manual/cu03/source.md",
        "build-notes/guide.md",
        "docs/build.md",
        "README.md",
    }
    excluded = {
        "build/ha_db_pdf/ha_db_clean.md",
        "docs/build/nested/intermediate.md",
        "build/deep/nested/generated.md",
        "manual/cu03/source.txt",
    }
    for filename in included | excluded:
        path = tmp_path / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# Kandungan ujian", encoding="utf-8")

    # Modul ini membina parameter ujian semasa import; hadkan imbasan kepada fixture.
    monkeypatch.chdir(tmp_path)
    script = Path(__file__).resolve().parents[1] / "test_okf_compliance.py"
    spec = importlib.util.spec_from_file_location("okf_compliance_discovery", script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    discovered = module.get_markdown_files()

    assert discovered == sorted(discovered)
    assert {Path(path).as_posix() for path in discovered} == included
