"""Unit tests for the Enterprise HA Database solution PDF compiler script (tools/compile_ha_db_pdf.py)."""

from pathlib import Path
import subprocess
from unittest.mock import Mock, call

import pytest

import tools.compile_ha_db_pdf as ha_pdf_compiler

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def test_clean_markdown_strips_frontmatter_and_footers(tmp_path):
    """Verify clean_markdown strips OKF frontmatter and DSOM footers."""
    src_file = tmp_path / "ha_db.md"
    src_file.write_text(
        "---\nokf_version: '0.2'\ntitle: 'Title'\n---\n\n# Heading\nContent\n---\n*Linux for NOSS Malaysia (Sovereign Manual)*\n*Standard: UK English*",
        encoding="utf-8",
    )
    cleaned = ha_pdf_compiler.clean_markdown(src_file, tmp_path)
    content = cleaned.read_text(encoding="utf-8")
    assert "okf_version" not in content
    assert "# Heading" in content
    assert "Content" in content
    assert "Linux for NOSS Malaysia" not in content


def test_write_css_generates_pure_white_css(tmp_path):
    """Verify write_css creates CSS with mandated A4 margins and pure white background."""
    css_file = ha_pdf_compiler.write_css(tmp_path)
    assert css_file.exists()
    css_content = css_file.read_text(encoding="utf-8")
    assert "#FFFFFF !important" in css_content
    assert "margin: 10mm 10mm 12mm 10mm;" in css_content


def test_generated_ha_db_pdf_artifact_exists_and_exceeds_min_size():
    """Verify the generated HA Database PDF in docs/dist exists and exceeds 10KB."""
    pdf_path = REPO_ROOT / "docs" / "dist" / "solusi-pangkalan-data-kebolehseediaan-tinggi.pdf"
    assert pdf_path.is_file()
    assert pdf_path.stat().st_size > 10240


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        pytest.param("", "", id="empty"),
        pytest.param(" \n\t", "", id="whitespace"),
        pytest.param("# Pangkalan data\n\nKetersediaan tinggi — ≥ 3 nod.",
                     "# Pangkalan data\n\nKetersediaan tinggi — ≥ 3 nod.", id="unicode"),
        pytest.param("---\ntitle: Belum lengkap\n# Isi", "---\ntitle: Belum lengkap\n# Isi",
                     id="unclosed-frontmatter"),
        pytest.param("---\ntitle: DB\n---\n\n# Isi\n\n---\n\nPenutup",
                     "# Isi\n\n---\n\nPenutup", id="preserve-body-rule"),
        pytest.param("# Isi\n---\n*Linux for NOSS Malaysia*\n*Standard: UK English*\n\nNota",
                     "# Isi\n---\n*Linux for NOSS Malaysia*\n*Standard: UK English*\n\nNota",
                     id="preserve-interior-signature"),
        pytest.param("# Isi\n---\n*Linux for NOSS Malaysia*\n*Standard: UK English*\n \n",
                     "# Isi", id="footer-with-trailing-whitespace"),
        pytest.param("---\nokf_version: '0.2'\n---\n", "", id="frontmatter-only"),
    ],
)
def test_clean_markdown_preserves_document_content(tmp_path, source, expected):
    """Kekalkan kandungan biasa dan buang metadata atau pengaki yang lengkap sahaja."""
    source_path = tmp_path / "source.md"
    source_path.write_text(source, encoding="utf-8")
    build_dir = tmp_path / "build"
    build_dir.mkdir()

    result = ha_pdf_compiler.clean_markdown(source_path, build_dir)

    assert result == build_dir / "ha_db_clean.md"
    assert result.read_text(encoding="utf-8") == expected
    assert source_path.read_text(encoding="utf-8") == source


def test_clean_markdown_missing_source_does_not_create_output(tmp_path):
    with pytest.raises(FileNotFoundError):
        ha_pdf_compiler.clean_markdown(tmp_path / "missing.md", tmp_path)
    assert not (tmp_path / "ha_db_clean.md").exists()


def test_write_css_preserves_print_pagination_rules(tmp_path):
    """Pastikan pengepala jadual berulang dan nombor halaman tersedia untuk cetakan."""
    css_path = ha_pdf_compiler.write_css(tmp_path)
    css = css_path.read_text(encoding="utf-8")
    assert css_path == tmp_path / "style.css"
    assert "size: A4 portrait;" in css
    assert "counter(page)" in css and "counter(pages)" in css
    assert "thead {\n    display: table-header-group;" in css
    assert "tr {\n    page-break-inside: avoid;" in css


@pytest.fixture
def html_inputs(tmp_path):
    """Sediakan fail berasingan daripada artifak sebenar repositori."""
    build_dir = tmp_path / "build with spaces"
    dist_dir = tmp_path / "dist with spaces"
    build_dir.mkdir()
    dist_dir.mkdir()
    md_path = build_dir / "source.md"
    md_path.write_text("# Pangkalan data\n\nKetersediaan tinggi.", encoding="utf-8")
    css_path = build_dir / "style.css"
    css_path.write_text("body { color: black; }", encoding="utf-8")
    return md_path, css_path, build_dir, dist_dir / "report.html"


def test_compile_html_pandoc_copies_assets_and_removes_column_widths(html_inputs, monkeypatch):
    md_path, css_path, build_dir, dist_html = html_inputs
    which = Mock(return_value="/opt/pandoc bin/pandoc")
    monkeypatch.setattr(ha_pdf_compiler.shutil, "which", which)
    raw_html = (
        '<html><head><link rel="stylesheet" href="style.css"></head><body>'
        '<table><colgroup>\n<col style="width: 50%">\n</colgroup><tr><td>≥ 3 nod</td></tr></table>'
        '<table><colgroup><col></colgroup><tr><td>Galera</td></tr></table></body></html>'
    )

    def run_pandoc(command, **kwargs):
        Path(command[command.index("-o") + 1]).write_text(raw_html, encoding="utf-8")

    run = Mock(side_effect=run_pandoc)
    monkeypatch.setattr(ha_pdf_compiler.subprocess, "run", run)

    result = ha_pdf_compiler.compile_html(*html_inputs)

    which.assert_called_once_with("pandoc")
    run.assert_called_once_with(
        ["/opt/pandoc bin/pandoc", str(md_path), "-o", str(build_dir / "report.html"),
         "--standalone", "--css", "style.css", "--highlight-style=tango", "--metadata",
         "title=Solusi Pangkalan Data Kebolehseediaan Tinggi Enterprise"],
        check=True, cwd=build_dir,
    )
    assert result == dist_html
    expected = raw_html.replace('<colgroup>\n<col style="width: 50%">\n</colgroup>', "").replace(
        "<colgroup><col></colgroup>", ""
    )
    assert dist_html.read_text(encoding="utf-8") == expected
    assert (build_dir / "report.html").read_text(encoding="utf-8") == expected
    assert (dist_html.parent / "style.css").read_bytes() == css_path.read_bytes()


def test_compile_html_markdown_fallback_renders_document_features(html_inputs, monkeypatch):
    """Uji penukar Markdown sebenar tanpa memerlukan Pandoc atau WeasyPrint."""
    md_path, css_path, build_dir, dist_html = html_inputs
    md_path.write_text(
        '# Galera {#cluster}\n\nKetersediaan ≥ 3 nod.\n\n'
        '| Nod | Peranan |\n| --- | --- |\n| db1 | Utama |\n\n'
        '```sql\nSELECT 1;\n```\n\nHA\n: Ketersediaan tinggi\n', encoding="utf-8",
    )
    monkeypatch.setattr(ha_pdf_compiler.shutil, "which", Mock(return_value=None))
    run = Mock(side_effect=AssertionError("Fallback must not launch a process"))
    monkeypatch.setattr(ha_pdf_compiler.subprocess, "run", run)

    assert ha_pdf_compiler.compile_html(*html_inputs) == dist_html

    html = dist_html.read_text(encoding="utf-8")
    for fragment in (
        '<!DOCTYPE html>', '<html lang="ms">', '<meta charset="utf-8">',
        '<link rel="stylesheet" href="style.css">', '<h1 id="cluster">Galera</h1>',
        'Ketersediaan ≥ 3 nod.', '<table>', '<td>db1</td>', '<pre>', 'SELECT',
        '<dt>HA</dt>', '<dd>Ketersediaan tinggi</dd>',
    ):
        assert fragment in html
    assert (build_dir / "report.html").read_text(encoding="utf-8") == html
    assert (dist_html.parent / "style.css").read_bytes() == css_path.read_bytes()
    run.assert_not_called()


def test_compile_html_pandoc_failure_does_not_publish_stale_output(html_inputs, monkeypatch):
    _, _, build_dir, dist_html = html_inputs
    (build_dir / "report.html").write_text("stale", encoding="utf-8")
    monkeypatch.setattr(ha_pdf_compiler.shutil, "which", Mock(return_value="pandoc"))
    error = subprocess.CalledProcessError(1, ["pandoc"])
    monkeypatch.setattr(ha_pdf_compiler.subprocess, "run", Mock(side_effect=error))

    with pytest.raises(subprocess.CalledProcessError) as caught:
        ha_pdf_compiler.compile_html(*html_inputs)

    assert caught.value is error
    assert not dist_html.exists()
    assert not (dist_html.parent / "style.css").exists()


@pytest.mark.parametrize("size", [0, 1, 10239, 10240, 10241, 20480])
def test_compile_pdf_enforces_strict_size_boundary(tmp_path, monkeypatch, size):
    """10 KB tepat mesti ditolak; satu bait tambahan mesti diterima."""
    dist_html = tmp_path / "source with spaces.html"
    dist_pdf = tmp_path / "output with spaces.pdf"

    def render_pdf(command, **kwargs):
        Path(command[-1]).write_bytes(b"x" * size)

    run = Mock(side_effect=render_pdf)
    monkeypatch.setattr(ha_pdf_compiler.subprocess, "run", run)

    if size <= 10240:
        with pytest.raises(RuntimeError, match="at or below the 10KB limit"):
            ha_pdf_compiler.compile_pdf(dist_html, dist_pdf)
    else:
        assert ha_pdf_compiler.compile_pdf(dist_html, dist_pdf) == dist_pdf
    run.assert_called_once_with(
        [ha_pdf_compiler.sys.executable, "-m", "weasyprint", str(dist_html), str(dist_pdf)],
        check=True, timeout=120,
    )


def test_compile_pdf_rejects_missing_output(tmp_path, monkeypatch):
    monkeypatch.setattr(ha_pdf_compiler.subprocess, "run", Mock())
    with pytest.raises(RuntimeError, match="Output PDF file does not exist"):
        ha_pdf_compiler.compile_pdf(tmp_path / "source.html", tmp_path / "missing.pdf")


@pytest.mark.parametrize("error", [
    subprocess.CalledProcessError(1, ["weasyprint"]),
    subprocess.TimeoutExpired(["weasyprint"], 120),
    FileNotFoundError("Python executable unavailable"),
])
def test_compile_pdf_propagates_renderer_failures_even_with_stale_pdf(tmp_path, monkeypatch, error):
    dist_pdf = tmp_path / "old.pdf"
    dist_pdf.write_bytes(b"x" * 10241)
    monkeypatch.setattr(ha_pdf_compiler.subprocess, "run", Mock(side_effect=error))

    with pytest.raises(type(error)) as caught:
        ha_pdf_compiler.compile_pdf(tmp_path / "source.html", dist_pdf)

    assert caught.value is error


@pytest.mark.parametrize("existing_directories", [False, True])
def test_main_wires_pipeline_under_project_root(tmp_path, monkeypatch, existing_directories):
    """Laluan projek mesti bebas daripada direktori kerja semasa."""
    project = tmp_path / "project"
    monkeypatch.setattr(ha_pdf_compiler, "__file__", str(project / "tools" / "compile_ha_db_pdf.py"))
    monkeypatch.chdir(tmp_path)
    build = project / "build" / "ha_db_pdf"
    dist = project / "docs" / "dist"
    if existing_directories:
        build.mkdir(parents=True)
        dist.mkdir(parents=True)
    cleaned = build / "cleaned.md"
    css = build / "custom.css"
    html = dist / "compiled.html"
    pipeline = Mock()

    def clean(source, destination):
        assert build.is_dir() and dist.is_dir()
        return cleaned

    pipeline.clean_markdown.side_effect = clean
    pipeline.write_css.return_value = css
    pipeline.compile_html.return_value = html
    for name in ("clean_markdown", "write_css", "compile_html", "compile_pdf"):
        monkeypatch.setattr(ha_pdf_compiler, name, getattr(pipeline, name))

    ha_pdf_compiler.main()

    assert pipeline.mock_calls == [
        call.clean_markdown(project / "manual" / "cu03" /
                            "cu03-wa05-solusi-pangkalan-data-kebolehseediaan-tinggi.md", build),
        call.write_css(build),
        call.compile_html(cleaned, css, build, dist / "solusi-pangkalan-data-kebolehseediaan-tinggi.html"),
        call.compile_pdf(html, dist / "solusi-pangkalan-data-kebolehseediaan-tinggi.pdf"),
    ]


@pytest.mark.parametrize("failed_stage", ["clean_markdown", "write_css", "compile_html", "compile_pdf"])
def test_main_stops_after_pipeline_failure(tmp_path, monkeypatch, failed_stage):
    monkeypatch.setattr(ha_pdf_compiler, "__file__", str(tmp_path / "tools" / "compile_ha_db_pdf.py"))
    stages = ("clean_markdown", "write_css", "compile_html", "compile_pdf")
    mocks = {name: Mock(return_value=tmp_path / name) for name in stages}
    error = RuntimeError("Pipeline stage failed")
    mocks[failed_stage].side_effect = error
    for name, mock in mocks.items():
        monkeypatch.setattr(ha_pdf_compiler, name, mock)

    with pytest.raises(RuntimeError) as caught:
        ha_pdf_compiler.main()

    assert caught.value is error
    for name in stages[:stages.index(failed_stage) + 1]:
        mocks[name].assert_called_once()
    for name in stages[stages.index(failed_stage) + 1:]:
        mocks[name].assert_not_called()
