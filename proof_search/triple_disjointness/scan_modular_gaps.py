#!/usr/bin/env python3
"""Exhaustive finite-field scan for three consecutive inverse coefficients.

These are characteristic-p diagnostics, not counterexamples over QQ or CC.
For each (X,Y) in F_p^2 the inverse coefficients are produced directly from
I + I^2 + X I^3 + Y I^4 = w, using incremental convolutions.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def inverse_coefficients_mod_p(x: int, y: int, max_d: int, p: int) -> list[int]:
    """Return c[0..max_d+3] for I(w)=sum c[n]w^n over F_p."""
    max_k = max_d + 3
    c = [0] * (max_k + 1)
    power2 = [0] * (max_k + 1)
    power3 = [0] * (max_k + 1)
    power4 = [0] * (max_k + 1)
    c[1] = 1
    for k in range(2, max_k + 1):
        power2[k] = sum(c[i] * c[k - i] for i in range(1, k)) % p
        power3[k] = sum(c[i] * power2[k - i] for i in range(1, k)) % p
        power4[k] = sum(c[i] * power3[k - i] for i in range(1, k)) % p
        c[k] = -(power2[k] + x * power3[k] + y * power4[k]) % p
    return c


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    return all(n % q for q in range(2, int(n**0.5) + 1))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", type=int, nargs="+", default=[2, 3, 5, 7])
    parser.add_argument("--max-d", type=int, default=200)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    for p in args.primes:
        if not is_prime(p):
            parser.error(f"{p} is not prime")

    records: list[dict[str, object]] = []
    for p in args.primes:
        witnesses: list[dict[str, object]] = []
        for x in range(p):
            for y in range(p):
                c = inverse_coefficients_mod_p(x, y, args.max_d, p)
                for d in range(2, args.max_d + 1):
                    values = [c[d + 1], c[d + 2], c[d + 3]]
                    if values == [0, 0, 0]:
                        witnesses.append({"d": d, "point": [x, y]})
        first_d = min((int(w["d"]) for w in witnesses), default=None)
        record = {
            "p": p,
            "parameter_points": p * p,
            "d_range": [2, args.max_d],
            "triple_zero_count": len(witnesses),
            "first_d": first_d,
            "witnesses": witnesses,
        }
        records.append(record)
        print(
            f"p={p:2d} points={p*p:4d} triples={len(witnesses):5d} "
            f"first_d={first_d}"
        )

    payload = {
        "warning": "finite-characteristic evidence only; not a CC counterexample",
        "records": records,
    }
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
