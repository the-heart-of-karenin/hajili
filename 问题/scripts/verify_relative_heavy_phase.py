"""Verify one prescribed HEAVY-birth/clean word; no orientation enumeration."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent
K = 2
A = ("a", "b0", "b1", "c")
V = A + ("r",)
arcs = {}


def add(prefix, tail, head, multiplicity):
    for j in range(multiplicity):
        arcs[f"{prefix}_{j}"] = [tail, head]


add("A_B", "a", "b1", 2)
add("B_A", "b1", "a", 2)
add("A_C", "a", "c", 1)
add("C_A", "c", "a", 3)
add("U_B", "b0", "b1", 2)
add("B_U", "b1", "b0", 4)
add("B_R", "b1", "r", 1)
add("C_R", "c", "r", 1)
add("R_B", "r", "b1", 1)
add("R_C", "r", "c", 2)
initial = {e: ends[:] for e, ends in arcs.items()}
boundary = {e: ends[:] for e, ends in arcs.items() if "r" in ends}


def shores(vertices):
    for mask in range(1, (1 << len(vertices)) - 1):
        yield frozenset(v for j, v in enumerate(vertices) if mask & (1 << j))


def cuts(x):
    outgoing = sum(u in x and v not in x for u, v in arcs.values())
    incoming = sum(u not in x and v in x for u, v in arcs.values())
    return outgoing, incoming


def names(x):
    return sorted(x)


def report(stage):
    global_rows = []
    for x in shores(V):
        out, inc = cuts(x)
        assert out >= K and inc >= K, (stage, names(x), out, inc)
        global_rows.append({"shore": names(x), "out": out, "in": inc})
    out_tight, in_tight = [], []
    residual = []
    for x in shores(A):
        out, inc = cuts(x)
        if out == K:
            out_tight.append(x)
        if inc == K:
            in_tight.append(x)
        r_x = sum(u in x and v == "r" for u, v in arcs.values())
        s_complement = sum(u == "r" and v in set(A) - x for u, v in arcs.values())
        q_x = min(r_x, s_complement)
        y = frozenset(A) - x
        r_y = sum(u in y and v == "r" for u, v in arcs.values())
        s_x = sum(u == "r" and v in x for u, v in arcs.values())
        q_y = min(r_y, s_x)
        h_cut = sum((u in x) != (v in x) for u, v in arcs.values() if "r" not in (u, v))
        mu = h_cut - (K - q_x) - (K - q_y)
        assert mu >= 2, (names(x), mu)
        residual.append({"shore": names(x), "mu": mu})
    tight_union = set(out_tight + in_tight)
    minimal = sorted(
        (x for x in tight_union if not any(y < x for y in tight_union)),
        key=lambda x: (len(x), sorted(x)),
    )
    potential = sum(len(A) - len(x) for x in minimal)
    assert all(arcs[e] == ends for e, ends in boundary.items())
    return {
        "stage": stage,
        "out_tight": [names(x) for x in out_tight],
        "in_tight": [names(x) for x in in_tight],
        "minimal": [names(x) for x in minimal],
        "v": potential,
        "global_cut_rows": global_rows,
        "residual_rows": residual,
    }


states = [report("initial_no_I")]
weak_word = ["B_U_0", "A_B_0", "C_A_0"]
for j, edge in enumerate(weak_word, 1):
    u, v = arcs[edge]
    assert u != "r" and v != "r"
    arcs[edge] = [v, u]
    states.append(report(f"weak_prefix_{j}"))

assert states[0]["minimal"] == [["b0"]]
assert not states[0]["in_tight"]
assert states[0]["v"] == 3
assert sorted(states[3]["minimal"]) == [["a", "c"], ["b0", "b1"]]
assert states[3]["v"] == 4
assert ["a", "c"] in states[3]["out_tight"]
assert ["b0", "b1"] in states[3]["in_tight"]
assert sum("r" in ends and any(v in {"a", "c"} for v in ends) for ends in boundary.values()) == K + 1

# Clean phase: a genuine proper minimal IN source {b0,b1},
# proper minimal OUT sink {a,c}, with selected endpoints b1 and a.
clean_word = ["B_A_0"]
for edge in clean_word:
    u, v = arcs[edge]
    assert (u, v) == ("b1", "a")
    arcs[edge] = [v, u]
    states.append(report("clean_endpoint_strict"))
assert not states[-1]["out_tight"] and not states[-1]["in_tight"]
assert states[-1]["v"] == 0

raw = {
    "purpose": "One prescribed fixed-boundary HEAVY phase certificate, no graph/orientation search",
    "k": K,
    "A": list(A),
    "root": "r",
    "physical_initial_arcs": initial,
    "weak_directed_path": ["c", "a", "b1", "b0"],
    "weak_word_reverse_edge_order": weak_word,
    "clean_word": clean_word,
    "original_label": {"initial": ["b0"], "weak_endpoint": ["b0", "b1"], "strict_endpoint": "dropped"},
    "heavy_label": {"birth": ["a", "c"], "boundary_weight": 3, "strict_endpoint": "dropped"},
    "states": states,
}
output = ROOT / "data" / "relative_heavy_phase_certificate.json"
output.write_text(json.dumps(raw, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
sha_path = ROOT / "data" / "relative_heavy_phase_sha256.json"
sha_path.write_text(json.dumps({
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "raw_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
}, indent=2) + "\n", encoding="utf-8")
print(json.dumps({
    "status": "PASS",
    "vertices": len(V), "physical_edges": len(arcs),
    "prescribed_states": len(states), "global_cuts_per_state": (1 << len(V)) - 2,
    "macro_endpoint_v": [states[j]["v"] for j in (0, 3, 4)],
    "minimum_mu": min(x["mu"] for x in states[0]["residual_rows"]),
    "word_length": len(weak_word) + len(clean_word),
}, ensure_ascii=False))
