#!/usr/bin/env python3
"""Replay exact Stage 2 identities and bounded characteristic-zero checks.

The raising identity is proved for all d in PROOF_MEMO.md; checking instances is
only a mutation/index receipt.  Gröbner calculations are explicitly finite.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp

from explore_triples import X, Y, lagrange_g


VX = 2 * X - 6 * X**2 + 4 * Y
VY = 4 * Y - 9 * X * Y


def vector_field(poly: sp.Expr) -> sp.Expr:
    return sp.expand(VX * sp.diff(poly, X) + VY * sp.diff(poly, Y))


def is_unit_basis(basis: sp.GroebnerBasis) -> bool:
    return len(basis.polys) == 1 and basis.polys[0].as_expr() == 1


def fail(message: str) -> None:
    raise RuntimeError(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--identity-max", type=int, default=24)
    parser.add_argument("--exact-max", type=int, default=15)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if args.exact_max < 2 or args.identity_max < args.exact_max + 1:
        parser.error("require identity-max >= exact-max+1 and exact-max >= 2")

    g = [lagrange_g(n).as_expr() for n in range(args.identity_max + 2)]
    for n in range(args.identity_max + 1):
        coefficient = 3 * n * X - 4 * n - 2
        residual = sp.expand(
            vector_field(g[n]) - (n + 2) * g[n + 1] + coefficient * g[n]
        )
        if residual != 0:
            fail(f"raising identity failed at n={n}: {residual}")

    stationary_points = [
        (sp.Integer(0), sp.Integer(0)),
        (sp.Rational(1, 3), sp.Integer(0)),
        (sp.Rational(4, 9), sp.Rational(2, 27)),
    ]
    for n in range(args.identity_max + 1):
        expected = [
            (-1) ** n * sp.binomial(2 * n, n) / (n + 1),
            3 ** (n + 1) * sp.binomial(sp.Rational(1, 3), n + 1),
            sp.Rational(3, 2)
            * sp.Rational(8, 3) ** (n + 1)
            * sp.binomial(sp.Rational(1, 4), n + 1),
        ]
        for point, target in zip(stationary_points, expected):
            value = sp.factor(g[n].subs({X: point[0], Y: point[1]}))
            if sp.factor(value - target) != 0 or value == 0:
                fail(f"stationary evaluation failed at n={n}, point={point}")

    exact_records = []
    for d in range(2, args.exact_max + 1):
        f, next_f, third_f = g[d], g[d + 1], g[d + 2]
        jacobian = sp.expand(
            sp.diff(f, X) * sp.diff(next_f, Y)
            - sp.diff(f, Y) * sp.diff(next_f, X)
        )
        c_d = 3 * d * X - 4 * d - 2
        c_next = 3 * (d + 1) * X - 4 * (d + 1) - 2
        syzygy_x = sp.expand(
            VY * jacobian
            - (d + 3) * sp.diff(f, X) * third_f
            + c_next * sp.diff(f, X) * next_f
            + (d + 2) * sp.diff(next_f, X) * next_f
            - c_d * sp.diff(next_f, X) * f
        )
        syzygy_y = sp.expand(
            -VX * jacobian
            - (d + 3) * sp.diff(f, Y) * third_f
            + c_next * sp.diff(f, Y) * next_f
            + (d + 2) * sp.diff(next_f, Y) * next_f
            - c_d * sp.diff(next_f, Y) * f
        )
        if syzygy_x != 0 or syzygy_y != 0:
            fail(f"Jacobian syzygy failed at d={d}")
        triple_basis = sp.groebner([f, next_f, third_f], X, Y, order="grevlex")
        tangency_basis = sp.groebner([f, next_f, jacobian], X, Y, order="grevlex")
        triple_unit = is_unit_basis(triple_basis)
        tangency_unit = is_unit_basis(tangency_basis)
        if not triple_unit or not tangency_unit:
            fail(
                f"bounded exact check failed at d={d}: "
                f"triple={triple_unit}, tangency={tangency_unit}"
            )
        exact_records.append(
            {
                "d": d,
                "triple_ideal_unit": True,
                "consecutive_pair_transverse": True,
                "jacobian_syzygies": True,
            }
        )

    payload = {
        "status": "PASS",
        "all_d_proof_receipt": {
            "raising_identity_checked_range": [0, args.identity_max],
            "stationary_evaluations_checked_range": [0, args.identity_max],
            "warning": "finite symbolic replay supports, but does not prove, the all-d derivation",
        },
        "finite_exact_evidence": {
            "range": [2, args.exact_max],
            "records": exact_records,
            "warning": "finite Groebner evidence only",
        },
    }
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n")
    print(
        f"PASS raising n=0..{args.identity_max}; exact triple/transversality "
        f"d=2..{args.exact_max}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
