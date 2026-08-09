# Stage 2.5 fail-closed assurance audit

**Candidate:** `outputs/smooth-point-certificates-polydegree-stage2-2026-08-09`  
**Candidate version:** `0.4.0-candidate`  
**Audit date:** 9 August 2026  
**Scope:** mathematical/evidence claims, numerical and range claims, citation uses, replay and integrity receipts, metadata, declarations, and all seven AI Research Failure Modes  
**Policy:** gray zone = FAIL; replay is not independent reproduction  
**Output mutation policy:** the candidate directory was read-only; all fresh reports were written under `/tmp/polydegree-stage25.DYOljv`

## Verdict

**FAIL — block publication/finalisation at Stage 2.5 pending revision and re-audit.**

The mathematical and computational core survived this audit. I audited all
16 claim-ledger entries (100%), traced the written theorem chain, checked the
load-bearing external sources, and replayed all principal finite evidence from
a fresh temporary copy under both ordinary Python and `python -O`. I found no
counterexample to the stated identities, the Jacobian/Hensel theorem, the
bounded affine or boundary results, or the uniform boundary-squarefreeness
proof.

The blocking result instead comes from integrity and machine-semantics defects:

1. the Funding, Competing interests, and CRediT declarations have no supplied
   signed author attestation or externally checkable source;
2. `EVIDENCE_PRESS_META_TEMPLATE.json` says `aiGenerated:false` while also
   saying language-model tools assisted drafting, without a schema definition
   that makes the intended distinction auditable;
3. the metadata one-line description says “the uniform e=3 theorem remains
   open”, although a uniform e=3 *boundary* theorem is proved; only the uniform
   e=3 *affine* theorem remains open;
4. ledger entries `N1` and `X1` use affirmative claim text paired with
   non-affirmative statuses, creating a polarity trap for downstream readers;
5. the asserted byte identity with the earlier v0.2.0 witness corpus is
   supported by a retained Stage 1 report, but the v0.2.0 bytes are not in the
   frozen Stage 2 package, so this audit could not independently redo that
   comparison.

Under the supplied gray-zone rule, each unresolved item fails closed even
though none presently falsifies the mathematics.

## Audit coverage

- Core ledger: **16/16 claims audited (100%)**.
- Canonicalised additional material claims: package inventory and hashes;
  replay counts and ranges; PDF/page/abstract/citation counts; publication
  state; independence boundary; v0.2/v0.3 reconciliation; declarations; and
  Evidence Press provenance/summary semantics.
- Citations: **9/9 bibliographic identities and uses checked** against primary
  or authoritative records; two load-bearing finite-free-convolution PDFs were
  also inspected from the frozen source records.
- Interpreter modes: all principal deterministic checks rerun with `python3
  -B` and `python3 -B -O`.
- Negative controls: **17/17** passed in both modes: 16 mutation/negative
  controls plus one positive bad-characteristic rescue regression.
- Candidate files modified: **none**.

## Claim-ledger audit

The labels below use the claim-verification protocol. “VERIFIED” means the
claim matches the cited proof/receipt within the stated boundary; it does not
mean formal verification or unaffiliated peer review.

| ID | Verdict | Independent audit evidence and boundary |
|---|---|---|
| `T1` | VERIFIED | Lemma 2.1 gives the integral recurrence and formal-inverse coefficient interpretation. Exact sparse-polynomial construction also passed the replacement verifier. |
| `T2` | VERIFIED | Proposition 3.1 follows by coefficient reindexing; the no-import verifier checked the derivative identity coefficient-by-coefficient. |
| `T3` | VERIFIED | Corollary 3.2 correctly obtains the sign `(-1)^e` because the alpha matrix is the negative transpose of the derivative matrix. Exact determinant gates passed. |
| `T4` | VERIFIED | Proposition 4.1's weighted-Euler column replacement and determinant sign were checked algebraically and computationally; wrong-weight and wrong-sign controls were detected. |
| `T5` | VERIFIED | Corollary 4.2 states the necessary `x_1 != 0` and residue-characteristic restriction for equivalence with the mod-p determinant-unit certificate. |
| `T6` | VERIFIED | Theorem 5.1 uses a simple finite-field point to Hensel-lift, localises at the nonzero next coefficient and Jacobian, then uses faithful base change and weak Nullstellensatz. The exact identity over characteristic zero makes the legacy determinant nonzero even if `p` divides `d+e-1`; only its mod-p unit test then fails. The `d=8,p=5` positive regression passed. |
| `T7` | VERIFIED | The scheme-theoretic smooth-curve argument correctly turns a reduced nonempty affine zero divisor avoiding the next coefficient into a point where the differentials are independent. |
| `T8` | VERIFIED | Over a perfect field, the coefficient-one closed point has separable residue field; after base change it is a reduced geometric collection. The stated support hypotheses are retained. |
| `T9` | VERIFIED, EXTERNALLY DEPENDENT | The terminating hypergeometric factorisation, sign-preservation step, reflection, and logarithmic-mesh simplicity argument match the frozen primary PDFs. Exact identity/squarefree replay passed through `n=301`, adjacent gcd through `d=300`, and Sturm interlacing through `d=120`. This is a written proof with inherited theorems, not a proof-assistant check. |
| `C1` | VERIFIED, BOUNDED | All 51 rows for `50 <= d <= 100` passed both the legacy archive verifier and the separate standard-library verifier in ordinary and optimized modes. |
| `C2` | VERIFIED, BOUNDED | Fresh exact replay reproduced `d=2..20`: the quotient length is `floor(d(d+1)/6)`, while adjoining `J_d` or `G_(d+2)` gives the unit ideal. Zero-dimensional smoothness implies reducedness. |
| `C3` | VERIFIED, BOUNDED | Fresh exact replay reproduced adjacent boundary gcd degree zero for `d=2..200`. The supplementary hypergeometric verifier reaches `d=300`, but the manuscript deliberately claims only `d<=200`. |
| `I1` | VERIFIED, EXTERNALLY INHERITED | The LPS source extract and live arXiv record agree on the specialisation implication; the frozen transcription records Theorem 4's precise zero/nonzero hypotheses and containment conclusion. |
| `O1` | VERIFIED AS OPEN/NOT CLAIMED | The manuscript consistently labels the all-`d` affine radicality/Jacobian-unit/next-coefficient-unit statement as Conjecture 7.4. Finite evidence is not promoted to a theorem. |
| `N1` | MINOR_DISTORTION / GRAY-ZONE FAIL | The affirmative text “is new to the literature” is stronger than status `priority_provisional`, whose definition says only a bounded collision search was completed. Prose elsewhere is appropriately cautious. Machine text should be rewritten as a bounded-search finding. |
| `X1` | MINOR_DISTORTION / GRAY-ZONE FAIL | The affirmative text says the work “has been independently reproduced...” while status `not_assessed` means no positive assurance claim. Supporting prose correctly denies these assurances, but the machine claim's polarity is unsafe. |

### Ledger totals

- VERIFIED or correctly open/status-bounded: **14**
- MINOR_DISTORTION / ambiguous machine polarity: **2**
- MAJOR_DISTORTION: **0**
- UNVERIFIABLE among the 16 core ledger entries: **0**

The ledger does not pass the user's stricter gray-zone rule until `N1` and
`X1` are rewritten.

## Written-proof review

### Determinant–Jacobian–Euler chain

The derivative identity, transpose/sign convention, and weighted Euler
syzygy are mutually consistent. On the common-zero locus, the specialization
identity has the form

\[
A=-(d+e-1)G_{d+e-1}J.
\]

For `e=3` this is `A_d=-(d+2)G_(d+2)J_d`. The manuscript correctly
distinguishes two consequences:

- a `J`-based simple finite-field point with nonzero next coefficient lifts
  and yields a nonzero characteristic-zero determinant even when the prime
  divides the scalar; and
- a direct *mod-p* `A`-unit certificate still needs that scalar to be a unit.

Thus `d=8,p=5` is correctly a positive bad-characteristic rescue regression,
not a rejected witness or a reason to impose `p` not dividing `d+2` in the
new theorem.

### Hensel and complex-specialisation bridge

The proof does not claim an embedding of `Q_p` into `C`. It instead obtains a
nonzero finite-type localisation over `Q`, preserves nonzeroness after the
faithfully flat extension `Q -> C`, and applies weak Nullstellensatz. That is
the correct algebraic route.

### Boundary theorem

The previously invalid shortcut from strict interlacing was not retained.
The repaired proof uses:

- hypergeometric parameter concatenation and half-line sign preservation from
  arXiv:2404.11479v2;
- reflection and positive-root logarithmic-mesh preservation from
  arXiv:2309.10970v3; and
- the Jacobi representation and simple-zero facts from NIST DLMF.

Inspection of the frozen PDFs confirmed the cited propositions and their sign
and positivity hypotheses. No mismatch was found. The finite replay supports
the transformations but is not itself the all-`n` proof.

## Fresh replay from a temporary extraction

The audit copy was `/tmp/polydegree-stage25.DYOljv/candidate`. Runtime:

- Python 3.14.6
- SymPy 1.14.0
- Singular 4.4.1
- pandoc 3.9

Representative commands, all run from the temporary candidate root:

```sh
python3 -B scripts/verify_manifest.py --root "$PWD"
python3 -B -O scripts/verify_manifest.py --root "$PWD"

python3 -B scripts/validate_candidate.py --root "$PWD" \
  --report /tmp/polydegree-stage25.DYOljv/validation_replay_normal.json
python3 -B -O scripts/validate_candidate.py --root "$PWD" \
  --report /tmp/polydegree-stage25.DYOljv/validation_replay_optimized.json

python3 -B scripts/verify_jacobian_refactor.py \
  --witness-data evidence/upstream/polydegree_e3_witnesses_50_100.json \
  --report /tmp/polydegree-stage25.DYOljv/independent_normal.json
python3 -B -O scripts/verify_jacobian_refactor.py \
  --witness-data evidence/upstream/polydegree_e3_witnesses_50_100.json \
  --report /tmp/polydegree-stage25.DYOljv/independent_optimized.json

python3 -B scripts/test_mutations.py \
  --witness-data evidence/upstream/polydegree_e3_witnesses_50_100.json \
  --report /tmp/polydegree-stage25.DYOljv/mutations_normal.json
python3 -B -O scripts/test_mutations.py \
  --witness-data evidence/upstream/polydegree_e3_witnesses_50_100.json \
  --report /tmp/polydegree-stage25.DYOljv/mutations_optimized.json

python3 -B scripts/probe_archive_assert.py \
  --archive-verifier /tmp/polydegree-stage25.DYOljv/upstream/polydegree-hensel-certificates-e3-v0.3.0/repro/verify_polydegree_witnesses.py \
  --report /tmp/polydegree-stage25.DYOljv/assert_probe_normal.json
python3 -B -O scripts/probe_archive_assert.py \
  --archive-verifier /tmp/polydegree-stage25.DYOljv/upstream/polydegree-hensel-certificates-e3-v0.3.0/repro/verify_polydegree_witnesses.py \
  --report /tmp/polydegree-stage25.DYOljv/assert_probe_optimized.json

python3 -B scripts/explore_geometry.py --d-min 2 --d-max 20 \
  --json /tmp/polydegree-stage25.DYOljv/geometry_normal.json
python3 -B -O scripts/explore_geometry.py --d-min 2 --d-max 20 \
  --json /tmp/polydegree-stage25.DYOljv/geometry_optimized.json

python3 -B scripts/boundary_sweep.py --d-min 2 --d-max 200 \
  --json /tmp/polydegree-stage25.DYOljv/boundary_normal.json
python3 -B -O scripts/boundary_sweep.py --d-min 2 --d-max 200 \
  --json /tmp/polydegree-stage25.DYOljv/boundary_optimized.json

python3 -B scripts/verify_boundary_hypergeom.py \
  --d-max 300 --factor-max 300 --interlace-max 120 \
  --json /tmp/polydegree-stage25.DYOljv/hypergeom_normal.json
python3 -B -O scripts/verify_boundary_hypergeom.py \
  --d-max 300 --factor-max 300 --interlace-max 120 \
  --json /tmp/polydegree-stage25.DYOljv/hypergeom_optimized.json
```

Supplementary exact recorded-boundary replays also passed:

```sh
python3 -B proof_search/affine_nondegeneracy/face_system_audit.py \
  --max-d 250 --json /tmp/polydegree-stage25.DYOljv/face_normal.json
python3 -B -O proof_search/affine_nondegeneracy/face_system_audit.py \
  --max-d 250 --json /tmp/polydegree-stage25.DYOljv/face_optimized.json

python3 -B proof_search/affine_nondegeneracy/validate_affine_receipts.py \
  --directory proof_search/affine_nondegeneracy --d-min 21 --d-max 30 \
  --json /tmp/polydegree-stage25.DYOljv/affine_receipts_normal.json
python3 -B -O proof_search/affine_nondegeneracy/validate_affine_receipts.py \
  --directory proof_search/affine_nondegeneracy --d-min 21 --d-max 30 \
  --json /tmp/polydegree-stage25.DYOljv/affine_receipts_optimized.json

python3 -B proof_search/triple_disjointness/verify_structural_reduction.py \
  --identity-max 24 --exact-max 15 \
  --json /tmp/polydegree-stage25.DYOljv/triple_normal.json
python3 -B -O proof_search/triple_disjointness/verify_structural_reduction.py \
  --identity-max 24 --exact-max 15 \
  --json /tmp/polydegree-stage25.DYOljv/triple_optimized.json
```

The affine `d=21..30` validator checks schemas, hashes, and stated quotient
dimensions; it explicitly does **not** recompute the expensive Groebner bases.
The face and triple receipts are finite supporting searches and do not prove
the open affine theorem.

The publication-ready negative control was also rerun in both modes and
correctly exited 1 because `datePublished`, `doi`, `pdfUrl`, `repoUrl`,
`releaseUrl`, and `license` are absent.

### Replay results and hashes

| Artifact | Result | SHA-256 |
|---|---|---|
| candidate validator, normal and `-O` | PASS; byte-identical to each other and frozen reports | `25dc2bbff661f79221a081c498ffc8cc1745f4d885b0659edc7f235005ea6f98` |
| replacement verifier, normal and `-O` | 10/10 symbolic; 51/51 witnesses; byte-identical | `a6ace1972c6457be476ae808d7103d1fce40140617f9462de84ada80c7f03529` |
| mutation report, normal | 17/17 | `ba81de85bd824a93449bfae89f0da9e9121b3c08a14a32dd7a325e4d570179a5` |
| mutation report, `-O` | 17/17; differs only in recorded optimization level | `fcd887897e79c779481543a836eb3fafdcb69d0d1a6cccc22e579b58933b46ce` |
| archive assert probe, normal | injected non-integral coefficient rejected | `d0f6bc487155836efd930c78de9772e063ebd3f94ed7f5ef294acc8a1b18d6cc` |
| archive assert probe, `-O` | guard removed; silent floor division observed | `cfac0278b4eb71997e22cbce668442ae97d9c256241d9c3c57b5ca71ef7f7b07` |
| affine geometry `d=2..20`, both modes | exact PASS; byte-identical | `f000424d80988ceeed66b3f33ce0ae5f58bbbba2d031508420b66a9a8065edee` |
| adjacent boundary `d=2..200`, both modes | exact PASS; byte-identical | `f9d8cc61ccd81105a5af41aea3631831dcf1f68f31029c625c84d3267f8cf2d4` |
| hypergeometric/boundary replay, both modes | exact PASS; byte-identical | `8fbc4d290027577180e418160e94ebf288ec30367ff33f8f538383dfa3045e5b` |
| face audit `d=2..250`, both modes | exact finite PASS; byte-identical | `0e135e2e8bd241a325dcedf9774d9f6c81802e501b45aca333a6924aefd2e75a` |
| affine receipt validation `d=21..30`, both modes | schema/hash PASS; byte-identical | `26d2db480e8b76f38ac1bd8d6d6236af889afed490619503e5ab82f52d390287` |
| triple structural receipt, both modes | identities `n=0..24`, exact `d=2..15`; byte-identical | `260e6d66150dab817f74e5e94b3fb8b57f8908c6c4ee1d7c64969c062d8046e8` |
| publication-ready expected failure, both modes | expected FAIL; byte-identical to frozen control | `736c20178a5aca9f1a0d78d905d50eebc85c96d518cfa8ea48bbc8921dec86ac` |

The upstream verifier passed 51/51 in both modes. Its raw JSON hashes differ
because it records wall-clock elapsed time; after removing only
`elapsed_seconds` and canonicalising with `jq -S`, both reports hash to
`4f39c06014f7c86d19a54cac848f2f4dfda4530690ea55fd86403497a139abad`.

Key frozen payload hashes independently reproduced:

- upstream v0.3.0 archive:
  `e51af558a067c28847219a788f8dd4d28de4a6e9bc3b8d00c5ecab2c3b123334`
- 51-row witness JSON:
  `b659a8bccea30df4f800df526319bcbe01f429c3bee2ee8146983933da9cb38b`
- candidate PDF:
  `fd65f6e0e988066a32263b083fa97f3996c42a5d037deeffd4783032530ee2ce`
- `MANUSCRIPT.md`:
  `a9f06d035fe2ce1c4b4e1d9d7044f2dfd8006c9f2cab605e1cc34e4de8bf9bd8`
- `EVIDENCE_PRESS_BODY.md`:
  `8f4af40a44f755022ffaf93fdd135b747575ca8c6797143dfb190a8af9ff5887`
- `CLAIM_STATUS.json`:
  `f67d6d66dcd81e959979276e17b0d9850f0b0577ff2176e706a4ebae864d5786`

The outer manifest passed **85/85** in both modes. The embedded upstream
archive's 38-file manifest also passed. The PDF is 17 pages and 381,570 bytes.
The checkpoint's “210 words” is reproducible as a raw Markdown whitespace
count of the main abstract; pandoc-rendered plain text counts 207, so the
dashboard should retain or state its counting convention.

## Mutation and negative-control audit

All 17 controls passed in both modes. The controls detect:

- corrupted recorded `A`, `J`, and next-coefficient residues;
- a changed point coordinate, composite “prime”, zero chart coordinate,
  removed witness row, and Boolean masquerading as an integer;
- wrong derivative sign, alpha-column shift, determinant sign, Euler weights,
  scalar `d+1` versus `d+2`, and Euler–Jacobian sign;
- a singular common zero with `J=0`; and
- removal of the replacement verifier's explicit integrality guard under
  optimized Python.

The `d=8,p=5` case is deliberately a **positive theorem-regression fixture**:
the `J`-based hypotheses pass with `G_(d+2)=2` and `J=3`, while `A=0 mod 5`.
That is the intended bad-characteristic rescue.

## Ordinary Python versus `python -O`

The current candidate validator, replacement verifier, geometry scripts, and
supporting exact checks either use explicit exceptions or do not depend on
proof-critical assertions. Their ordinary/optimized substantive outcomes
agree, and deterministic reports are byte-identical where designed to be.

The embedded upstream verifier retains a proof-critical assertion in
`repro/verify_polydegree_witnesses.py` before integer floor division. The
fresh probe established:

- ordinary Python: the injected non-integral numerator raises an assertion;
- `python -O`: the assertion disappears and the code silently returns
  floor-divided zero coefficients.

This is a **latent fail-open mutation/error-detection risk**, not evidence that
any of the current 51 witnesses is false. The unmodified corpus passed both
modes and the replacement verifier recomputed the relations with explicit
guards. Nevertheless, the archived verifier should not be reused as a sole
assurance path until the assertion is replaced by an unconditional exception.

## Independence boundary

The replacement verifier is genuinely separate at the code level:

- it imports no upstream verifier functions;
- it uses its own sparse-polynomial representation and determinant routine;
- it recomputes the derivatives, determinants, Euler identities, and witness
  relations; and
- it has independent mutation controls.

It is **not** independent in the stronger research sense. It necessarily uses
the same mathematical definitions, the same theorem formulas, and the same
frozen witness JSON, and it was produced within the same AI-assisted workflow.
A shared misunderstanding of the definitions or cited theorems could survive
both code paths. This is producer-side code-path diversity, not unaffiliated
reproduction, external specialist review, or formal proof.

## Citation audit

All nine bibliography records exist and their identity fields agree with
primary or authoritative records:

1. Lewis–Perry–Straub, arXiv:1809.09681 / DOI
   `10.1016/j.jpaa.2019.04.002`;
2. Perry's 2016 University of Alabama dissertation;
3. Edo–van den Essen, arXiv:1304.3956 / DOI
   `10.1016/j.jalgebra.2013.09.011`;
4. Grochow, DOI `10.1080/00029890.2024.2440297`;
5. Stacks Project Tag 00HP;
6. Stacks Project Tag 00FV;
7. arXiv:2404.11479v2;
8. arXiv:2309.10970v3; and
9. NIST DLMF §§15.8, 18.5, and 18.16.

No fabricated citation, author, title, venue, DOI, or theorem attribution was
found. This verifies cited identity and the stated use, not an exhaustive
prior-art search. The package correctly records that authenticated specialist
database searches and original-author contact remain outstanding.

## Non-ledger integrity findings

### F1 — author declarations lack supplied attestation — BLOCKING

`MANUSCRIPT.md` lines 1032–1045 assert:

- no specific public, commercial, or not-for-profit funding;
- no known competing financial interests or relevant personal relationships;
  and
- a specific CRediT role allocation to “Anonymous”.

These are factual author declarations, not consequences of the mathematics or
code. The frozen source contains no signed declaration, identity-bound author
record, dated attestation, or other supplied evidence from which an auditor can
verify them. The manuscript's own assertions cannot independently verify
themselves. Verdict for each: **UNVERIFIABLE** under the strict protocol.

Remedy: obtain and freeze a dated author attestation covering funding,
conflicts, CRediT roles, authorship responsibility, and AI/tool disclosure;
record its hash and access boundary. It may remain private if necessary, but
the public package should state that the declarations are author-attested.

### F2 — `aiGenerated:false` is not auditable against disclosed drafting — BLOCKING

The metadata simultaneously states:

- `provenance.aiGenerated: false`;
- `provenance.aiAssisted: true`; and
- language-model tools assisted “drafting and package preparation”.

These can be compatible only if `aiGenerated` has a defined narrower meaning,
such as “not wholly generated without human authorship”. No schema or field
definition is supplied. A downstream consumer could reasonably understand
`aiGenerated:false` as “no AI-generated prose”, which conflicts with the
drafting disclosure. Verdict: **UNVERIFIABLE / internally ambiguous**.

Remedy: define the fields in a versioned schema, or replace the Boolean with a
less misleading value/field set that explicitly represents AI-assisted text
generation and human responsibility.

### F3 — one-line “uniform e=3 theorem” wording is over-broad — BLOCKING

The package proves a uniform e=3 boundary-factor theorem (Theorem 7.2), while
the uniform all-`d` affine radicality/Jacobian-unit/next-coefficient-unit
theorem remains open. The one-line phrase “the uniform e=3 theorem remains
open” collapses these two statements and can be read as denying the proved
boundary theorem. Verdict: **MINOR_DISTORTION / gray-zone FAIL**.

Remedy: say “the uniform e=3 affine theorem remains open.”

### F4 — machine-ledger polarity for `N1` and `X1` — BLOCKING

The status scale repairs these entries for a careful reader, but their claim
strings are affirmative. Safer replacements are:

- `N1`: “A bounded collision search found no prior derivative–Jacobian
  packaging; novelty and priority are not established.”
- `X1`: “No independent reproduction, formal verification, external
  specialist review, or peer review has been established.”

### F5 — v0.2.0 byte-identity claim is one receipt short of direct replay — BLOCKING UNDER GRAY-ZONE RULE

The current witness hash is confirmed and the frozen Stage 1 assurance report
states that it matched v0.2.0 byte-for-byte. The Stage 2 package, however,
contains only the v0.3.0 archive and the report, not the v0.2.0 corpus itself.
This audit therefore verified *consistency with the prior receipt*, not the
underlying byte comparison. Remedy: include the old witness file or a
content-addressed immutable reference sufficient to fetch and compare it.

### F6 — retained upstream assert-only guard — NON-BLOCKING FOR CURRENT RESULTS, REQUIRED ROBUSTNESS FIX

This defect is accurately disclosed and independently demonstrated. It does
not invalidate the present 51 rows because multiple explicit-guard paths pass,
but it remains a fail-open hazard for future mutated or newly generated data.

### F7 — intentional publication metadata gaps — EXPECTED, NOT A DEFECT

The DOI, repository/release URLs, datePublished, and license fields are null;
the package is labelled pre-deposit and its publication-ready validator fails
closed. No release identifiers should be invented merely to make the control
pass.

## Seven AI Research Failure Modes

The paper is theoretical and computer-assisted rather than experimental/ML.
The checklist was therefore applied by mapping “experiments” to exact symbolic
and CAS runs, “datasets” to the frozen witness/receipt corpus, and “shortcut”
to an implementation or finite-range artefact standing in for the intended
mathematical mechanism.

| Mode | Status | Evidence and theoretical-paper applicability |
|---|---|---|
| 1. Implementation bug passing self-review | **CLEAR, with disclosed latent defect** | Every claimed finite result has a script/receipt and fresh exit-0 replay. Exact arithmetic, independent code paths, and mutations found no scientifically wrong row. The upstream assert-only guard is a real bug, but it is disclosed, the current data pass explicit replacement checks, and no paper conclusion depends solely on it. |
| 2. Hallucinated citation | **CLEAR** | All 9 records exist; identity and load-bearing uses were checked against primary/authoritative records. Frozen PDFs support the repaired boundary-proof citations. |
| 3. Hallucinated experimental result | **CLEAR** | There are no empirical effect sizes or invented experiments. The analogous numerical claims—10/10, 51/51, 17/17, `d`/`n` ranges, quotient lengths, gcds, hashes, and page count—map to retained artifacts and were freshly replayed or directly counted. |
| 4. Shortcut reliance | **CLEAR** | The result is not an ML generalisation claim. The analogous danger—checking only a convenient formula/path or treating finite sweeps as the all-`d` theorem—is addressed by exact dual constructions, negative controls, separate algebraic arguments, and explicit open-status language. Code paths still share the mathematical definitions, which is recorded as an assurance limitation. |
| 5. Bug reframed as novel insight | **CLEAR** | The bad-characteristic rescue is forced by the exact characteristic-zero syzygy and passes an explicit positive regression; it is not a failed mod-p check retold as discovery. The earlier invalid strict-interlacing shortcut was rejected and repaired rather than promoted. |
| 6. Methodology fabrication | **SUSPECTED — BLOCKING** | The computational Methods/receipts themselves match the scripts and fresh runs. The narrow concern is provenance reporting: `aiGenerated:false` lacks a supplied definition despite an explicit disclosure that language models assisted drafting. That reporting drift cannot be cleared from the frozen record. |
| 7. Frame-lock at an early stage | **CLEAR** | The manuscript changed framing from an auxiliary determinant to a Jacobian, records a referee-driven repair, separates the boundary theorem from the open affine theorem, and declines to promote supplementary finite searches. No evidence shows that a known wrong framing was preserved merely to complete the pipeline. |

Because Mode 6 is **SUSPECTED**, the academic-pipeline rule blocks progress.
The user's stricter gray-zone rule independently blocks on F1–F5.

## Required remediation before re-audit

1. Freeze a human author attestation for funding, competing interests, CRediT,
   authorship responsibility, and AI/tool disclosure.
2. Define or revise `aiGenerated`/`aiAssisted` so the metadata cannot deny the
   disclosed use of language models in drafting.
3. Change the one-line summary to “uniform e=3 affine theorem remains open.”
4. Rewrite `N1` and `X1` as negative/bounded findings, not affirmative claims
   with negating statuses.
5. Add the v0.2.0 witness bytes or an immutable content-addressed reference so
   byte identity can be independently replayed.
6. Replace the upstream verifier's proof-critical `assert` with an explicit
   unconditional exception before using it for any future corpus.
7. Rerun manifest, candidate validator, provenance checks, and the seven-mode
   audit in normal and optimized modes after revision.

## Assurance limits

This audit is a detailed producer-side adversarial review. It does not provide
proof-assistant formalisation, unaffiliated reconstruction, specialist peer
review, novelty/priority determination, venue acceptance, or a REF grade. The
uniform affine theorem and uniform adjacent-factor coprimality remain open.
