"""Audit interval algebra and one specified 14-edge contraction witness."""
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def interval_one(k, ea, eb, ra, rb):
    return (max(0, k - ra, rb - eb),
            min(k + 1, k + 1 + ea - ra, rb + 1))


def interval_two(k, ra, rb, rc):
    return (max(0, k - ra, rb - 1, k - rc),
            min(k + 1, k + 2 - ra, rb + 1, k + 2 - rc))


def check_profiles():
    summaries = []
    for k in range(2, 7):
        for ea, eb in ((3, 0), (2, 0), (2, 1), (1, 1)):
            profiles = {}
            for ra in range(k + ea + 1):
                for rb in range(k + eb + 1):
                    if k <= ra + rb <= k + ea + eb:
                        bounds = interval_one(k, ea, eb, ra, rb)
                        assert bounds[1] - bounds[0] >= 1
                        profiles[(ra, rb)] = bounds
            adjacencies = 0
            for p, bounds in profiles.items():
                for i in range(2):
                    q = tuple(value + (j == i) for j, value in enumerate(p))
                    if q in profiles:
                        other = profiles[q]
                        assert max(bounds[0], other[0]) <= min(bounds[1], other[1])
                        adjacencies += 1
            summaries.append({"kind": "one_exception", "k": k,
                              "excess_pair": [ea, eb], "profiles": len(profiles),
                              "adjacent_profile_checks": adjacencies})
        profiles = {}
        for ra, rb, rc in itertools.product(range(k + 2), repeat=3):
            if (k <= ra + rb <= k + 2 and abs(ra - rc) <= 1
                    and k <= rb + rc <= k + 2):
                bounds = interval_two(k, ra, rb, rc)
                assert bounds[1] - bounds[0] >= 1
                profiles[(ra, rb, rc)] = bounds
        adjacencies = 0
        for p, bounds in profiles.items():
            for i in range(3):
                q = tuple(value + (j == i) for j, value in enumerate(p))
                if q in profiles:
                    other = profiles[q]
                    assert max(bounds[0], other[0]) <= min(bounds[1], other[1])
                    adjacencies += 1
        summaries.append({"kind": "two_exception_high", "k": k,
                          "profiles": len(profiles), "adjacent_profile_checks": adjacencies})
    return summaries


def cut_rows(vertices, arcs, flips):
    rows = []
    for mask in range(1, (1 << len(vertices)) - 1):
        shore = {v for i, v in enumerate(vertices) if mask >> i & 1}
        out = inc = 0
        for label, u, v in arcs:
            if label in flips:
                u, v = v, u
            out += u in shore and v not in shore
            inc += u not in shore and v in shore
        rows.append({"shore": sorted(shore), "out": out, "in": inc})
    return rows


def specified_witness():
    vertices = ("a", "b", "c", "d", "e")
    arcs = [(f"ab{i}", "a", "b") for i in range(3)]
    arcs += [(f"ac{i}", "c", "a") for i in range(3)]
    arcs += [("bd", "b", "d"), ("be", "b", "e"), ("eb", "e", "b"),
             ("ce", "c", "e"), ("dc0", "d", "c"), ("dc1", "d", "c"),
             ("de", "d", "e"), ("ed", "e", "d")]
    base_rows = cut_rows(vertices, arcs, set())
    lam = min(r["out"] + r["in"] for r in base_rows)
    assert lam == 5
    quotient = [(label, "r" if u in {"a", "b"} else u,
                 "r" if v in {"a", "b"} else v)
                for label, u, v in arcs if not label.startswith("ab")]
    fibers = []
    for outside_flips, expected in ((set(), {2, 3}), ({"ac0"}, {1, 2, 3})):
        qrows = cut_rows(("r", "c", "d", "e"), quotient, outside_flips)
        assert all(min(r["out"], r["in"]) >= 2 for r in qrows)
        states = []
        legal_masks = set()
        for mask in range(8):
            flips = outside_flips | {f"ab{i}" for i in range(3) if mask >> i & 1}
            rows = cut_rows(vertices, arcs, flips)
            legal = all(min(r["out"], r["in"]) >= 2 for r in rows)
            u = 3 - mask.bit_count()
            assert legal == (u in expected)
            if legal:
                legal_masks.add(mask)
            states.append({"internal_flip_mask": mask, "u": u,
                           "legal": legal, "global_cut_rows": rows})
        reached = {next(iter(legal_masks))}
        stack = list(reached)
        while stack:
            mask = stack.pop()
            for i in range(3):
                other = mask ^ (1 << i)
                if other in legal_masks and other not in reached:
                    reached.add(other)
                    stack.append(other)
        assert reached == legal_masks
        fibers.append({"outside_flips": sorted(outside_flips),
                       "quotient_cut_rows": qrows, "expected_interval": sorted(expected),
                       "all_8_internal_assignments": states,
                       "fiber_connected": True})
    return {"kind": "two_specified_quotient_states_with_8_internal_assignments_each",
            "k": 2, "lambda": lam, "labelled_arcs": arcs,
            "quotient_transition_copy": "ac0", "fibers": fibers,
            "common_weights": [2, 3]}


def main():
    summaries = check_profiles()
    raw = {"kind": "proof_profile_audit_not_graph_or_orientation_census",
           "profile_superset_note": "Only the proof inequalities are imposed; not all profiles claimed realizable.",
           "summaries": summaries, "specified_14_edge_witness": specified_witness()}
    output = ROOT / "data" / "five_vertex_next_layer_raw.json"
    output.write_text(json.dumps(raw, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    hashes = {"algorithm": "SHA256", "files": {
        Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        output.name: hashlib.sha256(output.read_bytes()).hexdigest()}}
    (ROOT / "data" / "five_vertex_next_layer_sha256.json").write_text(
        json.dumps(hashes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": "PASS", "k_values": list(range(2, 7)),
                      "profile_inequalities": sum(s["profiles"] for s in summaries),
                      "adjacent_profile_checks": sum(s["adjacent_profile_checks"] for s in summaries),
                      "specified_full_G_states": 16,
                      "all_full_G_cuts_per_state": 30}))


if __name__ == "__main__":
    main()
