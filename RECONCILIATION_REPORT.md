# Upstream reconciliation report

**Reconciliation date:** 9 August 2026  
**Upstream state:** `polydegree-hensel-certificates-e3-v0.3.0`  
**Stage 2.5 derivative:** `0.4.1-candidate`  
**Frozen Stage 2 ancestor:** `0.4.0-candidate`

## Source identity

The current source archive discovered in `0PROCESSED/polydegree-hensel` is
included unchanged at
`source_records/upstream/polydegree-hensel-certificates-e3-v0.3.0.zip`.
Its SHA-256 is:

```text
e51af558a067c28847219a788f8dd4d28de4a6e9bc3b8d00c5ecab2c3b123334
```

The frozen 51-row witness JSON has SHA-256:

```text
b659a8bccea30df4f800df526319bcbe01f429c3bee2ee8146983933da9cb38b
```

That witness file is byte-identical to the corpus audited from the earlier
v0.2.0 package.  The earlier JSON bytes are included under
`source_records/stage1_v0.2/`, and the Stage 2.5 validator checks both hashes
and direct byte identity.  The new manuscript is therefore reconciled to the
current upstream release without silently replacing its source evidence.

## Checks completed

- Upstream v0.3.0 manifest: 38/38 files matched.
- Upstream verifier: 51/51 rows passed under ordinary and optimized Python.
- No-import replacement verifier on the v0.3.0 data: 10/10 symbolic gates
  and 51/51 witness relations passed in both modes.
- Replacement-verifier reports are byte-identical across ordinary and
  optimized Python.
- Sixteen mutation or negative controls and one positive
  bad-characteristic regression passed in both modes.

The reconciliation receipts are retained in `evidence/reconciliation/`; the
replacement receipts are retained in `evidence/assurance/`.

## Retained upstream defect

The upstream verifier's coefficient divisibility guard is implemented with a
proof-critical Python `assert`. An injected non-integral numerator is rejected
in ordinary mode but slips past that guard under `python -O` and reaches floor
division. This is a latent fail-open risk in the verifier, not evidence that a
current frozen witness is false. The included replacement verifier uses an
explicit exception, and its negative control remains active in both modes.

## Boundary of this reconciliation

These checks establish source identity, internal replay and robustness of the
included replacement path. They do not establish independent reproduction,
formal proof verification, mathematical novelty, specialist acceptance,
journal acceptance or a REF grade.
