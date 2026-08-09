#!/usr/bin/env python3
"""Write or verify the SHA-256 manifest for the frozen candidate package."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path, PurePosixPath


MANIFEST_NAME = "MANIFEST.sha256"
LINE_PATTERN = re.compile(r"^([0-9a-f]{64})  (.+)$")
GENERATED_SUFFIXES = (".fdb_latexmk", ".fls", ".synctex.gz")


class ManifestError(RuntimeError):
    """Raised when the package boundary or a recorded digest is invalid."""


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def package_files(root: Path) -> dict[str, Path]:
    files: dict[str, Path] = {}
    for path in root.rglob("*"):
        relative_path = path.relative_to(root)
        if ".git" in relative_path.parts:
            continue
        if path.name.endswith(GENERATED_SUFFIXES):
            continue
        if path.name == MANIFEST_NAME:
            continue
        if path.is_symlink():
            raise ManifestError(f"symbolic links are outside the frozen boundary: {path}")
        if path.is_file():
            relative = relative_path.as_posix()
            files[relative] = path
    return files


def render_manifest(root: Path) -> str:
    files = package_files(root)
    return "".join(f"{sha256(files[name])}  {name}\n" for name in sorted(files))


def parse_manifest(path: Path) -> dict[str, str]:
    if not path.is_file():
        raise ManifestError(f"missing {MANIFEST_NAME}")
    entries: dict[str, str] = {}
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = LINE_PATTERN.fullmatch(line)
        if not match:
            raise ManifestError(f"malformed manifest line {number}")
        digest, relative = match.groups()
        pure = PurePosixPath(relative)
        if pure.is_absolute() or ".." in pure.parts or relative in {"", "."}:
            raise ManifestError(f"unsafe manifest path on line {number}: {relative}")
        if relative in entries:
            raise ManifestError(f"duplicate manifest path: {relative}")
        entries[relative] = digest
    if not entries:
        raise ManifestError("manifest is empty")
    return entries


def verify(root: Path) -> tuple[int, list[str]]:
    expected = parse_manifest(root / MANIFEST_NAME)
    actual = package_files(root)
    failures: list[str] = []
    missing = sorted(set(expected) - set(actual))
    extra = sorted(set(actual) - set(expected))
    failures.extend(f"missing file: {name}" for name in missing)
    failures.extend(f"unmanifested file: {name}" for name in extra)
    for name in sorted(set(expected) & set(actual)):
        observed = sha256(actual[name])
        if observed != expected[name]:
            failures.append(
                f"digest mismatch: {name}: expected {expected[name]}, observed {observed}"
            )
    return len(expected), failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error("--root must be a directory")
    try:
        if args.write:
            (root / MANIFEST_NAME).write_text(render_manifest(root), encoding="utf-8")
        count, failures = verify(root)
    except (OSError, UnicodeError, ManifestError) as exc:
        print(f"MANIFEST FAIL: {exc}", file=sys.stderr)
        return 1
    if failures:
        for failure in failures:
            print(f"MANIFEST FAIL: {failure}", file=sys.stderr)
        return 1
    print(f"MANIFEST PASS: {count}/{count} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
