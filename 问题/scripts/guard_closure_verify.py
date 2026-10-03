"""Tiny exact falsification test for the source-free deletion closure theorem.

The universe has three abstract rows. Test ALL pairs (with repetition) of
signatures with nonempty negative set, and both MAIN-trigger settings.
This verifies a logical algorithm, not terminal-realizability or connectivity.
"""
import hashlib
import itertools
import json
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
ROWS = 3
ALL = (1 << ROWS) - 1


def source_free(retained, edges):
    return all(not ((positive & retained) or main) or (negative & retained)
               for negative, positive, main in edges)


def canonical_maximum(candidate, edges):
    deleted = ALL ^ candidate
    while True:
        enlarged = deleted
        for negative, positive, main in edges:
            if not (negative & ~deleted):
                if main:
                    return None  # No source-free subset of candidate exists.
                enlarged |= positive
        if enlarged == deleted:
            return ALL ^ deleted
        deleted = enlarged


def main():
    start = time.perf_counter()
    signatures = []
    for word in itertools.product((-1, 0, 1), repeat=ROWS):
        negative = sum(1 << i for i, sign in enumerate(word) if sign == -1)
        positive = sum(1 << i for i, sign in enumerate(word) if sign == 1)
        if negative:
            for main in (False, True):
                signatures.append((negative, positive, main))

    systems = candidate_checks = union_checks = 0
    for edges in itertools.combinations_with_replacement(signatures, 2):
        systems += 1
        models = [s for s in range(ALL + 1) if source_free(s, edges)]
        assert ALL in models
        for first in models:
            for second in models:
                union_checks += 1
                assert source_free(first | second, edges)
        for candidate in range(ALL + 1):
            candidate_checks += 1
            feasible = [s for s in models if not (s & ~candidate)]
            expected = None
            if feasible:
                expected = 0
                for state in feasible:
                    expected |= state
                assert expected in feasible
            actual = canonical_maximum(candidate, edges)
            if actual != expected:
                raise RuntimeError((edges, candidate, expected, actual))

    # Explicit failure from the revised archive: rows 0,1,2 are Z1,Z2,Z3.
    example = [(0b001, 0b110, False),
               (0b010, 0b001, False),
               (0b100, 0b001, False)]
    example_models = [s for s in range(8) if source_free(s, example)]
    assert example_models == [0, 7]
    assert canonical_maximum(0b011, example) == 0

    # Intersection failure: either negative guard suffices for row 2.
    intersection_edges = [(0b011, 0b100, False)]
    assert source_free(0b101, intersection_edges)
    assert source_free(0b110, intersection_edges)
    assert not source_free(0b100, intersection_edges)

    report = {
        "classification": "EXACT_FINITE_LOGICAL_ALGORITHM_CHECK; not terminal or graph enumeration",
        "rows": ROWS,
        "signatures": len(signatures),
        "signature_systems": systems,
        "candidate_universe_checks": candidate_checks,
        "union_model_pair_checks": union_checks,
        "status": "PASS",
        "example_source_free_masks": example_models,
        "example_core_mask": 3,
        "example_maximum_inside_core": 0,
        "elapsed_seconds": round(time.perf_counter() - start, 6),
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    DATA.mkdir(exist_ok=True)
    output = DATA / "guard_closure_verify.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if json.loads(output.read_text(encoding="utf-8")) != report:
        raise RuntimeError("Saved output did not round trip")
    checksum = hashlib.sha256(output.read_bytes()).hexdigest()
    (DATA / "guard_closure_verify.sha256").write_text(
        checksum + "  guard_closure_verify.json\n", encoding="ascii")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
