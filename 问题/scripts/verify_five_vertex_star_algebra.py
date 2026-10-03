"""Exact symbolic/chain audit plus three specified heavy-triangle states."""
import hashlib
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
V = ("a", "b", "c", "r", "s")


def symbolic_identities():
    da, db, dc, m1, m2, m3, ra, rb, q, t, rc, k = sp.symbols(
        "da db dc m1 m2 m3 ra rb q t rc k")
    W = t + rc
    ra = q + t
    Dac = da + dc - 2 * m2
    Dab = da + db - 2 * m1
    Dabc = Dac + db - 2 * m1 - 2 * m3
    co = m2 - q + rc
    la, ua = k - ra, da - k - ra
    lb, ub = m1 + rb - db + k, m1 + rb - k
    lc, uc = k - W, Dac - k - W
    equations = {
        "b_upper_minus_a_lower": (ub - la, m1 + ra + rb - 2 * k),
        "a_upper_minus_b_lower": (ua - lb, Dab + m1 - 2 * k - ra - rb),
        "b_upper_minus_ac_lower": (ub - lc, m1 + rb + W - 2 * k),
        "ac_upper_minus_b_lower": (uc - lb, Dac + db - m1 - 2 * k - rb - W),
        "a_upper_minus_ac_lower": (ua - lc, da - 2 * k + co - m2),
        "ac_upper_minus_a_lower": (uc - la, da + dc - m2 - 2 * k - co),
        "quotient_abc_degree": (Dabc, da + db + dc - 2 * (m1 + m2 + m3)),
    }
    for label, (left, right) in equations.items():
        assert sp.expand(left - right) == 0, label
    return {label: {"left": str(left), "right": str(right), "difference": 0}
            for label, (left, right) in equations.items()}


def nested_chain():
    chain = ({"a"}, {"a", "c"}, set(V) - {"b"})
    records = []
    for u in V:
        for v in V:
            if u == v or {u, v} == {"a", "b"}:
                continue
            changes = [int(v in X) - int(u in X) for X in chain]
            assert all(x >= 0 for x in changes) or all(x <= 0 for x in changes)
            records.append({"outside_arc": [u, v], "normalized_cut_changes": changes})
    assert len(records) == 18
    return records


def rows(arcs, flips):
    result = []
    for mask in range(1, 31):
        X = {v for i, v in enumerate(V) if mask >> i & 1}
        out = inc = 0
        for label, u, v in arcs:
            if label in flips:
                u, v = v, u
            out += u in X and v not in X
            inc += u not in X and v in X
        result.append({"shore": sorted(X), "out": out, "in": inc})
    return result


def heavy_triangle_control():
    arcs = [("rs0", "r", "s"), ("rs1", "s", "r"),
            ("ra", "r", "a"), ("br", "b", "r"), ("cr", "c", "r"),
            ("as", "a", "s"), ("sb", "s", "b"), ("sc", "s", "c")]
    arcs += [("ab0", "a", "b"), ("ab1", "a", "b"), ("ba", "b", "a"),
             ("bc0", "b", "c"), ("bc1", "b", "c"), ("cb", "c", "b"),
             ("ca0", "c", "a"), ("ca1", "c", "a"), ("ac", "a", "c")]
    states = []
    for flips in (set(), {"ab0"}, {"ab0", "ab1"}):
        table = rows(arcs, flips)
        assert all(min(r["out"], r["in"]) >= 2 for r in table)
        lam = min(r["out"] + r["in"] for r in table)
        assert lam == 5
        legal = []
        for label, _, _ in arcs:
            next_flips = flips ^ {label}
            after = rows(arcs, next_flips)
            if all(min(r["out"], r["in"]) >= 2 for r in after):
                legal.append(label)
        internal = [label for label, u, v in arcs
                    if u in {"a", "b", "c"} and v in {"a", "b", "c"}]
        assert set(legal) & set(internal)
        states.append({"flips": sorted(flips), "cut_rows": table,
                       "legal_physical_copies": legal,
                       "legal_noncritical_copies": sorted(set(legal) & set(internal))})
    return {"kind": "3_specified_states_not_orientation_census", "k": 2,
            "lambda": 5, "edge_count": len(arcs), "labelled_arcs": arcs,
            "states": states, "theoretical_all_H_frozen_contradiction": {
                "atoms_if_H_frozen": 5, "global_source_lower": len(arcs) - 4 * 2,
                "critical_only_legal_upper": 2 * (2 + 1)}}


def main():
    raw = {"symbolic_cross_gap_identities": symbolic_identities(),
           "nested_chain_arc_signs": nested_chain(),
           "heavy_triangle_control": heavy_triangle_control(),
           "kind": "exact_symbolic_and_prescribed_controls"}
    output = ROOT / "data" / "five_vertex_star_algebra_raw.json"
    output.write_text(json.dumps(raw, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    hashes = {"algorithm": "SHA256", "files": {
        Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        output.name: hashlib.sha256(output.read_bytes()).hexdigest()}}
    (ROOT / "data" / "five_vertex_star_algebra_sha256.json").write_text(
        json.dumps(hashes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": "PASS", "symbolic_identities": 7,
                      "nested_chain_oriented_cases": 18,
                      "heavy_triangle_states": 3,
                      "legal_H_copy_counts": [len(s["legal_noncritical_copies"])
                                              for s in raw["heavy_triangle_control"]["states"]]}))


if __name__ == "__main__":
    main()
