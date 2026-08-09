#!/usr/bin/env python3
"""Exact long-range audit of the x1=0 boundary for e=3.

On the torus X*Y != 0, put z=Y^2/X^3.  The weighted-homogeneous
boundary polynomial B_n=g_{n,3}(0,X,Y) has the form

    B_n = X^A Y^epsilon P_n(z),

where epsilon=n mod 2 and A=(n-3*epsilon)/2.  This script checks exact
coprimality and squarefreeness of the P_n over QQ.  Coordinate monomial
factors are treated analytically in the accompanying report.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy as sp


z = sp.symbols("z")


def fail(message: str) -> None:
    raise RuntimeError(message)


def torus_polynomial(n: int) -> sp.Poly:
    epsilon = n % 2
    A = (n - 3 * epsilon) // 2
    if A < 0:
        fail(f"unexpected negative A for n={n}")
    expression = 0
    for k in range(A // 3 + 1):
        x_exponent = A - 3 * k
        y_exponent = epsilon + 2 * k
        if 2 * x_exponent + 3 * y_exponent != n:
            fail(f"weight mismatch for n={n}, k={k}")
        coefficient = sp.Rational(
            (-1) ** (x_exponent + y_exponent)
            * math.factorial(n + x_exponent + y_exponent),
            (n + 1)
            * math.factorial(n)
            * math.factorial(x_exponent)
            * math.factorial(y_exponent),
        )
        expression += coefficient * z**k
    poly = sp.Poly(expression, z, domain=sp.QQ)
    if poly.is_zero:
        fail(f"P_{n} vanished identically")
    return poly


def coordinate_x_valuation(n: int) -> int:
    """Minimum exponent of X among monomials of B_n."""
    residues = [b for b in range(3) if (2 * b - n) % 3 == 0]
    if len(residues) != 1:
        fail(f"could not determine X valuation for n={n}")
    return residues[0]


def coordinate_y_valuation(n: int) -> int:
    """Minimum exponent of Y among monomials of B_n."""
    return n % 2


def analyze(d_min: int, d_max: int) -> dict[str, object]:
    polys = {n: torus_polynomial(n) for n in range(d_min, d_max + 2)}
    rows = []
    for d in range(d_min, d_max + 1):
        p0, p1 = polys[d], polys[d + 1]
        torus_gcd = sp.gcd(p0, p1)
        squarefree0 = sp.gcd(p0, p0.diff()).degree() == 0
        squarefree1 = sp.gcd(p1, p1.diff()).degree() == 0
        x_common = min(coordinate_x_valuation(d), coordinate_x_valuation(d + 1))
        y_common = min(coordinate_y_valuation(d), coordinate_y_valuation(d + 1))
        predicted_x_common = 1 if d % 3 == 1 else 0
        if x_common != predicted_x_common or y_common != 0:
            fail(f"coordinate-factor classification failed at d={d}")
        rows.append(
            {
                "d": d,
                "p_d_degree": p0.degree(),
                "p_d1_degree": p1.degree(),
                "torus_gcd_degree": torus_gcd.degree(),
                "p_d_squarefree": squarefree0,
                "p_d1_squarefree": squarefree1,
                "boundary_common_x_valuation": x_common,
                "boundary_common_y_valuation": y_common,
            }
        )
    failures = [
        row
        for row in rows
        if row["torus_gcd_degree"] != 0
        or not row["p_d_squarefree"]
        or not row["p_d1_squarefree"]
    ]
    return {
        "schema": "polydegree.e3.boundary-sweep.v1",
        "arithmetic": "exact QQ univariate polynomial arithmetic",
        "range": [d_min, d_max],
        "all_torus_pairs_coprime": all(row["torus_gcd_degree"] == 0 for row in rows),
        "all_torus_polynomials_squarefree": all(
            row["p_d_squarefree"] and row["p_d1_squarefree"] for row in rows
        ),
        "coordinate_common_factor": "X exactly when d mod 3 = 1; otherwise 1",
        "failures": failures,
        "rows": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d-min", type=int, default=2)
    parser.add_argument("--d-max", type=int, default=200)
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
    return 0 if not report["failures"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
