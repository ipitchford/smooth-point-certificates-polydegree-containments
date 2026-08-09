# Stage 2.5 correction log

**Derivative:** `0.4.1-candidate`  
**Frozen ancestor:** `0.4.0-candidate`  
**Correction rounds used:** 1 of 3 permitted rounds

The frozen Stage 2 package was audited read-only.  It failed the initial
fail-closed integrity gate even though no mathematical or computational-core
defect was found.  This derivative records the first correction round; the
ancestor remains unchanged.

## Initial blocking findings

1. Four bibliography records had exact-metadata defects, and one LPS citation
   context exceeded what the cited theorem states.
2. Funding, competing-interest and CRediT declarations lacked an
   accountable-author attestation.
3. `aiGenerated:false` conflicted with an explicit language-model drafting
   disclosure under an undefined machine schema.
4. The metadata phrase “uniform e=3 theorem” blurred the proved boundary
   theorem and the open affine theorem.
5. Claim-ledger entries `N1` and `X1` used affirmative text whose statuses
   qualified or negated it.
6. The v0.2/v0.3 witness byte-identity statement could not be replayed from
   the Stage 2 package because the earlier bytes were absent.
7. The inherited dashboard's “210 words” description did not state its
   counting convention.

## Corrections applied

- Replaced both Stacks records with the official 2026 project citation and
  exact Tag 00HP/00FV locators.
- Corrected the punctuation in arXiv:2404.11479v2, pinned both arXiv source
  versions, and replaced the synthetic DLMF record with Release 1.2.7,
  date, editors and three exact equation permalinks.
- Narrowed the LPS sentence to the source-supported statement that Theorem 4
  supplies a sufficient condition; clarified Perry's indexing.
- Replaced unsupported declaration claims with explicit pre-deposit pending
  statements.  No funding, conflict or CRediT status is asserted.
- Set both `aiGenerated` and `aiAssisted` to true and retained the explicit
  language-model drafting disclosure and human-responsibility boundary.
- Changed the one-line summary to “uniform e=3 affine theorem remains open.”
- Rewrote `N1` as a bounded-search result with novelty/priority unestablished,
  and `X1` as a negative assurance statement.
- Included the Stage 1 v0.2 witness JSON and a provenance note; the validator
  now checks both hashes and direct byte identity with the v0.3 witness.
- Recorded the abstract count as 210 raw-Markdown whitespace tokens and 207
  Pandoc-rendered words.
- Strengthened the candidate validator to enforce these semantic repairs,
  version consistency and the pre-deposit publication boundary.
- Rebuilt TeX, PDF and extracted text from the corrected sources, then reran
  the proof-facing computations under ordinary and optimized Python.

## Mathematical effect

None of these changes expands or contracts a theorem.  The general
Jacobian/Euler/Hensel and curve results and the uniform boundary-squarefreeness
theorem remain proved in the candidate; the uniform affine theorem and
uniform adjacent-boundary coprimality remain open.

## Remaining pre-publication work

Accountable-author declarations, licensing, DOI, repository/release URLs and
live publication readback remain external publication blockers.  They are
not filled with placeholders and are not represented as completed by this
Stage 2.5 correction.
