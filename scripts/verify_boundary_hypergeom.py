#!/usr/bin/env python3
"""Fail-closed exact checks for the e=3 boundary hypergeometric formula.

For n >= 2, write

    g_{n,3}(0, X, Y) = X^A Y^epsilon P_n(Y^2/X^3),

where epsilon = n mod 2 and A = (n - 3 epsilon)/2.  The accompanying
proof memo shows that the normalized reciprocal of P_n is a terminating
3F2 polynomial.  This script checks that identity and its two-factor
finite-free-convolution coefficient identity exactly over QQ.

Finite sweeps of squarefreeness, adjacent coprimality, irreducibility, and
strict adjacent root interlacing are evidence only.  They are deliberately
reported separately from the all-n proof in PROOF_MEMO.md.

No correctness condition uses ``assert`` so ``python -O`` cannot remove a
check.
"""
from __future__ import annotations

import argparse
import json
import math
import platform
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import sympy as sp


z = sp.symbols("z")


def fail(message: str) -> None:
    raise RuntimeError(message)


def product(values: Iterable[sp.Rational]) -> sp.Rational:
    answer = sp.Rational(1)
    for value in values:
        answer *= value
    return answer


def rising(value: sp.Rational, length: int) -> sp.Rational:
    answer = sp.Rational(1)
    for offset in range(length):
        answer *= value + offset
    return answer


@dataclass(frozen=True)
class BoundaryParameters:
    n: int
    epsilon: int
    A: int
    M: int
    delta: int
    sigma: sp.Rational
    a: sp.Rational
    H: int
    beta1: sp.Rational
    beta2: sp.Rational


def parameters(n: int) -> BoundaryParameters:
    if n < 2:
        fail(f"the boundary normalization is only used for n >= 2, got {n}")
    epsilon = n % 2
    A = (n - 3 * epsilon) // 2
    if 2 * A + 3 * epsilon != n or A < 0:
        fail(f"invalid A,epsilon decomposition for n={n}")
    M, delta = divmod(A, 3)
    sigma = sp.Rational(1, 2) if epsilon == 0 else sp.Rational(-1, 2)
    a = -M + sigma
    N = n + A + epsilon
    H = N - M + 1
    beta_table = {
        0: (sp.Rational(1, 3), sp.Rational(2, 3)),
        1: (sp.Rational(2, 3), sp.Rational(4, 3)),
        2: (sp.Rational(4, 3), sp.Rational(5, 3)),
    }
    beta1, beta2 = beta_table[delta]
    return BoundaryParameters(
        n=n,
        epsilon=epsilon,
        A=A,
        M=M,
        delta=delta,
        sigma=sigma,
        a=a,
        H=H,
        beta1=beta1,
        beta2=beta2,
    )


def torus_polynomial(n: int) -> sp.Poly:
    """Return P_n in exact QQ arithmetic from the factorial formula."""
    data = parameters(n)
    expression = sp.Rational(0)
    for k in range(data.M + 1):
        x_exponent = data.A - 3 * k
        y_exponent = data.epsilon + 2 * k
        if x_exponent < 0 or 2 * x_exponent + 3 * y_exponent != n:
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
    polynomial = sp.Poly(expression, z, domain=sp.QQ)
    if polynomial.is_zero or polynomial.degree() != data.M:
        fail(f"P_{n} has unexpected degree {polynomial.degree()}, expected {data.M}")
    return polynomial


def hypergeometric_coefficients(
    degree: int,
    numerator_parameters: tuple[sp.Rational, ...],
    denominator_parameters: tuple[sp.Rational, ...],
    argument_scale: sp.Rational = sp.Rational(1),
) -> list[sp.Rational]:
    """Return ascending coefficients of a terminating hypergeometric sum."""
    coefficients = [sp.Rational(1)]
    current = sp.Rational(1)
    for j in range(degree):
        numerator = argument_scale * product(a + j for a in numerator_parameters)
        denominator = sp.Rational(j + 1) * product(
            b + j for b in denominator_parameters
        )
        if denominator == 0:
            fail(
                "zero denominator in hypergeometric recurrence at "
                f"degree={degree}, j={j}"
            )
        current *= numerator / denominator
        coefficients.append(sp.cancel(current))
    if len(coefficients) != degree + 1:
        fail("hypergeometric coefficient construction returned wrong length")
    return coefficients


def polynomial_coefficients(polynomial: sp.Poly) -> list[sp.Rational]:
    return [sp.Rational(polynomial.nth(k)) for k in range(polynomial.degree() + 1)]


def normalized_reciprocal_coefficients(polynomial: sp.Poly) -> list[sp.Rational]:
    coefficients = polynomial_coefficients(polynomial)
    leading = coefficients[-1]
    if leading == 0:
        fail("cannot reverse a polynomial with zero leading coefficient")
    return [sp.cancel(coefficients[-1 - j] / leading) for j in range(len(coefficients))]


def check_hypergeometric_identity(n: int, polynomial: sp.Poly) -> bool:
    data = parameters(n)
    direct = normalized_reciprocal_coefficients(polynomial)
    hypergeometric = hypergeometric_coefficients(
        data.M,
        (sp.Rational(-data.M), data.a, sp.Rational(data.H)),
        (data.beta1, data.beta2),
        sp.Rational(-4, 27),
    )
    return direct == hypergeometric


def check_convolution_coefficient_identity(n: int) -> bool:
    """Check the parameter-concatenation identity defining the 3F2 factorization.

    In ascending coefficients, division by (-M)_j/j! is the binomial
    normalization in the degree-M multiplicative finite free convolution.
    A global nonzero scalar depends on polynomial-normalization convention and
    is irrelevant to roots.
    """
    data = parameters(n)
    full = hypergeometric_coefficients(
        data.M,
        (sp.Rational(-data.M), data.a, sp.Rational(data.H)),
        (data.beta1, data.beta2),
    )
    negative_factor = hypergeometric_coefficients(
        data.M,
        (sp.Rational(-data.M), data.a),
        (data.beta1,),
    )
    positive_factor = hypergeometric_coefficients(
        data.M,
        (sp.Rational(-data.M), sp.Rational(data.H)),
        (data.beta2,),
    )
    reconstructed: list[sp.Rational] = []
    for j in range(data.M + 1):
        normalization = rising(sp.Rational(-data.M), j) / math.factorial(j)
        if normalization == 0:
            fail(f"unexpected zero convolution normalization for n={n}, j={j}")
        reconstructed.append(
            sp.cancel(negative_factor[j] * positive_factor[j] / normalization)
        )
    return reconstructed == full


def jacobi_parameter_conditions(n: int) -> tuple[bool, dict[str, sp.Rational]]:
    data = parameters(n)
    values = {
        "negative_alpha": data.beta1 - 1,
        "negative_gamma": -data.sigma,
        "positive_alpha": data.beta2 - 1,
        "positive_gamma": sp.Rational(data.H - data.M) - data.beta2,
    }
    return all(value > -1 for value in values.values()), values


def squarefree(polynomial: sp.Poly) -> bool:
    return sp.gcd(polynomial, polynomial.diff()).degree() == 0


def irreducible_if_nonconstant(polynomial: sp.Poly) -> bool:
    if polynomial.degree() == 0:
        return True
    factors = sp.factor_list(polynomial)[1]
    return (
        len(factors) == 1
        and factors[0][0].degree() == polynomial.degree()
        and factors[0][1] == 1
    )


def root_interval_label(
    interval: tuple[sp.Rational, sp.Rational],
    first: sp.Poly,
    second: sp.Poly,
) -> str | None:
    lower, upper = interval
    if lower == upper:
        first_has_root = first.eval(lower) == 0
        second_has_root = second.eval(lower) == 0
    else:
        first_has_root = first.eval(lower) * first.eval(upper) < 0
        second_has_root = second.eval(lower) * second.eval(upper) < 0
    if first_has_root == second_has_root:
        return None
    return "P_d" if first_has_root else "P_d_plus_1"


def exact_strict_interlacing(first: sp.Poly, second: sp.Poly) -> bool:
    """Certify alternating simple positive roots using rational isolating intervals."""
    first_degree, second_degree = first.degree(), second.degree()
    if abs(first_degree - second_degree) > 1:
        return False
    if first_degree == 0 and second_degree == 0:
        return True
    union = first * second
    isolating_intervals = union.intervals()
    if sum(multiplicity for _, multiplicity in isolating_intervals) != union.degree():
        return False
    labels: list[str] = []
    for interval, multiplicity in isolating_intervals:
        if multiplicity != 1:
            return False
        lower, upper = interval
        if lower < 0 or upper <= 0:
            return False
        label = root_interval_label(interval, first, second)
        if label is None:
            return False
        labels.append(label)
    if any(labels[index] == labels[index + 1] for index in range(len(labels) - 1)):
        return False
    if first_degree > second_degree and labels:
        return labels[0] == "P_d" and labels[-1] == "P_d"
    if second_degree > first_degree and labels:
        return labels[0] == "P_d_plus_1" and labels[-1] == "P_d_plus_1"
    return True


def analyze(
    d_min: int,
    d_max: int,
    factor_max: int,
    interlace_max: int,
) -> dict[str, object]:
    largest_n = max(d_max + 1, factor_max, interlace_max + 1)
    polynomials = {n: torus_polynomial(n) for n in range(d_min, largest_n + 1)}

    identity_failures: list[int] = []
    convolution_failures: list[int] = []
    jacobi_condition_failures: list[int] = []
    squarefree_failures: list[int] = []
    irreducibility_failures: list[int] = []
    gcd_failures: list[int] = []
    interlacing_failures: list[int] = []
    jacobi_minima: dict[str, sp.Rational] = {}

    for n, polynomial in polynomials.items():
        if not check_hypergeometric_identity(n, polynomial):
            identity_failures.append(n)
        if not check_convolution_coefficient_identity(n):
            convolution_failures.append(n)
        conditions_hold, values = jacobi_parameter_conditions(n)
        if not conditions_hold:
            jacobi_condition_failures.append(n)
        for name, value in values.items():
            jacobi_minima[name] = min(jacobi_minima.get(name, value), value)
        if not squarefree(polynomial):
            squarefree_failures.append(n)
        if n <= factor_max and not irreducible_if_nonconstant(polynomial):
            irreducibility_failures.append(n)

    for d in range(d_min, d_max + 1):
        if sp.gcd(polynomials[d], polynomials[d + 1]).degree() != 0:
            gcd_failures.append(d)
        if d <= interlace_max and not exact_strict_interlacing(
            polynomials[d], polynomials[d + 1]
        ):
            interlacing_failures.append(d)

    residue_table = []
    for residue in range(6):
        sample_n = residue if residue >= d_min else residue + 6
        while sample_n < d_min:
            sample_n += 6
        data = parameters(sample_n)
        residue_table.append(
            {
                "n_mod_6": residue,
                "sample_n": sample_n,
                "M": data.M,
                "delta": data.delta,
                "a": str(data.a),
                "H": data.H,
                "beta": [str(data.beta1), str(data.beta2)],
            }
        )

    failures = {
        "reciprocal_3f2_identity": identity_failures,
        "convolution_coefficient_identity": convolution_failures,
        "jacobi_parameter_conditions": jacobi_condition_failures,
        "squarefree_QQ": squarefree_failures,
        "irreducible_QQ": irreducibility_failures,
        "adjacent_gcd_QQ": gcd_failures,
        "adjacent_strict_interlacing": interlacing_failures,
    }
    return {
        "schema": "polydegree.e3.boundary-hypergeom.v1",
        "arithmetic": "exact QQ coefficients and rational Sturm isolation",
        "runtime": {
            "python": platform.python_version(),
            "sympy": sp.__version__,
        },
        "ranges": {
            "d_adjacent": [d_min, d_max],
            "n_identity_and_squarefree": [d_min, largest_n],
            "n_irreducible": [d_min, factor_max],
            "d_strict_interlacing": [d_min, interlace_max],
        },
        "checked_identities": {
            "all_reciprocal_3f2": not identity_failures,
            "all_convolution_coefficients": not convolution_failures,
            "all_jacobi_parameter_inequalities": not jacobi_condition_failures,
            "jacobi_parameter_minima": {
                name: str(value) for name, value in sorted(jacobi_minima.items())
            },
        },
        "finite_evidence": {
            "all_P_n_squarefree_over_QQ": not squarefree_failures,
            "all_nonconstant_P_n_irreducible_over_QQ": not irreducibility_failures,
            "all_adjacent_pairs_coprime_over_QQ": not gcd_failures,
            "all_adjacent_pairs_strictly_interlace": not interlacing_failures,
        },
        "residue_parameter_samples": residue_table,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d-min", type=int, default=2)
    parser.add_argument("--d-max", type=int, default=300)
    parser.add_argument("--factor-max", type=int, default=300)
    parser.add_argument("--interlace-max", type=int, default=120)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if args.d_min < 2:
        parser.error("d-min must be at least 2")
    if args.d_max < args.d_min:
        parser.error("d-max must be at least d-min")
    if not args.d_min <= args.factor_max <= args.d_max + 1:
        parser.error("factor-max must lie between d-min and d-max+1")
    if not args.d_min <= args.interlace_max <= args.d_max:
        parser.error("interlace-max must lie between d-min and d-max")

    report = analyze(
        d_min=args.d_min,
        d_max=args.d_max,
        factor_max=args.factor_max,
        interlace_max=args.interlace_max,
    )
    rendered = json.dumps(report, indent=2, sort_keys=True)
    print(rendered)
    if args.json is not None:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered + "\n")
    has_failures = any(report["failures"].values())
    return 1 if has_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
