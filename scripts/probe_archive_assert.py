#!/usr/bin/env python3
"""Demonstrate the v0.2.0 verifier's optimized-mode assert gap.

The archive module is loaded only for this diagnostic.  Its cached g-term
builder is replaced with a deliberately non-divisible numerator.  Normal
Python rejects it at the proof-critical assert; python -O silently floor-divides
the value.  This probe does not modify the archive.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from types import ModuleType


def load_module(path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location("archive_witness_verifier_probe", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive-verifier", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    module = load_module(args.archive_verifier)
    # For d=1 the archive divides evaluated numerator sums by q=d+1=2.
    # The injected constant numerator 1 is deliberately not divisible by 2.
    module.g_terms = lambda _d: ((0, 0, 0, 1),)
    assertion_triggered = False
    returned = None
    try:
        returned = module.eval_g_and_derivatives(1, 0, 0, 5)
    except AssertionError:
        assertion_triggered = True

    expected = assertion_triggered if __debug__ else not assertion_triggered
    silent_floor_division = not assertion_triggered and returned == (0, 0, 0)
    report = {
        "schema": "irreducible-norms.archive-assert-fragility-probe.v1",
        "python_optimization_level": sys.flags.optimize,
        "debug_mode": __debug__,
        "injected_numerator": 1,
        "required_divisor": 2,
        "assertion_triggered": assertion_triggered,
        "returned": list(returned) if returned is not None else None,
        "silent_floor_division_observed": silent_floor_division,
        "probe_status": "PASS" if expected else "FAIL",
        "interpretation": (
            "normal mode rejects the injected non-integral coefficient"
            if assertion_triggered
            else "optimized mode removes the guard and accepts floor-divided data"
        ),
    }
    print("Archive assert fragility probe")
    print(f"Optimization level: {sys.flags.optimize}")
    print(f"Assertion triggered: {assertion_triggered}")
    print(f"Silent floor division observed: {silent_floor_division}")
    print(f"Probe status: {report['probe_status']}")
    if args.report is not None:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    return 0 if report["probe_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
