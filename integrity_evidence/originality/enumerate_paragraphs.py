#!/usr/bin/env python3
"""Enumerate and deterministically sample prose paragraphs from the manuscript."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from pathlib import Path


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
LIST_ITEM_RE = re.compile(r"^\s*(?:\d+[.)]|[-*+])\s+")
WORD_RE = re.compile(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*")


def clean_heading(value: str) -> str:
    return re.sub(r"\s+\{[^}]+\}\s*$", "", value).strip()


def normalize_block(lines: list[str]) -> str:
    text = " ".join(line.strip() for line in lines)
    text = re.sub(r"^>\s*", "", text)
    text = re.sub(r"^\d+\.\s+", "", text)
    text = re.sub(r"^[-*+]\s+", "", text)
    return re.sub(r"\s+", " ", text).strip()


def is_prose_block(lines: list[str]) -> bool:
    stripped = [line.strip() for line in lines if line.strip()]
    if not stripped:
        return False
    if all(line.startswith("|") and line.endswith("|") for line in stripped):
        return False
    if all(re.fullmatch(r"[-:| ]+", line) for line in stripped):
        return False
    text = normalize_block(lines)
    if text.startswith("```") or text.endswith("```"):
        return False
    if text.startswith("$$") or text.endswith("$$"):
        return False
    return len(WORD_RE.findall(text)) >= 4


def risk_score(section_path: str, text: str) -> int:
    target = f"{section_path} {text}".lower()
    score = 10
    if any(term in target for term in ("relation to prior", "novelty", "priority")):
        score += 100
    if any(term in target for term in ("introduction", "discussion", "limitations")):
        score += 75
    if "proof" in section_path.lower():
        score += 65
    if any(term in target for term in ("theorem", "proposition", "corollary", "lemma")):
        score += 35
    if "[@" in text or "arxiv:" in text.lower() or "dlmf" in text.lower():
        score += 45
    if len(WORD_RE.findall(text)) >= 45:
        score += 10
    return score


def enumerate_paragraphs(source: Path) -> list[dict[str, object]]:
    lines = source.read_text(encoding="utf-8").splitlines()
    headings: dict[int, str] = {}
    paragraphs: list[dict[str, object]] = []
    in_yaml = False
    yaml_closed = False
    in_fence = False
    in_display_math = False
    active = False
    block: list[str] = []
    block_start = 0

    def flush(end_line: int) -> None:
        nonlocal block, block_start
        if block and active and is_prose_block(block):
            major = headings.get(1, "")
            if major not in {"Declarations", "References"}:
                text = normalize_block(block)
                path = " > ".join(headings[level] for level in sorted(headings))
                paragraphs.append(
                    {
                        "id": f"P{len(paragraphs) + 1:03d}",
                        "line_start": block_start,
                        "line_end": end_line,
                        "major_section": major,
                        "section_path": path,
                        "text": text,
                        "word_count": len(WORD_RE.findall(text)),
                        "risk_score": risk_score(path, text),
                    }
                )
        block = []
        block_start = 0

    for line_number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if line_number == 1 and stripped == "---":
            in_yaml = True
            continue
        if in_yaml:
            if stripped == "---":
                in_yaml = False
                yaml_closed = True
            continue
        if not yaml_closed:
            yaml_closed = True

        if stripped.startswith("```"):
            flush(line_number - 1)
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if stripped == "$$":
            flush(line_number - 1)
            in_display_math = not in_display_math
            continue
        if in_display_math:
            continue

        heading_match = HEADING_RE.match(line)
        if heading_match:
            flush(line_number - 1)
            level = len(heading_match.group(1))
            headings[level] = clean_heading(heading_match.group(2))
            for deeper in [key for key in headings if key > level]:
                del headings[deeper]
            active = headings.get(1) == "Abstract" or (
                active and headings.get(1) not in {"Declarations", "References"}
            )
            if headings.get(1) in {"Declarations", "References"}:
                active = False
            continue

        if not stripped:
            flush(line_number - 1)
            continue
        if block and LIST_ITEM_RE.match(line):
            flush(line_number - 1)
        if not block:
            block_start = line_number
        block.append(line)

    flush(len(lines))
    return paragraphs


def choose_sample(paragraphs: list[dict[str, object]]) -> list[dict[str, object]]:
    target = math.ceil(0.30 * len(paragraphs))
    eligible = [p for p in paragraphs if int(p["word_count"]) >= 20]
    selected: dict[str, dict[str, object]] = {}

    majors: list[str] = []
    for paragraph in eligible:
        major = str(paragraph["major_section"])
        if major not in majors:
            majors.append(major)
    for major in majors:
        candidates = [p for p in eligible if p["major_section"] == major]
        best = max(candidates, key=lambda p: (int(p["risk_score"]), int(p["word_count"])))
        selected[str(best["id"])] = best

    ordered = sorted(
        eligible,
        key=lambda p: (
            -int(p["risk_score"]),
            hashlib.sha256((str(p["id"]) + str(p["text"])).encode()).hexdigest(),
        ),
    )
    for paragraph in ordered:
        if len(selected) >= target:
            break
        selected[str(paragraph["id"])] = paragraph

    return sorted(selected.values(), key=lambda p: int(str(p["id"])[1:]))


def write_markdown(path: Path, paragraphs: list[dict[str, object]], sample_ids: set[str]) -> None:
    rows = [
        "# Paragraph inventory",
        "",
        "Body scope: Abstract through Conclusion; Declarations and References excluded.",
        "",
        "| ID | Lines | Major section | Section path | Words | Risk | Sampled | Text |",
        "|---|---:|---|---|---:|---:|---|---|",
    ]
    for p in paragraphs:
        text = str(p["text"]).replace("|", "\\|")
        rows.append(
            f"| {p['id']} | {p['line_start']}-{p['line_end']} | "
            f"{p['major_section']} | {p['section_path']} | {p['word_count']} | "
            f"{p['risk_score']} | {'yes' if p['id'] in sample_ids else 'no'} | {text} |"
        )
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manuscript", type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    paragraphs = enumerate_paragraphs(args.manuscript)
    sample = choose_sample(paragraphs)
    inventory = {
        "schema": "evidence-press.originality.paragraph-inventory.v1",
        "source": str(args.manuscript.resolve()),
        "body_scope": "Abstract through Conclusion; Declarations and References excluded",
        "total_body_paragraphs": len(paragraphs),
        "paragraphs": paragraphs,
    }
    plan = {
        "schema": "evidence-press.originality.sample-plan.v1",
        "mode": "Stage 2.5 pre-review",
        "minimum_rate": 0.30,
        "total_body_paragraphs": len(paragraphs),
        "sampled_paragraphs": len(sample),
        "sampling_rate": len(sample) / len(paragraphs) if paragraphs else 0,
        "major_sections": list(dict.fromkeys(str(p["major_section"]) for p in paragraphs)),
        "sample": sample,
    }
    (args.out_dir / "paragraph_inventory.json").write_text(
        json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (args.out_dir / "sample_plan.json").write_text(
        json.dumps(plan, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    write_markdown(
        args.out_dir / "paragraph_inventory.md",
        paragraphs,
        {str(p["id"]) for p in sample},
    )
    print(json.dumps({key: plan[key] for key in ("total_body_paragraphs", "sampled_paragraphs", "sampling_rate", "major_sections")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
