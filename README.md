# Smooth-point certificates for Polydegree containments

**Anonymous · version 0.4.1-candidate · unrefereed research candidate**

This repository contains a mathematical manuscript, exact symbolic checks,
review records and a deterministic evidence package about the Polydegree
Conjecture for polynomial transformations of the complex plane.

## The idea in plain English

Earlier work reduced certain geometric containment questions to finding
numbers that make several explicit polynomials vanish while an extra
determinant remains non-zero. The main observation here is that the extra
determinant is not a separate mystery: it is the Jacobian of the same
polynomials.

Geometrically, the test is therefore asking for an ordinary smooth point of
an intersection, away from one additional hypersurface. This gives a smaller
finite-field certificate and a cleaner route from modular evidence to a
complex solution.

The paper proves the Jacobian identity, an integral Euler syzygy, the sharper
Hensel-lifting criterion, a curve-theoretic bridge, and a uniform theorem that
the individual one-variable boundary factors are squarefree. Exact
computation establishes the full affine statement for `2 <= d <= 20` and
adjacent boundary coprimality through `d = 200`.

The corresponding all-`d` affine theorem and uniform adjacent coprimality are
open. The finite ranges are evidence for those questions, not proofs of them.

## Start here

- [Paper PDF](build/main.pdf)
- [Accessible paper source](MANUSCRIPT.md)
- [Claim and evidence ledger](CLAIM_STATUS.json)
- [Status](STATUS.md)
- [Assurance boundary](ASSURANCE.md)
- [Provenance](PROVENANCE.md)
- [Academic-integrity report](ACADEMIC_INTEGRITY_REPORT.md)
- [Build and replay instructions](BUILD.md)

## Replaying the principal checks

Install the pinned Python dependency and ensure Singular is available:

```sh
python3 -m pip install -r requirements.txt
```

Then run the fail-closed package validation and the core exact checks:

```sh
python3 -B scripts/verify_manifest.py --root "$PWD"
python3 -B -O scripts/verify_manifest.py --root "$PWD"

python3 -B scripts/validate_candidate.py --root "$PWD"
python3 -B -O scripts/validate_candidate.py --root "$PWD"

python3 -B scripts/verify_jacobian_refactor.py \
  --witness-data evidence/upstream/polydegree_e3_witnesses_50_100.json
python3 -B scripts/test_mutations.py \
  --witness-data evidence/upstream/polydegree_e3_witnesses_50_100.json
```

The extended affine, boundary and hypergeometric commands are recorded in
[`BUILD.md`](BUILD.md). The source package records 10/10 symbolic gates,
51/51 witness relations and 17/17 mutation or regression controls in ordinary
and optimized Python modes.

These are producer-side regression checks. They are not independent
reproduction, proof-assistant formalisation, external specialist review or
editorial peer review.

## Licence and AI disclosure

Original non-code research and release material is dedicated under CC0 1.0.
Original code is licensed under MIT. Embedded upstream material retains its
own licence, and cited papers retain their original rights; see
[`LICENSES.md`](LICENSES.md).

Automated research, symbolic-computation and language-model tools assisted
literature triage, proof exploration, exact verification, adversarial review,
drafting and packaging under human direction. They are not scholarly authors.
Agreement among tools inside one coordinated workflow is not independent
review.
