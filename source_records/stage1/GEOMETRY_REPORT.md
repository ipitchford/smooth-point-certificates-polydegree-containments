# Exact audit of the all-\(d\), \(e=3\) geometric gateway

## Scope and status

This is an independent, exact characteristic-zero investigation of

\[
Z_d=V(g_{d,3},g_{d+1,3})\subset \mathbf P(1,2,3).
\]

It does **not** prove the uniform all-\(d\) theorem. It proves the complete
affine statement for every \(2\le d\le20\), gives an exact boundary sweep for
\(2\le d\le200\), and isolates three precise uniform statements that remain to
be proved.

All computations use exact arithmetic over \(\mathbf Q\). The main sweep was
run with Python 3.14.6, SymPy 1.14.0 and Singular 4.4.1. Normal and `python -O`
runs produced byte-identical JSON receipts.

## 1. Exact construction of \(G_n\)

For \(a+2b+3c=n\), Lagrange inversion gives

\[
g_{n,3}(x_1,x_2,x_3)
=\frac1{n+1}\sum
(-1)^{a+b+c}
\frac{(n+a+b+c)!}{n!a!b!c!}
x_1^a x_2^b x_3^c.
\]

In the chart \(x_1=1\), put

\[
G_n(X,Y)=g_{n,3}(1,X,Y).
\]

If \(I(w)\in w\mathbf Z[X,Y][[w]]\) is determined by

\[
I+I^2+XI^3+YI^4=w,
\]

then

\[
G_n(X,Y)=[w^{n+1}]I(w).
\]

The main script constructs every coefficient twice: directly from the
multinomial formula and independently from the recurrence obtained by taking
coefficients in the inverse equation. A disagreement is a fail-closed error.
This also supplies a direct integrality check without division modulo a prime.

## 2. Exact affine result for \(2\le d\le20\)

Let

\[
I_d=(G_d,G_{d+1})\subset\mathbf Q[X,Y],\qquad
J_d=\det\frac{\partial(G_d,G_{d+1})}{\partial(X,Y)}.
\]

For every \(2\le d\le20\), exact Gröbner-basis computation proves:

1. \(g_{d,3}\) and \(g_{d+1,3}\) have homogeneous gcd \(1\). Hence the
   weighted-projective intersection is proper.
2. \(I_d\) is zero-dimensional and

   \[
   \dim_{\mathbf Q}\mathbf Q[X,Y]/I_d
   =\left\lfloor\frac{d(d+1)}6\right\rfloor.
   \]

3. \(I_d+(J_d)=(1)\).
4. \(I_d+(G_{d+2})=(1)\).

The quotient lengths for \(d=2,\ldots,20\) are

\[
1,2,3,5,7,9,12,15,18,22,26,30,35,40,45,51,57,63,70.
\]

These are exactly \(\lfloor d(d+1)/6\rfloor\).

### Scheme-theoretic interpretation

Singular returns vector-space dimension zero for the last two quotient ideals.
That means each is the unit ideal, not merely that a numerical root search found
nothing.

Because \(I_d\) is a height-two complete intersection in the smooth surface
\(\mathbf A^2\), \(I_d+(J_d)=(1)\) says that every geometric point has full
Jacobian rank. Every zero-dimensional local ring is therefore regular, hence a
field. Thus the **entire affine scheme is reduced** (indeed finite etale over
\(\mathbf Q\)).

Likewise, \(I_d+(G_{d+2})=(1)\) proves that the entire affine scheme is
scheme-theoretically disjoint from \(V(G_{d+2})\). Consequently every one of
its \(\lfloor d(d+1)/6\rfloor\) geometric points is a smooth point avoiding
\(G_{d+2}=0\).

This is stronger than proving existence of one good point, but only in the
verified finite range.

## 3. Why the length formula is natural

The Newton polygon of \(G_n\) is

\[
\Delta_n=\operatorname{conv}\{(b,c)\in\mathbf Z_{\ge0}^2:2b+3c\le n\}.
\]

An elementary calculation of the vertices in the six residue classes modulo
\(6\) gives

\[
\operatorname{MV}(\Delta_d,\Delta_{d+1})
=\left\lfloor\frac{d(d+1)}6\right\rfloor.
\]

The script calculates this mixed volume directly from the exact supports and
checks the formula for every \(2\le d\le20\). The observed quotient length
therefore attains the BKK count. A promising uniform route is to prove that the
specific coefficient pair \((G_d,G_{d+1})\), not merely a generic pair with
these supports, is torically nondegenerate.

There is also a weighted-projective explanation. On the stack
\(\mathcal P(1,2,3)\), proper intersections have total intersection number

\[
\frac{d(d+1)}{1\cdot2\cdot3}=\frac{d(d+1)}6.
\]

The fractional part when \(d\equiv1\pmod3\) is accounted for by the order-three
stack point at the boundary, as described next.

## 4. Exact boundary analysis

Write

\[
B_n(X,Y)=g_{n,3}(0,X,Y).
\]

Let \(\epsilon=n\bmod2\), \(A=(n-3\epsilon)/2\), and
\(z=Y^2/X^3\). On the boundary torus \(XY\ne0\),

\[
B_n=X^A Y^\epsilon P_n(z),
\]

where

\[
P_n(z)=\frac1{n+1}
\sum_{k=0}^{\lfloor A/3\rfloor}
(-1)^{A+\epsilon-k}
\frac{(n+A+\epsilon-k)!}
{n!(A-3k)!(\epsilon+2k)!}\,z^k.
\]

The adjacent coefficient ratio is

\[
\frac{[z^{k+1}]P_n}{[z^k]P_n}
=-
\frac{(A-3k)(A-3k-1)(A-3k-2)}
{(n+A+\epsilon-k)(\epsilon+2k+1)(\epsilon+2k+2)}.
\]

This terminating hypergeometric form is a possible route to a uniform
interlacing/coprimality proof.

### Coordinate factors: uniform elementary result

The minimum exponent of \(X\) in \(B_n\) is the unique
\(r\in\{0,1,2\}\) satisfying \(2r\equiv n\pmod3\). The minimum exponent of
\(Y\) is \(n\bmod2\). Therefore the common **monomial** factor of
\(B_d,B_{d+1}\) is

\[
X\quad\text{if }d\equiv1\pmod3,
\qquad 1\quad\text{otherwise}.
\]

No power \(X^2\) can divide both, and no \(Y\) can divide both. This part is a
uniform proof. Ruling out an additional torus factor is separate.

### Exact finite result

For every \(2\le d\le200\), exact univariate arithmetic proves

\[
\gcd(P_d,P_{d+1})=1.
\]

It also proves that every \(P_n\) for \(2\le n\le201\) is squarefree. Hence,
through this range, the full boundary gcd is exactly \(X\) when
\(d\equiv1\pmod3\), and \(1\) otherwise. This is strong evidence, not a proof
for all \(d\).

### Stack versus coarse multiplicity

For \(d=3k+1\), the boundary support is the coarse point

\[
P_3=[0:0:1].
\]

On its uniformising \(\mathbf A^2\)-cover, with coordinates
\((u,v)=(x_1,x_2)\) and \(x_3=1\), the lowest terms are a non-zero multiple of
\(u\) in \(g_{d,3}\) and a non-zero multiple of \(v\) in \(g_{d+1,3}\).
Thus the intersection is transverse on the cover and contributes
\(1/3\) to the **stack** intersection number because the stabiliser is
\(\mu_3\).

Consequently, provided there is no additional boundary-torus intersection,

\[
\operatorname{length}(Z_d\cap\{x_1\ne0\})
=\frac{d(d+1)}6-
\begin{cases}
1/3,&d\equiv1\pmod3,\\
0,&d\not\equiv1\pmod3,
\end{cases}
=\left\lfloor\frac{d(d+1)}6\right\rfloor.
\]

The \(1/3\) is not an ordinary coarse-scheme length. The coarse support is one
point; rational multiplicity arises from stack/intersection theory at the
quotient singularity. This distinction must be kept explicit.

## 5. Uniform conjecture suggested by the data

The exact data support the following substantially stronger conjecture.

> For every \(d\ge2\), the ideal \((G_d,G_{d+1})\) is radical of length
> \(\lfloor d(d+1)/6\rfloor\), and both \(J_d\) and \(G_{d+2}\) are units in
> its coordinate algebra.

Together with the Euler-Jacobian identity in characteristic zero, this would
give the desired smooth point avoiding \(g_{d+2,3}=0\) for every \(d\), in
fact showing that every affine point is good.

What has been proved here is only:

- the displayed algebraic conjecture for \(2\le d\le20\);
- boundary torus coprimality and squarefreeness for \(2\le d\le200\);
- the coordinate-factor classification for every \(d\).

The highest-value next proofs are:

1. prove \(\gcd(P_d,P_{d+1})=1\) uniformly, perhaps via the displayed
   hypergeometric recurrence and interlacing;
2. prove properness or toric nondegeneracy of \((G_d,G_{d+1})\) uniformly;
3. prove the discriminant/Jacobian resultant never vanishes;
4. prove \(G_{d+2}\) is a unit modulo \((G_d,G_{d+1})\), equivalently that the
   triple resultant has no characteristic-zero zero.

## 6. Counterexample boundary

A counterexample to the smooth-point target at one \(d\) would mean that the
affine common-zero scheme is empty, or that every affine common zero is
singular or lies on \(G_{d+2}=0\). It would disprove this specific smooth-affine
specialization route at that \(d\).

It would **not** be a counterexample to the Polydegree Conjecture. The
Lewis-Perry-Straub specialization condition is sufficient, not known to be
necessary; another degeneration or argument could still establish the desired
Polydegree containment. Likewise, failure of properness alone would only break
the proposed intersection-length proof—a common curve could still contain good
smooth points.

## 7. Reproduction

Main affine/projective sweep:

```sh
python3 explore_geometry.py --d-min 2 --d-max 20 --json results_2_20.json
python3 -O explore_geometry.py --d-min 2 --d-max 20 --json results_2_20_optimized.json
cmp results_2_20.json results_2_20_optimized.json
```

Boundary sweep:

```sh
python3 boundary_sweep.py --d-min 2 --d-max 200 --json boundary_results_2_200.json
python3 -O boundary_sweep.py --d-min 2 --d-max 200 --json boundary_results_2_200_optimized.json
cmp boundary_results_2_200.json boundary_results_2_200_optimized.json
```

Receipt SHA-256 values:

- `results_2_20.json`: `f000424d80988ceeed66b3f33ce0ae5f58bbbba2d031508420b66a9a8065edee`
- `boundary_results_2_200.json`: `f9d8cc61ccd81105a5af41aea3631831dcf1f68f31029c625c84d3267f8cf2d4`
