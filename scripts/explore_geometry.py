#!/usr/bin/env python3
"""Exact exploratory audit of the e=3 weighted-projective gateway.

This script deliberately separates three questions:

1. Do the two weighted-homogeneous equations have a common curve?
2. What happens in the affine chart x1 != 0 and on the boundary x1 = 0?
3. Does the affine zero-dimensional scheme contain a smooth point avoiding G_{d+2}?

All polynomial arithmetic is exact over QQ.  SymPy constructs the inverse-series
coefficients in two independent ways; Singular supplies exact ideal dimensions
and quotient-vector-space dimensions.
"""
from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
import tempfile
from pathlib import Path

import sympy as sp


X1, X, Y, w, t = sp.symbols("x1 X Y w t")


def fail(message: str) -> None:
    raise RuntimeError(message)


def compositions_weighted_123(total: int):
    for a3 in range(total // 3 + 1):
        for a2 in range((total - 3 * a3) // 2 + 1):
            a1 = total - 2 * a2 - 3 * a3
            yield a1, a2, a3


def multinomial_tail(a: tuple[int, int, int], tail: int) -> int:
    remaining = sum(a)
    value = math.comb(tail + remaining, tail)
    for entry in a:
        value *= math.comb(remaining, entry)
        remaining -= entry
    return value


def g_explicit(n: int) -> sp.Poly:
    """Return g_{n,3}, exactly, using the Lagrange multinomial formula."""
    expression = 0
    for a in compositions_weighted_123(n):
        numerator = (-1) ** sum(a) * multinomial_tail(a, n)
        coefficient, remainder = divmod(numerator, n + 1)
        if remainder != 0:
            fail(f"non-integral coefficient for n={n}, a={a}")
        expression += coefficient * X1 ** a[0] * X ** a[1] * Y ** a[2]
    return sp.Poly(expression, X1, X, Y, domain=sp.QQ)


def inverse_coefficients(max_n: int) -> list[sp.Poly]:
    """Compute [w^k] I(w) from I+I^2+X I^3+Y I^4=w."""
    size = max_n + 2
    zero = sp.Poly(0, X, Y, domain=sp.QQ)
    coeffs = [zero for _ in range(size)]
    powers2 = [zero for _ in range(size)]
    powers3 = [zero for _ in range(size)]
    powers4 = [zero for _ in range(size)]
    coeffs[1] = sp.Poly(1, X, Y, domain=sp.QQ)
    x_poly = sp.Poly(X, X, Y, domain=sp.QQ)
    y_poly = sp.Poly(Y, X, Y, domain=sp.QQ)

    # Since I has valuation one, [w^n] I^k never involves [w^n] I for k >= 2.
    # We may therefore update the power arrays before solving for coeffs[n].
    for degree in range(2, size):
        powers2[degree] = sum(
            (coeffs[i] * coeffs[degree - i] for i in range(1, degree)),
            zero,
        )
        powers3[degree] = sum(
            (powers2[i] * coeffs[degree - i] for i in range(2, degree)),
            zero,
        )
        powers4[degree] = sum(
            (powers3[i] * coeffs[degree - i] for i in range(3, degree)),
            zero,
        )
        coeffs[degree] = -(powers2[degree] + x_poly * powers3[degree] + y_poly * powers4[degree])
    return coeffs


def affine_g(poly: sp.Poly) -> sp.Poly:
    return sp.Poly(poly.as_expr().subs(X1, 1), X, Y, domain=sp.QQ)


def boundary_g(poly: sp.Poly) -> sp.Poly:
    return sp.Poly(poly.as_expr().subs(X1, 0), X, Y, domain=sp.QQ)


def convex_hull(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def cross(o: tuple[int, int], a: tuple[int, int], b: tuple[int, int]) -> int:
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

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


def newton_mixed_volume(first: sp.Poly, second: sp.Poly) -> int:
    """Return the two-dimensional BKK mixed volume of two Newton polygons."""
    p = convex_hull([tuple(map(int, exponent)) for exponent, coefficient in first.terms() if coefficient])
    q = convex_hull([tuple(map(int, exponent)) for exponent, coefficient in second.terms() if coefficient])
    minkowski = convex_hull([(a + c, b + d) for a, b in p for c, d in q])
    numerator = twice_area(minkowski) - twice_area(p) - twice_area(q)
    quotient, remainder = divmod(numerator, 2)
    if remainder != 0:
        fail(f"non-integral mixed volume: numerator={numerator}")
    return quotient


def primitive_expr(poly: sp.Poly) -> str:
    primitive = sp.Poly(poly, *poly.gens, domain=sp.QQ).clear_denoms(convert=True)[1].primitive()[1]
    return str(sp.expand(primitive.as_expr())).replace("**", "^")


def singular_metrics(g0: sp.Poly, g1: sp.Poly, g2: sp.Poly) -> dict[str, int]:
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular executable not found")
    jac = sp.Poly(
        sp.diff(g0.as_expr(), X) * sp.diff(g1.as_expr(), Y)
        - sp.diff(g0.as_expr(), Y) * sp.diff(g1.as_expr(), X),
        X,
        Y,
        domain=sp.QQ,
    )
    program = f"""
ring r=0,(X,Y),dp;
poly f={primitive_expr(g0)};
poly g={primitive_expr(g1)};
poly h={primitive_expr(g2)};
poly j={primitive_expr(jac)};
ideal i=f,g;
ideal s=std(i);
ideal ij=f,g,j;
ideal ih=f,g,h;
ideal sj=std(ij);
ideal sh=std(ih);
print(\"DIM \"+string(dim(s)));
print(\"VDIM \"+string(vdim(s)));
print(\"SING_VDIM \"+string(vdim(sj)));
print(\"NEXT_VDIM \"+string(vdim(sh)));
quit;
"""
    with tempfile.TemporaryDirectory(prefix="polydegree-geometry-") as temporary:
        script = Path(temporary) / "query.sing"
        script.write_text(program)
        result = subprocess.run(
            [singular, "-q", str(script)],
            check=True,
            text=True,
            capture_output=True,
        )
    metrics: dict[str, int] = {}
    for line in result.stdout.splitlines():
        parts = line.strip().split()
        if len(parts) == 2 and parts[0] in {"DIM", "VDIM", "SING_VDIM", "NEXT_VDIM"}:
            metrics[parts[0].lower()] = int(parts[1])
    expected = {"dim", "vdim", "sing_vdim", "next_vdim"}
    if set(metrics) != expected:
        fail(f"could not parse Singular output: {result.stdout!r}, stderr={result.stderr!r}")
    return metrics


def analyze(d_min: int, d_max: int) -> dict[str, object]:
    inverse = inverse_coefficients(d_max + 2)
    homogeneous = {n: g_explicit(n) for n in range(d_min, d_max + 3)}
    for n, poly in homogeneous.items():
        from_inverse = inverse[n + 1]
        direct_affine = affine_g(poly)
        if direct_affine != from_inverse:
            fail(f"inverse-series and multinomial constructions disagree at n={n}")
        weighted_degrees = {
            a1 + 2 * a2 + 3 * a3
            for (a1, a2, a3), coefficient in poly.terms()
            if coefficient
        }
        if weighted_degrees != {n}:
            fail(f"g_{n} is not weighted homogeneous of degree {n}: {weighted_degrees}")

    rows = []
    for d in range(d_min, d_max + 1):
        h0, h1, h2 = homogeneous[d], homogeneous[d + 1], homogeneous[d + 2]
        g0, g1, g2 = affine_g(h0), affine_g(h1), affine_g(h2)
        homogeneous_gcd = sp.gcd(h0, h1)
        affine_gcd = sp.gcd(g0, g1)
        b0, b1 = boundary_g(h0), boundary_g(h1)
        boundary_gcd = sp.gcd(b0, b1)
        metrics = singular_metrics(g0, g1, g2)
        expected_affine_length = d * (d + 1) // 6
        mixed_volume = newton_mixed_volume(g0, g1)
        rows.append(
            {
                "d": d,
                "homogeneous_gcd_total_degree": homogeneous_gcd.total_degree(),
                "homogeneous_gcd": str(homogeneous_gcd.as_expr()),
                "affine_gcd_total_degree": affine_gcd.total_degree(),
                "boundary_gcd": str(boundary_gcd.as_expr()),
                "boundary_gcd_total_degree": boundary_gcd.total_degree(),
                "expected_affine_length_floor_d_d1_over_6": expected_affine_length,
                "newton_mixed_volume": mixed_volume,
                "mixed_volume_matches_formula": mixed_volume == expected_affine_length,
                "affine_length_matches_formula": metrics["vdim"] == expected_affine_length,
                "affine_reduced_by_jacobian_criterion": metrics["sing_vdim"] == 0,
                "affine_disjoint_from_g_d2": metrics["next_vdim"] == 0,
                **metrics,
            }
        )
    all_proper = all(row["homogeneous_gcd_total_degree"] == 0 for row in rows)
    all_length_formula = all(row["affine_length_matches_formula"] for row in rows)
    all_mixed_volume_formula = all(row["mixed_volume_matches_formula"] for row in rows)
    all_reduced = all(row["affine_reduced_by_jacobian_criterion"] for row in rows)
    all_avoid_next = all(row["affine_disjoint_from_g_d2"] for row in rows)
    return {
        "schema": "polydegree.e3.geometry-exploration.v1",
        "arithmetic": "exact QQ polynomial arithmetic",
        "construction_cross_check": "multinomial Lagrange formula equals formal inverse recursion",
        "range": [d_min, d_max],
        "all_weighted_projective_pairs_proper": all_proper,
        "all_affine_lengths_match_floor_d_d1_over_6": all_length_formula,
        "all_newton_mixed_volumes_match_floor_d_d1_over_6": all_mixed_volume_formula,
        "all_affine_schemes_reduced_by_jacobian_criterion": all_reduced,
        "all_affine_schemes_disjoint_from_g_d2": all_avoid_next,
        "rows": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d-min", type=int, default=2)
    parser.add_argument("--d-max", type=int, default=20)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if args.d_min < 2 or args.d_max < args.d_min:
        parser.error("require 2 <= d-min <= d-max")
    report = analyze(args.d_min, args.d_max)
    rendered = json.dumps(report, indent=2, sort_keys=True)
    print(rendered)
    if args.json is not None:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
