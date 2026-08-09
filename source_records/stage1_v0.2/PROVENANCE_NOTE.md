# Stage 1 v0.2 witness provenance

This directory carries the exact witness JSON from the frozen Stage 1 output
`irreducible-norms-ref-stage1-2026-08-09` so that the v0.2/v0.3 byte-identity
claim is replayable without relying only on an earlier prose receipt.

- Stage 1 ZIP SHA-256:
  `c6e3ebe6acd78f8a02bd91e851585abd3eb4ea06875c2c9202e2132beac02a8d`
- Stage 1 manifest entry:
  `b659a8bccea30df4f800df526319bcbe01f429c3bee2ee8146983933da9cb38b  evidence/polydegree_e3_witnesses_50_100.json`
- Included v0.2 witness SHA-256:
  `b659a8bccea30df4f800df526319bcbe01f429c3bee2ee8146983933da9cb38b`
- Current v0.3 witness SHA-256:
  `b659a8bccea30df4f800df526319bcbe01f429c3bee2ee8146983933da9cb38b`

The two JSON files are required to compare byte-for-byte during Stage 2.5
validation.  This provenance statement does not turn the producer-side
comparison into unaffiliated reproduction.
