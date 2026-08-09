## Summary

This paper finds a geometric meaning for a determinant that had previously
appeared as an auxiliary part of an algorithm.

The setting is the Polydegree Conjecture, a problem about how families of
polynomial transformations of the plane fit together when one family is
allowed to approach the boundary of another. Lewis, Perry and Straub reduced
many such questions to explicit polynomial calculations. Their criterion asks
for several coefficient polynomials to vanish while one later coefficient and
an additional determinant stay non-zero.

The new observation is that the additional determinant is not really an
independent object. Up to sign, it is the Jacobian determinant of the same
coefficient polynomials. In geometric language, the test is asking for one
ordinary, non-singular point of an intersection that avoids the next
hypersurface.

That translation simplifies both computation and proof. A finite-field search
only needs to find a simple common zero with the next coefficient non-zero.
Hensel lifting then carries the point to characteristic zero. This remains
valid even when the chosen prime makes the old determinant vanish modulo that
prime: the determinant becomes non-zero again at the characteristic-zero
lift. An exact example at (d=8) and (p=5) is retained to demonstrate that
the enlargement is real.

The paper also shows how a reduced zero divisor on a smooth curve can provide
the same good point. Finally, exact computations explore the first
non-trivial (e=3) column. For every (2\le d\le20), the entire affine
intersection is reduced and avoids the next coefficient. Every individual
one-variable boundary factor is proved squarefree; adjacent coprimality is
checked through (d=200).

The finite affine and adjacent-coprimality ranges are not an all-(d) theorem. They motivate a precise
uniform conjecture and identify the structural work still required.

## Summary for specialists

For the Lewis--Perry--Straub polynomials (g_{n,e}), (alpha_{i,j,e}) and
(a_{d,e}), coefficient reindexing gives

$$
\alpha_{i,j,e}=-\partial_{x_{i+1}}g_{j+1,e},
\qquad
a_{d,e}=(-1)^e\det D(g_{d,e},\ldots,g_{d+e-1,e}).
$$

Weighted Euler expansion produces an exact integral syzygy

$$
x_1a_{d,e}+(d+e-1)g_{d+e-1,e}J_{d,e}
=\sum_{r=0}^{e-2}(-1)^{e+r}(d+r)g_{d+r,e}M_r,
$$

where (J_{d,e}) is the (x_2,\ldots,x_e) Jacobian minor of the first
(e-1) coefficients and (M_r) are the corresponding signed minors. In the
chart (x_1=1), the LPS condition is therefore a smooth point of
(g_d=\cdots=g_{d+e-2}=0) outside (g_{d+e-1}=0).

The finite-field theorem assumes only a simple common zero with
(F_{e-1}J_{d,e}\ne0). Multivariate Hensel lifting gives a
(\mathbf Z_p)-point; evaluating the localised (\mathbf Q)-algebra in
(\mathbf Q_p), then using faithful base change and the weak
Nullstellensatz, gives the required complex point. No restriction
(p\nmid d+e-1) is needed. If (p\mid d+e-1), (a_{d,e}) is zero only in
the residue field; at the exact lift it equals
(-(d+e-1)F_{e-1}J_{d,e}\ne0) in (\mathbf Q_p).

The curve bridge requires the first (e-2) equations to cut out the smooth
geometrically integral curve scheme-theoretically, the zero divisor of the
next function to be non-empty, reduced and affine, and the final function to
avoid that support. A separate perfect-ground-field corollary handles a
coefficient-one closed point before base change. This avoids the ill-posed
practice of assigning degree greater than one to a closed point over an
algebraically closed field.

For (e=3), exact (\mathbf Q)/Singular calculations prove for
(2\le d\le20) that

$$
\dim_{\mathbf Q}\mathbf Q[X,Y]/(G_d,G_{d+1})
=\left\lfloor\frac{d(d+1)}6\right\rfloor,
$$

with (J_d) and (G_{d+2}) units in every coordinate algebra. Exact boundary
reduction through (d=200) finds adjacent torus factors coprime. A separate
terminating-hypergeometric argument proves every individual boundary factor
squarefree uniformly. Uniform radicality, Jacobian non-vanishing
and triple-zero exclusion remain open.

## Technical summary

The formal inverse of

$$
t+x_1t^2+\cdots+x_et^{e+1}
$$

has coefficients in (\mathbf Z[x_1,\ldots,x_e]), and its coefficient of
(w^{n+1}) is (g_{n,e}). This proves integrality before any reduction
modulo a prime and supplies a second internal construction of the
coefficients.

The derivative identity is a one-step multinomial reindexing, but the
weighted-Euler consequence is what changes the problem. On the partial zero
locus, it reduces the full determinant to a scalar times the next coefficient
and the affine Jacobian minor. The full alpha matrix may therefore be removed
from witness discovery; retaining it is useful only as redundant software
cross-checking.

The evidence archive distinguishes the following layers:

| Layer | Status |
|---|---|
| Derivative, determinant and Euler identities | Proved in the manuscript |
| Hensel/localisation/complex-existence theorem | Proved in the manuscript |
| Prime--gap--Jacobian curve bridge | Proved in the manuscript |
| Individual boundary-factor squarefreeness for all indices | Proved in the manuscript |
| Affine (e=3) result for (2\le d\le20) | Exact finite computation |
| Adjacent boundary coprimality through (d=200) | Exact finite computation |
| Uniform all-(d) statement | Open conjecture |

The 51 frozen witnesses for (50\le d\le100) replay under the upstream
dual-path verifier and a no-import standard-library verifier in ordinary and
optimised Python. The independent-code reports are byte-identical across
modes. Sixteen negative or mutation controls and one positive
bad-characteristic regression are retained. These are producer-side checks,
not unaffiliated reproduction.

One upstream robustness defect is preserved in the record: an integrality
guard is a Python `assert`, so optimised Python removes it. The current data
still pass, and the replacement verifier uses explicit exceptions. The issue
is a fail-open detection risk, not evidence that a current certificate is
false.

## Why this matters

| Audience | What the paper changes | Useful next action |
|---|---|---|
| Polynomial-automorphism researchers | Replaces an auxiliary determinant condition by a local smoothness statement. | Audit the bridge to Lewis--Perry--Straub Theorem 4 and test the method in other polydegree columns. |
| Algebraic geometers | Connects weighted coefficient identities, complete intersections, divisor zeros and affine support. | Seek a uniform toric or intersection-theoretic proof for the (e=3) complete intersections. |
| Arithmetic and computational algebra researchers | Shrinks the modular certificate and admits primes excluded by a determinant-unit test. | Reimplement the Hensel certificate independently and formalise the localisation/base-change step. |
| Special-functions researchers | Finite free convolution proves the individual boundary factors have simple positive roots. | Prove or refute uniform adjacent coprimality across the changing hypergeometric families. |
| Computer-assisted mathematics researchers | Provides a worked separation between written proof, finite exact evidence and assurance controls. | Challenge the verifier with independent representations and retain fail-closed negative controls. |

## What is proved—and what is not

The paper proves a general Jacobian interpretation, exact weighted-Euler
syzygy, sharper Hensel criterion and curve-theoretic bridge. It does not prove
the Polydegree Conjecture, the Polydegree Ideal Conjecture or the all-(d)
(e=3) statement.

It also does not claim the first infinite family. Lewis--Perry--Straub
Theorem 14, attributed to Edo, already covers (d\equiv1\pmod3) in the
(e=3) column. The derivative--Jacobian packaging was not located in the
bounded prior-art search, but priority remains provisional pending specialist
database searches, original-author contact and expert review.

Internal replay, a clean manifest, exact arithmetic and negative controls do
not amount to independent reproduction, proof-assistant verification,
specialist acceptance, editorial peer review or a REF rating.

## The most valuable next projects

### 1. Prove the uniform (e=3) geometry

Show for every (d\ge2) that ((G_d,G_{d+1})) is radical of length
(\lfloor d(d+1)/6\rfloor), with (J_d) and (G_{d+2}) units in its
coordinate algebra. A proof would make every affine point good, not merely
show existence.

### 2. Settle adjacent boundary coprimality

Prove adjacent coprimality for the one-variable boundary polynomials
uniformly. Individual squarefreeness is now proved; the unresolved comparison
is between two different, simultaneously changing hypergeometric families.

### 3. Exclude triple common zeros structurally

Find a recurrence, syzygy or resultant identity proving
((G_d,G_{d+1},G_{d+2})=(1)) in the affine chart, or find a counterexample.
This is logically distinct from radicality.

### 4. Obtain independent and specialist checks

Ask the original authors whether the Jacobian observation or larger
computations are known, rerun the theorem chain outside the producing
workflow, and formalise the elementary identities and Hensel bridge.

## What is in the evidence package

The candidate package contains the manuscript in PDF, LaTeX and
accessible Markdown; bilingual abstracts; an Evidence Press reading layer and
metadata template; verified bibliography; exact affine and boundary receipts;
the uniform boundary-squarefreeness proof and its repaired referee record;
the frozen 51-witness corpus; the standard-library Jacobian verifier;
mutation and bad-characteristic controls; the upstream-source reconciliation;
claim-status, provenance and assurance records; build instructions; and a
SHA-256 manifest.

The package is a pre-publication candidate. No repository, release tag, DOI or
live Evidence Press page is claimed until those external objects exist and
their public bytes have been read back.
