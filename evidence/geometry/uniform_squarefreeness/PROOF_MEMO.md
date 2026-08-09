# Uniform boundary analysis for \(e=3\)

## Claim ledger

This memo concerns only the torus polynomials \(P_n\) defined by

\[
g_{n,3}(0,X,Y)=X^A Y^\epsilon P_n(Y^2/X^3),\qquad
\epsilon=n\bmod 2,\quad A=\frac{n-3\epsilon}{2}.
\]

- **[PROVED, all \(n\ge2\)]** \(P_n\) has only simple positive real
  zeros. In particular, \(P_n\) is squarefree over every
  characteristic-zero field.
- **[OPEN, all \(d\)]** No uniform proof was found for
  \(\gcd(P_d,P_{d+1})=1\).
- **[EXACT FINITE EVIDENCE]** Over \(\mathbf Q\), adjacent coprimality holds
  for \(2\le d\le300\), every nonconstant \(P_n\) is irreducible for
  \(2\le n\le300\), and adjacent roots strictly interlace for
  \(2\le d\le120\). The last result uses rational Sturm isolating intervals,
  not floating-point roots.

Thus the strongest safe Stage 2 upgrade is **uniform squarefreeness**, not
uniform adjacent coprimality.

## 1. Exact reciprocal hypergeometric form

Write

\[
P_n(z)=\sum_{k=0}^{M}c_{n,k}z^k,\qquad
M=\left\lfloor\frac A3\right\rfloor,\qquad
A=3M+\delta,\quad\delta\in\{0,1,2\}.
\]

Lagrange inversion gives

\[
c_{n,k}=\frac{(-1)^{A+\epsilon-k}}{n+1}
\frac{(n+A+\epsilon-k)!}
{n!(A-3k)!(\epsilon+2k)!}.
\]

Put

\[
N=n+A+\epsilon,\qquad H=N-M+1,
\]

and

\[
(\beta_1,\beta_2)=
\begin{cases}
(1/3,2/3),&\delta=0,\\
(2/3,4/3),&\delta=1,\\
(4/3,5/3),&\delta=2.
\end{cases}
\]

Finally, set

\[
\sigma=\begin{cases}1/2,&\epsilon=0,\\-1/2,&\epsilon=1,\end{cases}
\qquad a=-M+\sigma.
\]

Normalize the reciprocal by

\[
R_n(s)=\frac{s^M P_n(1/s)}{c_{n,M}}
      =\sum_{j=0}^{M}\frac{c_{n,M-j}}{c_{n,M}}s^j.
\]

Direct division of consecutive coefficients gives

\[
\frac{c_{n,M-j-1}}{c_{n,M-j}}
=-
\frac{(N-M+j+1)(\epsilon+2M-2j-1)(\epsilon+2M-2j)}
{(\delta+3j+1)(\delta+3j+2)(\delta+3j+3)}.
\]

The parity and residue factors satisfy

\[
(\epsilon+2M-2j-1)(\epsilon+2M-2j)
=4(j-M)(j-M+\sigma)
\]

and

\[
(\delta+3j+1)(\delta+3j+2)(\delta+3j+3)
=27(j+1)(j+\beta_1)(j+\beta_2).
\]

Since \(H=N-M+1\), this is exactly the hypergeometric coefficient ratio:

\[
\boxed{
R_n(s)={}_3F_2\!\left(
\begin{matrix}-M,\,a,\,H\\ \beta_1,\,\beta_2\end{matrix};
-\frac{4s}{27}
\right).}
\tag{1}
\]

This is an algebraic identity, with no asymptotic or genericity step.

For \(n=6m+r\), the parameters are:

| \(r\) | \(M\) | \(a\) | \(H\) | \((\beta_1,\beta_2)\) |
|---:|---:|---:|---:|---:|
| 0 | \(m\) | \(-m+1/2\) | \(8m+1\) | \((1/3,2/3)\) |
| 1 | \(m-1\) | \(-m+1/2\) | \(8m+3\) | \((4/3,5/3)\) |
| 2 | \(m\) | \(-m+1/2\) | \(8m+4\) | \((2/3,4/3)\) |
| 3 | \(m\) | \(-m-1/2\) | \(8m+5\) | \((1/3,2/3)\) |
| 4 | \(m\) | \(-m+1/2\) | \(8m+7\) | \((4/3,5/3)\) |
| 5 | \(m\) | \(-m-1/2\) | \(8m+8\) | \((2/3,4/3)\) |

The \(r=1\) row starts at \(n=7\), so \(m\ge1\) there.

## 2. All-\(n\) theorem: simple positive zeros

Define

\[
F_n(x)={}_3F_2\!\left(
\begin{matrix}-M,\,a,\,H\\ \beta_1,\,\beta_2\end{matrix};x
\right).
\]

The parameter-concatenation theorem for degree-\(M\) multiplicative finite
free convolution gives, up to a nonzero scalar,

\[
F_n=p_n\boxtimes_M q_n,
\tag{2}
\]

where

\[
p_n(x)={}_2F_1(-M,a;\beta_1;x),\qquad
q_n(x)={}_2F_1(-M,H;\beta_2;x).
\]

If \(p_j,q_j\) are the coefficients of \(x^j\) in the two factors, the
coefficient of \(x^j\) in \(F_n\) is

\[
\frac{p_jq_j}{(-M)_j/j!}.
\]

This is precisely the binomial normalization in the degree-\(M\)
multiplicative convolution. The verifier checks it term by term.

### 2.1 The first factor has simple negative zeros

Pfaff's transformation and \(a=-M+\sigma\) give

\[
p_n(x)=(1-x)^M
{}_2F_1\!\left(-M,M+\beta_1-\sigma;\beta_1;
\frac{x}{x-1}\right).
\tag{3}
\]

The hypergeometric polynomial on the right is a Jacobi polynomial with

\[
\alpha=\beta_1-1>-1,\qquad
\gamma=-\sigma\in\{-1/2,1/2\}>-1.
\]

It has \(M\) simple roots \(y\in(0,1)\). Under \(y=x/(x-1)\), they map to

\[
x=\frac{y}{y-1}<0.
\]

Because \(p_n\) has degree exactly \(M\), these are all its roots. Hence
\(p_n\) has \(M\) simple negative roots.

### 2.2 The second factor has simple positive zeros

The direct Jacobi representation is

\[
q_n(x)=\frac{M!}{(\beta_2)_M}
P_M^{(\beta_2-1,\,H-M-\beta_2)}(1-2x).
\tag{4}
\]

Its Jacobi parameters obey

\[
\beta_2-1>-1
\]

and, because \(A=3M+\delta\),

\[
H-M-\beta_2
=n+M+\delta+\epsilon+1-\beta_2>-1.
\]

Thus \(q_n\) has \(M\) simple roots in \((0,1)\).

### 2.3 Convolution preserves sign and logarithmic mesh forces simplicity

The cited sign-preservation theorem says that the multiplicative convolution
of a negative-rooted and a positive-rooted degree-\(M\) polynomial is
negative-rooted. Equation (2) therefore puts all roots of \(F_n\) in
\((-\infty,0)\), counting multiplicity.

Simplicity follows from logarithmic-mesh preservation, without invoking a
strict-interlacing clause. Put

\[
\widehat p_n(x)=p_n(-x).
\]

By Section 2.1, \(\widehat p_n\) has \(M\) simple positive roots, and by
Section 2.2, \(q_n\) has \(M\) positive roots. For \(M\ge2\), order the roots
of a positive-rooted polynomial \(h\) as
\(\lambda_1(h)\ge\cdots\ge\lambda_M(h)>0\) and define

\[
\operatorname{lmesh}(h)
=\min_{1\le i<M}\frac{\lambda_i(h)}{\lambda_{i+1}(h)}.
\]

The roots of \(\widehat p_n\) are simple, so
\(\operatorname{lmesh}(\widehat p_n)>1\). Proposition 2.17 of
arXiv:2309.10970v3 gives

\[
\operatorname{lmesh}(\widehat p_n\boxtimes_Mq_n)
\ge \operatorname{lmesh}(\widehat p_n)>1.
\]

Consequently \(\widehat p_n\boxtimes_Mq_n\) has only simple positive roots.
The reflection identity for multiplicative finite free convolution gives,
up to a nonzero scalar,

\[
\widehat p_n\boxtimes_Mq_n
\simeq (p_n\boxtimes_Mq_n)(-x).
\]

Thus \(F_n\simeq p_n\boxtimes_Mq_n\) has only simple negative roots. When
\(M=1\), sign preservation gives a degree-one negative-rooted polynomial,
which is automatically simple; the \(M=0\) cases are constant and trivial.

Finally, (1) says \(R_n(s)=F_n(-4s/27)\), so \(R_n\) has only simple positive
roots. Reciprocation preserves simplicity and inverts each nonzero root.
Therefore:

> **Theorem.** For every \(n\ge2\), every zero of \(P_n\) is real, positive,
> and simple. Consequently \(P_n\) is squarefree over \(\mathbf Q\), and
> over every characteristic-zero extension field.

## 3. External theorems and checked assumptions

The proof uses exactly the following external results.

1. **Pfaff transformation.** DLMF equation
   [15.8.1](https://dlmf.nist.gov/15.8.E1). Here one upper parameter is
   \(-M\), so the identity specializes to a polynomial identity and no
   analytic-continuation issue remains.
2. **Jacobi representation and zeros.** The normalization is DLMF equation
   [18.5.7](https://dlmf.nist.gov/18.5.E7), and the classical zero theorem is
   in [DLMF section 18.16](https://dlmf.nist.gov/18.16): for both Jacobi
   parameters greater than \(-1\), the degree-\(M\) polynomial has \(M\)
   simple zeros in \((-1,1)\). The four required inequalities are displayed
   in Sections 2.1 and 2.2 and checked exactly by the verifier.
3. **Finite free convolution: concatenation and signs.** A.
   Martínez-Finkelshtein, R. Morales, and D. Perales,
   [“Zeros of generalized hypergeometric polynomials via finite free
   convolution. Applications to multiple orthogonality”](https://arxiv.org/pdf/2404.11479),
   arXiv:2404.11479v2, posted 3 June 2024:
   **Theorem A** concatenates hypergeometric parameters under multiplicative
   finite free convolution, and **Proposition 2.4(v)** sends a
   negative-rooted polynomial convolved with a positive-rooted one to a
   negative-rooted polynomial, including strict half-lines. Here \(p_n,q_n\)
   both have exact degree \(M\), \(p_n\) is negative-rooted, and \(q_n\) is
   positive-rooted, so every hypothesis used from this source is met.
4. **Logarithmic-mesh preservation.** A. Martínez-Finkelshtein, R. Morales,
   and D. Perales,
   [“Real roots of hypergeometric polynomials via finite free
   convolution”](https://arxiv.org/pdf/2309.10970),
   arXiv:2309.10970v3, posted 2 May 2024:
   **Proposition 2.17** states that multiplicative finite free convolution of
   positive-rooted polynomials does not decrease logarithmic mesh, and
   **Remark 2.12** records the reflection identity used above. We apply the
   proposition only for \(M\ge2\); \(M=0,1\) are handled separately.

These exact numbered statements and their assumptions were inspected directly
for this memo. Scalar normalization conventions do not affect roots,
logarithmic mesh, or squarefreeness. We deliberately do not use the strict
sentence following Proposition 2.6 of arXiv:2404.11479v2: its cited proof
source establishes non-strict preservation, and the broader wording with a
merely nonnegative-rooted convolution factor admits the degeneracy
\(q(x)=x^M\). The positive-half-line logarithmic-mesh result above is the
applicable nondegenerate theorem and is sufficient.

## 4. Adjacent coprimality: open status and obstruction

### [OPEN]

The theorem above does **not** prove

\[
\gcd(P_d,P_{d+1})=1.
\]

It excludes repeated roots within each polynomial but does not exclude a root
shared by two different polynomials.

Strict adjacent interlacing would suffice. The exact Sturm sweep proves it
through \(d=120\), and exact polynomial arithmetic finds no common factor
through \(d=300\), but the convolution proof compares neither
\(F_d\) with \(F_{d+1}\) nor their two simultaneously changing factors.

The six-row table isolates the difficulty: under \(n\mapsto n+1\), the
terminating degree may change, \(a\) may shift by \(1\), \(H\) shifts by
\(1\) or \(2\), and the denominator pair cycles among thirds. This is not
one standard integer contiguous shift and not one fixed Jacobi family.
Real-rootedness of each member alone gives no adjacent comparison.

Two promising routes, neither completed here, are:

1. find a residue-class-specific contiguous identity that, at a hypothetical
   common root, forces \(P_d'\) to vanish and contradicts the proved
   squarefreeness; or
2. prove uniform irreducibility over \(\mathbf Q\), then exclude association
   for equal-degree adjacent pairs.

The second route is supported only by finite factorization evidence. Direct
adjacent resultants quickly acquire large unstructured factors, giving no
observed product formula. Uniform adjacent coprimality therefore remains a
conjecture.

## 5. Exact verification receipt

The fail-closed verifier checks:

- the reciprocal \({}_3F_2\) identity coefficient by coefficient;
- the convolution factorization coefficient by coefficient;
- every Jacobi parameter inequality used above;
- squarefreeness for \(2\le n\le301\);
- irreducibility for every nonconstant \(P_n\), \(2\le n\le300\);
- adjacent gcd \(1\) for \(2\le d\le300\); and
- exact strict interlacing for \(2\le d\le120\).

It was run under Python 3.14.6 and SymPy 1.14.0 in normal and optimized modes:

    python3 verify_boundary_hypergeom.py \
      --d-max 300 --factor-max 300 --interlace-max 120 \
      --json results_2_300.json

    python3 -O verify_boundary_hypergeom.py \
      --d-max 300 --factor-max 300 --interlace-max 120 \
      --json results_2_300_optimized.json

The JSON files are byte-identical and both have SHA-256

    8fbc4d290027577180e418160e94ebf288ec30367ff33f8f538383dfa3045e5b

No correctness condition depends on Python assertions.
