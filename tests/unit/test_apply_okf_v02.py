"""Ujian unit migrasi OKF v0.2 menggunakan fail sementara sahaja."""

import builtins
import importlib.util
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import Mock

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture
def migration():
    """Muatkan skrip tanpa menjalankan migrasi repositori."""
    spec = importlib.util.spec_from_file_location(
        "apply_okf_v02_target", REPO_ROOT / "scripts/apply_okf_v02.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_document(root, relative="note.md", metadata=None, body="# Tajuk\n\nIsi café."):
    """Sediakan dokumen UTF-8 dengan metadata pilihan."""
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    prefix = "" if metadata is None else "---\n" + yaml.safe_dump(metadata) + "---\n"
    path.write_text(prefix + body, encoding="utf-8")
    return path


def read_document(path):
    """Baca metadata dan isi selepas migrasi."""
    _, frontmatter, body = path.read_text(encoding="utf-8").split("---", 2)
    return yaml.safe_load(frontmatter), body.strip()


@pytest.mark.parametrize(
    "path,existing,expected",
    [
        ("playbooks/task.md", None, "Attested Computation"),
        ("roles/web/README.md", None, "Attested Computation"),
        ("deploy/docs/tutorials/task.md", "guide", "Attested Computation"),
        (".agents/skills/demo/SKILL.md", None, "agent_skill"),
        (".agents/skills/demo/references/task.md", None, "agent_skill"),
        ("docs/explanation/governance/task.md", None, "governance_protocol"),
        ("AGENTS.md", None, "governance_protocol"),
        ("LEGAL-NOTICE.md", None, "governance_protocol"),
        (".agents/brain/wings/note.md", None, "architecture_concept"),
        ("tools/task.md", None, "automation_tool"),
        ("scripts/task.md", None, "automation_tool"),
        ("docs/how-to/task.md", "reference", "guide"),
        ("docs/tutorials/task.md", None, "guide"),
        ("START-HERE.md", None, "guide"),
        ("README.md", None, "guide"),
        ("manual/cu01/task.md", None, "reference"),
        ("docs/reference/task.md", None, "reference"),
        ("references/task.md", None, "reference"),
        ("openwiki/task.md", None, "explanation"),
        ("docs/explanation/task.md", None, "explanation"),
        ("other/task.md", "custom", "custom"),
        ("other/task.md", "", "documentation"),
        ("other/task.md", None, "documentation"),
        ("docs/how-to/task.md", "attested_computation", "Attested Computation"),
        ("README.md", "Attested Computation", "Attested Computation"),
        ("my-deploy/roles-guide.md", None, "documentation"),
        ("docs/README.md", None, "documentation"),
        (r"docs\how-to\task.md", None, "guide"),
    ],
)
def test_classification_and_rule_precedence(migration, path, existing, expected):
    """Semak klasifikasi, keutamaan peraturan dan sempadan nama direktori."""
    assert migration.get_okf_type(path, existing) == expected


@pytest.mark.parametrize(
    "content,filename,expected",
    [
        ("## Subheading\n# First title  \n# Second", "note.md", "First title"),
        ("# Café Melayu", "note.md", "Café Melayu"),
        ("#No space\n## Lower level", "my_linux-notes.md", "My Linux Notes"),
        ("", "release.v2-notes.md", "Release.V2 Notes"),
    ],
)
def test_title_extraction(migration, content, filename, expected):
    """Gunakan tajuk aras pertama atau nama fail sebagai sandaran."""
    assert migration.extract_title(content, filename) == expected


def test_plain_document_gets_defaults_without_false_verification(migration, tmp_path, monkeypatch):
    """Metadata baharu mesti mempunyai asal usul dan masa UTC yang tepat."""
    clock = Mock()
    clock.now.return_value = datetime(2026, 10, 2, 12, 30, 45, tzinfo=timezone.utc)
    monkeypatch.setattr(migration, "datetime", clock)
    path = write_document(tmp_path)

    assert migration.process_file(str(path), str(tmp_path), "unit-test") == (True, True)
    metadata, body = read_document(path)

    assert metadata["okf_version"] == metadata["spec_version"] == "0.2"
    assert metadata["type"] == "documentation"
    assert metadata["title"] == "Tajuk"
    assert metadata["description"] == "Dokumentasi OKF v0.2 bagi note.md."
    assert metadata["status"] == "stable"
    assert metadata["stale_after"] == "2027-12-31"
    assert metadata["generated"] == {"by": "unit-test", "at": "2026-10-02T12:30:45Z"}
    clock.now.assert_called_once_with(timezone.utc)
    assert "verified" not in metadata
    assert "executor" not in metadata
    assert metadata["sources"] == migration.MANDATORY_SOURCES
    assert body == "# Tajuk\n\nIsi café.\n\n" + migration.SOVEREIGN_FOOTER
    assert path.read_bytes().endswith(b"\n")
    assert b"\r" not in path.read_bytes()


def test_preserves_custom_metadata_and_existing_provenance(migration, tmp_path):
    """Naik taraf versi tanpa menggantikan rekod pengguna."""
    original = {
        "okf_version": "0.1", "spec_version": "0.1", "title": "Existing title",
        "name": "skill-name", "description": "Custom description", "status": "draft",
        "stale_after": "2030-01-01", "topics": ["linux"], "custom": {"nested": True},
        "generated": {"by": "original", "at": "2025-01-01T00:00:00Z"},
        "verified": {"by": "reviewer", "at": "2025-01-02T00:00:00Z"},
    }
    path = write_document(tmp_path, metadata=original)
    assert migration.process_file(str(path), str(tmp_path)) == (True, True)
    metadata, _ = read_document(path)
    for key, value in original.items():
        assert metadata[key] == ("0.2" if key in {"okf_version", "spec_version"} else value)


@pytest.mark.parametrize(
    "metadata,expected",
    [({"name": "Skill name"}, "Skill name"), ({"title": 42}, "42"),
     ({"title": "", "name": "Name fallback"}, "Name fallback")],
)
def test_title_metadata_precedes_heading(migration, tmp_path, metadata, expected):
    """Kekalkan keutamaan title, name dan tajuk Markdown."""
    path = write_document(tmp_path, metadata=metadata)
    migration.process_file(str(path), str(tmp_path))
    assert read_document(path)[0]["title"] == expected


@pytest.mark.parametrize("raw", ["broken: [", "- list item", "scalar", "null", ""])
def test_invalid_or_non_mapping_frontmatter_is_replaced(migration, tmp_path, raw):
    """Metadata rosak tidak boleh menyebabkan isi dokumen hilang."""
    path = write_document(tmp_path, body=f"---\n{raw}\n---\n# Kept\n\nBody")
    assert migration.process_file(str(path), str(tmp_path)) == (True, True)
    metadata, body = read_document(path)
    assert metadata["title"] == "Kept"
    assert body.startswith("# Kept\n\nBody\n")


def test_frontmatter_delimiters_must_be_on_separate_lines(migration, tmp_path):
    """Tiga sempang dalam nilai dan isi tidak menutup frontmatter."""
    path = write_document(tmp_path, metadata={"title": "Before---After"}, body="Body\n---\nMore")
    migration.process_file(str(path), str(tmp_path))
    content = path.read_text(encoding="utf-8")
    metadata = yaml.safe_load(content.split("\n---\n", 1)[0].removeprefix("---\n"))
    assert metadata["title"] == "Before---After"
    assert "Body\n---\nMore" in content


def test_unclosed_frontmatter_is_retained_as_body(migration, tmp_path):
    """Jangan buang teks yang tidak mempunyai penutup frontmatter."""
    original = "---\ntitle: Unclosed\n# Heading\n"
    path = write_document(tmp_path, body=original)
    migration.process_file(str(path), str(tmp_path))
    assert original.strip() in read_document(path)[1]


def test_crlf_input_is_normalised(migration, tmp_path):
    """Pengekodan baris keluaran adalah LF dan metadata kekal sah."""
    path = tmp_path / "note.md"
    path.write_bytes(b"---\r\ntitle: Existing\r\n---\r\nBody\r\n")
    migration.process_file(str(path), str(tmp_path))
    assert read_document(path)[0]["title"] == "Existing"
    assert b"\r" not in path.read_bytes()


@pytest.mark.parametrize("sources", [None, "invalid", {"id": "not-a-list"}, []])
def test_invalid_sources_container_is_replaced(migration, tmp_path, sources):
    """Senarai sumber lalai menggantikan bekas sumber yang tidak sah."""
    path = write_document(tmp_path, metadata={"sources": sources})
    migration.process_file(str(path), str(tmp_path))
    assert read_document(path)[0]["sources"] == migration.MANDATORY_SOURCES


@pytest.mark.parametrize("match_by", ["id", "url", "resource"])
def test_sources_merge_preserves_entries_without_duplicate_defaults(migration, tmp_path, match_by):
    """Padanan ID, URL atau resource mengelakkan pendua sumber wajib."""
    mandatory = migration.MANDATORY_SOURCES[0]
    existing = {match_by: mandatory["id" if match_by == "id" else "url"], "title": "Custom"}
    sources = [existing, "legacy citation", {"url": "https://example.org/custom"}]
    path = write_document(tmp_path, metadata={"sources": sources})
    migration.process_file(str(path), str(tmp_path))
    assert read_document(path)[0]["sources"] == sources + migration.MANDATORY_SOURCES[1:]


@pytest.mark.parametrize("relative", ["deploy/task.md", "note.md"])
def test_attested_computation_receives_execution_contract(migration, tmp_path, relative):
    """Kontrak diwujudkan melalui laluan atau jenis sedia ada."""
    metadata = {} if relative.startswith("deploy/") else {"type": "attested_computation"}
    path = write_document(tmp_path, relative, metadata)
    migration.process_file(str(path), str(tmp_path))
    actual, _ = read_document(path)
    assert actual["type"] == "Attested Computation"
    assert actual["runtime"] == "python"
    assert actual["parameters"] == [{"name": "target_environment", "type": "string", "required": True}]
    assert actual["executor"] == {"resource": "run_all_tests.py", "receipt": ["exit_code", "stdout", "stderr"]}
    assert actual["attester"] == {"resource": "tests/test_okf_compliance.py"}


def test_existing_execution_contract_is_preserved(migration, tmp_path):
    """Kontrak pengguna termasuk parameter kosong tidak diganti."""
    contract = {
        "runtime": "bash", "parameters": [],
        "executor": {"resource": "custom.sh"}, "attester": {"resource": "verify.sh"},
    }
    path = write_document(tmp_path, "deploy/task.md", contract)
    migration.process_file(str(path), str(tmp_path))
    actual, _ = read_document(path)
    for key, value in contract.items():
        assert actual[key] == value


@pytest.mark.parametrize(
    "body,append_footer",
    [
        ("", True), ("LinuxMalaysia", True), ("CC BY-SA 4.0", True),
        ("LinuxMalaysia Dwi-Lesen", True),
        ("LinuxMalaysia Dwi-Lesen /docs/legal-notice.md", False),
        ("Harisfazillah Jamel CC BY-SA 4.0 [Notis Perundangan](legal.md)", False),
    ],
)
def test_footer_requires_attribution_license_and_legal_notice(migration, tmp_path, body, append_footer):
    """Tambahkan pengaki hanya apabila penanda yang diperlukan tiada."""
    path = write_document(tmp_path, body=body)
    migration.process_file(str(path), str(tmp_path))
    actual_body = read_document(path)[1]
    assert (migration.SOVEREIGN_FOOTER in actual_body) is append_footer
    assert actual_body.startswith(body)


def test_second_run_is_byte_stable_and_does_not_write(migration, tmp_path, monkeypatch):
    """Ujian regresi: migrasi berulang tidak menulis atau menduplikasi kandungan."""
    path = write_document(tmp_path, "deploy/task.md")
    assert migration.process_file(str(path), str(tmp_path)) == (True, True)
    before = path.read_bytes()
    real_open = builtins.open

    def read_only_open(file, mode="r", **kwargs):
        """Gagalkan sebarang cubaan menulis pada larian kedua."""
        assert mode == "r"
        return real_open(file, mode, **kwargs)

    monkeypatch.setattr(migration, "open", read_only_open, raising=False)
    clock = Mock()
    clock.now.return_value = datetime(2030, 1, 1, tzinfo=timezone.utc)
    monkeypatch.setattr(migration, "datetime", clock)
    assert migration.process_file(str(path), str(tmp_path), "different-actor") == (True, False)
    assert path.read_bytes() == before


def test_invalid_utf8_is_skipped_without_modification(migration, tmp_path, capsys):
    """Fail bukan UTF-8 dilaporkan tanpa ditulis semula."""
    path = tmp_path / "bad.md"
    path.write_bytes(b"\xff\xfeinvalid")
    assert migration.process_file(str(path), str(tmp_path)) == (False, False)
    assert path.read_bytes() == b"\xff\xfeinvalid"
    assert "[SKIP] Non-UTF-8 encoding in file: bad.md" in capsys.readouterr().err


@pytest.mark.parametrize("operation", ["read", "write"])
def test_io_errors_are_reported(migration, tmp_path, monkeypatch, capsys, operation):
    """Ralat baca dan tulis menghasilkan status gagal yang boleh dikendalikan."""
    path = write_document(tmp_path)
    before = path.read_bytes()
    real_open = builtins.open

    def failing_open(file, mode="r", **kwargs):
        """Simulasikan kegagalan I/O tanpa kebergantungan kebenaran OS."""
        if mode == {"read": "r", "write": "w"}[operation]:
            raise PermissionError("denied for test")
        return real_open(file, mode, **kwargs)

    monkeypatch.setattr(migration, "open", failing_open, raising=False)
    assert migration.process_file(str(path), str(tmp_path)) == (False, False)
    assert f"Cannot {operation} file note.md" in capsys.readouterr().err
    assert path.read_bytes() == before


def test_missing_file_is_reported(migration, tmp_path, capsys):
    """Fail yang tiada menghasilkan ralat terkawal."""
    assert migration.process_file(str(tmp_path / "missing.md"), str(tmp_path)) == (False, False)
    assert "Cannot read file missing.md" in capsys.readouterr().err


def test_main_filters_directories_and_file_extensions(migration, tmp_path, monkeypatch, capsys):
    """Imbas direktori bersarang sambil memangkas direktori yang dikecualikan."""
    included = ["README.md", "docs/nested/note.md", ".agents/skills/demo/SKILL.md", "html-notes/kept.md"]
    excluded = ["notes.txt", "upper.MD"]
    for directory in [".git", "node_modules", "html", ".pytest_cache", "scratch"]:
        excluded.extend([f"{directory}/ignored.md", f"docs/{directory}/nested/ignored.md"])
    for relative in included + excluded:
        write_document(tmp_path, relative)
    process = Mock(return_value=(True, True))
    monkeypatch.setattr(migration, "process_file", process)

    assert migration.main(str(tmp_path)) == 0
    assert {Path(call.args[0]).relative_to(tmp_path).as_posix() for call in process.call_args_list} == set(included)
    assert all(call.args[1] == str(tmp_path) for call in process.call_args_list)
    assert "Modified: 4, Errors: 0." in capsys.readouterr().out


def test_main_continues_after_errors_and_counts_only_changes(migration, tmp_path, monkeypatch, capsys):
    """Unchanged dan gagal tidak dikira sebagai fail yang diubah."""
    results = {"changed.md": (True, True), "unchanged.md": (True, False), "failed.md": (False, False)}
    for filename in results:
        write_document(tmp_path, filename)
    process = Mock(side_effect=lambda path, root: results[Path(path).name])
    monkeypatch.setattr(migration, "process_file", process)
    assert migration.main(str(tmp_path)) == 1
    assert process.call_count == 3
    assert "Modified: 1, Errors: 1." in capsys.readouterr().out


@pytest.mark.parametrize("missing", [False, True])
def test_main_with_no_documents(migration, tmp_path, capsys, missing):
    """Pokok kosong atau sasaran tiada tidak menghasilkan perubahan."""
    target = tmp_path / "missing" if missing else tmp_path
    assert migration.main(str(target)) == 0
    assert "Modified: 0, Errors: 0." in capsys.readouterr().out


@pytest.mark.parametrize("generated", [None, {}, ""])
def test_empty_generation_record_uses_requested_actor(migration, tmp_path, generated):
    """Rekod asal usul kosong diisi menggunakan identiti yang dibekalkan."""
    path = write_document(tmp_path, metadata={"generated": generated})
    migration.process_file(str(path), str(tmp_path), "replacement-actor")
    assert read_document(path)[0]["generated"]["by"] == "replacement-actor"


def test_partial_execution_contract_only_fills_missing_fields(migration, tmp_path):
    """Melengkapkan kontrak separa tanpa menggantikan pelaksana tersuai."""
    path = write_document(tmp_path, "deploy/task.md", {"executor": {"resource": "custom.sh"}})
    migration.process_file(str(path), str(tmp_path))
    metadata, _ = read_document(path)
    assert metadata["executor"] == {"resource": "custom.sh"}
    assert metadata["runtime"] == "python"
    assert metadata["parameters"][0]["required"] is True
    assert metadata["attester"] == {"resource": "tests/test_okf_compliance.py"}


def test_main_does_not_follow_directory_symlinks(migration, tmp_path, monkeypatch):
    """Pautan direktori tidak meluaskan imbasan keluar daripada sasaran."""
    root = tmp_path / "root"
    root.mkdir()
    outside = tmp_path / "outside"
    write_document(outside)
    (root / "linked").symlink_to(outside, target_is_directory=True)
    process = Mock()
    monkeypatch.setattr(migration, "process_file", process)
    assert migration.main(str(root)) == 0
    process.assert_not_called()


def test_main_migrates_only_target_and_is_repeatable(migration, tmp_path, monkeypatch, capsys):
    """Uji aliran sebenar pada pokok sementara melalui sasaran lalai."""
    monkeypatch.chdir(tmp_path)
    path = write_document(tmp_path, "docs/how-to/task.md")
    ignored = write_document(tmp_path, "html/ignored.md")
    ignored_before = ignored.read_bytes()
    assert migration.main() == 0
    assert "Modified: 1, Errors: 0." in capsys.readouterr().out
    assert read_document(path)[0]["type"] == "guide"
    assert migration.main() == 0
    assert "Modified: 0, Errors: 0." in capsys.readouterr().out
    assert ignored.read_bytes() == ignored_before
