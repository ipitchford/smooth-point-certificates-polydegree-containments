#!/usr/bin/env python3
"""Strictly validate the exact d=21..30 affine-computation receipts.

This validator checks receipt structure and all theorem-relevant fields.  It
does not recompute the Groebner bases, so the memo treats it as validation of
finite producer evidence rather than an independent reproduction.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


SUMMARY_TRUE_FIELDS = [
    "all_affine_lengths_match_floor_d_d1_over_6",
    "all_affine_schemes_disjoint_from_g_d2",
    "all_affine_schemes_reduced_by_jacobian_criterion",
    "all_newton_mixed_volumes_match_floor_d_d1_over_6",
    "all_weighted_projective_pairs_proper",
]

ROW_TRUE_FIELDS = [
    "affine_disjoint_from_g_d2",
    "affine_length_matches_formula",
    "affine_reduced_by_jacobian_criterion",
    "mixed_volume_matches_formula",
]


def fail(message: str) -> None:
    raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while block := handle.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def require_equal(actual: object, expected: object, context: str) -> None:
    if actual != expected:
        fail(f"{context}: expected {expected!r}, received {actual!r}")


def load_json(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        fail(f"cannot read {path}: {error}")
    if not isinstance(value, dict):
        fail(f"top-level JSON value is not an object in {path}")
    return value


def validate_single(path: Path, d: int) -> dict[str, object]:
    receipt = load_json(path)
    require_equal(receipt.get("schema"), "polydegree.e3.geometry-exploration.v1", f"{path}:schema")
    require_equal(receipt.get("arithmetic"), "exact QQ polynomial arithmetic", f"{path}:arithmetic")
    require_equal(receipt.get("range"), [d, d], f"{path}:range")
    for field in SUMMARY_TRUE_FIELDS:
        require_equal(receipt.get(field), True, f"{path}:{field}")
    rows = receipt.get("rows")
    if not isinstance(rows, list) or len(rows) != 1 or not isinstance(rows[0], dict):
        fail(f"{path}: expected exactly one object in rows")
    row = rows[0]
    expected_length = d * (d + 1) // 6
    require_equal(row.get("d"), d, f"{path}:row.d")
    for field in ROW_TRUE_FIELDS:
        require_equal(row.get(field), True, f"{path}:row.{field}")
    expected_values = {
        "dim": 0,
        "vdim": expected_length,
        "sing_vdim": 0,
        "next_vdim": 0,
        "expected_affine_length_floor_d_d1_over_6": expected_length,
        "newton_mixed_volume": expected_length,
        "homogeneous_gcd_total_degree": 0,
        "affine_gcd_total_degree": 0,
    }
    for field, expected in expected_values.items():
        require_equal(row.get(field), expected, f"{path}:row.{field}")
    require_equal(row.get("homogeneous_gcd"), "1", f"{path}:row.homogeneous_gcd")
    predicted_boundary_degree = 1 if d % 3 == 1 else 0
    predicted_boundary_gcd = "X" if predicted_boundary_degree else "1"
    require_equal(
        row.get("boundary_gcd_total_degree"),
        predicted_boundary_degree,
        f"{path}:row.boundary_gcd_total_degree",
    )
    require_equal(row.get("boundary_gcd"), predicted_boundary_gcd, f"{path}:row.boundary_gcd")
    return row


def analyze(directory: Path, d_min: int, d_max: int) -> dict[str, object]:
    if d_min < 2 or d_max < d_min:
        fail("require 2 <= d_min <= d_max")
    source_receipts = []
    rows = []
    for d in range(d_min, d_max + 1):
        path = directory / f"affine_d{d}.json"
        if not path.is_file():
            fail(f"missing source receipt {path}")
        row = validate_single(path, d)
        rows.append(
            {
                "d": d,
                "length": row["vdim"],
                "jacobian_quotient_vdim": row["sing_vdim"],
                "g_d2_quotient_vdim": row["next_vdim"],
            }
        )
        source_receipts.append({"file": path.name, "sha256": sha256(path)})

    combined_path = directory / f"affine_{d_min}_{d_max}.json"
    combined_validation: dict[str, object]
    if combined_path.is_file():
        combined = load_json(combined_path)
        require_equal(combined.get("range"), [d_min, d_max], f"{combined_path}:range")
        for field in SUMMARY_TRUE_FIELDS:
            require_equal(combined.get(field), True, f"{combined_path}:{field}")
        combined_rows = combined.get("rows")
        if not isinstance(combined_rows, list):
            fail(f"{combined_path}:rows is not a list")
        require_equal(
            [row.get("d") if isinstance(row, dict) else None for row in combined_rows],
            list(range(d_min, d_max + 1)),
            f"{combined_path}:row indices",
        )
        combined_validation = {
            "file": combined_path.name,
            "sha256": sha256(combined_path),
            "validated": True,
        }
    else:
        combined_validation = {"file": combined_path.name, "validated": False, "reason": "absent"}

    return {
        "schema": "irreducible-norms.affine-receipt-validation.v1",
        "status": "PASS",
        "range": [d_min, d_max],
        "assertions_used_for_acceptance": False,
        "interpretation": {
            "vdim": "length of QQ[X,Y]/(G_d,G_(d+1))",
            "sing_vdim_zero": "(G_d,G_(d+1),J_d) is the unit ideal",
            "next_vdim_zero": "(G_d,G_(d+1),G_(d+2)) is the unit ideal",
        },
        "all_lengths_equal_floor_d_d1_over_6": True,
        "all_jacobian_quotients_are_unit_ideal": True,
        "all_g_d2_quotients_are_unit_ideal": True,
        "rows": rows,
        "source_receipts": source_receipts,
        "combined_receipt": combined_validation,
        "independence_limit": (
            "schema/hash validation only; Groebner bases were produced by the existing "
            "geometry exploration program and are not recomputed here"
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--d-min", type=int, default=21)
    parser.add_argument("--d-max", type=int, default=30)
    parser.add_argument("--json", type=Path)
    arguments = parser.parse_args()
    report = analyze(arguments.directory.resolve(), arguments.d_min, arguments.d_max)
    rendered = json.dumps(report, indent=2, sort_keys=True)
    print(rendered)
    if arguments.json is not None:
        arguments.json.parent.mkdir(parents=True, exist_ok=True)
        arguments.json.write_text(rendered + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
