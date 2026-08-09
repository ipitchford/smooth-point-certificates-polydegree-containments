#!/usr/bin/env python3
"""Exact exploratory calculations for three consecutive e=3 inverse coefficients.

The compositional inverse I(w) of

    H(t) = t + t^2 + X*t^3 + Y*t^4

has G_n(X,Y) as its coefficient of w**(n+1).  This script constructs the
coefficients by formal-series recurrence and tests the ideals
(G_d, G_{d+1}, G_{d+2}) over QQ with SymPy.

The calculations are finite evidence only unless a displayed symbolic identity
is separately proved in the accompanying memo.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy as sp


X, Y = sp.symbols("X Y")


def inverse_coefficients(max_n: int) -> list[sp.Poly]:
    """Return c[0..max_n+1], where I(w)=sum c[k] w**k and G_n=c[n+1]."""
    w = sp.symbols("w")
    coeffs: list[sp.Expr] = [sp.Integer(0), sp.Integer(1)]
    for k in range(2, max_n + 2):
        truncated = sum(coeffs[j] * w**j for j in range(1, k))
        rhs = sp.expand(truncated**2 + X * truncated**3 + Y * truncated**4)
        coeffs.append(-rhs.coeff(w, k))
    return [sp.Poly(c, X, Y, domain=sp.QQ) for c in coeffs]


def lagrange_g(n: int) -> sp.Poly:
    """Construct G_n directly from the integral Lagrange multinomial formula."""
    expr = 0
    for a3 in range(n // 3 + 1):
        for a2 in range((n - 3 * a3) // 2 + 1):
            a1 = n - 2 * a2 - 3 * a3
            size = a1 + a2 + a3
            numerator = (-1) ** size * math.factorial(n + size)
            denominator = (
                math.factorial(a1)
                * math.factorial(a2)
                * math.factorial(a3)
                * math.factorial(n)
                * (n + 1)
            )
            coefficient, remainder = divmod(numerator, denominator)
            if remainder:
                raise ArithmeticError(
                    f"nonintegral coefficient for n={n}, a={(a1, a2, a3)}"
                )
            expr += coefficient * X**a2 * Y**a3
    return sp.Poly(expr, X, Y, domain=sp.QQ)


def lagrange_coefficients(max_n: int) -> list[sp.Poly]:
    """Return c[0..max_n+1] using c[n+1]=G_n from Lagrange inversion."""
    zero = sp.Poly(0, X, Y, domain=sp.QQ)
    return [zero] + [lagrange_g(n) for n in range(max_n + 1)]


def triple_record(d: int, coeffs: list[sp.Poly]) -> dict[str, object]:
    triple = [coeffs[d + offset + 1] for offset in range(3)]
    basis = sp.groebner([p.as_expr() for p in triple], X, Y, order="grevlex")
    resultant_01 = sp.Poly(
        sp.resultant(triple[0].as_expr(), triple[1].as_expr(), Y), X,
        domain=sp.QQ,
    )
    resultant_02 = sp.Poly(
        sp.resultant(triple[0].as_expr(), triple[2].as_expr(), Y), X,
        domain=sp.QQ,
    )
    resultant_gcd = sp.gcd(resultant_01, resultant_02)
    return {
        "d": d,
        "degrees": [p.total_degree() for p in triple],
        "terms": [len(p.terms()) for p in triple],
        "unit_ideal": len(basis.polys) == 1 and basis.polys[0].as_expr() == 1,
        "groebner_basis": [str(p) for p in basis.polys],
        "resultant_y_gcd_degree": resultant_gcd.degree(),
        "resultant_y_gcd": str(resultant_gcd.as_expr()),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-d", type=int, default=12)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if args.max_d < 2:
        parser.error("--max-d must be at least 2")

    coeffs = lagrange_coefficients(args.max_d + 2)
    recurrence_check_bound = min(args.max_d + 2, 10)
    recurrence_coeffs = inverse_coefficients(recurrence_check_bound)
    for n in range(recurrence_check_bound + 1):
        if coeffs[n + 1] != recurrence_coeffs[n + 1]:
            raise AssertionError(f"Lagrange/recurrence mismatch at G_{n}")
    records = []
    for d in range(2, args.max_d + 1):
        record = triple_record(d, coeffs)
        records.append(record)
        print(
            f"d={d:3d} unit={record['unit_ideal']} "
            f"gcd_degree={record['resultant_y_gcd_degree']} "
            f"terms={record['terms']}"
        )

    payload = {
        "object": "three consecutive coefficients of inverse(t+t^2+X*t^3+Y*t^4)",
        "range": [2, args.max_d],
        "independent_recurrence_check": [0, recurrence_check_bound],
        "records": records,
    }
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
