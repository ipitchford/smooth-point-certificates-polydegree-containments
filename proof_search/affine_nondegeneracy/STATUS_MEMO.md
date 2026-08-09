# Affine nondegeneracy attack: exact status memo

## Verdict

**OPEN, with one substantial uniform face theorem proved.**  The present work
does not prove that

\[
I_d=(G_d,G_{d+1})\subset\mathbf Q[X,Y]
\]

is radical of length \(\lfloor d(d+1)/6\rfloor\), with \(J_d\) and
\(G_{d+2}\) units, for every \(d\).  It does prove the Newton support and
mixed-volume formula uniformly, reduces every nonzero-weight face system to
three explicit univariate families, and proves consecutive coprimality for one
of those three families for every \(d\).  Two boundary families and two
interior unit-ideal conditions remain genuinely open.

No candidate manuscript or release output was edited.

## Status ledger

| Statement | Status | Basis |
|---|---|---|
| Exact support of \(G_n\) | **PROVED, all \(n\)** | Explicit nonzero Lagrange coefficient |
| Newton-polygon vertex/facet classification | **PROVED, all \(n\)** | Six residue classes modulo 6 |
| \(\operatorname{MV}(\Delta_d,\Delta_{d+1})=\lfloor d(d+1)/6\rfloor\) | **PROVED, all \(d\ge2\)** | Exact polygon-area calculation |
| Only three possible common positive-dimensional faces for \(d\ge8\) | **PROVED** | Common-normal enumeration; \(2\le d<8\) is direct |
| \(\gcd(G_d(X,0),G_{d+1}(X,0))=1\) | **PROVED, all \(d\ge2\)** | Jacobi representation plus two contiguous identities |
| \(\gcd(G_d(0,Y),G_{d+1}(0,Y))=1\) | **OPEN** | Exact through \(d=250\) |
| Coprimality of consecutive top-weight faces | **OPEN** | Exact through \(d=250\) |
| Affine length formula | **OPEN uniformly** | Conditional on the preceding two face claims; exact through \(d=30\) |
| \(I_d+(J_d)=(1)\), hence radicality and \(J_d\) a unit | **OPEN uniformly** | Exact through \(d=30\) |
| \(I_d+(G_{d+2})=(1)\) | **OPEN uniformly** | Exact through \(d=30\) |

The exact computations found no counterexample: the full affine statement now
holds computationally for \(2\le d\le30\), extending the previous range
\(2\le d\le20\), and all three face gcd tests pass for \(2\le d\le250\).
These are finite exact results, not extrapolated theorems.

## 1. Uniform Newton support

Lagrange inversion gives

\[
G_n(X,Y)=\sum_{2b+3c\le n}\gamma_{n,b,c}X^bY^c,
\]

where

\[
\gamma_{n,b,c}=
(-1)^{n-b}
\frac{(2n-b-2c)!}
{(n+1)n!(n-2b-3c)!b!c!}.
\]

Every displayed coefficient is nonzero.  Consequently

\[
\Delta_n=\operatorname{Newt}(G_n)
=\operatorname{conv}\{(b,c)\in\mathbf Z_{\ge0}^2:2b+3c\le n\}.
\]

For \(n=6q+r\), the vertices are as follows; repeated or collinear entries in
the few smallest cases are deleted.

| \(r\) | vertices in counterclockwise order |
|---:|---|
| 0 | \((0,0),(3q,0),(0,2q)\) |
| 1 | \((0,0),(3q,0),(3q-1,1),(2,2q-1),(0,2q)\) |
| 2 | \((0,0),(3q+1,0),(1,2q),(0,2q)\) |
| 3 | \((0,0),(3q+1,0),(3q,1),(0,2q+1)\) |
| 4 | \((0,0),(3q+2,0),(2,2q),(0,2q+1)\) |
| 5 | \((0,0),(3q+2,0),(3q+1,1),(1,2q+1),(0,2q+1)\) |

For the nondegenerate residue-class polygons, the common base normals are

\[
(0,-1),\quad(-1,0),\quad(2,3).
\]

The additional outward normals by residue are

\[
\begin{array}{c|c}
r&\text{additional normals}\\ \hline
0&\varnothing\\
1&(1,1),(1,2)\\
2&(0,1)\\
3&(1,1)\\
4&(1,2)\\
5&(1,1),(0,1).
\end{array}
\]

Adjacent residue classes share none of the additional normals.  Thus, for
every \(d\ge8\), the only normals selecting edges of both \(\Delta_d\) and
\(\Delta_{d+1}\) are precisely the three base normals.  If a normal is not
shared, at least one initial form is a nonzero monomial and its torus face
system has no zero.  Direct enumeration gives only a subset of the same three
families for \(2\le d<8\).

It follows that nondegeneracy at infinity reduces exactly to consecutive
coprimality for

\[
V_n(X)=G_n(X,0),\qquad U_n(Y)=G_n(0,Y),
\]

and the top-weight face polynomial \(P_n\) defined below.  This is a complete
face ledger, not a genericity heuristic.

## 2. Uniform mixed-volume calculation

Twice the area of \(\Delta_{6q+r}\) is

\[
6q^2,\quad 6q^2+2q-1,\quad 6q^2+4q,\quad
6q^2+6q+1,\quad 6q^2+8q+2,\quad 6q^2+10q+3
\]

for \(r=0,\ldots,5\).  Twice the area of
\(\Delta_d+\Delta_{d+1}\), in the same six cases for \(d\), is

\[
24q^2+4q-1,\ 24q^2+12q-1,\ 24q^2+20q+3,
\]
\[
24q^2+28q+7,\ 24q^2+36q+11,\ 24q^2+44q+19.
\]

Substitution in

\[
\operatorname{MV}(P,Q)=
\operatorname{Area}(P+Q)-\operatorname{Area}(P)-\operatorname{Area}(Q)
\]

gives, respectively,

\[
6q^2+q,\quad6q^2+3q,\quad6q^2+5q+1,
\]
\[
6q^2+7q+2,\quad6q^2+9q+3,\quad6q^2+11q+5,
\]

which is \(\lfloor d(d+1)/6\rfloor\) in every residue class.

This count is multiplicity-weighted.  Even after both remaining face gcds are
proved, Bernstein's theorem will give the affine length, not radicality.

## 3. A uniform theorem for the \(Y=0\) face

Let \(m=\lfloor n/2\rfloor\).  Reversing and normalising \(V_n\), with
\(s=(4X)^{-1}\), gives

\[
A_m(s)={}_2F_1\!\left(\begin{matrix}-m,3m+1\\1/2\end{matrix};s\right)
\quad(n=2m),
\]

\[
B_m(s)={}_2F_1\!\left(\begin{matrix}-m,3m+3\\3/2\end{matrix};s\right)
\quad(n=2m+1).
\]

More precisely, if \(v_{n,m}\) is the nonzero leading coefficient of
\(V_n\), then

\[
V_{2m}(X)=v_{2m,m}X^mA_m((4X)^{-1}),\qquad
V_{2m+1}(X)=v_{2m+1,m}X^mB_m((4X)^{-1}).
\]

They are positive multiples of shifted Jacobi polynomials:

\[
A_m(s)\propto P_m^{(-1/2,,2m+1/2)}(1-2s),\qquad
B_m(s)\propto P_m^{(1/2,,2m+3/2)}(1-2s).
\]

Both Jacobi parameters exceed \(-1\); hence all roots are simple and lie in
\((0,1)\).  Direct coefficient comparison in the terminating series proves
the two polynomial identities

\[
B_m=\frac{2}{3m+2}A_m+
\frac{4s-3}{2(3m+2)(3m+1)}A_m',
\]

\[
A_{m+1}=(1-8(m+1)s)B_m+2s\left(1-\frac43s\right)B_m'.
\]

The coefficient comparison is uniform in \(m\) and the coefficient index;
the script's bounded checks are regression tests, not the logical basis of the
identities.

If \(A_m\) and \(B_m\) had a common root, the first identity and simplicity
would force \(s=3/4\).  If \(B_m\) and \(A_{m+1}\) had a common root, the
second identity, the nonzero constant term, and simplicity again force
\(s=3/4\).  Thus every hypothetical consecutive common root has \(X=1/3\).

At \((X,Y)=(1/3,0)\), the inverse equation is

\[
w=I+I^2+\frac13I^3=\frac{(1+I)^3-1}{3},
\]

so

\[
I(w)=(1+3w)^{1/3}-1,
\qquad
V_n(1/3)=3^{n+1}\binom{1/3}{n+1}\ne0.
\]

Also \(V_n(0)\ne0\), so the reversal loses no possible common root.  Therefore

\[
\boxed{\gcd(V_d,V_{d+1})=1\quad\text{for every }d\ge2.}
\]

## 4. The two unresolved face families

### 4.1 The \(X=0\) family

For \(n=3m+r\), reversal and normalisation of \(U_n\) gives

\[
H_{m,r}(s)={}_3F_2\!\left(
\begin{matrix}-m,\,2m+r+1,\,2m+r+1/2\\
\beta_{r,1},\,\beta_{r,2}
\end{matrix};s\right),
\qquad s=-\frac4{27Y},
\]

where

\[
(\beta_{0,1},\beta_{0,2})=(1/3,2/3),\quad
(\beta_{1,1},\beta_{1,2})=(2/3,4/3),\quad
(\beta_{2,1},\beta_{2,2})=(4/3,5/3).
\]

The three consecutive transitions are \((m,0)\to(m,1)\),
\((m,1)\to(m,2)\), and \((m,2)\to(m+1,0)\).  No uniform interlacing,
resultant, or contiguous-identity proof for all three transitions was found.
Exact arithmetic proves coprimality through \(d=250\).

Terminating \({}_3F_2\) multiple-orthogonality theory is a plausible source of
tools, for example [Lima--Loureiro (arXiv:2012.13913)](https://arxiv.org/abs/2012.13913)
and [Lima (arXiv:2208.03539)](https://arxiv.org/abs/2208.03539).  This is only a
route: the required parameter matching, positive measures, and interlacing
across the three changing parameter families have not been established here.

### 4.2 The top-weight family

Let \(\epsilon=n\bmod2\), \(A=(n-3\epsilon)/2\), and
\(z=Y^2/X^3\).  On the torus the top face is a nonzero monomial times

\[
P_n(z)=\frac1{n+1}
\sum_{k=0}^{\lfloor A/3\rfloor}
(-1)^{A+\epsilon-k}
\frac{(n+A+\epsilon-k)!}
{n!(A-3k)!(\epsilon+2k)!}z^k.
\]

Its adjacent coefficient ratio is

\[
\frac{[z^{k+1}]P_n}{[z^k]P_n}
=-
\frac{(A-3k)(A-3k-1)(A-3k-2)}
{(n+A+\epsilon-k)(\epsilon+2k+1)(\epsilon+2k+2)}.
\]

This gives another terminating hypergeometric family, but no uniform
consecutive-coprimality proof was obtained.  Exact arithmetic proves the claim
through \(d=250\).

## 5. Exact theorem gates

Define four explicit conditions:

\[
\mathsf U_d:\ \gcd(U_d,U_{d+1})=1,
\qquad
\mathsf P_d:\ \gcd(P_d,P_{d+1})=1,
\]

\[
\mathsf S_d:\ (G_d,G_{d+1},J_d)=(1),
\qquad
\mathsf T_d:\ (G_d,G_{d+1},G_{d+2})=(1).
\]

The proved \(V\)-face theorem plus \(\mathsf U_d\) and \(\mathsf P_d\)
exclude coordinate-axis solutions and all roots at toric infinity.  Bernstein's
theorem then gives

\[
\dim_{\mathbf Q}\mathbf Q[X,Y]/I_d
=\left\lfloor\frac{d(d+1)}6\right\rfloor.
\]

Condition \(\mathsf S_d\) is independent of the nonzero-weight face ledger.
For the zero-dimensional complete intersection in characteristic zero it is
equivalent to every geometric point having full Jacobian rank; it makes the
quotient finite etale, so \(I_d\) is radical and \(J_d\) is a unit.
Condition \(\mathsf T_d\) separately says that \(G_{d+2}\) is a unit in the
same quotient.  Neither follows from the multiplicity-weighted BKK count.

A commutative-algebra proof could close \(\mathsf S_d\) or \(\mathsf T_d\)
by a uniform Bezout identity, or by a closed nonzero formula for the norms of
\(J_d\) and \(G_{d+2}\) in the finite algebra.  Resultant or subresultant
recurrences are a plausible technique, but no such identity or nonvanishing
formula was obtained.  Squarefreeness of a single elimination polynomial
would require the usual leading-coefficient and shape/fibre hypotheses; it
must not be treated as automatically proving radicality.

## 6. Exact finite evidence

### Face systems

The independent script `face_system_audit.py` reconstructs coefficients from
the explicit Lagrange formula and imports no archive verifier.  Over exact
\(\mathbf Q\) arithmetic it checked:

- the support, hull, facet-normal and mixed-volume formulas through \(d=250\);
- all three consecutive face gcds for \(2\le d\le250\);
- squarefreeness of each face polynomial for \(2\le n\le251\);
- the Jacobi transformations, contiguous identities and special value over the
  corresponding bounded range;
- one injected-common-factor and one perturbed-identity rejection control.

All checks passed.

### Full affine ideals beyond the previous range

Exact SymPy/Singular computations over \(\mathbf Q\) for \(21\le d\le30\)
gave

\[
\dim \mathbf Q[X,Y]/I_d=
77,84,92,100,108,117,126,135,145,155,
\]

exactly \(\lfloor d(d+1)/6\rfloor\), and returned quotient dimension zero for
both \(I_d+(J_d)\) and \(I_d+(G_{d+2})\) at every index.  Thus no counterexample
was found through \(d=30\).

These heavy receipts were produced by the existing geometry exploration
program, whose SHA-256 is
`8e7454b5edfd7676561382659e700869bd991b347e1c3e1c200dba1377961715`.
It uses explicit fail-closed tests and contains no Python `assert`.  The new
`validate_affine_receipts.py` strictly validates their schema, index set,
formula fields, unit-ideal dimensions and hashes, but does **not** recompute the
Groebner bases and is not an independent reproduction.

## 7. Reproduction and assurance boundary

Environment used: Python 3.14.6, SymPy 1.14.0, Singular 4.4.1, macOS arm64.

```sh
cd work/irreducible-norms-ref-upgrade/stage2/affine_nondegeneracy

python3 face_system_audit.py --max-d 250 --json face_audit_2_250.json
python3 -O face_system_audit.py --max-d 250 --json face_audit_2_250_optimized.json
cmp face_audit_2_250.json face_audit_2_250_optimized.json

python3 validate_affine_receipts.py --json affine_21_30_validated.json
python3 -O validate_affine_receipts.py --json affine_21_30_validated_optimized.json
cmp affine_21_30_validated.json affine_21_30_validated_optimized.json
```

Both comparisons succeeded.  The acceptance logic in both new scripts uses no
`assert`, and normal/`-O` outputs are byte-identical.

SHA-256 receipts:

- `face_system_audit.py`:
  `05c2a2773184a6e57168e1ae82e8ccdebc526f53c170ae96ac2cb83f88d1d121`
- `face_audit_2_250.json` (same hash in normal and `-O`):
  `0e135e2e8bd241a325dcedf9774d9f6c81802e501b45aca333a6924aefd2e75a`
- `validate_affine_receipts.py`:
  `04b263863cc4f5ec7ced1fda5a861b9282b8889e8b47756292f4b56c826f8e18`
- `affine_21_30_validated.json` (same hash in normal and `-O`):
  `26d2db480e8b76f38ac1bd8d6d6236af889afed490619503e5ab82f52d390287`
- combined heavy-computation receipt `affine_21_30.json`:
  `5de222adb95abff801cb41004600a0da564b5a6b1b72a337f3f31e3e522f9060`

The face verifier is code-independent from the archive but necessarily tests
the same published coefficient formula.  The affine receipt validator shares
the producer data boundary and provides integrity/schema assurance only.  None
of the computations constitutes an all-\(d\) proof, formal verification, or
independent peer review.

