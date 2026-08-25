"""Ujian unit untuk scripts/generate_palace_registry.py (penjana Master Palace Registry)."""

import importlib.util
from pathlib import Path
from types import ModuleType

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def _import_palace_registry_script() -> ModuleType:
    """Muatkan skrip generate_palace_registry.py secara dinamik untuk ujian terasing.

    Returns:
        ModuleType: Instans modul generate_palace_registry yang dimuatkan.
    """
    script_path = REPO_ROOT / "scripts" / "generate_palace_registry.py"
    spec = importlib.util.spec_from_file_location("palace_registry_mod", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


palace_mod = _import_palace_registry_script()


def test_extract_yaml_frontmatter_valid():
    """Mengesahkan pengekstrakan YAML frontmatter daripada kandungan Markdown yang sah."""
    content = "---\nokf_version: 0.2\ntitle: Sample Skill\n---\n# Heading\n"
    fm = palace_mod.extract_yaml_frontmatter(content)
    assert "okf_version: 0.2" in fm
    assert "title: Sample Skill" in fm


def test_extract_yaml_frontmatter_invalid():
    """Mengesahkan cawangan pulangan rentetan kosong untuk kandungan tanpa frontmatter."""
    content = "# Heading without frontmatter\n"
    fm = palace_mod.extract_yaml_frontmatter(content)
    assert fm == ""


def test_parse_metadata_extracts_title_name_desc_topics():
    """Mengesahkan penceraian medan metadata daripada frontmatter."""
    fm = 'name: "my-skill"\ndescription: "Skill description"\ntopics: ["linux", "cu01"]'
    meta = palace_mod.parse_metadata(fm)
    assert meta["title"] == "my-skill"
    assert meta["description"] == "Skill description"
    assert "linux" in meta["topics"]


def test_generate_registry_execution(tmp_path, monkeypatch):
    """Mengesahkan fungsi generate_registry menghasilkan fail indeks yang lengkap."""
    skills_dir = tmp_path / ".agents" / "skills" / "sample-skill"
    skills_dir.mkdir(parents=True, exist_ok=True)
    skill_file = skills_dir / "SKILL.md"
    skill_file.write_text(
        '---\nokf_version: 0.2\nname: "sample-skill"\ndescription: "A sample skill."\ntopics: ["test"]\n---\n',
        encoding="utf-8",
    )

    monkeypatch.setattr(palace_mod, "skills_dir", str(tmp_path / ".agents" / "skills"))
    output_file = tmp_path / ".agents" / "skills" / "index.md"
    monkeypatch.setattr(palace_mod, "output_file", str(output_file))

    palace_mod.generate_registry()

    assert output_file.exists()
    content = output_file.read_text(encoding="utf-8")
    assert "Master Palace Registry" in content
    assert "sample-skill" in content
