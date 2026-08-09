# Academic integrity verification report

## Verification mode

Initial Verification — Academic Pipeline Stage 2.5, pre-review integrity.
The frozen `0.4.0-candidate` was checked first, failed closed, corrected once,
and re-audited as `0.4.1-candidate`.

## Verdict

**PASS WITH NOTES after correction round 1.**

There are zero unresolved SERIOUS or MEDIUM issues, zero
`MAJOR_DISTORTION`, zero `UNVERIFIABLE`, zero `CLOSE_MATCH`, and zero
`VERBATIM` findings in the corrected pre-deposit candidate.  The notes are
scope and publication-boundary notes, not waived integrity defects.

## Verification summary

| Category | Scope | Final result | Unresolved issues |
|---|---:|---:|---:|
| Reference existence | 9/9 records | 9 PASS | 0 |
| Bibliographic accuracy and targets | 9/9 records | 9 PASS | 0 |
| Ghost citations | complete closure | 0 orphan / 0 dangling | 0 |
| Citation-context accuracy | 14/14 occurrences (100%) | 14 PASS | 0 |
| Statistical/computational data | all reported counts, hashes and claimed finite ranges | PASS | 0 |
| Internal consistency | manuscript, ledger, metadata, sources and replay boundaries | PASS | 0 |
| Originality D1 | 40/132 eligible paragraphs (30.303%); 12/12 major sections | PASS | 0 close/verbatim |
| Self-plagiarism D2 | author anonymous; identity corpus unavailable | NOT EXECUTABLE | note only |
| Claim verification E | 16/16 ledger claims (100%) | 16 PASS in their stated proof/evidence/status class | 0 |
| Seven AI failure modes | 7/7 | CLEAR after correction | 0 |

## Phase A and B: sources and citation context

All nine sources exist.  Three journal DOIs resolve to the correct works; the
dissertation resolves to the official institutional record; the two Stacks
tags, two fixed arXiv versions and DLMF release/permalinks resolve to their
authoritative sources.  Four ancestor metadata defects and one unsupported
context clause were corrected.  Fresh source-layer and generated-artifact
readback found 9/9 exact records and 14/14 supported contexts.

Semantic Scholar's official API supplied structured exact matches for the
DOI/arXiv records it returned.  Rate limiting prevented a complete structured
API pass for two records, and Stacks/DLMF are not ordinary paper identifiers;
the audit therefore completed those identities against DOI registries,
publishers, arXiv, the institutional repository, Stacks and NIST rather than
silently treating an API gap as verification.

## Phase C: statistical and computational data

The paper contains no inferential statistics, effect sizes or empirical
sample claims.  Every computational count or range was audited.  Fresh replay
under Python 3.14.6, SymPy 1.14.0 and Singular 4.4.1 reproduced:

- 10/10 symbolic gates and 51/51 witness relations;
- 17/17 mutation/regression controls in ordinary and optimized modes;
- exact affine geometry for `d=2..20`;
- exact adjacent boundary coprimality for `d=2..200`;
- hypergeometric identities and individual squarefreeness through `n=301`,
  adjacent gcd evidence through `d=300`, and strict interlacing through
  `d=120`.

The first, affine, boundary and hypergeometric reports are byte-identical
between ordinary and optimized modes.  Mutation reports differ only in the
recorded optimization level, as intended.  These finite checks support only
their stated ranges; they do not prove the open uniform affine theorem.

## Phase D: originality

| Grade | Paragraphs | Proportion of sample |
|---|---:|---:|
| `ORIGINAL` | 20 | 50.0% |
| `COMMON_KNOWLEDGE` | 10 | 25.0% |
| `PARAPHRASE` | 10 | 25.0% |
| `CLOSE_MATCH` | 0 | 0.0% |
| `VERBATIM` | 0 | 0.0% |

The deterministic risk-weighted sample covers every major section.  The ten
paraphrases are cited mathematical background or source-theorem applications,
not close structural copying.  D2 is not executable because the scholarly
author is Anonymous and no identity-linked publication corpus was supplied;
no inference about self-reuse is made.

## Phase E: claim verification

All 16 ledger entries were checked, exceeding the Mode 1 minimum of ten.
`T1`–`T8` match their written proofs and hypotheses; `T9` matches the repaired
boundary proof and fixed external theorems; `C1`–`C3` match the retained exact
receipts and bounds; `I1` matches Lewis–Perry–Straub Theorem 4; `O1` is
correctly open and not claimed; `N1` is a bounded negative search with
novelty/priority unestablished; and `X1` correctly denies unestablished
external assurance.  No ledger entry is a major distortion or unverifiable.

## Correction-round disposition

The initial frozen candidate failed on exact citation metadata/context,
unsupported declarations, ambiguous AI metadata, an over-broad one-line
summary, unsafe ledger polarity and a non-replayable v0.2/v0.3 comparison.
All were repaired in one round.  The theorem claims were not expanded during
correction.  `CORRECTION_LOG.md` records the item-level changes.

## Notes and continuing boundaries

- Phase D uses public Web search as a heuristic, not Turnitin or iThenticate.
- D2 could not be run without an accountable author identity/corpus.
- Funding, competing-interest and CRediT attestations are still required
  before deposit; the candidate now says they are pending instead of asserting
  unsupported facts.
- DOI, licence, repository/release URLs and live Evidence Press readback are
  intentionally absent at the pre-deposit stage.
- Internal replay, code-path diversity and this AI-assisted audit do not
  establish independent reproduction, formal proof, external specialist
  review, peer review, acceptance, novelty, priority or a REF grade.

## Tool-limitation disclaimer

The originality screen searched publicly accessible Web material for a
30.303% paragraph sample and is not professional plagiarism-detection
software.  It cannot cover private manuscripts, every paywalled full text or
cross-language reuse.  Professional full-corpus screening remains appropriate
before formal submission.

## Audit trail

Detailed record-by-record search queries, source targets, citation contexts,
paragraph searches, claim reasoning, failure-mode reasoning and fresh replay
hashes are retained under `integrity_evidence/` in this package.
