# Mathematical and computational assurance audit

**Scope:** immutable v0.2.0 baseline plus the proposed determinant--Jacobian and Euler--Jacobian refactor  
**Audit date:** 9 August 2026  
**Audit boundary:** internal exact replay and adversarial controls; not external reproduction, formal verification, peer review, or a proof of the all-$d$ programme

## Executive conclusion

The v0.2.0 archive is intact and its advertised calculations replay. I found no defect that invalidates the frozen 51 finite-field certificates. The proposed Jacobian refactor is also strongly corroborated: a new standard-library-only verifier, written without importing archive code, checked the derivative identity coefficient by coefficient, checked the determinant and weighted-Euler consequences as exact sparse-polynomial identities in bounded general-$e$ cases, and rederived the Euler--Jacobian relation at all 51 frozen witnesses.

The main assurance defect in v0.2.0 is real but latent: a coefficient-divisibility check in `repro/verify_polydegree_witnesses.py` is implemented only as a Python `assert`. Normal Python rejects an injected non-integral numerator; `python -O` removes the guard and silently floor-divides it. The current unmodified data and code pass in both modes, so this is not evidence of a present false certificate. It is a fail-open mutation/error-detection risk and should be replaced by an explicit exception before the next release.

The refactor also changes the evidence accounting. On a common zero in the chart $x_1=1$,

\[
A_d=-(d+2)G_{d+2}J_d.
\]

Thus $A_d$, $G_{d+2}$, and $J_d$ are separately computed residues, useful for catching implementation errors, but they are not three algebraically independent unit conditions.

**Corrected characteristic conclusion.** The restriction $p\nmid d+2$ is required only for the *legacy mod-$p$ \(A_d\)-unit certificate*. It is unnecessary for the refactored existence theorem. If a finite-field common zero has $G_{d+2}J_d\ne0$, the nonzero Jacobian lifts it to an exact point over $\mathbf Z_p$, where both $G_{d+2}$ and $J_d$ remain units. The exact identity then gives

\[
A_d(\widetilde P)=-(d+2)G_{d+2}(\widetilde P)J_d(\widetilde P)\ne0
\quad\text{in }\mathbf Q_p.
\]

Even when $p\mid d+2$, the integer $d+2$ is nonzero in the field $\mathbf Q_p$; it is merely a nonunit in $\mathbf Z_p$. Therefore the required localization still maps to $\mathbf Q_p$, and faithful base change supplies the complex specialization. All 51 frozen witnesses happen to satisfy the stronger legacy mod-$p$ unit condition, but the new theorem should not impose it.

## Reproduction results

| Gate | Normal Python | `python -O` | Interpretation |
|---|---:|---:|---|
| Internal manifest | 23/23 files match | not mode-dependent | Frozen payload integrity passes |
| Structural verifier | 31/31 PASS | 31/31 PASS | Existing exact SymPy checks replay |
| Archive witness verifier | 51/51 PASS | 51/51 PASS | Existing dual-path witness checks replay |
| Discovery replay | 51/51, exact frozen match | not rerun under `-O` | Search regenerates the JSON table; this is same-family replay |
| New independent-code verifier | 10/10 symbolic gates; 51/51 witnesses | identical result | No proof-critical `assert`; normal and optimized reports are byte-identical |
| New mutation controls | 17/17 PASS | 17/17 PASS | Same detection outcomes in both modes |
| Archive assert probe | injected error rejected | injected error silently accepted | Confirms latent optimized-mode fail-open guard |

The archive ZIP SHA-256 is:

```text
d05151716e7cc5e22074ee9acd5683b15e008b366fa450d60c9157d452eda52e
```

It matches the supplied sidecar. The frozen JSON and CSV contain the same 51 rows, and the live deterministic search regenerated the JSON witness list exactly.

## Independent verifier design and results

`verify_jacobian_refactor.py` uses only the Python standard library. It does not import the archive verifiers. Its implementation choices deliberately differ from the archive:

- largest-weight-first recursive enumeration of weighted compositions;
- factorial-ratio reconstruction of integer coefficients;
- sparse integer dictionaries for polynomials;
- dictionary differentiation and weighted-variable multiplication;
- a generic Leibniz permutation determinant instead of the archive's hard-coded $3\times3$ determinant;
- exact modular evaluation of the supplied points.

It checked:

1. **Derivative identity:** 238 exact coefficient comparisons for $2\le e\le5$, $0\le j\le16$, and every valid row $i$:

   \[
   \alpha_{i,j,e}=-\partial_{x_{i+1}}g_{j+1,e}.
   \]

2. **Weighted Euler identity:** 64 exact coefficient comparisons for $2\le e\le5$ and $1\le n\le16$:

   \[
   \sum_{s=1}^e s x_s\partial_{x_s}g_{n,e}=n g_{n,e}.
   \]

3. **Exact sparse determinant identities:** seven full polynomial cases, including $e=4$, with zero residual. Writing $M_r$ for the minor obtained from the full derivative matrix by deleting row $r$ and the $x_1$-column, the verifier checked the stronger ideal-membership certificate

   \[
   x_1a_{d,e}+(d+e-1)g_{d+e-1,e}J_{d,e}
   =\sum_{r=0}^{e-2}(-1)^{e+r}(d+r)g_{d+r,e}M_r.
   \]

4. **General-$e$ numerical sweep:** 72 exact-integer determinant and Euler--Jacobian comparisons for $2\le e\le5$, $2\le d\le10$, at two deterministic integer points.

5. **Full witness relation:** all 51 rows for $50\le d\le100$ were rebuilt from the multinomial definitions. Every vanishing, recorded residue, primality condition, chart condition, refactored $G_{d+2}J_d$ unit condition, stronger legacy mod-$p$ \(A_d\)-unit condition, and equality

   \[
   a_{d,3}\equiv-(d+2)g_{d+2,3}J_d\pmod p
   \]

   passed.

These calculations support the signs and indices in the proposed theorem note. They remain bounded regression tests; the paper must still contain the general coefficient reindexing and determinant/Euler proof.

## Mutation, negative, and positive-regression controls

`test_mutations.py` detected all 17 controls under both normal and optimized Python: 16 mutation/negative controls and one positive theorem-regression fixture.

- changed recorded $a$, $J$, and $g_{d+2}$ residues;
- changed affine point, composite modulus, $x_1=0$, missing row, and Boolean masquerading as an integer;
- wrong derivative sign and one-column index shift;
- wrong determinant sign;
- ordinary rather than weighted Euler coefficients;
- $d+1$ rather than $d+2$, and the wrong congruence sign;
- a positive bad-characteristic rescue fixture;
- a singular common-zero point;
- an injected non-integral coefficient in the replacement verifier.

Two especially informative frozen controls are:

- **Bad-characteristic rescue:** $d=8,p=5,(x_1,x_2,x_3)=(1,3,0)$ has $g_d=g_{d+1}=0$, $g_{d+2}=2$, and $J=3$, while $a=0$ modulo $5$ because $p\mid d+2$. The legacy mod-$p$ \(A_d\)-unit test rejects it, but the refactored $J$-based Hensel criterion accepts it. At the exact lift, \(A_d=-10G_{10}J_8\) is nonzero in $\mathbf Q_5$ with positive valuation.
- $d=3,p=7,(1,2,5)$: $g_d=g_{d+1}=0$ and $J=a=0$, providing a singular-point rejection case.

## Findings and severity

### A1. Proof-critical `assert` disappears under optimization — medium

Archive line `repro/verify_polydegree_witnesses.py:64` checks divisibility of evaluated numerator sums and their derivatives only with:

```python
assert val % q == 0 and du % q == 0 and dv % q == 0
```

The subsequent floor divisions execute even when the guard is removed. `probe_archive_assert.py` replaced the cached term builder with a deliberately invalid constant numerator. Normal Python raised `AssertionError`; optimized Python returned `(0,0,0)`. Replace the `assert` with an explicit `if ...: raise ArithmeticError(...)`, preferably checking coefficient-level integrality when terms are constructed.

### A2. Three unit residues are algebraically coupled — medium for assurance wording, no validity loss

`POLYDEGREE_HENSEL_EXTENSION.md:286` calls $G_{d+2},A_d,J_d$ “three independently checked non-zero residues.” They are independently *evaluated*, but the new identity makes them algebraically dependent on the common-zero locus. The wording should say that the redundant calculations are implementation cross-checks. The simplified theorem hypotheses should use only $G_{d+2}J_d\ne0$ at a finite-field common zero. No restriction $p\nmid d+2$ is needed for existence over $\mathbf Q_p$ and hence over $\mathbf C$. Direct mod-$p$ \(A_d\) evaluation can remain a verification path for the stronger legacy unit certificate.

### A3. The two archive paths are implementation-diverse, not externally independent — assurance boundary

The archive already says this accurately in `ASSURANCE.md:49`. More specifically:

- discovery and the direct verifier both implement the same multinomial definitions and a $3\times3$ determinant;
- the frozen expected residues were generated by that discovery family;
- the formal-series path is algebraically distinct for $g$ and derivatives, but shares the same input JSON, determinant function, runner, and authoring environment;
- Wolfram covers only $d=50$ and $d=100$.

This is strong producer-side triangulation. It is not reproduction by an unaffiliated group, nor an independent mathematical derivation of the Hensel or Lewis--Perry--Straub implications. The new verifier improves code-path diversity but remains an internal verifier of the same definitions and the same frozen data.

### A4. No frozen negative controls in v0.2.0 — medium for future assurance

The archive contains positive replays but no mutation/negative-control suite for sign, index, singularity, or malformed-certificate failures, and no positive regression for the newly enlarged characteristic scope. The 16 failure controls and the bad-characteristic rescue fixture added here should be retained in the next candidate.

### A5. Row counters can be misleading on a global range failure — low

At `repro/verify_polydegree_witnesses.py:167-188`, a missing or duplicated $d$ adds a global failure, but each remaining row's status considers only failures prefixed by that row's $d$. The overall process correctly fails, yet `witnesses_passed` may still report every remaining row as passing. Separate `rows_valid` from `coverage_valid`, or propagate global failures into the summary status.

### A6. Input validation is permissive — low

The archive verifier does not require the advertised schema/range metadata, canonical residue coordinates, or strict JSON integer types. These omissions do not affect the frozen table, but stronger validation makes mutation behaviour clearer. The new verifier checks all of them and rejects Python/JSON booleans as integers.

## Independence and claim boundary

The new verifier is “independent” only in the code-path sense: it shares no archive functions and uses a separate polynomial representation and determinant algorithm. It necessarily shares the published definitions of $g$ and $\alpha$, and it consumes the same frozen witness JSON. A common misunderstanding of those definitions could therefore survive both packages. Its factorial helper is also shared internally by its $g$ and $\alpha$ constructors.

The audit does **not** establish:

- the general identities without the accompanying written proof;
- the Hensel-specialization theorem or faithful-base-change passage independently;
- the Lewis--Perry--Straub theorem;
- novelty, priority, peer-review status, or a uniform all-$d$ theorem;
- full external CAS reproduction of all 51 rows.

## Commands

Run from the workspace root:

```bash
python3 work/irreducible-norms-ref-upgrade/analysis/assurance_agent/verify_jacobian_refactor.py \
  --witness-data work/irreducible-norms-ref-upgrade/baseline/irreducible-norms-gap-separation-v0.2.0/data/polydegree_e3_witnesses_50_100.json \
  --report work/irreducible-norms-ref-upgrade/analysis/assurance_agent/independent_verification_report.json

python3 -O work/irreducible-norms-ref-upgrade/analysis/assurance_agent/verify_jacobian_refactor.py \
  --witness-data work/irreducible-norms-ref-upgrade/baseline/irreducible-norms-gap-separation-v0.2.0/data/polydegree_e3_witnesses_50_100.json \
  --report work/irreducible-norms-ref-upgrade/analysis/assurance_agent/independent_verification_report_optimized.json

python3 work/irreducible-norms-ref-upgrade/analysis/assurance_agent/test_mutations.py \
  --witness-data work/irreducible-norms-ref-upgrade/baseline/irreducible-norms-gap-separation-v0.2.0/data/polydegree_e3_witnesses_50_100.json \
  --report work/irreducible-norms-ref-upgrade/analysis/assurance_agent/mutation_report.json

python3 -O work/irreducible-norms-ref-upgrade/analysis/assurance_agent/test_mutations.py \
  --witness-data work/irreducible-norms-ref-upgrade/baseline/irreducible-norms-gap-separation-v0.2.0/data/polydegree_e3_witnesses_50_100.json \
  --report work/irreducible-norms-ref-upgrade/analysis/assurance_agent/mutation_report_optimized.json

python3 work/irreducible-norms-ref-upgrade/analysis/assurance_agent/probe_archive_assert.py \
  --archive-verifier work/irreducible-norms-ref-upgrade/baseline/irreducible-norms-gap-separation-v0.2.0/repro/verify_polydegree_witnesses.py \
  --report work/irreducible-norms-ref-upgrade/analysis/assurance_agent/archive_assert_probe_normal.json

python3 -O work/irreducible-norms-ref-upgrade/analysis/assurance_agent/probe_archive_assert.py \
  --archive-verifier work/irreducible-norms-ref-upgrade/baseline/irreducible-norms-gap-separation-v0.2.0/repro/verify_polydegree_witnesses.py \
  --report work/irreducible-norms-ref-upgrade/analysis/assurance_agent/archive_assert_probe_optimized.json
```

The archive assert probe takes the baseline verifier path explicitly and must be run in both modes; its optimized success means the probe observed the latent failure, not that the archive guard is safe.

## Artifact hashes

```text
0bfb6d767148ffb6bffffbb7112d4050ede84c0e11a1167b908b04e5fc0265d5  verify_jacobian_refactor.py
f303ea3bb70f8f1c1313af79194b68686ee56ed2d14e22ae619336d910959359  test_mutations.py
14e0daf6e3f9dc0d6546b9a360da9a32b3214da0f6f20f22d5b29ab6c249fd77  probe_archive_assert.py
a6ace1972c6457be476ae808d7103d1fce40140617f9462de84ada80c7f03529  independent_verification_report.json
a6ace1972c6457be476ae808d7103d1fce40140617f9462de84ada80c7f03529  independent_verification_report_optimized.json
ba81de85bd824a93449bfae89f0da9e9121b3c08a14a32dd7a325e4d570179a5  mutation_report.json
fcd887897e79c779481543a836eb3fafdcb69d0d1a6cccc22e579b58933b46ce  mutation_report_optimized.json
d0f6bc487155836efd930c78de9772e063ebd3f94ed7f5ef294acc8a1b18d6cc  archive_assert_probe_normal.json
cfac0278b4eb71997e22cbce668442ae97d9c256241d9c3c57b5ca71ef7f7b07  archive_assert_probe_optimized.json
```

The two independent-verifier reports are byte-identical across normal and optimized Python. The mutation reports differ only because each records the interpreter optimization level in the explicit-guard control; all 17 outcomes agree.

## Recommended next-release changes

1. Replace the archive `assert` with an explicit fail-closed integrality check and retain a normal/optimized mutation that proves it fires.
2. Add the general derivative, determinant, Euler, and ideal-membership proofs to the theorem note; use the new verifier only as supporting evidence.
3. Recast mod-$p$ \(A_d\) as a redundant verification value for the legacy unit subcase. State explicitly that $p\mid d+2$ makes it zero modulo $p$ but does not make its exact value zero at the $\mathbf Q_p$ lift.
4. Freeze the 16 mutation/negative controls, the positive bad-characteristic rescue fixture, and their machine-readable expected outcomes.
5. Keep code-path diversity, internal replay, external reproduction, formalisation, specialist review, and novelty as separate status fields.
