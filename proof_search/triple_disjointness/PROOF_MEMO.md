# Triple disjointness for the (e=3) inverse coefficients

**Stage 2 verdict:** open. No characteristic-zero counterexample was found, but
the work below does not prove

\[
(G_d,G_{d+1},G_{d+2})=(1)\quad\text{in }\mathbf Q[X,Y]
\]

for every (d\). It proves an all-(d) differential identity, excludes every
transverse triple zero, proves the entire (Y=0) slice, and reduces the open
case to non-transverse intersections of two consecutive coefficient curves.
Exact Gröbner evidence is kept explicitly finite.

## 1. Set-up

Let (I(w)) be the compositional inverse of

\[
H(t)=t+t^2+Xt^3+Yt^4=tP(t),
\qquad P(t)=1+t+Xt^2+Yt^3.
\]

Then

\[
G_n(X,Y)=[w^{n+1}]I(w)
=\frac1{n+1}[t^n]P(t)^{-(n+1)}.
\]

The direct multinomial construction and the recurrence from
(I+I^2+XI^3+YI^4=w) agree in the supplied replay.

## 2. An all-(d) diagonal raising identity

Define the polynomial vector field

\[
V=(2X-6X^2+4Y)\partial_X+(4Y-9XY)\partial_Y.
\]

### Proposition 2.1

For every (n\ge0),

\[
\boxed{
V(G_n)=(n+2)G_{n+1}-(3nX-4n-2)G_n.}
\]

### Proof

Put

\[
Q_k^{(\lambda)}=[t^k]P(t)^{-\lambda},
\qquad A=(n+1)G_n=Q_n^{(n+1)},
\]

and write (q_k=Q_k^{(n+2)}). Differentiation in the parameters gives

\[
A_X=-(n+1)q_{n-2},\qquad A_Y=-(n+1)q_{n-3}.
\]

Since (P^{-(n+1)}=P\,P^{-(n+2)}),

\[
A=q_n+q_{n-1}+Xq_{n-2}+Yq_{n-3}.
\]

The differential equation

\[
P(P^{-(n+2)})'+(n+2)P'P^{-(n+2)}=0
\]

at degrees (n-1) and (n) gives, after solving for (q_{n-1},q_n),

\[
q_{n-1}=\frac{-nA+2XA_X+3YA_Y}{n+1},
\]

\[
q_n=\frac{(2n+1)A-XA_X-2YA_Y}{n+1},
\]

and

\[
q_{n+1}+2q_n+3Xq_{n-1}+4Yq_{n-2}=0.
\]

Substitution, together with (q_{n+1}=(n+2)G_{n+1}), yields the displayed
identity. \(\square\)

The vector field is the infinitesimal form of recentering (H) at (t=s)
and renormalizing its linear and quadratic coefficients. This interpretation
explains why the same (V) raises every diagonal coefficient.

## 3. Every hypothetical triple zero is non-transverse

Let

\[
f=G_d,\qquad g=G_{d+1},\qquad h=G_{d+2},
\]

and let

\[
J_d=f_Xg_Y-f_Yg_X.
\]

At a common zero of (f,g,h), Proposition 2.1 gives

\[
df(V)=dg(V)=0.
\]

If (J_d\ne0), the covectors (df,dg) are independent, so (V=0). The
stationary locus of (V) consists exactly of

\[
(0,0),\qquad (1/3,0),\qquad (4/9,2/27).
\]

At these points the inverse series are respectively

\[
\frac{\sqrt{1+4w}-1}{2},
\]

\[
(1+3w)^{1/3}-1,
\]

and

\[
\frac32\bigl((1+8w/3)^{1/4}-1\bigr).
\]

Every coefficient (G_n) is nonzero in all three series. Hence:

### Theorem 3.1

For every (d\ge2),

\[
G_d=G_{d+1}=G_{d+2}=0\quad\Longrightarrow\quad J_d=0.
\]

Thus an all-(d) proof of

\[
(G_d,G_{d+1},J_d)=(1)
\]

would prove triple disjointness. This transversality statement is the remaining
structural bottleneck; it is not proved here.

Two exact syzygies make the reduction checkable. Put

\[
A_V=2X-6X^2+4Y,\qquad B_V=4Y-9XY,
\]

and (c_n=3nX-4n-2). Then

\[
B_VJ_d
=(d+3)f_Xh-c_{d+1}f_Xg-(d+2)g_Xg+c_dg_Xf,
\]

\[
-A_VJ_d
=(d+3)f_Yh-c_{d+1}f_Yg-(d+2)g_Yg+c_dg_Yf.
\]

They follow by expanding (f_XV(g)-g_XV(f)) and
(f_YV(g)-g_YV(f)).

## 4. A proved all-(d) slice: (Y=0)

For (X\ne0), put (z=-1/(2\sqrt X)). The Gegenbauer generating function
gives

\[
G_n(X,0)=\frac{X^{n/2}}{n+1}C_n^{n+1}(z).
\]

The zeros of (C_n^{n+1}) are simple and lie in ((-1,1)). Parity pairs the
nonzero zeros (z,-z), so all finite zeros of the polynomial (G_n(X,0))
are simple. If (G_n(X,0)=G_{n+1}(X,0)=0), Proposition 2.1 restricts to

\[
2X(1-3X)\frac{d}{dX}G_n(X,0)=0.
\]

The exceptional values do not vanish: at (X=0) the coefficients are signed
Catalan numbers, and at (X=1/3) they come from
((1+3w)^{1/3}-1). Otherwise the displayed equation contradicts simplicity.
Therefore

\[
\boxed{(G_n(X,0),G_{n+1}(X,0))=(1)\text{ for every }n\ge0.}
\]

In particular, a characteristic-zero triple zero must have (Y\ne0).

## 5. Exact evidence and counterexample search

The following evidence is finite and is not used as an all-(d) proof:

- `structural_receipt.json`: exact Gröbner bases over \(\mathbf Q\) certify
  both \((G_d,G_{d+1},G_{d+2})=(1)\) and
  \((G_d,G_{d+1},J_d)=(1)\) for (2\le d\le15).
- `exploratory_d2_12.json`: an independent exact construction records unit
  triple ideals for (2\le d\le12), together with elimination-resultant gcds.
- `modular_scan_p2_11_d200.json`: exhaustive scans of every
  \((X,Y)\in\mathbf F_p^2\), for (p=2,3,5,7,11) and (2\le d\le200), find
  many triple gaps in every tested characteristic. These are not
  characteristic-zero counterexamples. They show that a valid proof cannot be
  characteristic-free and should expect prime divisors in Bézout denominators.
- `derive_ode.py`: for a generic numerical quartic sample, the first homogeneous
  differential dependence has order four for (I) (order three for (I'));
  after clearing denominators its coefficient recurrence has five terms.
  Algebraicity alone therefore does not propagate three consecutive zeros.

## 6. Final claim boundary

**Proved for all (d):** Proposition 2.1, Theorem 3.1, the two syzygies, and
the (Y=0) slice.

**Finite exact evidence:** unit triple ideals and transverse consecutive-pair
intersections only in the ranges stated above.

**Open:** exclusion of non-transverse common zeros of
(G_d,G_{d+1}) for arbitrary (d), equivalently the remaining route to the
all-(d) triple-disjointness claim. No complex counterexample was found.

## 7. Replay commands

Run from this directory:

```sh
python3 -u verify_structural_reduction.py --identity-max 24 --exact-max 15 --json structural_receipt.json
python3 -O -u verify_structural_reduction.py --identity-max 24 --exact-max 15
python3 -u explore_triples.py --max-d 12 --json exploratory_d2_12.json
python3 -u scan_modular_gaps.py --primes 2 3 5 7 11 --max-d 200 --json modular_scan_p2_11_d200.json
python3 -u derive_ode.py --x 2 --y 3 --max-order 5
```
