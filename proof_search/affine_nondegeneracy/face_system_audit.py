#!/usr/bin/env python3
"""Fail-closed exact audit of the Newton-face reduction for the e=3 family.

This is finite evidence, not an all-d proof.  The accompanying memo supplies
the elementary residue-class arguments and labels the remaining theorem gaps.
No verifier from the candidate archive is imported.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy as sp


X, Y, s, z = sp.symbols("X Y s z")


def fail(message: str) -> None:
    raise RuntimeError(message)


def coefficient(n: int, b: int, c: int) -> sp.Rational:
    """Coefficient of X^b Y^c in G_n, from Lagrange inversion."""
    a = n - 2 * b - 3 * c
    if n < 0 or b < 0 or c < 0 or a < 0:
        fail(f"invalid coefficient index n={n}, b={b}, c={c}")
    return sp.Rational(
        (-1) ** (n - b) * math.factorial(2 * n - b - 2 * c),
        (n + 1)
        * math.factorial(n)
        * math.factorial(a)
        * math.factorial(b)
        * math.factorial(c),
    )


def support(n: int) -> list[tuple[int, int]]:
    return [
        (b, c)
        for c in range(n // 3 + 1)
        for b in range((n - 3 * c) // 2 + 1)
    ]


def vertical_face(n: int) -> sp.Poly:
    """G_n(X,0): the c=0 Newton face."""
    return sp.Poly(
        sum((coefficient(n, b, 0) * X**b for b in range(n // 2 + 1)), sp.S.Zero),
        X,
        domain=sp.QQ,
    )


def horizontal_face(n: int) -> sp.Poly:
    """G_n(0,Y): the b=0 Newton face."""
    return sp.Poly(
        sum((coefficient(n, 0, c) * Y**c for c in range(n // 3 + 1)), sp.S.Zero),
        Y,
        domain=sp.QQ,
    )


def top_torus_face(n: int) -> sp.Poly:
    """Univariate top face after z=Y^2/X^3 and a monomial is removed."""
    epsilon = n % 2
    a_value = (n - 3 * epsilon) // 2
    if a_value < 0:
        fail(f"negative top-face exponent at n={n}")
    expression = sp.S.Zero
    for k in range(a_value // 3 + 1):
        b = a_value - 3 * k
        c = epsilon + 2 * k
        if 2 * b + 3 * c != n:
            fail(f"top-face weight mismatch at n={n}, k={k}")
        expression += coefficient(n, b, c) * z**k
    result = sp.Poly(expression, z, domain=sp.QQ)
    if result.is_zero:
        fail(f"top torus face vanished at n={n}")
    return result


def cross(
    origin: tuple[int, int],
    first: tuple[int, int],
    second: tuple[int, int],
) -> int:
    return (first[0] - origin[0]) * (second[1] - origin[1]) - (
        first[1] - origin[1]
    ) * (second[0] - origin[0])


def convex_hull(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower: list[tuple[int, int]] = []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper: list[tuple[int, int]] = []
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def twice_area(polygon: list[tuple[int, int]]) -> int:
    if len(polygon) < 3:
        return 0
    return abs(
        sum(
            polygon[i][0] * polygon[(i + 1) % len(polygon)][1]
            - polygon[i][1] * polygon[(i + 1) % len(polygon)][0]
            for i in range(len(polygon))
        )
    )


def outward_normals(polygon: list[tuple[int, int]]) -> set[tuple[int, int]]:
    if len(polygon) == 2:
        dx = polygon[1][0] - polygon[0][0]
        dy = polygon[1][1] - polygon[0][1]
        divisor = math.gcd(abs(dx), abs(dy))
        return {(dy // divisor, -dx // divisor), (-dy // divisor, dx // divisor)}
    result: set[tuple[int, int]] = set()
    for first, second in zip(polygon, polygon[1:] + polygon[:1]):
        nx = second[1] - first[1]
        ny = first[0] - second[0]
        divisor = math.gcd(abs(nx), abs(ny))
        if divisor == 0:
            fail(f"zero polygon edge in {polygon}")
        result.add((nx // divisor, ny // divisor))
    return result


def residue_vertices(n: int) -> list[tuple[int, int]]:
    """Closed vertex formula, with hull removing small-class coincidences."""
    q, residue = divmod(n, 6)
    formulas = {
        0: [(0, 0), (3 * q, 0), (0, 2 * q)],
        1: [(0, 0), (3 * q, 0), (3 * q - 1, 1), (2, 2 * q - 1), (0, 2 * q)],
        2: [(0, 0), (3 * q + 1, 0), (1, 2 * q), (0, 2 * q)],
        3: [(0, 0), (3 * q + 1, 0), (3 * q, 1), (0, 2 * q + 1)],
        4: [(0, 0), (3 * q + 2, 0), (2, 2 * q), (0, 2 * q + 1)],
        5: [
            (0, 0),
            (3 * q + 2, 0),
            (3 * q + 1, 1),
            (1, 2 * q + 1),
            (0, 2 * q + 1),
        ],
    }
    return convex_hull(formulas[residue])


def mixed_volume(first: list[tuple[int, int]], second: list[tuple[int, int]]) -> int:
    first_hull = convex_hull(first)
    second_hull = convex_hull(second)
    minkowski = convex_hull(
        [(a + c, b + d) for a, b in first_hull for c, d in second_hull]
    )
    numerator = twice_area(minkowski) - twice_area(first_hull) - twice_area(second_hull)
    if numerator % 2:
        fail(f"nonintegral mixed volume numerator {numerator}")
    return numerator // 2


def mixed_volume_residue_formula(d: int) -> int:
    q, residue = divmod(d, 6)
    values = {
        0: 6 * q * q + q,
        1: 6 * q * q + 3 * q,
        2: 6 * q * q + 5 * q + 1,
        3: 6 * q * q + 7 * q + 2,
        4: 6 * q * q + 9 * q + 3,
        5: 6 * q * q + 11 * q + 5,
    }
    return values[residue]


def terminating_hypergeometric(
    degree: int,
    upper_second: sp.Rational | int,
    lower_first: sp.Rational | int,
) -> sp.Poly:
    expression = sp.S.Zero
    for k in range(degree + 1):
        expression += (
            sp.rf(-degree, k)
            * sp.rf(upper_second, k)
            / (sp.rf(lower_first, k) * math.factorial(k))
            * s**k
        )
    return sp.Poly(expression, s, domain=sp.QQ)


def jacobi_a(m: int) -> sp.Poly:
    return terminating_hypergeometric(m, 3 * m + 1, sp.Rational(1, 2))


def jacobi_b(m: int) -> sp.Poly:
    return terminating_hypergeometric(m, 3 * m + 3, sp.Rational(3, 2))


def reversed_normalized(poly: sp.Poly, variable: sp.Symbol, scale: int) -> sp.Poly:
    degree = poly.degree()
    leading = poly.nth(degree)
    if leading == 0:
        fail(f"missing leading coefficient in {poly.as_expr()}")
    return sp.Poly(
        sum(
            (
                sp.Rational(poly.nth(degree - k), leading)
                * scale**k
                * s**k
                for k in range(degree + 1)
            ),
            sp.S.Zero,
        ),
        s,
        domain=sp.QQ,
    )


def is_squarefree(poly: sp.Poly) -> bool:
    if poly.degree() <= 0:
        return True
    return sp.gcd(poly, poly.diff()).degree() == 0


def analyze(max_d: int) -> dict[str, object]:
    if max_d < 12:
        fail("max_d must be at least 12")

    supports = {n: support(n) for n in range(2, max_d + 2)}
    hulls = {n: convex_hull(points) for n, points in supports.items()}
    vertices_failures = []
    coefficient_failures = []
    facet_failures = []
    shared_normal_failures = []
    mixed_volume_failures = []

    for n, points in supports.items():
        if any(coefficient(n, b, c) == 0 for b, c in points):
            coefficient_failures.append(n)
        if n >= 6 and hulls[n] != residue_vertices(n):
            vertices_failures.append(
                {"n": n, "actual": hulls[n], "formula": residue_vertices(n)}
            )

    base_normals = {(-1, 0), (0, -1), (2, 3)}
    extras = {
        0: set(),
        1: {(1, 1), (1, 2)},
        2: {(0, 1)},
        3: {(1, 1)},
        4: {(1, 2)},
        5: {(1, 1), (0, 1)},
    }
    for n in range(12, max_d + 2):
        actual = outward_normals(hulls[n])
        expected = base_normals | extras[n % 6]
        if actual != expected:
            facet_failures.append(
                {"n": n, "actual": sorted(actual), "expected": sorted(expected)}
            )

    small_shared = {}
    for d in range(2, max_d + 1):
        shared = outward_normals(hulls[d]) & outward_normals(hulls[d + 1])
        expected = (
            {(0, -1)}
            if d == 2
            else {(-1, 0), (0, -1)}
            if d < 8
            else base_normals
        )
        if shared != expected:
            shared_normal_failures.append(
                {"d": d, "actual": sorted(shared), "expected": sorted(expected)}
            )
        if d <= 8:
            small_shared[str(d)] = [list(item) for item in sorted(shared)]

        actual_mv = mixed_volume(supports[d], supports[d + 1])
        residue_mv = mixed_volume_residue_formula(d)
        floor_formula = d * (d + 1) // 6
        if actual_mv != residue_mv or actual_mv != floor_formula:
            mixed_volume_failures.append(
                {
                    "d": d,
                    "actual": actual_mv,
                    "residue_formula": residue_mv,
                    "floor_formula": floor_formula,
                }
            )

    vertical = {n: vertical_face(n) for n in range(2, max_d + 2)}
    horizontal = {n: horizontal_face(n) for n in range(2, max_d + 2)}
    top = {n: top_torus_face(n) for n in range(2, max_d + 2)}

    gcd_failures: dict[str, list[dict[str, int]]] = {
        "c_equals_0": [],
        "b_equals_0": [],
        "top_weight": [],
    }
    families = {
        "c_equals_0": vertical,
        "b_equals_0": horizontal,
        "top_weight": top,
    }
    for name, family in families.items():
        for d in range(2, max_d + 1):
            degree = sp.gcd(family[d], family[d + 1]).degree()
            if degree != 0:
                gcd_failures[name].append({"d": d, "gcd_degree": degree})

    squarefree_failures = {
        name: [n for n, poly in family.items() if not is_squarefree(poly)]
        for name, family in families.items()
    }

    identity_failures = []
    transform_failures = []
    maximum_m = (max_d + 1) // 2
    for m in range(0, maximum_m + 1):
        a_poly = jacobi_a(m)
        b_poly = jacobi_b(m)
        first_identity = sp.Poly(
            sp.Rational(2, 3 * m + 2) * a_poly.as_expr()
            + sp.Rational(1, 2 * (3 * m + 2) * (3 * m + 1))
            * (4 * s - 3)
            * a_poly.diff().as_expr()
            - b_poly.as_expr(),
            s,
            domain=sp.QQ,
        )
        second_identity = sp.Poly(
            (1 - 8 * (m + 1) * s) * b_poly.as_expr()
            + 2 * s * (1 - sp.Rational(4, 3) * s) * b_poly.diff().as_expr()
            - jacobi_a(m + 1).as_expr(),
            s,
            domain=sp.QQ,
        )
        if not first_identity.is_zero or not second_identity.is_zero:
            identity_failures.append(m)

        even_n = 2 * m
        odd_n = 2 * m + 1
        if even_n >= 2 and even_n <= max_d + 1:
            if reversed_normalized(vertical[even_n], X, 4) != a_poly:
                transform_failures.append(even_n)
        if odd_n >= 2 and odd_n <= max_d + 1:
            if reversed_normalized(vertical[odd_n], X, 4) != b_poly:
                transform_failures.append(odd_n)

    special_value_failures = []
    for n, poly in vertical.items():
        actual = poly.eval(sp.Rational(1, 3))
        expected = 3 ** (n + 1) * sp.binomial(sp.Rational(1, 3), n + 1)
        if actual != expected or actual == 0:
            special_value_failures.append(n)

    # Negative controls exercise rejection paths without changing evidence data.
    control_base = vertical[12]
    mutated_pair_gcd_degree = sp.gcd(
        control_base, sp.Poly(control_base.as_expr() * (X + 1), X, domain=sp.QQ)
    ).degree()
    identity_mutation = sp.Poly(jacobi_a(5).as_expr() + 1, s, domain=sp.QQ) != jacobi_a(5)
    negative_controls = {
        "injected_common_factor_detected": mutated_pair_gcd_degree > 0,
        "perturbed_identity_detected": identity_mutation,
    }

    failures = {
        "coefficient": coefficient_failures,
        "vertices": vertices_failures,
        "facets": facet_failures,
        "shared_normals": shared_normal_failures,
        "mixed_volume": mixed_volume_failures,
        "gcd": gcd_failures,
        "squarefree": squarefree_failures,
        "jacobi_identities": identity_failures,
        "jacobi_transforms": transform_failures,
        "special_value": special_value_failures,
    }
    passed = (
        not any(
            failures[key]
            for key in [
                "coefficient",
                "vertices",
                "facets",
                "shared_normals",
                "mixed_volume",
                "jacobi_identities",
                "jacobi_transforms",
                "special_value",
            ]
        )
        and not any(gcd_failures.values())
        and not any(squarefree_failures.values())
        and all(negative_controls.values())
    )
    return {
        "schema": "irreducible-norms.affine-face-audit.v1",
        "status": "PASS" if passed else "FAIL",
        "arithmetic": "exact QQ polynomial arithmetic",
        "assertions_used_for_acceptance": False,
        "range": [2, max_d],
        "newton_support": "all (b,c) in Z_{>=0}^2 with 2b+3c<=n",
        "shared_facet_normals_for_d_ge_8": [[-1, 0], [0, -1], [2, 3]],
        "small_d_shared_facet_normals": small_shared,
        "mixed_volume_residue_formulas": {
            "d=6q": "6q^2+q",
            "d=6q+1": "6q^2+3q",
            "d=6q+2": "6q^2+5q+1",
            "d=6q+3": "6q^2+7q+2",
            "d=6q+4": "6q^2+9q+3",
            "d=6q+5": "6q^2+11q+5",
        },
        "consecutive_face_gcds": {
            name: {
                "all_coprime": not rows,
                "failures": rows,
            }
            for name, rows in gcd_failures.items()
        },
        "individual_face_squarefree": {
            name: {
                "all_squarefree": not rows,
                "failures": rows,
            }
            for name, rows in squarefree_failures.items()
        },
        "jacobi_contiguous_identities_checked_m": [0, maximum_m],
        "negative_controls": negative_controls,
        "failures": failures,
        "limitations": [
            "finite gcd and squarefreeness sweeps are not all-d proofs",
            "this script does not test the interior Jacobian ideal",
            "this script does not test G_(d+2) in the affine quotient",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-d", type=int, default=250)
    parser.add_argument("--json", type=Path)
    arguments = parser.parse_args()
    report = analyze(arguments.max_d)
    rendered = json.dumps(report, indent=2, sort_keys=True)
    print(rendered)
    if arguments.json is not None:
        arguments.json.parent.mkdir(parents=True, exist_ok=True)
        arguments.json.write_text(rendered + "\n")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
