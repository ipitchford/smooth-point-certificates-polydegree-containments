#!/usr/bin/env python3
"""Derive a linear differential relation for a numerical quartic inverse.

This is a structural diagnostic.  For fixed rational X,Y, calculations take
place in QQ(w)[z]/(Y*z**4 + X*z**3 + z**2 + z - w).  The script computes
successive total derivatives of z and finds their first linear dependence.
"""

from __future__ import annotations

import argparse

import sympy as sp


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=int, default=2)
    parser.add_argument("--y", type=int, default=3)
    parser.add_argument("--max-order", type=int, default=5)
    args = parser.parse_args()
    if args.y == 0:
        parser.error("this quartic diagnostic requires --y nonzero")

    w, z = sp.symbols("w z")
    f = args.y * z**4 + args.x * z**3 + z**2 + z - w
    q = sp.diff(f, z)
    field = sp.QQ.frac_field(w)
    f_poly = sp.Poly(f, z, domain=field)
    q_poly = sp.Poly(q, z, domain=field)
    dz = sp.invert(q_poly, f_poly).as_expr()

    def reduce_mod_f(expr: sp.Expr) -> sp.Expr:
        numerator, denominator = sp.cancel(expr).as_numer_denom()
        reduced_numerator = sp.rem(
            sp.Poly(numerator, z, domain=field), f_poly
        ).as_expr()
        return sp.cancel(reduced_numerator / denominator)

    def total_derivative(expr: sp.Expr) -> sp.Expr:
        return reduce_mod_f(sp.diff(expr, w) + sp.diff(expr, z) * dz)

    derivatives = [z]
    for _ in range(args.max_order):
        derivatives.append(total_derivative(derivatives[-1]))

    for order in range(1, len(derivatives)):
        columns = []
        for expr in derivatives[: order + 1]:
            poly = sp.Poly(reduce_mod_f(expr), z, domain=field)
            columns.append([poly.nth(i) for i in range(4)])
        matrix = sp.Matrix(4, order + 1, lambda i, j: columns[j][i])
        nullspace = matrix.nullspace()
        if not nullspace:
            continue
        relation = [sp.factor(entry) for entry in nullspace[0]]
        print(f"first homogeneous dependence order: {order}")
        for derivative_order, coefficient in enumerate(relation):
            numerator, denominator = sp.cancel(coefficient).as_numer_denom()
            print(
                f"D^{derivative_order}: ({sp.factor(numerator)}) / "
                f"({sp.factor(denominator)})"
            )
        return 0

    print("no dependence found within requested order")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
