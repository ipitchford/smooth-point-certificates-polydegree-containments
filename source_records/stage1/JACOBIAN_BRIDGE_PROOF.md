# Jacobian bridge: exact statements and proofs

**Status:** proved from the displayed Lewis--Perry--Straub definitions; priority
not established.  This note is a research-stage proof record, not a submitted
manuscript.

## 1. Definitions

Fix \(e\geq1\). For \(\mathbf a=(a_1,\ldots,a_e)\), put

\[
|\mathbf a|=a_1+\cdots+a_e,
\qquad
\mathbf a\cdot\mathbf N=a_1+2a_2+\cdots+ea_e.
\]

For \(n\geq 0\), define

\[
g_{n,e}=\frac{1}{n+1}
\sum_{\mathbf a\cdot\mathbf N=n}
(-1)^{|\mathbf a|}
\binom{n+|\mathbf a|}{\mathbf a,n}\mathbf x^{\mathbf a}.
\]

For \(0\leq i\leq e-1\) and \(j\geq-1\), define

\[
\alpha_{i,j,e}=
\sum_{\mathbf a\cdot\mathbf N=j-i}
(-1)^{|\mathbf a|}
\binom{|\mathbf a|+j+2}{\mathbf a,j+2}\mathbf x^{\mathbf a},
\]

with an empty sum when \(j-i<0\), and set

\[
a_{d,e}=\det(\alpha_{i,j,e})_{
0\leq i\leq e-1,\ d-1\leq j\leq d+e-2}.
\]

These are the definitions in Lewis, Perry and Straub, *An algorithmic
approach to the Polydegree Conjecture for plane polynomial automorphisms*,
Journal of Pure and Applied Algebra 223 (2019), 5346--5359,
<https://doi.org/10.1016/j.jpaa.2019.04.002>.

### Lemma 1.1 (integrality)

Every \(g_{n,e}\) lies in \(\mathbf Z[x_1,\ldots,x_e]\).

### Proof

Let \(I(w)\) be the unique compositional inverse of

\[
H(t)=t+x_1t^2+\cdots+x_et^{e+1}.
\]

The equation

\[
I+x_1I^2+\cdots+x_eI^{e+1}=w
\]

determines each coefficient of \(I\), after its linear coefficient, as an
integer polynomial in earlier coefficients. Hence
\(I\in\mathbf Z[x_1,\ldots,x_e][[w]]\). Lagrange inversion gives

\[
[w^{n+1}]I(w)=\frac1{n+1}[t^n]
(1+x_1t+\cdots+x_et^e)^{-(n+1)}=g_{n,e}.
\]

Thus the apparently rational multinomial formula defines an integer
polynomial. \(\square\)

## 2. Derivative identity

### Proposition 2.1

For \(0\leq i\leq e-1\) and \(j\geq-1\),

\[
\boxed{\alpha_{i,j,e}=-\frac{\partial g_{j+1,e}}{\partial x_{i+1}}.}
\]

### Proof

Only terms of \(g_{j+1,e}\) with exponent
\(b_{i+1}>0\) survive differentiation.  Write
\(\mathbf b=\mathbf a+\mathbf e_{i+1}\).  Then

\[
\mathbf a\cdot\mathbf N=j-i,
\qquad
|\mathbf b|=|\mathbf a|+1.
\]

After multiplying by \(b_{i+1}=a_{i+1}+1\), the coefficient of
\(\mathbf x^{\mathbf a}\) in the derivative is

\[
\begin{aligned}
&\frac{1}{j+2}(-1)^{|\mathbf a|+1}
\frac{(j+1+|\mathbf b|)!}
{b_1!\cdots b_e!(j+1)!}(a_{i+1}+1)\\
&\quad=(-1)^{|\mathbf a|+1}
\frac{(j+2+|\mathbf a|)!}
{a_1!\cdots a_e!(j+2)!},
\end{aligned}
\]

which is the negative of the corresponding coefficient in
\(\alpha_{i,j,e}\).  Summing proves the identity. \(\square\)

## 3. Full determinant identity

Let

\[
D_{d,e}=\left(
\frac{\partial g_{d+r,e}}{\partial x_s}
\right)_{0\leq r\leq e-1,\ 1\leq s\leq e}.
\]

Here and below, \(d\geq2\) and \(e\geq2\).

### Corollary 3.1

\[
\boxed{a_{d,e}=(-1)^e\det D_{d,e}.}
\]

### Proof

Proposition 2.1 says that the matrix defining \(a_{d,e}\) is
\(-D_{d,e}^{\mathsf T}\).  Taking determinants gives the formula. \(\square\)

## 4. Weighted Euler congruence

Each \(g_{n,e}\) is weighted homogeneous of weighted degree \(n\) for
\(\operatorname{wt}(x_s)=s\).  Hence

\[
\sum_{s=1}^{e}s x_s\frac{\partial g_{n,e}}{\partial x_s}=n g_{n,e}.
\]

Define the affine minor

\[
J_{d,e}=\det\left(
\frac{\partial g_{d+r,e}}{\partial x_s}
\right)_{0\leq r\leq e-2,\ 2\leq s\leq e}.
\]

More generally, let \(M_r\) be the determinant of the
\((e-1)\times(e-1)\) submatrix of \(D_{d,e}\) obtained by deleting row
\(r\) and the \(x_1\)-column. Thus \(M_{e-1}=J_{d,e}\).

### Proposition 4.1

In \(\mathbf Z[x_1,\ldots,x_e]\),

\[
\boxed{
x_1a_{d,e}+(d+e-1)g_{d+e-1,e}J_{d,e}
=\sum_{r=0}^{e-2}(-1)^{e+r}(d+r)g_{d+r,e}M_r.}
\]

In particular,

\[
x_1a_{d,e}\equiv
-(d+e-1)g_{d+e-1,e}J_{d,e}
\pmod{(g_{d,e},\ldots,g_{d+e-2,e})}.
\]

### Proof

In \(D_{d,e}\), replace the first column by the weighted column sum

\[
C=\sum_{s=1}^{e}s x_s(D_{d,e})_s.
\]

Multilinearity shows that the new determinant is
\(x_1\det D_{d,e}\), since every term with \(s\geq2\) repeats another
column. The weighted Euler identities make entry \(r\) of \(C\) equal to
\((d+r)g_{d+r,e}\). Expansion down the first column, followed by
\(a_{d,e}=(-1)^e\det D_{d,e}\), gives

\[
x_1a_{d,e}=\sum_{r=0}^{e-1}
(-1)^{e+r}(d+r)g_{d+r,e}M_r.
\]

The \(r=e-1\) term is
\(-(d+e-1)g_{d+e-1,e}J_{d,e}\). Moving it to the left proves the
displayed identity and its congruence. \(\square\)

## 5. Smooth-point reformulation

### Corollary 5.1

Let \(K\) be a field, let \(P\in K^e\) satisfy

\[
g_{d,e}(P)=\cdots=g_{d+e-2,e}(P)=0,
\]

and suppose \(x_1(P)\neq0\) and
\(\operatorname{char}K\nmid d+e-1\).  Then the following are equivalent:

1. \(g_{d+e-1,e}(P)\neq0\) and \(a_{d,e}(P)\neq0\);
2. \(g_{d+e-1,e}(P)\neq0\) and \(J_{d,e}(P)\neq0\);
3. \(P\) lies outside \(V(g_{d+e-1,e})\), and the closed subscheme
   \[
   \operatorname{Spec}K[x_1,\ldots,x_e]/
   (g_{d,e},\ldots,g_{d+e-2,e})
   \]
   is smooth of codimension \(e-1\) at \(P\).

### Proof

Proposition 4.1 makes (1) and (2) equivalent.  On the common zero locus,
the weighted Euler identities express the \(x_1\)-column of the partial
Jacobian as a linear combination of its \(x_2,\ldots,x_e\) columns because
\(x_1(P)\neq0\).  Consequently the partial Jacobian has rank \(e-1\) if
and only if its \((x_2,\ldots,x_e)\)-minor \(J_{d,e}\) is nonzero.
\(\square\)

## 6. Simplified finite-field certificate

### Theorem 6.1

Let \(d\geq2\), \(e\geq2\), and put

\[
F_r(x_2,\ldots,x_e)=g_{d+r,e}(1,x_2,\ldots,x_e).
\]

Suppose a prime \(p\) and \(Q\in\mathbf F_p^{e-1}\) satisfy

\[
F_0(Q)=\cdots=F_{e-2}(Q)=0,
\qquad
F_{e-1}(Q)J_{d,e}(1,Q)\neq0.
\]

Then there is a complex specialization satisfying the hypotheses of
Lewis--Perry--Straub Theorem 4, and therefore

\[
\mathcal G_{(d+e)}\subseteq\overline{\mathcal G_{(d,e+1)}}.
\]

### Proof

The nonzero affine Jacobian determinant makes \(Q\) a simple zero of the
square system \(F_0=\cdots=F_{e-2}=0\). Lemma 1.1 makes these integral
polynomials, so multivariate Hensel lifting gives a
\(\widetilde Q\in\mathbf Z_p^{e-1}\) satisfying the equations exactly and
with \(F_{e-1}(\widetilde Q)J_{d,e}(1,\widetilde Q)\) a unit.

Define

\[
R=\frac{\mathbf Q[x_2,\ldots,x_e,\,
1/(F_{e-1}J_{d,e})]}
{(F_0,\ldots,F_{e-2})},
\]

where \(J_{d,e}\) is evaluated at \(x_1=1\). Evaluation at
\(\widetilde Q\) defines a \(\mathbf Q\)-algebra map \(R\to\mathbf Q_p\),
so \(R\ne0\). Faithful scalar extension gives
\(R\otimes_{\mathbf Q}\mathbf C\ne0\). A maximal ideal and the weak
Nullstellensatz therefore give a complex common zero at which
\(F_{e-1}J_{d,e}\ne0\). Corollary 5.1 makes \(a_{d,e}\ne0\) there, and
Lewis--Perry--Straub Theorem 4 supplies the containment. \(\square\)

### Remark 6.2 (bad-characteristic rescue)

No restriction \(p\nmid d+e-1\) is needed in Theorem 6.1. If
\(p\mid d+e-1\), Proposition 4.1 forces the residue of \(a_{d,e}\) to
vanish at a finite-field common zero, so \(a_{d,e}\) is not a unit at the
lift. It is nevertheless nonzero in \(\mathbf Q_p\):

\[
a_{d,e}(1,\widetilde Q)
=-(d+e-1)F_{e-1}(\widetilde Q)J_{d,e}(1,\widetilde Q),
\]

and all three factors on the right are nonzero in characteristic zero.
The characteristic restriction is needed only if one insists on certifying
\(a_{d,e}\) as a nonzero residue modulo \(p\); it is not needed for the
smooth-point Hensel certificate.

## 7. Prime--gap--Jacobian bridge

### Theorem 7.1

Work over \(\mathbf C\). In
the chart \(x_1=1\), suppose the first \(e-2\) polynomials
\(F_0,\ldots,F_{e-3}\) cut out a smooth complete-intersection curve
\(C\subset\mathbf A^{e-1}\) scheme-theoretically, and that \(C\) is
geometrically integral. Let \(\overline C\) be its smooth projective
completion, and regard the \(F_r\) as rational functions on \(\overline C\).
Assume:

1. \(F_{e-2}|_{\overline C}\) is nonzero, and its zero divisor is nonempty,
   reduced, and supported inside the affine open \(C\);
2. \(F_{e-1}(Q)\ne0\) for every
   \(Q\in\operatorname{Supp}(F_{e-2}|_{\overline C})_0\).

Then every geometric point \(Q\) of that zero divisor satisfies

\[
F_0(Q)=\cdots=F_{e-2}(Q)=0,
\qquad
F_{e-1}(Q)J_{d,e}(1,Q)\neq0.
\]

Consequently it supplies a Lewis--Perry--Straub specialization.

### Proof

The support condition makes \(Q\) an affine point at which all the displayed
polynomials are regular.  At \(Q\), smooth complete-intersection status says that
\(dF_0,\ldots,dF_{e-3}\) are independent and cut the tangent space down to
the one-dimensional space \(T_QC\).  Reducedness of the zero divisor says
that \(F_{e-2}|_C\) has a simple zero, equivalently
\(dF_{e-2}|_{T_QC}\neq0\).  Thus
\(dF_0,\ldots,dF_{e-2}\) are independent, so
\(J_{d,e}(1,Q)\neq0\).
The second hypothesis gives \(F_{e-1}(Q)\neq0\).  Corollary 5.1 finishes
the proof. \(\square\)

### Corollary 7.2 (perfect-ground-field descent)

Let \(k\subset\mathbf C\) be a perfect field of characteristic zero, choose
its algebraic closure \(\overline k\) inside \(\mathbf C\), and suppose the
scheme-theoretic complete intersection \(C\), its smooth projective
completion, and the \(F_r\) are defined over \(k\). Assume the zero divisor
of \(F_{e-2}\) is one closed point with coefficient one, is supported in
the affine open \(C\), and is disjoint from the zero and pole support of
\(F_{e-1}\). Then after base change to \(\overline k\), every geometric
point above that closed point satisfies the hypotheses and conclusion of
Theorem 7.1.

### Proof

Over a perfect field, the residue extension of a closed point is separable.
Coefficient one therefore becomes a disjoint reduced collection of geometric
points after base change. The affine-support and disjointness hypotheses are
preserved by base change, so Theorem 7.1 applies. \(\square\)

This is the form relevant to coefficient-one prime-pushforward certificates
over \(\mathbf Q\). The ground-field statement and the algebraically closed
smooth-point theorem must not be conflated.

## 8. Remaining proof obligations before publication

- Verify whether any equivalent derivative or Jacobian formulation appears
  in the literature, theses, code, or unpublished work of the original
  authors.
- State explicitly how scalar-normalized benchmark polynomials relate to the
  unnormalized \(g_{n,e}\); nonzero rational scalars preserve the characteristic
  zero argument but may not be units after reduction modulo every prime.
- For applications using a selected component rather than the entire partial
  complete intersection, verify smoothness and scheme-theoretic multiplicity
  at the selected zero divisor.
- Keep the characteristic-zero divisor theorem separate from the finite-field
  Hensel theorem.
