#!/usr/bin/env python3
"""Enumerate manuscript paragraphs, citations, references, and claim records.

This deliberately uses only the Python standard library and treats the frozen
Stage 2 directory as read-only input.  It is an audit-scope generator, not a
proof or citation verifier.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


CITATION_PATTERN = re.compile(r"(?<![\w-])@([A-Za-z0-9_:-]+)")
BIB_KEY_PATTERN = re.compile(r"^\s*@\w+\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
LIST_PATTERN = re.compile(r"^(?:[-*+] |\d+[.)]\s+)")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def clean_heading(value: str) -> str:
    value = re.sub(r"\s*\{[^{}]*\}\s*$", "", value)
    return re.sub(r"\s+", " ", value).strip()


def prose_paragraphs(text: str) -> list[dict[str, object]]:
    lines = text.splitlines()
    sections: dict[int, str] = {}
    paragraphs: list[dict[str, object]] = []
    buffer: list[str] = []
    start_line = 0
    in_frontmatter = False
    frontmatter_seen = False
    in_code = False
    in_math = False

    def current_section() -> str:
        return " > ".join(sections[level] for level in sorted(sections))

    def flush(end_line: int) -> None:
        nonlocal buffer, start_line
        if not buffer:
            return
        value = " ".join(part.strip() for part in buffer)
        value = re.sub(r"\s+", " ", value).strip()
        buffer = []
        if not value:
            return
        if value.startswith(("|", "<", "![](")):
            return
        if re.fullmatch(r"[-:| ]+", value):
            return
        words = re.findall(r"[A-Za-z][A-Za-z'-]*", value)
        if len(words) < 8:
            return
        paragraphs.append(
            {
                "id": f"P{len(paragraphs) + 1:03d}",
                "section": current_section(),
                "start_line": start_line,
                "end_line": end_line,
                "word_count": len(words),
                "citations": sorted(set(CITATION_PATTERN.findall(value))),
                "text": value,
            }
        )

    for number, raw in enumerate(lines, 1):
        stripped = raw.strip()
        if number == 1 and stripped == "---":
            in_frontmatter = True
            frontmatter_seen = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            continue
        if stripped.startswith("```"):
            flush(number - 1)
            in_code = not in_code
            continue
        if in_code:
            continue
        if stripped == "$$":
            flush(number - 1)
            in_math = not in_math
            continue
        if in_math:
            continue
        heading = HEADING_PATTERN.match(raw)
        if heading:
            flush(number - 1)
            level = len(heading.group(1))
            sections[level] = clean_heading(heading.group(2))
            for deeper in [key for key in sections if key > level]:
                del sections[deeper]
            continue
        if not stripped:
            flush(number - 1)
            continue
        if stripped.startswith(("|", ">")) or re.fullmatch(r"[-:| ]+", stripped):
            flush(number - 1)
            continue
        if LIST_PATTERN.match(stripped):
            flush(number - 1)
            start_line = number
            buffer = [LIST_PATTERN.sub("", stripped, count=1)]
            flush(number)
            continue
        if not buffer:
            start_line = number
        buffer.append(stripped)
    flush(len(lines))
    if not frontmatter_seen:
        raise ValueError("manuscript frontmatter was not detected")
    return paragraphs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    manuscript_path = root / "MANUSCRIPT.md"
    references_path = root / "references.bib"
    claims_path = root / "CLAIM_STATUS.json"

    manuscript = manuscript_path.read_text(encoding="utf-8")
    references = references_path.read_text(encoding="utf-8")
    claim_data = json.loads(claims_path.read_text(encoding="utf-8"))

    citation_occurrences = CITATION_PATTERN.findall(manuscript)
    citation_keys = sorted(set(citation_occurrences))
    reference_keys = sorted(set(BIB_KEY_PATTERN.findall(references)))
    paragraphs = prose_paragraphs(manuscript)
    payload = {
        "schema": "polydegree.stage2_5.integrity-scope.v1",
        "input": {
            "root_name": root.name,
            "manuscript_sha256": sha256(manuscript_path),
            "references_sha256": sha256(references_path),
            "claims_sha256": sha256(claims_path),
        },
        "paragraphs": paragraphs,
        "paragraph_count": len(paragraphs),
        "minimum_originality_sample_30_percent": (3 * len(paragraphs) + 9) // 10,
        "citation_occurrences": len(citation_occurrences),
        "citation_keys": citation_keys,
        "reference_keys": reference_keys,
        "dangling_citation_keys": sorted(set(citation_keys) - set(reference_keys)),
        "orphan_reference_keys": sorted(set(reference_keys) - set(citation_keys)),
        "claim_count": len(claim_data.get("claims", [])),
        "claim_ids": [item.get("id") for item in claim_data.get("claims", [])],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        "SCOPE PASS: "
        f"{payload['paragraph_count']} prose paragraphs; "
        f"minimum sample {payload['minimum_originality_sample_30_percent']}; "
        f"{len(citation_keys)}/{len(reference_keys)} citation/reference keys; "
        f"{payload['claim_count']} claims"
    )
    if payload["dangling_citation_keys"] or payload["orphan_reference_keys"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
