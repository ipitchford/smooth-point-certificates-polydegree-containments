#!/usr/bin/env python3
"""Mutation and negative controls for verify_jacobian_refactor.py.

Every control is expected to expose an invalid certificate or invalid formula.
The runner uses explicit failures so its behaviour is unchanged by python -O.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any, Callable

import verify_jacobian_refactor as verifier


def finite_field_values(d: int, p: int, point: tuple[int, int, int]) -> dict[str, int]:
    g = [
        verifier.poly_eval_mod(verifier.g_polynomial(d + offset, 3), point, p)
        for offset in range(3)
    ]
    derivative_rows = [
        [
            verifier.poly_eval_mod(
                verifier.poly_derivative(verifier.g_polynomial(d + offset, 3), variable),
                point,
                p,
            )
            for variable in (1, 2)
        ]
        for offset in (0, 1)
    ]
    jacobian = verifier.integer_determinant(derivative_rows) % p
    alpha_matrix = [
        [
            verifier.poly_eval_mod(verifier.alpha_polynomial(i, j, 3), point, p)
            for j in range(d - 1, d + 2)
        ]
        for i in range(3)
    ]
    return {
        "g_d": g[0],
        "g_d1": g[1],
        "g_d2": g[2],
        "jac23": jacobian,
        "a": verifier.integer_determinant(alpha_matrix) % p,
    }


def locate_bad_characteristic_rescue() -> dict[str, Any] | None:
    """Find a J-based witness with p | d+2 and a=0 modulo p.

    Such a point fails the legacy mod-p a-unit test but remains valid for the
    refactored lifting argument: at the exact Q_p lift, d+2 is nonzero (though
    nonunit), so the Euler--Jacobian identity makes a nonzero in Q_p.
    """

    fallback: dict[str, Any] | None = None
    for d in range(2, 21):
        for p in (2, 3, 5, 7, 11, 13, 17, 19):
            if (d + 2) % p:
                continue
            found: list[dict[str, Any]] = []
            for u in range(p):
                for v in range(p):
                    point = (1, u, v)
                    values = finite_field_values(d, p, point)
                    if values["g_d"] == values["g_d1"] == 0:
                        if values["a"] != 0:
                            raise verifier.VerificationError(
                                f"bad-characteristic identity violation at d={d}, p={p}, point={point}"
                            )
                        found.append({"point": list(point), **values})
            if found:
                sharp = next(
                    (
                        example
                        for example in found
                        if example["g_d2"] != 0 and example["jac23"] != 0
                    ),
                    None,
                )
                candidate = {
                    "d": d,
                    "p": p,
                    "common_zeros_checked": len(found),
                    "example": sharp or found[0],
                    "all_other_unit_factors_nonzero": sharp is not None,
                    "refactored_j_based_finite_field_hypotheses": sharp is not None,
                    "legacy_mod_p_a_unit_certificate": False,
                }
                if sharp is not None:
                    return candidate
                if fallback is None:
                    fallback = candidate
    return fallback


def locate_singular_control() -> dict[str, Any] | None:
    """Find a common zero with vanishing affine Jacobian."""

    for d in range(2, 16):
        for p in (5, 7, 11, 13):
            for u in range(p):
                for v in range(p):
                    point = (1, u, v)
                    values = finite_field_values(d, p, point)
                    if (
                        values["g_d"] == 0
                        and values["g_d1"] == 0
                        and values["jac23"] == 0
                    ):
                        return {"d": d, "p": p, "point": list(point), **values}
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--witness-data", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    payload = verifier.load_witness_payload(args.witness_data)
    controls: list[dict[str, Any]] = []

    def control(
        name: str,
        detected: bool,
        evidence: Any,
        control_type: str = "mutation or negative control",
    ) -> None:
        controls.append(
            {
                "name": name,
                "control_type": control_type,
                "status": "PASS" if detected else "FAIL",
                "evidence": evidence,
            }
        )

    data_mutations: list[tuple[str, Callable[[dict[str, Any]], None]]] = []

    def mutate_a(candidate: dict[str, Any]) -> None:
        candidate["witnesses"][0]["a"] += 1

    def mutate_jacobian(candidate: dict[str, Any]) -> None:
        candidate["witnesses"][0]["jac23"] += 1

    def mutate_g_next(candidate: dict[str, Any]) -> None:
        candidate["witnesses"][0]["g_next"] += 1

    def mutate_point(candidate: dict[str, Any]) -> None:
        row = candidate["witnesses"][0]
        row["point"][1] = (row["point"][1] + 1) % row["p"]

    def mutate_prime(candidate: dict[str, Any]) -> None:
        candidate["witnesses"][0]["p"] **= 2

    def mutate_chart(candidate: dict[str, Any]) -> None:
        candidate["witnesses"][0]["point"][0] = 0

    def remove_row(candidate: dict[str, Any]) -> None:
        del candidate["witnesses"][20]

    def mutate_type(candidate: dict[str, Any]) -> None:
        candidate["witnesses"][0]["d"] = True

    data_mutations.extend(
        [
            ("recorded a residue +1", mutate_a),
            ("recorded Jacobian residue +1", mutate_jacobian),
            ("recorded next-g residue +1", mutate_g_next),
            ("affine point coordinate +1", mutate_point),
            ("prime replaced by its square", mutate_prime),
            ("x1 chart coordinate changed to zero", mutate_chart),
            ("one witness row removed", remove_row),
            ("integer d replaced by boolean", mutate_type),
        ]
    )

    for name, mutation in data_mutations:
        candidate = copy.deepcopy(payload)
        mutation(candidate)
        result = verifier.verify_witness_payload(candidate)
        control(name, result["status"] == "FAIL", result["failures"][:3])

    # Formula-level mutations use exact polynomials or exact integer evaluation.
    e, i, j = 3, 1, 5
    derivative = verifier.poly_derivative(verifier.g_polynomial(j + 1, e), i)
    alpha = verifier.alpha_polynomial(i, j, e)
    control(
        "wrong sign in derivative identity",
        alpha != derivative and alpha == verifier.poly_scale(derivative, -1),
        {"e": e, "i": i, "j": j, "alpha_terms": len(alpha)},
    )
    shifted_alpha = verifier.alpha_polynomial(i, j + 1, e)
    control(
        "one-step alpha column shift",
        shifted_alpha != verifier.poly_scale(derivative, -1),
        {"e": e, "i": i, "j": j},
    )

    d = 6
    point = (1, 2, 3)
    derivative_matrix = [
        [
            verifier.poly_eval(
                verifier.poly_derivative(verifier.g_polynomial(d + row, e), variable),
                point,
            )
            for variable in range(e)
        ]
        for row in range(e)
    ]
    alpha_matrix = [
        [
            verifier.poly_eval(verifier.alpha_polynomial(variable, column, e), point)
            for column in range(d - 1, d + 2)
        ]
        for variable in range(e)
    ]
    a_value = verifier.integer_determinant(alpha_matrix)
    full_jacobian = verifier.integer_determinant(derivative_matrix)
    control(
        "wrong determinant sign",
        full_jacobian != 0
        and a_value == (-1) ** e * full_jacobian
        and a_value != (-1) ** (e + 1) * full_jacobian,
        {"a": a_value, "full_jacobian": full_jacobian, "e": e},
    )

    g = verifier.g_polynomial(6, 3)
    ordinary_euler = sum(
        point[variable] * verifier.poly_eval(verifier.poly_derivative(g, variable), point)
        for variable in range(3)
    )
    weighted_euler = sum(
        (variable + 1)
        * point[variable]
        * verifier.poly_eval(verifier.poly_derivative(g, variable), point)
        for variable in range(3)
    )
    expected_euler = 6 * verifier.poly_eval(g, point)
    control(
        "ordinary weights substituted for weighted Euler coefficients",
        weighted_euler == expected_euler and ordinary_euler != expected_euler,
        {
            "ordinary": ordinary_euler,
            "weighted": weighted_euler,
            "expected": expected_euler,
        },
    )

    first = payload["witnesses"][0]
    d = first["d"]
    p = first["p"]
    wrong_factor = (-(d + 1) * first["g_next"] * first["jac23"]) % p
    wrong_sign = ((d + 2) * first["g_next"] * first["jac23"]) % p
    control(
        "d+1 substituted for d+2 in e=3 relation",
        wrong_factor != first["a"] % p,
        {"wrong_rhs": wrong_factor, "recorded_a": first["a"] % p},
    )
    control(
        "positive substituted for negative Euler--Jacobian sign",
        wrong_sign != first["a"] % p,
        {"wrong_rhs": wrong_sign, "recorded_a": first["a"] % p},
    )

    bad_characteristic = locate_bad_characteristic_rescue()
    control(
        "bad-characteristic rescue: J-based hypotheses pass while the mod-p a-unit test fails",
        (
            bad_characteristic is not None
            and bad_characteristic["all_other_unit_factors_nonzero"]
            and bad_characteristic["example"]["a"] == 0
        ),
        bad_characteristic or "no bounded bad-characteristic rescue fixture found",
        control_type="positive theorem-regression fixture",
    )
    singular = locate_singular_control()
    control(
        "singular common-zero negative control exists and has J=0",
        singular is not None and singular["jac23"] == 0,
        singular or "no bounded singular control found",
    )

    # Unlike the archive's assert, the replacement coefficient-integrality
    # guard must remain active under python -O.  Inject a deliberately invalid
    # primitive factorial ratio and require an explicit exception.
    original_ratio = verifier._factorial_multinomial
    explicit_guard_triggered = False
    try:
        verifier.g_polynomial.cache_clear()
        verifier._factorial_multinomial = lambda _a, _tail: 1
        try:
            verifier.g_polynomial(1, 3)
        except verifier.VerificationError:
            explicit_guard_triggered = True
    finally:
        verifier._factorial_multinomial = original_ratio
        verifier.g_polynomial.cache_clear()
    control(
        "replacement integrality guard survives optimized mode",
        explicit_guard_triggered,
        {"guard_triggered": explicit_guard_triggered, "python_optimize": sys.flags.optimize},
    )

    passed = sum(item["status"] == "PASS" for item in controls)
    report = {
        "schema": "irreducible-norms.jacobian-refactor-mutation-and-regression-controls.v2",
        "optimization_safe": "no proof-critical assert statements",
        "controls_passed": passed,
        "controls_total": len(controls),
        "overall_status": "PASS" if passed == len(controls) else "FAIL",
        "controls": controls,
    }
    print("Jacobian-refactor mutation and regression controls")
    print(f"Controls: {passed}/{len(controls)}")
    print(f"Overall status: {report['overall_status']}")
    if args.report is not None:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if report["overall_status"] != "PASS":
        for item in controls:
            if item["status"] == "FAIL":
                print(f"FAIL: {item['name']}: {item['evidence']}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
