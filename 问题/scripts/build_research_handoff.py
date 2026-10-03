"""Build and verify the portable research checkpoint, without running math probes."""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import zipfile
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DAY = "2026-10-03"
SUMMARY = f"本轮研究总结与审计状态_{DAY}.md"
HANDOFF = f"网页版Work研究交接_问题引入与继续任务_{DAY}.md"
README = f"研究交接资料包说明_{DAY}.md"
PACKAGE = f"研究交接资料包_{DAY}.zip"
EXPECTED_SOURCE = "d3443d0f143c475d0b98a6267d60eb468a95d18ab3fbad9e5ac77f84ac96ceb6"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def check_hash_records() -> list[dict]:
    audited = []
    for record in sorted((ROOT / "data").glob("*_sha256.json")):
        obj = json.loads(record.read_text(encoding="utf-8-sig"))
        if "files" in obj:
            pairs = obj["files"]
        elif "script_sha256" in obj and "raw_sha256" in obj:
            stem = record.stem.removesuffix("_sha256")
            pairs = {
                f"scripts/verify_{stem}.py": obj["script_sha256"],
                f"data/{stem}_certificate.json": obj["raw_sha256"],
            }
        else:
            pairs = obj
        checked = []
        for name, expected in pairs.items():
            check(isinstance(expected, str) and bool(re.fullmatch("[0-9a-fA-F]{64}", expected)),
                  f"Unrecognized SHA record: {record.name}, {name}")
            relative = Path(name.replace("\\", "/"))
            if len(relative.parts) == 1:
                directory = "scripts" if relative.suffix in {".py", ".cpp"} else "data"
                path = ROOT / directory / relative
            else:
                path = ROOT / relative
            check(path.is_file(), f"Missing hash target: {path}")
            check(digest(path) == expected.lower(), f"Hash mismatch: {path}")
            checked.append(path.relative_to(ROOT).as_posix())
        audited.append({"record": record.relative_to(ROOT).as_posix(),
                        "checked": checked, "result": "MATCH"})
    return audited


def selected_files() -> list[Path]:
    selected = list(ROOT.glob("*.md"))
    selected += [p for p in (ROOT / "scripts").iterdir()
                 if p.is_file() and p.suffix in {".py", ".cpp"}]
    selected += [p for p in (ROOT / "data").iterdir()
                 if p.is_file() and p.suffix in {".json", ".sha256"}]
    selected += [p for p in (ROOT / "sources").iterdir()
                 if p.is_file() and p.suffix in {".md", ".txt"}]
    return sorted(set(selected), key=lambda p: p.relative_to(ROOT).as_posix())


def check_new_document_links() -> int:
    count = 0
    for name in (SUMMARY, HANDOFF, README):
        text = (ROOT / name).read_text(encoding="utf-8")
        check(text.count(r"\[") == text.count(r"\]"), f"Unpaired display math: {name}")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if "://" in target:
                continue
            path_part = unquote(target.split("#", 1)[0].strip("<>"))
            if path_part == PACKAGE:
                continue  # Validated after creating the archive.
            check((ROOT / path_part).is_file(), f"Missing document link: {name}: {target}")
            count += 1
    return count


def main() -> None:
    sources = ROOT / "sources"
    sources.mkdir(exist_ok=True)
    original = Path("D:/Users/Downloads/graph_orientation_reconfiguration_progress_2026-10-02_revised.md")
    original_copy = sources / "原始用户修订档_2026-10-02.md"
    if original.is_file():
        check(digest(original) == EXPECTED_SOURCE, "Original revised source changed")
        if not original_copy.exists():
            shutil.copy2(original, original_copy)
    check(original_copy.is_file() and digest(original_copy) == EXPECTED_SOURCE,
          "Original revised source copy is missing or changed")

    prompts = [
        ("f6346c3e-a9e8-4f87-bcc5-9360cd79f0b0", "用户提供的长研究提示_早期.txt"),
        ("49628bbe-d884-4eb7-a73f-274efccbcaa4", "用户提供的MAIN任务提示_2026-10-03.txt"),
    ]
    for attachment_id, name in prompts:
        local = Path("C:/Users/HUAWEI/.codex-gui-openai/attachments") / attachment_id / "已粘贴的文本.txt"
        destination = sources / name
        if local.is_file() and not destination.exists():
            shutil.copy2(local, destination)

    manifest_path = ROOT / "data" / "research_checkpoint_manifest.json"
    if manifest_path.exists():
        previous = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
        if previous.get("schema") != "portable-research-handoff-v1":
            snapshot = ROOT / "data" / f"research_checkpoint_manifest_{DAY}_pre_handoff.json"
            if not snapshot.exists():
                shutil.copy2(manifest_path, snapshot)

    hash_records = check_hash_records()
    checked_links = check_new_document_links()
    selected = selected_files()
    inventory = {p.relative_to(ROOT).as_posix(): {"bytes": p.stat().st_size, "sha256": digest(p)}
                 for p in selected if p != manifest_path}
    manifest = {
        "schema": "portable-research-handoff-v1",
        "snapshot_created_local": datetime.now().astimezone().isoformat(timespec="seconds"),
        "report_date": DAY,
        "status": "RESEARCH HANDOFF; MAIN OPEN; no genuine ambient counterexample",
        "reports": {"summary": SUMMARY, "standalone_introduction": HANDOFF, "package_readme": README},
        "source_download_sha256": EXPECTED_SOURCE,
        "theorem_status": {
            "MAIN": "OPEN", "RSM": "OPEN",
            "global_up_to_five_vertices_all_k_and_multiplicities": "PROVED_IN_ARCHIVED_PROOFS",
            "dominant_neighbor_contraction": "PROVED_IN_ARCHIVED_PROOFS",
            "six_vertices_nontrivial_critical_cut": "PROVED_IN_ARCHIVED_PROOFS",
            "six_vertices_minimum_edges_6k_plus_3": "PROVED_IN_ARCHIVED_PROOFS",
            "six_vertices_6k_plus_4_excess_single_high_2": "PROVED_IN_ARCHIVED_PROOFS",
            "six_vertices_6k_plus_4_excess_two_high_1_1": "OPEN",
            "six_vertex_next_layer_candidates_in_handoff_section_11": "UNAUDITED_CANDIDATES_NOT_PROVED",
            "B_plus": "PROVED_IN_ARCHIVED_PROOFS",
            "nonboundary_lift": "PROVED_IN_ARCHIVED_PROOFS",
            "genuine_critical_all_proper_mu_ge_2_fiber": "PROVED_IN_ARCHIVED_PROOFS",
            "small_critical_fiber_up_to_three": "PROVED_IN_ARCHIVED_PROOFS",
        },
        "delivery_verification": {
            "existing_sha_records": hash_records,
            "new_document_relative_links_checked": checked_links,
            "new_math_probe_runs": [],
            "six_vertex_candidate_probe_runs": [],
            "note": "This delivery checks file provenance and archive contents; existing PASS runs remain prior research evidence.",
        },
        "package_policy": {
            "selection": "root Markdown; scripts Python/C++; data JSON/SHA records; original source and prompt copies",
            "excluded": ["local executable binaries", "unrelated course files", "other archive subdirectories", "ZIP itself"],
            "historical_environment_hash_record": "Validated on the previous host; its .exe target is deliberately excluded from this portable archive.",
            "manifest_self_hash": "Excluded to avoid circular self-reference",
        },
        "files": inventory,
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    package_path = ROOT / PACKAGE
    with zipfile.ZipFile(package_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in selected:
            archive.write(path, arcname=path.relative_to(ROOT).as_posix())

    with zipfile.ZipFile(package_path) as archive:
        check(archive.testzip() is None, "Archive CRC check failed")
        names = set(archive.namelist())
        expected_names = {p.relative_to(ROOT).as_posix() for p in selected}
        check(names == expected_names, "Archive membership mismatch")
        for relative, facts in inventory.items():
            payload = archive.read(relative)
            check(len(payload) == facts["bytes"] and hashlib.sha256(payload).hexdigest() == facts["sha256"],
                  f"Archive content mismatch: {relative}")
        check(archive.read(manifest_path.relative_to(ROOT).as_posix()) == manifest_path.read_bytes(),
              "Archived manifest differs")

    package_hash = digest(package_path)
    (ROOT / f"{PACKAGE}.sha256").write_text(f"{package_hash}  {PACKAGE}\n", encoding="utf-8")
    print(json.dumps({
        "result": "PASS", "files_in_archive": len(selected), "archive_bytes": package_path.stat().st_size,
        "archive_sha256": package_hash, "sha_records_verified": len(hash_records),
        "sha_targets_verified": sum(len(record["checked"]) for record in hash_records),
        "new_document_links_verified": checked_links, "math_probes_rerun": False,
        "source_original_preserved": True,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
