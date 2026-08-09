# Seven-mode AI research failure audit

**Stage:** 2.5, pre-review integrity  
**Candidate:** `0.4.1-candidate`  
**Final disposition:** all seven modes CLEAR after correction round 1

This is a theoretical and computer-assisted mathematics paper.  Experimental
language in the checklist is mapped to symbolic/CAS runs, frozen witnesses,
exact finite ranges and the distinction between finite evidence and a uniform
proof.

| Mode | Final status | Evidence |
|---|---|---|
| 1. Implementation bug passing AI self-review | **CLEAR, disclosed latent defect retained** | Every claimed finite result has a script and receipt and was freshly replayed with exit 0 under ordinary and optimized Python. Mutation controls pass 17/17. The embedded upstream verifier's assertion-only guard is a real fail-open risk under `-O`, but it is disclosed, probed, and not the sole path: the explicit-guard replacement passes 10/10 symbolic gates and 51/51 witnesses. |
| 2. Hallucinated citation | **CLEAR** | All 9 records pass existence, exact metadata and target checks after correction; all 14 citation contexts pass; no orphan or dangling citation remains. Load-bearing source versions are frozen. |
| 3. Hallucinated experimental result | **CLEAR** | The analogous claims—10/10, 51/51, 17/17, bounded `d`/`n` ranges, quotient lengths, gcds and hashes—map to retained artifacts and fresh replays. There are no empirical effect sizes or invented experimental runs. |
| 4. Shortcut reliance | **CLEAR** | Exact dual constructions, negative controls and written algebraic proofs guard against a convenient code path standing in for the mechanism. Finite sweeps are never promoted to the open all-index affine theorem. Shared definitions remain an explicit independence limitation. |
| 5. Implementation bug reframed as novel insight | **CLEAR** | The bad-characteristic rescue follows from the exact characteristic-zero syzygy and has a positive `d=8,p=5` regression. The earlier over-broad strict-interlacing shortcut was rejected and repaired with a checked logarithmic-mesh argument. |
| 6. Methodology fabrication | **CLEAR after correction** | The methods match the scripts, environments and receipts. On the ancestor this mode was SUSPECTED because `aiGenerated:false` was ambiguous against the drafting disclosure. The derivative now records `aiGenerated:true`, `aiAssisted:true`, explicit language-model drafting and human responsibility. |
| 7. Frame-lock at an early stage | **CLEAR** | The workflow changed framing from an auxiliary determinant to a Jacobian, accepted an adversarial proof repair, separated the proved boundary theorem from the open affine theorem, and declined to turn larger finite tables into a uniform claim. |

No mode is `SUSPECTED` or `INSUFFICIENT EVIDENCE` in the corrected candidate.
This is producer-side adversarial assurance, not an assertion of independent
human review, formal verification or peer review.
