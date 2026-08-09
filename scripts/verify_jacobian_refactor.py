#!/usr/bin/env python3
"""Independent exact verifier for the proposed Polydegree Jacobian refactor.

This file deliberately imports no code from the v0.2.0 archive.  It rebuilds
the Lewis--Perry--Straub polynomials from factorial ratios, represents them as
sparse dictionaries over the integers, differentiates those dictionaries, and
uses a generic permutation determinant.

What it checks:

* alpha_{i,j,e} = - d(g_{j+1,e})/d(x_{i+1}) coefficient by coefficient;
* weighted Euler identities for g_{n,e};
* a_{d,e} = (-1)^e det D(g_d,...,g_{d+e-1});
* the exact ideal-membership certificate behind the Euler--Jacobian
  congruence, for a bounded collection of small (d,e) cases;
* the Euler--Jacobian relation and all defining residues at every supplied
  e=3 finite-field witness, while distinguishing the legacy mod-p a-unit
  certificate from the weaker J-based finite-field hypotheses.

The sweeps are exact but bounded; they are regression evidence for the general
paper proof, not a proof for all d and e.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable, Sequence


Exponent = tuple[int, ...]
Polynomial = dict[Exponent, int]


class VerificationError(RuntimeError):
    """Fail-closed error for malformed data or non-integral coefficients."""


def _integer(value: Any, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise VerificationError(f"{label} must be an integer")
    return value


@lru_cache(maxsize=None)
def weighted_compositions(total: int, variables: int) -> tuple[Exponent, ...]:
    """Enumerate a with sum((s+1)*a_s) == total.

    The recursion removes the largest weight first.  This is intentionally a
    different enumeration route from both archive implementations.
    """

    if total < 0:
        return ()
    if variables < 1:
        raise VerificationError("variables must be positive")
    if variables == 1:
        return ((total,),)
    out: list[Exponent] = []
    for last in range(total // variables + 1):
        remainder = total - variables * last
        for prefix in weighted_compositions(remainder, variables - 1):
            out.append(prefix + (last,))
    return tuple(out)


def _factorial_multinomial(a: Exponent, tail: int) -> int:
    numerator = math.factorial(tail + sum(a))
    denominator = math.factorial(tail)
    for exponent in a:
        denominator *= math.factorial(exponent)
    quotient, remainder = divmod(numerator, denominator)
    if remainder:
        raise VerificationError(
            f"non-integral multinomial ratio for a={a}, tail={tail}"
        )
    return quotient


@lru_cache(maxsize=None)
def g_polynomial(n: int, e: int) -> Polynomial:
    """Return g_{n,e} as an exact sparse integer polynomial."""

    if n < 0 or e < 1:
        raise VerificationError("g indices require n >= 0 and e >= 1")
    polynomial: Polynomial = {}
    for a in weighted_compositions(n, e):
        numerator = (-1) ** sum(a) * _factorial_multinomial(a, n)
        coefficient, remainder = divmod(numerator, n + 1)
        if remainder:
            raise VerificationError(
                f"non-integral g coefficient for n={n}, e={e}, a={a}"
            )
        if coefficient:
            polynomial[a] = coefficient
    return polynomial


@lru_cache(maxsize=None)
def alpha_polynomial(i: int, j: int, e: int) -> Polynomial:
    """Return alpha_{i,j,e} from its defining multinomial sum."""

    if not 0 <= i < e:
        raise VerificationError(f"alpha row i={i} is outside 0..{e - 1}")
    target = j - i
    if target < 0:
        return {}
    polynomial: Polynomial = {}
    for a in weighted_compositions(target, e):
        coefficient = (-1) ** sum(a) * _factorial_multinomial(a, j + 2)
        if coefficient:
            polynomial[a] = coefficient
    return polynomial


def poly_scale(polynomial: Polynomial, scalar: int) -> Polynomial:
    if scalar == 0:
        return {}
    return {
        exponent: scalar * coefficient
        for exponent, coefficient in polynomial.items()
        if scalar * coefficient
    }


def poly_add(*polynomials: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            updated = out.get(exponent, 0) + coefficient
            if updated:
                out[exponent] = updated
            elif exponent in out:
                del out[exponent]
    return out


def poly_mul(left: Polynomial, right: Polynomial) -> Polynomial:
    if not left or not right:
        return {}
    out: Polynomial = {}
    for left_exp, left_coefficient in left.items():
        for right_exp, right_coefficient in right.items():
            exponent = tuple(a + b for a, b in zip(left_exp, right_exp))
            updated = out.get(exponent, 0) + left_coefficient * right_coefficient
            if updated:
                out[exponent] = updated
            elif exponent in out:
                del out[exponent]
    return out


def poly_derivative(polynomial: Polynomial, variable: int) -> Polynomial:
    out: Polynomial = {}
    for exponent, coefficient in polynomial.items():
        power = exponent[variable]
        if power == 0:
            continue
        reduced = list(exponent)
        reduced[variable] -= 1
        out[tuple(reduced)] = coefficient * power
    return out


def poly_times_variable(polynomial: Polynomial, variable: int) -> Polynomial:
    out: Polynomial = {}
    for exponent, coefficient in polynomial.items():
        raised = list(exponent)
        raised[variable] += 1
        out[tuple(raised)] = coefficient
    return out


def poly_eval(polynomial: Polynomial, point: Sequence[int]) -> int:
    total = 0
    for exponent, coefficient in polynomial.items():
        term = coefficient
        for coordinate, power in zip(point, exponent):
            term *= coordinate**power
        total += term
    return total


def poly_eval_mod(polynomial: Polynomial, point: Sequence[int], prime: int) -> int:
    total = 0
    for exponent, coefficient in polynomial.items():
        term = coefficient % prime
        for coordinate, power in zip(point, exponent):
            term = term * pow(coordinate, power, prime) % prime
        total = (total + term) % prime
    return total


def _permutation_sign(permutation: Sequence[int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def integer_determinant(matrix: Sequence[Sequence[int]]) -> int:
    size = len(matrix)
    if size == 0:
        return 1
    if any(len(row) != size for row in matrix):
        raise VerificationError("determinant requires a square matrix")
    total = 0
    for permutation in itertools.permutations(range(size)):
        term = _permutation_sign(permutation)
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def polynomial_determinant(matrix: Sequence[Sequence[Polynomial]]) -> Polynomial:
    size = len(matrix)
    if size == 0:
        return {(): 1}
    if any(len(row) != size for row in matrix):
        raise VerificationError("polynomial determinant requires a square matrix")
    variables = 0
    for row in matrix:
        for polynomial in row:
            if polynomial:
                variables = len(next(iter(polynomial)))
                break
        if variables:
            break
    one: Polynomial = {(0,) * variables: 1}
    terms: list[Polynomial] = []
    for permutation in itertools.permutations(range(size)):
        term = one
        for row, column in enumerate(permutation):
            term = poly_mul(term, matrix[row][column])
            if not term:
                break
        if term:
            terms.append(poly_scale(term, _permutation_sign(permutation)))
    return poly_add(*terms)


def _minor(matrix: Sequence[Sequence[Polynomial]], omitted_row: int) -> list[list[Polynomial]]:
    return [
        list(row[1:])
        for row_index, row in enumerate(matrix)
        if row_index != omitted_row
    ]


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, math.isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def _record(checks: list[dict[str, Any]], name: str, failures: list[str], evidence: str) -> None:
    checks.append(
        {
            "name": name,
            "status": "PASS" if not failures else "FAIL",
            "evidence": evidence,
            "failures": failures[:20],
        }
    )


def verify_symbolic_identities() -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    derivative_failures: list[str] = []
    derivative_cases = 0
    for e in range(2, 6):
        for j in range(0, 17):
            g = g_polynomial(j + 1, e)
            for i in range(e):
                derivative_cases += 1
                observed = alpha_polynomial(i, j, e)
                expected = poly_scale(poly_derivative(g, i), -1)
                if observed != expected:
                    derivative_failures.append(f"e={e}, i={i}, j={j}")
    _record(
        checks,
        "coefficientwise derivative identity",
        derivative_failures,
        f"{derivative_cases} exact coefficient-dictionary comparisons; e=2..5, j=0..16",
    )

    euler_failures: list[str] = []
    euler_cases = 0
    for e in range(2, 6):
        for n in range(1, 17):
            euler_cases += 1
            g = g_polynomial(n, e)
            weighted_terms = [
                poly_scale(poly_times_variable(poly_derivative(g, variable), variable), variable + 1)
                for variable in range(e)
            ]
            if poly_add(*weighted_terms) != poly_scale(g, n):
                euler_failures.append(f"e={e}, n={n}")
    _record(
        checks,
        "weighted Euler identity",
        euler_failures,
        f"{euler_cases} exact coefficient-dictionary comparisons; e=2..5, n=1..16",
    )

    exact_cases = ((2, 2), (2, 5), (3, 2), (3, 4), (3, 6), (4, 2), (4, 3))
    for e, d in exact_cases:
        failures: list[str] = []
        g_rows = [g_polynomial(d + row, e) for row in range(e)]
        derivative_matrix = [
            [poly_derivative(g, variable) for variable in range(e)]
            for g in g_rows
        ]
        alpha_matrix = [
            [alpha_polynomial(variable, j, e) for j in range(d - 1, d + e - 1)]
            for variable in range(e)
        ]
        a_from_definition = polynomial_determinant(alpha_matrix)
        full_jacobian = polynomial_determinant(derivative_matrix)
        if a_from_definition != poly_scale(full_jacobian, (-1) ** e):
            failures.append("determinant--Jacobian equality failed")

        affine_minor = polynomial_determinant(
            [row[1:] for row in derivative_matrix[:-1]]
        )
        left = poly_add(
            poly_times_variable(a_from_definition, 0),
            poly_scale(poly_mul(g_rows[-1], affine_minor), d + e - 1),
        )
        ideal_terms: list[Polynomial] = []
        for row in range(e - 1):
            cofactor_minor = polynomial_determinant(_minor(derivative_matrix, row))
            scalar = (-1) ** (e + row) * (d + row)
            ideal_terms.append(poly_scale(poly_mul(g_rows[row], cofactor_minor), scalar))
        right = poly_add(*ideal_terms)
        if left != right:
            failures.append("Euler--Jacobian ideal-membership certificate failed")
        _record(
            checks,
            f"exact sparse determinant case e={e}, d={d}",
            failures,
            (
                f"terms: a={len(a_from_definition)}, J={len(affine_minor)}, "
                f"congruence_residual={len(poly_add(left, poly_scale(right, -1)))}"
            ),
        )

    evaluation_failures: list[str] = []
    evaluation_cases = 0
    seed_points = (
        (1, -1, 2, -2, 3),
        (2, 1, -2, 3, -1),
    )
    for e in range(2, 6):
        for d in range(2, 11):
            for seed in seed_points:
                evaluation_cases += 1
                point = seed[:e]
                g_rows = [g_polynomial(d + row, e) for row in range(e)]
                derivative_matrix = [
                    [poly_eval(poly_derivative(g, variable), point) for variable in range(e)]
                    for g in g_rows
                ]
                alpha_matrix = [
                    [
                        poly_eval(alpha_polynomial(variable, j, e), point)
                        for j in range(d - 1, d + e - 1)
                    ]
                    for variable in range(e)
                ]
                a_value = integer_determinant(alpha_matrix)
                jacobian_value = integer_determinant(derivative_matrix)
                if a_value != (-1) ** e * jacobian_value:
                    evaluation_failures.append(
                        f"determinant relation e={e}, d={d}, point={point}"
                    )
                    continue
                affine_minor = integer_determinant([row[1:] for row in derivative_matrix[:-1]])
                left = point[0] * a_value + (d + e - 1) * poly_eval(g_rows[-1], point) * affine_minor
                right = 0
                for row in range(e - 1):
                    numeric_minor = [
                        derivative_matrix[r][1:]
                        for r in range(e)
                        if r != row
                    ]
                    right += (
                        (-1) ** (e + row)
                        * (d + row)
                        * poly_eval(g_rows[row], point)
                        * integer_determinant(numeric_minor)
                    )
                if left != right:
                    evaluation_failures.append(
                        f"Euler--Jacobian relation e={e}, d={d}, point={point}"
                    )
    _record(
        checks,
        "general-e exact-integer evaluation sweep",
        evaluation_failures,
        f"{evaluation_cases} determinant and Euler--Jacobian comparisons; e=2..5, d=2..10",
    )
    return checks


def load_witness_payload(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise VerificationError(f"cannot read witness JSON: {error}") from error
    if not isinstance(payload, dict):
        raise VerificationError("witness payload must be a JSON object")
    return payload


def verify_witness_payload(payload: dict[str, Any]) -> dict[str, Any]:
    failures: list[str] = []
    row_results: list[dict[str, Any]] = []
    if payload.get("schema") != "evidence-press.polydegree-hensel-witnesses.v1":
        failures.append("unexpected or missing witness schema")
    rows = payload.get("witnesses")
    if not isinstance(rows, list):
        return {
            "status": "FAIL",
            "rows_passed": 0,
            "rows_total": 0,
            "failures": failures + ["witnesses must be a list"],
            "results": [],
        }

    parsed_d: list[int] = []
    for index, raw in enumerate(rows):
        row_failures: list[str] = []
        label = f"row[{index}]"
        try:
            if not isinstance(raw, dict):
                raise VerificationError(f"{label} must be an object")
            d = _integer(raw.get("d"), f"{label}.d")
            p = _integer(raw.get("p"), f"{label}.p")
            parsed_d.append(d)
            point_raw = raw.get("point")
            if not isinstance(point_raw, list) or len(point_raw) != 3:
                raise VerificationError(f"{label}.point must contain exactly three integers")
            point = tuple(
                _integer(coordinate, f"{label}.point[{coordinate_index}]")
                for coordinate_index, coordinate in enumerate(point_raw)
            )
            recorded = {
                key: _integer(raw.get(key), f"{label}.{key}")
                for key in ("g_next", "a", "jac23")
            }
            if d < 2:
                row_failures.append("d must be at least 2")
            if not is_prime(p):
                row_failures.append(f"p={p} is not prime")
            if point[0] != 1:
                row_failures.append("point is not in the x1=1 chart")
            if p > 1 and any(not 0 <= coordinate < p for coordinate in point):
                row_failures.append("point coordinates are not canonical residues")
            if p <= 1:
                raise VerificationError(f"{label}.p must exceed 1 for modular evaluation")

            g_values = [
                poly_eval_mod(g_polynomial(d + offset, 3), point, p)
                for offset in range(3)
            ]
            derivative_rows = [
                [
                    poly_eval_mod(poly_derivative(g_polynomial(d + offset, 3), variable), point, p)
                    for variable in (1, 2)
                ]
                for offset in (0, 1)
            ]
            jacobian = integer_determinant(derivative_rows) % p
            alpha_matrix = [
                [
                    poly_eval_mod(alpha_polynomial(i, j, 3), point, p)
                    for j in range(d - 1, d + 2)
                ]
                for i in range(3)
            ]
            a_value = integer_determinant(alpha_matrix) % p
            relation_rhs = (-(d + 2) * g_values[2] * jacobian) % p

            if g_values[0] != 0 or g_values[1] != 0:
                row_failures.append(f"common-zero equations fail: values={g_values[:2]}")
            if g_values[2] != recorded["g_next"] % p:
                row_failures.append(
                    f"g_next={g_values[2]} does not match recorded {recorded['g_next'] % p}"
                )
            if a_value != recorded["a"] % p:
                row_failures.append(
                    f"a={a_value} does not match recorded {recorded['a'] % p}"
                )
            if jacobian != recorded["jac23"] % p:
                row_failures.append(
                    f"jac23={jacobian} does not match recorded {recorded['jac23'] % p}"
                )
            if a_value != relation_rhs:
                row_failures.append(
                    f"Euler--Jacobian relation fails: a={a_value}, rhs={relation_rhs}"
                )
            refactored_j_hypotheses = (
                is_prime(p)
                and point[0] == 1
                and g_values[0] == 0
                and g_values[1] == 0
                and g_values[2] != 0
                and jacobian != 0
            )
            legacy_mod_p_a_unit = refactored_j_hypotheses and a_value != 0
            if g_values[2] == 0 or jacobian == 0:
                row_failures.append(
                    "one or more refactored J-based finite-field unit conditions vanish"
                )
            if a_value == 0:
                row_failures.append(
                    "legacy mod-p a-unit condition fails; the J-based lifting criterion "
                    "may still apply because nonzero in Q_p does not require a mod-p unit"
                )

            row_results.append(
                {
                    "d": d,
                    "p": p,
                    "point": list(point),
                    "computed": {
                        "g_d": g_values[0],
                        "g_d1": g_values[1],
                        "g_d2": g_values[2],
                        "a": a_value,
                        "jac23": jacobian,
                        "euler_jacobian_rhs": relation_rhs,
                    },
                    "criteria": {
                        "refactored_j_based_finite_field_hypotheses": refactored_j_hypotheses,
                        "legacy_mod_p_a_unit_certificate": legacy_mod_p_a_unit,
                        "p_divides_d_plus_2": (d + 2) % p == 0,
                    },
                    "status": "PASS" if not row_failures else "FAIL",
                    "failures": row_failures,
                }
            )
        except (VerificationError, ArithmeticError, ValueError) as error:
            row_failures.append(str(error))
            row_results.append(
                {
                    "index": index,
                    "status": "FAIL",
                    "failures": row_failures,
                }
            )
        failures.extend(f"{label}: {failure}" for failure in row_failures)

    expected_d = list(range(50, 101))
    if parsed_d != expected_d:
        failures.append("witness d-values are not exactly one ordered copy of 50..100")
    range_metadata = payload.get("range")
    if range_metadata != {"d_min": 50, "d_max": 100, "count": 51}:
        failures.append("range metadata does not exactly describe 50..100")
    return {
        "status": "PASS" if not failures else "FAIL",
        "rows_passed": sum(result["status"] == "PASS" for result in row_results),
        "rows_total": len(row_results),
        "failures": failures,
        "results": row_results,
    }


def build_report(witness_path: Path) -> dict[str, Any]:
    symbolic_checks = verify_symbolic_identities()
    witness_report = verify_witness_payload(load_witness_payload(witness_path))
    symbolic_passed = sum(check["status"] == "PASS" for check in symbolic_checks)
    overall = (
        "PASS"
        if symbolic_passed == len(symbolic_checks) and witness_report["status"] == "PASS"
        else "FAIL"
    )
    return {
        "schema": "irreducible-norms.jacobian-refactor-independent-verification.v1",
        "implementation": {
            "language": "Python standard library only",
            "arithmetic": "exact sparse integer polynomials and finite-field residues",
            "archive_code_imported": False,
            "determinant": "generic Leibniz permutation formula",
            "optimization_safe": "no proof-critical assert statements",
        },
        "scope": {
            "symbolic_sweeps_are_bounded": True,
            "witness_relation_range": [50, 100],
            "claim": "regression evidence for a separately written mathematical proof, not a proof for all d,e",
            "criterion_distinction": (
                "p not dividing d+2 is required for a mod-p a-unit certificate, "
                "but not for the J-based Hensel-to-Q_p existence argument"
            ),
        },
        "symbolic_checks_passed": symbolic_passed,
        "symbolic_checks_total": len(symbolic_checks),
        "symbolic_checks": symbolic_checks,
        "witness_verification": witness_report,
        "overall_status": overall,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--witness-data", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    try:
        report = build_report(args.witness_data)
    except (VerificationError, ArithmeticError, OSError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print("Independent Jacobian-refactor verification")
    print(
        f"Symbolic checks: {report['symbolic_checks_passed']}/"
        f"{report['symbolic_checks_total']}"
    )
    witness = report["witness_verification"]
    print(f"Witnesses: {witness['rows_passed']}/{witness['rows_total']}")
    print(f"Overall status: {report['overall_status']}")
    if args.report is not None:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if report["overall_status"] != "PASS":
        for check in report["symbolic_checks"]:
            for failure in check["failures"]:
                print(f"FAIL: {check['name']}: {failure}", file=sys.stderr)
        for failure in witness["failures"]:
            print(f"FAIL: witness: {failure}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
