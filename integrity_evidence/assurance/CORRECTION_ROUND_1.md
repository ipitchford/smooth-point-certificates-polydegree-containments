# Correction round 1 focused re-audit

**Candidate:** `work/irreducible-norms-ref-upgrade/stage2_5/candidate`  
**Candidate version represented by the principal files:** `0.4.1-candidate`  
**Snapshot audited:** `2026-08-09T20:11:57+0100`  
**Scope:** original findings F1–F5, AI Research Failure Mode 6, the abstract-count note, and the strengthened validator gates  
**Mutation policy:** read-only against the candidate; fresh reports written only to `/tmp`

## Verdict

**FAIL — correction round 1 is not yet freezeable or Stage 2.5-passing.**

All requested substantive corrections F1–F5 are resolved, Failure Mode 6 is
now CLEAR, and the abstract-count note is exact. The staged directory still
fails package-integrity gates in ordinary and optimized Python, however:

- the outer manifest is the old 85-entry manifest and does not describe the
  corrected 102-file payload;
- five files required by the strengthened validator are absent;
- the citation-metadata gate contains a counting bug and rejects the corrected
  bibliography;
- several retained reports and an active reconciliation document still carry
  `0.4.0-candidate`; and
- the version gate is too narrow to detect those stale artifacts.

Under the instruction “PASS only if every blocker is resolved”, these are
blocking. They are package/gate defects, not regressions in the corrected
mathematics or the five targeted claim repairs.

## Focused correction results

| Item | Round-1 status | Evidence |
|---|---|---|
| F1: unsupported Funding/COI/CRediT declarations | **RESOLVED** | `MANUSCRIPT.md` now says each accountable-author attestation has not been supplied and explicitly asserts no funding, absence-of-conflict, or role allocation. The rendered `build/main.txt` matches. `STATUS.md` and `PUBLISHING_BLOCKERS.md` retain the pending-author boundary. |
| F2: `aiGenerated:false` versus AI-assisted drafting | **RESOLVED** | Metadata now records `aiGenerated:true`, `aiAssisted:true`, identifies language-model tools, and explicitly discloses drafting and package preparation. The manuscript and `PROVENANCE.md` agree. |
| F3: ambiguous “uniform e=3 theorem” one-line | **RESOLVED** | `oneLine` now says “the uniform e=3 affine theorem remains open”, preserving the proved uniform boundary theorem. No old one-line wording occurs in the active candidate outside historical source records. |
| F4: unsafe N1/X1 polarity | **RESOLVED** | `N1` now reports only a bounded negative collision search and says novelty/priority are not established. `X1` now says no independent reproduction, formal verification, external specialist review, or peer review has been established. |
| F5: v0.2 byte identity not directly replayable | **RESOLVED** | The earlier witness bytes and a provenance note are included. `cmp` succeeds; both v0.2 and v0.3 JSON files hash to `b659a8bccea30df4f800df526319bcbe01f429c3bee2ee8146983933da9cb38b`. The validator performs both expected-hash and byte-equality checks. |
| Mode 6: methodology/provenance fabrication concern | **CLEAR** | The metadata now truthfully represents AI-assisted generation/drafting, while computational methods continue to match retained scripts and receipts. No unresolved discrepancy between described and executed procedures was found in this focused pass. |
| Abstract-count note | **RESOLVED** | Independent commands reproduce 210 raw-Markdown whitespace tokens and 207 words after Pandoc plain rendering. `STAGE2_CHECKPOINT.md` states both conventions and labels itself historical. |

Thus the original F1–F5/Mode-6 block is cleared. The overall FAIL comes from
the new packaging and validator findings below.

## Fresh validator results

Commands run from the staged candidate:

```sh
python3 -B scripts/validate_candidate.py --root "$PWD" \
  --report /tmp/correction_round_1_validation_normal.json
python3 -B -O scripts/validate_candidate.py --root "$PWD" \
  --report /tmp/correction_round_1_validation_optimized.json
```

Both exited 1. Their JSON is byte-identical and has SHA-256:

```text
0b5454683edb04021eb97a77154908ec4415455de487e627ff383e523a1e4019
```

Both report `0.4.1-candidate` and the same two failures:

1. missing required files:
   `ACADEMIC_INTEGRITY_REPORT.md`,
   `AI_RESEARCH_FAILURE_MODE_AUDIT.md`, `CORRECTION_LOG.md`,
   `INTEGRITY_AUDIT.json`, and `STAGE2_5_CHECKPOINT.md`;
2. `Stage 2.5 exact-metadata citation repairs are absent or regressed`.

All focused semantic checks inside the same failed run pass:

- `author_attestation_boundary`;
- `claim_ledger`, including safe N1/X1 polarity;
- `frozen_source_hashes`, including v0.2/v0.3 byte identity;
- principal component `version_consistency`;
- `ai_provenance_consistency`;
- pre-deposit `metadata_boundary`;
- independent-verifier 10/10 and 51/51 receipts;
- mutation 17/17 receipts;
- affine/boundary receipt ranges; and
- uniform-squarefreeness receipt/proof-repair gates.

## Blocking package findings

### C1 — outer manifest is stale — BLOCKING

Both commands fail:

```sh
python3 -B scripts/verify_manifest.py --root "$PWD"
python3 -B -O scripts/verify_manifest.py --root "$PWD"
```

`MANIFEST.sha256` has 85 entries and SHA-256
`1f355eb5178aec20311c5ea5b245d54796f7f46c9674c9b103f4ba5661be5815`.
The directory has 103 files including the manifest, hence 102 payload files.
The verifier reports:

- **17 unmanifested files**, including both newly supplied v0.2 provenance
  files, ten Stage 2.5 replay reports, and five LaTeX auxiliary files; and
- **15 digest mismatches**, covering corrected source/metadata, rebuilt PDF
  artifacts, the normal validation report, bibliography, and validator.

This prevents a frozen-package PASS even though the newly added v0.2 bytes are
correct. Decide which transient build files belong in the release, remove or
exclude the rest from the candidate, then regenerate the full manifest only
after all Stage 2.5 records are present.

### C2 — mandatory Stage 2.5 records are absent — BLOCKING

The strengthened validator requires five integrity/checkpoint records that do
not yet exist in the staged candidate. This may be expected while reviewers
are still writing, but the candidate cannot pass or freeze until the final
records are assembled and included in the manifest.

### C3 — citation-metadata gate has a false-negative bug — BLOCKING

The bibliography repairs themselves are present:

- exact Martínez-Finkelshtein title punctuation;
- arXiv versioned URLs `2404.11479v2` and `2309.10970v3`;
- two Stacks Project records dated 2026;
- DLMF release `1.2.7 of 2026-06-15`; and
- exact DLMF equation URLs in the proof.

The validator nevertheless requires

```python
bibliography.count("year         = {2026}") == 2
```

There are correctly **three** such records: two Stacks entries plus DLMF.
Therefore the gate rejects correct data. It should test the two Stacks entries
structurally/by citation key, or expect the correct total of three while that
schema remains fixed. A manual reproduction of every other conjunct returned
true.

### C4 — version and receipt drift — BLOCKING

The principal manuscript, ledger, and metadata are consistently
`0.4.1-candidate`. The retained package is not globally consistent:

- `RECONCILIATION_REPORT.md` still says `Stage 2 derivative:
  0.4.0-candidate` without marking that field historical;
- `build/validation_report_optimized.json` is a stale passing
  `0.4.0-candidate` report;
- `build/publication_ready_expected_failure.json` is a stale
  `0.4.0-candidate` report; and
- ordinary and optimized retained validation reports are therefore neither
  the same version nor byte-identical.

These must be regenerated after the validator and required records are fixed.
The historical `STAGE2_CHECKPOINT.md` may retain 0.4.0 because it now explicitly
labels itself a superseded historical checkpoint.

## Strengthened-validator audit

### Effective new gates

- F1: requires explicit pending-attestation language and rejects the exact old
  unsupported declarations.
- F4: requires exact safe N1/X1 text.
- F5: checks both expected hashes and byte-for-byte equality.
- Principal version consistency: checks manuscript, ledger, and metadata.
- F2/Mode 6: requires `aiGenerated:true`, `aiAssisted:true`, and a
  language-model disclosure.

### Remaining gate weaknesses

1. The citation year-count predicate is erroneous as described in C3.
2. F3's metadata `oneLine` is not checked, so the old ambiguous phrase could
   regress without failing validation.
3. The abstract 210/207 conventions are not checked; the current values are
   correct only by manual replay.
4. The AI gate checks for `language-model` but not for the load-bearing word
   `drafting`; a disclosure could become incomplete and still pass.
5. The version gate checks only three principal components and misses active
   support documents and retained reports, as C4 demonstrates.
6. The F1 negative gate uses three exact old strings. A paraphrased unsupported
   funding/COI/CRediT assertion would evade it. The current manuscript is safe,
   but the gate is a sentinel, not a semantic proof.
7. `validate_candidate.py` does not invoke `verify_manifest.py`; the release
   workflow must retain both gates explicitly.

These weaknesses should be fixed or recorded before treating a future green
validator report as the complete Stage 2.5 integrity result.

## Mathematical replay receipts

The focused correction did not alter the mathematical boundary. The staged
fresh replay files agree with the previously audited receipts:

- Jacobian verifier normal/optimized: byte-identical,
  `a6ace1972c6457be476ae808d7103d1fce40140617f9462de84ada80c7f03529`,
  10/10 symbolic and 51/51 witness checks;
- mutations: 17/17 in both modes, with the expected optimization-level field
  difference;
- affine `d=2..20`: byte-identical,
  `f000424d80988ceeed66b3f33ce0ae5f58bbbba2d031508420b66a9a8065edee`;
- boundary `d=2..200`: byte-identical,
  `f9d8cc61ccd81105a5af41aea3631831dcf1f68f31029c625c84d3267f8cf2d4`;
- hypergeometric replay: byte-identical,
  `8fbc4d290027577180e418160e94ebf288ec30367ff33f8f538383dfa3045e5b`.

These receipts support the unchanged mathematics but do not waive C1–C4.

## Pre-deposit integrity versus publication readiness

The following are **publication/deposit blockers**, not defects in the
truthfulness of the corrected pre-deposit candidate:

- accountable-author attestations for funding, competing interests, and
  CRediT roles;
- final human-approved licences;
- DOI/concept DOI if used;
- publication date;
- public repository, release, PDF, and alternate-source URLs;
- immutable release tag/archive and public byte comparison;
- final review disposition and live Evidence Press/readback gates.

The candidate correctly leaves these values absent and explicitly says the
attestations are pending. `--publication-ready` therefore should fail on those
fields until real external objects and approvals exist. No placeholder should
be invented.

C1–C4 are different: they block **Stage 2.5 package integrity now**, before
publication readiness is considered.

## Required correction-round 2 actions

1. Add/finalise the five mandatory Stage 2.5 integrity/checkpoint records.
2. Fix the citation-metadata predicate so it accepts the correct three 2026
   records or scopes the count to the two Stacks entries.
3. Add gates for the corrected one-line wording, explicit drafting disclosure,
   and the two abstract-count conventions.
4. Expand version consistency to all active status/provenance/reconciliation
   documents and retained validator/control reports.
5. Update `RECONCILIATION_REPORT.md` to 0.4.1 or label its version field
   historical.
6. Regenerate ordinary and optimized template validation reports and the
   publication-ready expected-failure receipt at 0.4.1.
7. Remove/exclude transient build files as appropriate, then regenerate and
   verify the complete manifest in both modes from a fresh extraction.
8. Re-run this focused audit. PASS is appropriate only after all template
   integrity and manifest gates are green; publication fields may remain
   absent in the explicitly pre-deposit package.

