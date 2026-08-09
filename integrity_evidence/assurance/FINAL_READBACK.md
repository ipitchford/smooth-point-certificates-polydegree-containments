# Final frozen-boundary readback

**Candidate:** `smooth-point-certificates-polydegree-containments`  
**Version:** `0.4.1-candidate`  
**Candidate root:** `/Users/admin/Documents/Codex/2026-08-09/the-0processed-folder-on-the-mac/work/irreducible-norms-ref-upgrade/stage2_5/candidate`  
**Readback time:** `2026-08-09T20:28:17+0100`  
**Verdict:** **PASS_WITH_NOTES**

## Verdict

No Stage 2.5 integrity blocker remains in the frozen candidate. The complete
129-entry payload manifest passes in ordinary and optimized Python; fresh
template validation passes in both modes; the publication-ready negative
control fails in both modes for exactly the six intentionally absent deposit
fields; all requested semantic/polarity gates pass; and fresh principal
computational receipts are byte-identical to their frozen counterparts.

The notes are genuine assurance limits and publication-only prerequisites,
not waived defects. The package remains a local, unrefereed, pre-deposit
candidate. It does not establish independent reproduction, formal
verification, external specialist review, peer review, novelty, priority,
acceptance, or a REF grade.

## Frozen identity

| Item | Readback |
|---|---|
| Files | 130 total files: 129 payload files plus `MANIFEST.sha256` |
| Manifest entries | 129 |
| `MANIFEST.sha256` SHA-256 | `f67537d600d1f1a431f2cd27ddd69dff5024d9c1c0b64ada216f89b77e7720c8` |
| Candidate PDF | `build/main.pdf`, 17 pages, 381,537 bytes |
| PDF SHA-256 | `a93b3f92e6762123bae5edae0cdec8696541ea9082139cc95a8fde169fa02d16` |
| Frozen v0.3 archive SHA-256 | `e51af558a067c28847219a788f8dd4d28de4a6e9bc3b8d00c5ecab2c3b123334` |
| v0.2 and v0.3 witness JSON SHA-256 | `b659a8bccea30df4f800df526319bcbe01f429c3bee2ee8146983933da9cb38b` |

The audit was read-only against the candidate. All fresh reports were written
under `/tmp`; only this assurance-agent report and its JSON companion were
created outside the frozen boundary.

## Requested frozen-boundary gates

| Gate | Ordinary Python | `python -O` | Result |
|---|---:|---:|---|
| Manifest | 129/129, exit 0 | 129/129, exit 0 | PASS |
| Stage 2.5 template validator | PASS, exit 0 | PASS, exit 0 | PASS |
| Publication-ready negative control | expected FAIL, exit 1 | expected FAIL, exit 1 | PASS as negative control |
| Jacobian replacement verifier | 10/10 symbolic; 51/51 witnesses | 10/10 symbolic; 51/51 witnesses | PASS |
| Mutation/regression controls | 17/17 | 17/17 | PASS |
| Affine exact sweep | `d=2..20`, all flags true | same | PASS |
| Boundary exact sweep | `d=2..200`, no failures | same | PASS |
| Hypergeometric/boundary receipt | identities and squarefreeness `n=2..301`; adjacent gcd `d=2..300`; strict interlacing `d=2..120` | same | PASS |
| Upstream assert-fragility probe | injected non-integral coefficient rejected | injected coefficient silently floor-divided | PASS: latent upstream defect reproduced |

The fresh template reports are mutually and frozen-byte identical, SHA-256
`541448139b51b55f296b74aaf748e70a68dfe2ac968919f677a8b34e00ee8e5b`.
The fresh publication-ready reports are mutually and frozen-byte identical,
SHA-256
`9f5d3ea3e5421dcb100cba4fdb7d0f750c7f97842aa947ba93b043619ad71227`.
The publication negative control reports exactly one failure:

> publication-ready mode requires: datePublished, doi, pdfUrl, repoUrl,
> releaseUrl, license

No unexpected validator failure is hidden by that expected failure.

## Principal receipt pairs

Every fresh principal receipt compared byte-for-byte equal to the corresponding
frozen normal or optimized receipt.

| Receipt | Normal SHA-256 | Optimized SHA-256 | Interpretation |
|---|---|---|---|
| Jacobian/refactor | `a6ace1972c6457be476ae808d7103d1fce40140617f9462de84ada80c7f03529` | same | 10/10 plus 51/51; optimization-invariant |
| Mutation controls | `ba81de85bd824a93449bfae89f0da9e9121b3c08a14a32dd7a325e4d570179a5` | `fcd887897e79c779481543a836eb3fafdcb69d0d1a6cccc22e579b58933b46ce` | 17/17 in both; expected byte difference records optimization level |
| Affine `d=2..20` | `f000424d80988ceeed66b3f33ce0ae5f58bbbba2d031508420b66a9a8065edee` | same | length, reducedness, Jacobian and next-coefficient gates true |
| Boundary `d=2..200` | `f9d8cc61ccd81105a5af41aea3631831dcf1f68f31029c625c84d3267f8cf2d4` | same | squarefree and adjacent-coprime flags true; no failures |
| Hypergeometric/boundary | `8fbc4d290027577180e418160e94ebf288ec30367ff33f8f538383dfa3045e5b` | same | all recorded identities and finite ranges pass |
| Upstream assert probe | `d0f6bc487155836efd930c78de9772e063ebd3f94ed7f5ef294acc8a1b18d6cc` | `cfac0278b4eb71997e22cbce668442ae97d9c256241d9c3c57b5ca71ef7f7b07` | expected semantic divergence exposes `assert` removal under `-O` |

The 17 controls include the positive bad-characteristic rescue regression:
the J-based hypotheses can pass although the residue-level `a`-unit test
fails. This preserves the correct distinction: avoiding primes dividing
`d+2` is required for the mod-p `a`-unit certificate, but not for the
J-based Hensel-to-characteristic-zero existence theorem.

## Semantic and integrity gates

All five correction-round blockers remain resolved.

1. **Declarations:** `MANUSCRIPT.md` explicitly says accountable-author
   funding, competing-interest and CRediT attestations have not been supplied,
   and asserts no status or role allocation meanwhile. The former unsupported
   positive declarations are absent from active manuscript, rendered text,
   metadata, ledger and status files.
2. **AI provenance / Mode 6:** metadata has `aiGenerated:true` and
   `aiAssisted:true`, discloses language-model drafting, and assigns the human
   publication decision. `INTEGRITY_AUDIT.json` records Mode 6
   `CLEAR_AFTER_CORRECTION`, with zero unresolved serious or medium findings.
3. **Open-theorem wording:** `oneLine` says the **uniform e=3 affine theorem**
   remains open. It does not use the overbroad old wording “uniform e=3
   theorem remains open”, so it does not obscure the proved uniform boundary
   theorem.
4. **Claim polarity:** N1 says only that a bounded collision search found no
   prior packaging and expressly says novelty/priority are not established.
   X1 says no independent reproduction, formal verification, external
   specialist review or peer review has been established.
5. **Source coupling:** direct `cmp` of the retained v0.2 and v0.3 witness JSON
   exits 0; both have the hash recorded above. The validator checks both byte
   identity and expected hashes.

The historical abstract count also replays exactly: 210 raw-Markdown
whitespace tokens and 207 words after Pandoc 3.9 plain rendering.

## Stale and defect-phrase scan

There is no active stale `0.4.0-candidate` version or active occurrence of the
former declaration, ambiguous one-line, `aiGenerated:false`, or unsupported
“not known necessary” claims.

Occurrences found by an unrestricted recursive scan are provenance, not live
claims:

- `STAGE2_CHECKPOINT.md`, `CORRECTION_LOG.md`, `RECONCILIATION_REPORT.md` and
  `ACADEMIC_INTEGRITY_REPORT.md` explicitly label the frozen 0.4.0 ancestor;
- `integrity_evidence/**` intentionally preserves pre-correction snapshots and
  defect reports;
- `scripts/validate_candidate.py` contains the bad phrases as rejection
  sentinels.

This retained history is correctly labelled and does not conflict with the
active 0.4.1 candidate.

## Defect and independence boundary

The embedded upstream verifier contains a proof-critical Python `assert`.
The fresh diagnostic proves that this is a latent fail-open risk: normal
Python raises on an injected non-divisible numerator, whereas `python -O`
removes the guard and silently accepts floor-divided data. This is a real
upstream defect, not an alleged theoretical counterexample.

It is not a remaining Stage 2.5 blocker because the candidate discloses it and
does not rely on that route alone. The separately written verifier imports no
archive verifier functions, uses standard-library exact sparse-polynomial and
finite-field arithmetic plus a generic Leibniz determinant, uses explicit
exceptions rather than proof-critical assertions, passes in both modes, and
is mutation-tested. Its independence boundary must nevertheless remain
calibrated: it is independent **code implementing the same mathematical
formula**, produced and run inside the same research workflow. It is not an
external independent reproduction or an independent proof.

## Publication-only pending items

These items do not block Stage 2.5 integrity of the pre-deposit candidate, but
they block publication/deposit readiness:

- accountable-author funding attestation;
- accountable-author competing-interest attestation;
- accountable-author CRediT allocation/approval;
- `datePublished`, DOI, PDF URL, repository URL and release URL;
- an approved package-wide licence compatible with the retained upstream
  material;
- subsequent public archive parity and live Evidence Press readback.

Stage 3 must not be inferred from this PASS_WITH_NOTES. The explicit checkpoint
confirmation required by `STAGE2_5_CHECKPOINT.md` remains necessary.

## Exact replay commands

From the candidate root:

```sh
python3 -B scripts/verify_manifest.py --root "$PWD"
python3 -B -O scripts/verify_manifest.py --root "$PWD"

python3 -B scripts/validate_candidate.py --root "$PWD" \
  --report /tmp/final_readback_validation_normal.json
python3 -B -O scripts/validate_candidate.py --root "$PWD" \
  --report /tmp/final_readback_validation_optimized.json

python3 -B scripts/validate_candidate.py --root "$PWD" --publication-ready \
  --report /tmp/final_readback_publication_normal.json
python3 -B -O scripts/validate_candidate.py --root "$PWD" --publication-ready \
  --report /tmp/final_readback_publication_optimized.json

cmp source_records/stage1_v0.2/polydegree_e3_witnesses_50_100.json \
  evidence/upstream/polydegree_e3_witnesses_50_100.json

python3 -B scripts/verify_jacobian_refactor.py \
  --witness-data evidence/upstream/polydegree_e3_witnesses_50_100.json \
  --report /tmp/final_readback_jacobian_normal.json
python3 -B -O scripts/verify_jacobian_refactor.py \
  --witness-data evidence/upstream/polydegree_e3_witnesses_50_100.json \
  --report /tmp/final_readback_jacobian_optimized.json

python3 -B scripts/test_mutations.py \
  --witness-data evidence/upstream/polydegree_e3_witnesses_50_100.json \
  --report /tmp/final_readback_mutation_normal.json
python3 -B -O scripts/test_mutations.py \
  --witness-data evidence/upstream/polydegree_e3_witnesses_50_100.json \
  --report /tmp/final_readback_mutation_optimized.json

python3 -B scripts/explore_geometry.py --d-min 2 --d-max 20 \
  --json /tmp/final_readback_affine_normal.json
python3 -B -O scripts/explore_geometry.py --d-min 2 --d-max 20 \
  --json /tmp/final_readback_affine_optimized.json

python3 -B scripts/boundary_sweep.py --d-min 2 --d-max 200 \
  --json /tmp/final_readback_boundary_normal.json
python3 -B -O scripts/boundary_sweep.py --d-min 2 --d-max 200 \
  --json /tmp/final_readback_boundary_optimized.json

python3 -B scripts/verify_boundary_hypergeom.py --d-min 2 --d-max 300 \
  --factor-max 300 --interlace-max 120 \
  --json /tmp/final_readback_hypergeom_normal.json
python3 -B -O scripts/verify_boundary_hypergeom.py --d-min 2 --d-max 300 \
  --factor-max 300 --interlace-max 120 \
  --json /tmp/final_readback_hypergeom_optimized.json
```

## Final conclusion

**PASS_WITH_NOTES.** Zero Stage 2.5 blockers remain at the frozen boundary.
The only positive defect finding is the disclosed upstream assertion-only
fail-open risk, which is bounded by a separately implemented explicit-guard
verifier and normal/optimized mutation controls. Author attestations,
publication identifiers, licence choice and public readback remain
publication-only prerequisites.
