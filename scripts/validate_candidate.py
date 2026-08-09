#!/usr/bin/env python3
"""Fail-closed structural and integrity validator for the Stage 2.5 candidate."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


EXPECTED_VERSION = "0.4.1-candidate"

REQUIRED_MANUSCRIPT_SECTIONS = (
    "# Abstract {.unnumbered}",
    "# Introduction",
    "# Limitations",
    "# Conclusion",
    "# Declarations {.unnumbered}",
    "## Data and code availability",
    "## Ethics statement",
    "## Funding",
    "## Competing interests",
    "## Author contributions (CRediT)",
    "## AI and automated-tool disclosure",
    "# References {.unnumbered}",
)

REQUIRED_BODY_SECTIONS = (
    "## Summary",
    "## Summary for specialists",
    "## Technical summary",
    "## Why this matters",
    "## What is proved—and what is not",
    "## The most valuable next projects",
    "## What is in the evidence package",
)

REQUIRED_CLAIM_STATUSES = {
    "proved_in_manuscript",
    "exact_finite_computation",
    "externally_inherited",
    "open_not_claimed",
    "priority_provisional",
    "not_assessed",
}

FORBIDDEN_OVERCLAIMS = (
    "we prove the Polydegree Conjecture",
    "we prove the all-d",
    "independently reproduced by an unaffiliated",
    "peer-reviewed and accepted",
    "REF 4-star output",
)

EXPECTED_WITNESS_SHA256 = (
    "b659a8bccea30df4f800df526319bcbe01f429c3bee2ee8146983933da9cb38b"
)
EXPECTED_UPSTREAM_SHA256 = (
    "e51af558a067c28847219a788f8dd4d28de4a6e9bc3b8d00c5ecab2c3b123334"
)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"cannot parse {path.name}: {exc}")
        return {}


def bib_keys(text: str) -> set[str]:
    return set(re.findall(r"^@\w+\{([^,]+),", text, flags=re.MULTILINE))


def citation_keys(text: str) -> set[str]:
    found: set[str] = set()
    for group in re.findall(r"\[([^\]]*@[A-Za-z0-9_:-]+[^\]]*)\]", text):
        found.update(re.findall(r"@([A-Za-z0-9_:-]+)", group))
    return found


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def pdf_pages(path: Path, errors: list[str]) -> int | None:
    try:
        result = subprocess.run(
            ["pdfinfo", str(path)],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        fail(errors, f"pdfinfo failed for {path.name}: {exc}")
        return None
    match = re.search(r"^Pages:\s+(\d+)$", result.stdout, flags=re.MULTILINE)
    if not match:
        fail(errors, f"cannot determine page count for {path.name}")
        return None
    return int(match.group(1))


def validate(root: Path, publication_ready: bool) -> dict[str, object]:
    errors: list[str] = []
    checks: list[dict[str, object]] = []

    required_files = (
        "ACADEMIC_INTEGRITY_REPORT.md",
        "AI_RESEARCH_FAILURE_MODE_AUDIT.md",
        "CORRECTION_LOG.md",
        "INTEGRITY_AUDIT.json",
        "integrity_evidence/citation/BUILD_LAYER_READBACK.md",
        "integrity_evidence/citation/corrected_citation_ledger.json",
        "integrity_evidence/originality/CORRECTION_ROUND_1.md",
        "integrity_evidence/originality/correction_round_1.json",
        "integrity_evidence/originality/originality_audit.json",
        "integrity_evidence/originality/sample_plan.json",
        "integrity_evidence/assurance/STAGE2_5_ASSURANCE_AUDIT.md",
        "integrity_evidence/assurance/stage2_5_assurance_audit.json",
        "integrity_evidence/scope/integrity_scope.json",
        "integrity_evidence/scope/integrity_scope_optimized.json",
        "MANUSCRIPT.md",
        "BILINGUAL_ABSTRACTS.md",
        "EVIDENCE_PRESS_BODY.md",
        "EVIDENCE_PRESS_META.json",
        "CLAIM_STATUS.json",
        "CITATION_AUDIT.md",
        "STATUS.md",
        "STAGE2_5_CHECKPOINT.md",
        "ASSURANCE.md",
        "PROVENANCE.md",
        "LICENSE_STATUS.md",
        "references.bib",
        "build/main.tex",
        "build/main.pdf",
        "evidence/assurance/independent_verification_report.json",
        "evidence/assurance/independent_verification_report_optimized.json",
        "evidence/assurance/mutation_report.json",
        "evidence/assurance/mutation_report_optimized.json",
        "evidence/geometry/results_2_20.json",
        "evidence/geometry/results_2_20_optimized.json",
        "evidence/geometry/boundary_results_2_200.json",
        "evidence/geometry/boundary_results_2_200_optimized.json",
        "evidence/geometry/uniform_squarefreeness/PROOF_MEMO.md",
        "evidence/geometry/uniform_squarefreeness/results_2_300.json",
        "evidence/geometry/uniform_squarefreeness/results_2_300_optimized.json",
        "evidence/upstream/polydegree_e3_witnesses_50_100.json",
        "scripts/verify_boundary_hypergeom.py",
        "source_records/proof_referee/arxiv-2309.10970v3.pdf",
        "source_records/proof_referee/arxiv-2404.11479v2.pdf",
        "source_records/stage1_v0.2/PROVENANCE_NOTE.md",
        "source_records/stage1_v0.2/polydegree_e3_witnesses_50_100.json",
        "source_records/upstream/polydegree-hensel-certificates-e3-v0.3.0.zip",
    )
    missing = [name for name in required_files if not (root / name).is_file()]
    if missing:
        fail(errors, "missing required files: " + ", ".join(missing))
    checks.append({"check": "required_files", "passed": not missing, "count": len(required_files)})

    manuscript_path = root / "MANUSCRIPT.md"
    manuscript = manuscript_path.read_text(encoding="utf-8") if manuscript_path.is_file() else ""
    missing_sections = [s for s in REQUIRED_MANUSCRIPT_SECTIONS if s not in manuscript]
    if missing_sections:
        fail(errors, "missing manuscript sections: " + ", ".join(missing_sections))
    checks.append({"check": "manuscript_sections", "passed": not missing_sections})

    pending_declarations = (
        "An accountable-author funding attestation has not yet been supplied.",
        "An accountable-author competing-interest attestation has not yet been",
        "An accountable-author CRediT attestation has not yet been supplied.",
    )
    unsupported_declarations = (
        "This research received no specific grant",
        "The author declares no known competing",
        "**Anonymous:** Conceptualization",
    )
    missing_pending = [text for text in pending_declarations if text not in manuscript]
    unsupported_present = [text for text in unsupported_declarations if text in manuscript]
    if missing_pending:
        fail(errors, "pending author-attestation language is incomplete")
    if unsupported_present:
        fail(errors, "unsupported author declarations are still asserted")
    checks.append(
        {
            "check": "author_attestation_boundary",
            "passed": not missing_pending and not unsupported_present,
            "pending_attestations": ["funding", "competing interests", "CRediT"],
        }
    )

    body_path = root / "EVIDENCE_PRESS_BODY.md"
    body = body_path.read_text(encoding="utf-8") if body_path.is_file() else ""
    missing_body_sections = [s for s in REQUIRED_BODY_SECTIONS if s not in body]
    if missing_body_sections:
        fail(errors, "missing Evidence Press sections: " + ", ".join(missing_body_sections))
    checks.append({"check": "evidence_press_sections", "passed": not missing_body_sections})

    combined = manuscript + "\n" + body
    overclaims = [phrase for phrase in FORBIDDEN_OVERCLAIMS if phrase.lower() in combined.lower()]
    if overclaims:
        fail(errors, "forbidden overclaim phrases found: " + ", ".join(overclaims))
    if "Conjecture 7.4 (uniform affine smoothness) [Open]" not in manuscript:
        fail(errors, "uniform affine statement is not explicitly labelled Open")
    if "Theorem 7.2 (uniform boundary squarefreeness) [Proved]" not in manuscript:
        fail(errors, "uniform boundary-squarefreeness theorem is missing or mislabelled")
    checks.append({"check": "claim_language", "passed": not overclaims})

    bib_path = root / "references.bib"
    bibliography = bib_path.read_text(encoding="utf-8") if bib_path.is_file() else ""
    defined = bib_keys(bibliography)
    used = citation_keys(manuscript)
    undefined = sorted(used - defined)
    unused = sorted(defined - used)
    if undefined:
        fail(errors, "undefined citation keys: " + ", ".join(undefined))
    if unused:
        fail(errors, "unused bibliography keys: " + ", ".join(unused))
    checks.append(
        {
            "check": "citation_closure",
            "passed": not undefined and not unused,
            "used": sorted(used),
            "defined": sorted(defined),
        }
    )
    citation_repairs_ok = (
        "finite free convolution. Applications to multiple orthogonality" in bibliography
        and "Release 1.2.7 of 2026-06-15" in bibliography
        and bibliography.count("title        = {The Stacks project}") == 2
        and bibliography.count("year         = {2026}") == 3
        and "Tag 00HP, Lemma 10.39.15" in bibliography
        and "Tag 00FV, Theorem 10.34.1" in bibliography
        and "https://arxiv.org/abs/2404.11479v2" in bibliography
        and "https://arxiv.org/abs/2309.10970v3" in bibliography
        and "https://dlmf.nist.gov/15.8.E1" in manuscript
        and "https://dlmf.nist.gov/18.5.E7" in manuscript
        and "https://dlmf.nist.gov/18.16.E1" in manuscript
        and "finite free convolution: Applications to multiple orthogonality"
        not in bibliography
        and "not known necessary" not in manuscript
    )
    if not citation_repairs_ok:
        fail(errors, "Stage 2.5 exact-metadata citation repairs are absent or regressed")
    checks.append({"check": "citation_metadata_repairs", "passed": citation_repairs_ok})

    claims_obj = load_json(root / "CLAIM_STATUS.json", errors)
    claims = claims_obj.get("claims", []) if isinstance(claims_obj, dict) else []
    ids = [c.get("id") for c in claims if isinstance(c, dict)]
    if not claims or len(ids) != len(set(ids)) or any(not i for i in ids):
        fail(errors, "claim ledger is empty or has missing/duplicate ids")
    statuses = {
        status
        for claim in claims
        if isinstance(claim, dict)
        for status in claim.get("status", [])
        if isinstance(status, str)
    }
    missing_statuses = sorted(REQUIRED_CLAIM_STATUSES - statuses)
    if missing_statuses:
        fail(errors, "claim ledger misses status classes: " + ", ".join(missing_statuses))
    claims_by_id = {
        claim.get("id"): claim.get("claim")
        for claim in claims
        if isinstance(claim, dict) and isinstance(claim.get("id"), str)
    }
    safe_claim_polarity = (
        claims_by_id.get("N1")
        == "A bounded collision search found no prior derivative-Jacobian packaging; novelty and priority are not established."
        and claims_by_id.get("X1")
        == "No independent reproduction, formal verification, external specialist review or peer review has been established."
    )
    if not safe_claim_polarity:
        fail(errors, "N1/X1 machine-readable claim polarity is unsafe")
    checks.append(
        {
            "check": "claim_ledger",
            "passed": not missing_statuses and safe_claim_polarity,
            "claims": len(claims),
            "safe_priority_and_assurance_polarity": safe_claim_polarity,
        }
    )

    integrity_obj = load_json(root / "INTEGRITY_AUDIT.json", errors)
    integrity_modes = (
        integrity_obj.get("ai_failure_modes", {})
        if isinstance(integrity_obj, dict)
        else {}
    )
    final_integrity_ok = (
        isinstance(integrity_obj, dict)
        and integrity_obj.get("version") == EXPECTED_VERSION
        and integrity_obj.get("verdict") == "PASS_WITH_NOTES"
        and integrity_obj.get("unresolved_serious") == 0
        and integrity_obj.get("unresolved_medium") == 0
        and integrity_obj.get("phase_a", {}).get("metadata_and_target_passed") == 9
        and integrity_obj.get("phase_b", {}).get("passed") == 14
        and integrity_obj.get("phase_d", {}).get("sampled_paragraphs") == 40
        and integrity_obj.get("phase_d", {}).get("eligible_paragraphs") == 132
        and integrity_obj.get("phase_e", {}).get("claims_checked") == 16
        and integrity_obj.get("phase_e", {}).get("MAJOR_DISTORTION") == 0
        and integrity_obj.get("phase_e", {}).get("UNVERIFIABLE") == 0
        and len(integrity_modes) == 7
        and all("SUSPECTED" not in str(value) for value in integrity_modes.values())
        and all("INSUFFICIENT" not in str(value) for value in integrity_modes.values())
    )
    if not final_integrity_ok:
        fail(errors, "machine-readable Stage 2.5 integrity disposition is not passing")
    checks.append(
        {
            "check": "stage2.5_integrity_disposition",
            "passed": final_integrity_ok,
            "verdict": integrity_obj.get("verdict")
            if isinstance(integrity_obj, dict)
            else None,
        }
    )

    citation_audit_obj = load_json(
        root / "integrity_evidence/citation/corrected_citation_ledger.json", errors
    )
    citation_audit_ok = (
        isinstance(citation_audit_obj, dict)
        and citation_audit_obj.get("verdict", {}).get(
            "combined_citation_integrity_gate"
        )
        == "PASS"
        and citation_audit_obj.get("summary", {}).get("record_pass") == 9
        and citation_audit_obj.get("summary", {}).get("citation_context_pass") == 14
    )
    if not citation_audit_ok:
        fail(errors, "corrected citation audit is not a 9/9 and 14/14 PASS")
    checks.append({"check": "corrected_citation_audit", "passed": citation_audit_ok})

    originality_audit_obj = load_json(
        root / "integrity_evidence/originality/correction_round_1.json", errors
    )
    originality_coverage = (
        originality_audit_obj.get("current_phase_d_coverage", {})
        if isinstance(originality_audit_obj, dict)
        else {}
    )
    originality_audit_ok = (
        isinstance(originality_audit_obj, dict)
        and originality_audit_obj.get("verdict") == "PASS"
        and originality_coverage.get("sampled_paragraphs") == 40
        and originality_coverage.get("total_body_paragraphs") == 132
        and originality_coverage.get("major_sections_covered") == 12
        and originality_audit_obj.get("blocking_defects") == []
    )
    if not originality_audit_ok:
        fail(errors, "current-candidate originality correction audit is not passing")
    checks.append({"check": "current_originality_audit", "passed": originality_audit_ok})

    independent_paths = (
        root / "evidence/assurance/independent_verification_report.json",
        root / "evidence/assurance/independent_verification_report_optimized.json",
    )
    independent_reports = [load_json(path, errors) for path in independent_paths]
    independent_ok = all(
        isinstance(report, dict)
        and report.get("overall_status") == "PASS"
        and report.get("symbolic_checks_passed") == 10
        and report.get("symbolic_checks_total") == 10
        and report.get("witness_verification", {}).get("status") == "PASS"
        and report.get("witness_verification", {}).get("rows_passed") == 51
        and report.get("witness_verification", {}).get("rows_total") == 51
        for report in independent_reports
    )
    independent_bytes_equal = all(path.is_file() for path in independent_paths) and (
        independent_paths[0].read_bytes() == independent_paths[1].read_bytes()
    )
    if not independent_ok:
        fail(errors, "independent verifier receipts do not record 10/10 and 51/51 PASS")
    if not independent_bytes_equal:
        fail(errors, "ordinary and optimized independent-verifier receipts differ")
    checks.append(
        {
            "check": "independent_verifier_receipts",
            "passed": independent_ok and independent_bytes_equal,
            "symbolic": "10/10",
            "witnesses": "51/51",
            "ordinary_optimized_byte_identical": independent_bytes_equal,
        }
    )

    mutation_paths = (
        root / "evidence/assurance/mutation_report.json",
        root / "evidence/assurance/mutation_report_optimized.json",
    )
    mutation_reports = [load_json(path, errors) for path in mutation_paths]
    mutations_ok = all(
        isinstance(report, dict)
        and report.get("overall_status") == "PASS"
        and report.get("controls_passed") == 17
        and report.get("controls_total") == 17
        for report in mutation_reports
    )
    if not mutations_ok:
        fail(errors, "mutation receipts do not record 17/17 PASS in both modes")
    checks.append(
        {
            "check": "mutation_receipts",
            "passed": mutations_ok,
            "ordinary": "17/17",
            "optimized": "17/17",
        }
    )

    geometry_pairs = (
        (
            root / "evidence/geometry/results_2_20.json",
            root / "evidence/geometry/results_2_20_optimized.json",
            ("all_affine_lengths_match_floor_d_d1_over_6",
             "all_affine_schemes_disjoint_from_g_d2",
             "all_affine_schemes_reduced_by_jacobian_criterion",
             "all_newton_mixed_volumes_match_floor_d_d1_over_6",
             "all_weighted_projective_pairs_proper"),
            [2, 20],
        ),
        (
            root / "evidence/geometry/boundary_results_2_200.json",
            root / "evidence/geometry/boundary_results_2_200_optimized.json",
            ("all_torus_pairs_coprime", "all_torus_polynomials_squarefree"),
            [2, 200],
        ),
    )
    geometry_ok = True
    geometry_byte_equal = True
    for ordinary, optimized, flags, expected_range in geometry_pairs:
        ordinary_report = load_json(ordinary, errors)
        optimized_report = load_json(optimized, errors)
        pair_ok = all(
            isinstance(report, dict)
            and report.get("range") == expected_range
            and all(report.get(flag) is True for flag in flags)
            for report in (ordinary_report, optimized_report)
        )
        pair_equal = ordinary.is_file() and optimized.is_file() and (
            ordinary.read_bytes() == optimized.read_bytes()
        )
        geometry_ok = geometry_ok and pair_ok
        geometry_byte_equal = geometry_byte_equal and pair_equal
    if not geometry_ok:
        fail(errors, "geometry receipts do not record the claimed bounded exact results")
    if not geometry_byte_equal:
        fail(errors, "ordinary and optimized geometry receipts differ")
    checks.append(
        {
            "check": "geometry_receipts",
            "passed": geometry_ok and geometry_byte_equal,
            "affine_range": [2, 20],
            "boundary_range": [2, 200],
            "ordinary_optimized_byte_identical": geometry_byte_equal,
        }
    )

    squarefree_paths = (
        root / "evidence/geometry/uniform_squarefreeness/results_2_300.json",
        root
        / "evidence/geometry/uniform_squarefreeness/results_2_300_optimized.json",
    )
    squarefree_reports = [load_json(path, errors) for path in squarefree_paths]
    squarefree_ok = all(
        isinstance(report, dict)
        and report.get("schema") == "polydegree.e3.boundary-hypergeom.v1"
        and report.get("ranges", {}).get("n_identity_and_squarefree") == [2, 301]
        and report.get("ranges", {}).get("d_adjacent") == [2, 300]
        and report.get("checked_identities", {}).get("all_reciprocal_3f2") is True
        and report.get("checked_identities", {}).get("all_convolution_coefficients")
        is True
        and report.get("checked_identities", {}).get(
            "all_jacobi_parameter_inequalities"
        )
        is True
        and report.get("finite_evidence", {}).get("all_P_n_squarefree_over_QQ")
        is True
        and all(not failures for failures in report.get("failures", {}).values())
        for report in squarefree_reports
    )
    squarefree_bytes_equal = all(path.is_file() for path in squarefree_paths) and (
        squarefree_paths[0].read_bytes() == squarefree_paths[1].read_bytes()
    )
    proof_memo_path = root / "evidence/geometry/uniform_squarefreeness/PROOF_MEMO.md"
    proof_memo = (
        proof_memo_path.read_text(encoding="utf-8") if proof_memo_path.is_file() else ""
    )
    proof_repair_recorded = (
        "Proposition 2.17" in proof_memo
        and "We deliberately do not use the strict" in proof_memo
        and "logarithmic-mesh" in proof_memo
    )
    if not squarefree_ok:
        fail(errors, "uniform-squarefreeness receipts fail their semantic gates")
    if not squarefree_bytes_equal:
        fail(errors, "ordinary and optimized uniform-squarefreeness receipts differ")
    if not proof_repair_recorded:
        fail(errors, "uniform-squarefreeness proof memo does not retain the referee repair")
    checks.append(
        {
            "check": "uniform_squarefreeness_receipts",
            "passed": squarefree_ok and squarefree_bytes_equal and proof_repair_recorded,
            "identity_and_squarefree_range": [2, 301],
            "adjacent_evidence_range": [2, 300],
            "ordinary_optimized_byte_identical": squarefree_bytes_equal,
            "referee_repair_recorded": proof_repair_recorded,
        }
    )

    witness_path = root / "evidence/upstream/polydegree_e3_witnesses_50_100.json"
    stage1_witness_path = (
        root
        / "source_records/stage1_v0.2/polydegree_e3_witnesses_50_100.json"
    )
    upstream_path = (
        root
        / "source_records/upstream/polydegree-hensel-certificates-e3-v0.3.0.zip"
    )
    witness_hash = sha256(witness_path) if witness_path.is_file() else None
    stage1_witness_hash = (
        sha256(stage1_witness_path) if stage1_witness_path.is_file() else None
    )
    upstream_hash = sha256(upstream_path) if upstream_path.is_file() else None
    source_hashes_ok = (
        witness_hash == EXPECTED_WITNESS_SHA256
        and stage1_witness_hash == EXPECTED_WITNESS_SHA256
        and witness_path.is_file()
        and stage1_witness_path.is_file()
        and witness_path.read_bytes() == stage1_witness_path.read_bytes()
        and upstream_hash == EXPECTED_UPSTREAM_SHA256
    )
    if not source_hashes_ok:
        fail(errors, "frozen witness or upstream archive hash does not match provenance")
    checks.append(
        {
            "check": "frozen_source_hashes",
            "passed": source_hashes_ok,
            "witness_sha256": witness_hash,
            "stage1_v0.2_witness_sha256": stage1_witness_hash,
            "v0.2_v0.3_byte_identical": (
                witness_path.is_file()
                and stage1_witness_path.is_file()
                and witness_path.read_bytes() == stage1_witness_path.read_bytes()
            ),
            "upstream_archive_sha256": upstream_hash,
        }
    )

    meta_obj = load_json(root / "EVIDENCE_PRESS_META.json", errors)
    if not isinstance(meta_obj, dict):
        fail(errors, "metadata template is not a JSON object")
        meta_obj = {}
    expected_publication_state = "publication-ready" if publication_ready else "pre-deposit-template"
    if meta_obj.get("publicationState") != expected_publication_state:
        fail(errors, f"metadata publicationState must be {expected_publication_state}")
    if meta_obj.get("status") != "unrefereed-candidate":
        fail(errors, "metadata status must remain unrefereed-candidate")
    versions = {
        "manuscript": EXPECTED_VERSION in manuscript,
        "claim_ledger": isinstance(claims_obj, dict)
        and claims_obj.get("version") == EXPECTED_VERSION,
        "metadata": meta_obj.get("version") == EXPECTED_VERSION,
        "readme": EXPECTED_VERSION
        in (root / "README.md").read_text(encoding="utf-8"),
        "status": EXPECTED_VERSION
        in (root / "STATUS.md").read_text(encoding="utf-8"),
        "reconciliation": EXPECTED_VERSION
        in (root / "RECONCILIATION_REPORT.md").read_text(encoding="utf-8"),
    }
    if not all(versions.values()):
        fail(errors, "candidate components are not all bound to the Stage 2.5 version")
    checks.append(
        {
            "check": "version_consistency",
            "passed": all(versions.values()),
            "expected": EXPECTED_VERSION,
            "components": versions,
        }
    )
    provenance = meta_obj.get("provenance", {})
    ai_boundary_ok = (
        isinstance(provenance, dict)
        and provenance.get("aiGenerated") is True
        and provenance.get("aiAssisted") is True
        and "language-model" in provenance.get("disclosure", "")
        and "drafting" in provenance.get("disclosure", "")
    )
    if not ai_boundary_ok:
        fail(errors, "AI provenance flags do not match the explicit disclosure")
    checks.append({"check": "ai_provenance_consistency", "passed": ai_boundary_ok})
    one_line = meta_obj.get("oneLine", "")
    open_theorem_boundary_ok = (
        isinstance(one_line, str)
        and "uniform e=3 affine theorem remains open" in one_line
        and "uniform e=3 theorem remains open" not in one_line
    )
    if not open_theorem_boundary_ok:
        fail(errors, "metadata oneLine does not distinguish the open affine theorem")
    checks.append(
        {"check": "open_theorem_metadata_boundary", "passed": open_theorem_boundary_ok}
    )
    assurance = meta_obj.get("assurance", {})
    if not isinstance(assurance, dict):
        fail(errors, "metadata assurance is not an object")
        assurance = {}
    for key in ("independentRerun", "formalVerification", "specialistReview", "editorialPeerReview"):
        if assurance.get(key, {}).get("state") != "not-assessed":
            fail(errors, f"assurance.{key} must be not-assessed at Stage 2")

    publication_fields = (
        "datePublished",
        "doi",
        "pdfUrl",
        "repoUrl",
        "releaseUrl",
        "license",
    )
    absent_publication_fields = [key for key in publication_fields if not meta_obj.get(key)]
    if publication_ready and absent_publication_fields:
        fail(errors, "publication-ready mode requires: " + ", ".join(absent_publication_fields))
    if not publication_ready and not absent_publication_fields:
        fail(errors, "Stage 2 template unexpectedly contains all publication identifiers")
    checks.append(
        {
            "check": "metadata_boundary",
            "passed": not publication_ready and bool(absent_publication_fields)
            or publication_ready and not absent_publication_fields,
            "publication_ready_requested": publication_ready,
            "absent_publication_fields": absent_publication_fields,
        }
    )

    pages = pdf_pages(root / "build/main.pdf", errors) if (root / "build/main.pdf").is_file() else None
    if pages is not None and pages < 10:
        fail(errors, f"candidate PDF unexpectedly short: {pages} pages")
    checks.append({"check": "pdf_structure", "passed": pages is not None and pages >= 10, "pages": pages})

    forbidden_chars = {"U+2011": "\u2011", "NUL": "\x00"}
    present_chars = [name for name, char in forbidden_chars.items() if char in combined]
    if present_chars:
        fail(errors, "forbidden source characters found: " + ", ".join(present_chars))
    checks.append({"check": "source_characters", "passed": not present_chars})

    return {
        "candidate": "smooth-point-certificates-polydegree-containments",
        "version": EXPECTED_VERSION,
        "mode": "publication-ready" if publication_ready else "stage2.5-template",
        "checks": checks,
        "failures": errors,
        "overall_status": "PASS" if not errors else "FAIL",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--publication-ready", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    report = validate(root, args.publication_ready)
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(payload, encoding="utf-8")
    sys.stdout.write(payload)
    return 0 if report["overall_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
