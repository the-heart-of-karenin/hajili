"""Tiny symbolic set-geometry probe, not a terminal-orientation census.

For four atoms, asks whether a minimal nonempty source-free cross-free
family without complementary row pairs can have a proper terminal SCC
in its ALL-private-witness digraph. It chooses the maximal physical
ordered-pair set compatible with a proposed terminal SCC. Completeness
of this maximal-choice reduction is stated in the output note.
"""
from itertools import combinations
import json
from pathlib import Path

n = 4
whole = (1 << n) - 1
shores = list(range(1, whole))


def cross(x, y):
    return bool(x & y) and bool(x & ~y & whole) and bool(y & ~x & whole) and bool(whole & ~(x | y))


def sourcefree(s, edge_data):
    return all(not (p & s) or bool(neg & s) for _, _, neg, p in edge_data)


checked = 0
families = 0
counterexample = None
for size in range(2, len(shores) + 1):
    for rows in combinations(shores, size):
        if any(x == whole ^ y or cross(x, y) for x, y in combinations(rows, 2)):
            continue
        families += 1
        full = (1 << size) - 1
        raw = []
        for u in range(n):
            for v in range(n):
                if u == v:
                    continue
                neg = sum(1 << i for i, x in enumerate(rows) if x >> u & 1 and not (x >> v & 1))
                pos = sum(1 << i for i, x in enumerate(rows) if x >> v & 1 and not (x >> u & 1))
                if neg and pos:
                    raw.append((u, v, neg, pos))
        for c in range(1, full):
            # These are all non-source edges, except forbidden singleton-
            # negative witnesses which would create an outgoing private arc.
            edges = [e for e in raw if not (e[2].bit_count() == 1 and e[2] & c and e[3] & (full ^ c))]
            if any(not any(neg == 1 << i for _, _, neg, pos in edges) for i in range(size)):
                continue
            checked += 1
            if any(sourcefree(s, edges) for s in range(1, full)):
                continue
            counterexample = {
                "rows": rows,
                "terminal_subset": [rows[i] for i in range(size) if c >> i & 1],
                "edges": [{"u": u, "v": v, "N": [rows[i] for i in range(size) if neg >> i & 1], "P": [rows[i] for i in range(size) if pos >> i & 1]} for u, v, neg, pos in edges],
            }
            break
        if counterexample:
            break
    if counterexample:
        break

result = {
    "ground_size": n,
    "cross_free_no_complement_families": families,
    "FULL_supported_candidate_terminal_splits": checked,
    "counterexample": counterexample,
    "scope": "No MAIN triggers; no residual feasibility or terminal-origin claims. Geometric finite control only.",
    "maximal_choice_justification": "Any counterexample physical set is included in this maximal allowed set. Adding allowed edges cannot create a relative source in full T (all have N nonempty), preserves its proposed terminal private split, and can only destroy source-free proper subsets. FULL support remains available.",
}
out = Path(__file__).resolve().parents[1] / "data" / "guard_scc_geometry_probe.json"
out.write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
