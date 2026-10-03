"""Specified canonical controls and root-signature witnesses; no graph census."""
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V = ("w", "y", "c", "d")


def family(k):
    arcs = [("e", "w", "y"), ("f", "y", "w"),
            ("g", "c", "w"), ("dy", "d", "y"),
            ("cd", "c", "d"), ("dc", "d", "c")]
    for i in range(k - 1):
        arcs += [(f"wc{i}", "w", "c"), (f"yd{i}", "y", "d"),
                 (f"cy{i}", "c", "y"), (f"dw{i}", "d", "w")]
    return arcs


SHORES = [frozenset(V[i] for i in range(4) if mask >> i & 1)
          for mask in range(1, 15)]


def rows(arcs, flips=()):
    flips = set(flips)
    result = []
    for shore in SHORES:
        out = inc = 0
        for label, u, v in arcs:
            if label in flips:
                u, v = v, u
            out += u in shore and v not in shore
            inc += u not in shore and v in shore
        result.append({"shore": sorted(shore), "out": out, "in": inc})
    return result


def degrees(arcs, flips=()):
    table = rows(arcs, flips)
    return {v: next(r["out"] for r in table if r["shore"] == [v]) for v in V}


def record(k, arcs, flips, matching):
    table = rows(arcs, flips)
    assert all(min(r["out"], r["in"]) >= k for r in table)
    admissibility = []
    for shore, row in zip(SHORES, table):
        crossing = sum((u in shore) != (v in shore) for _, u, v in matching)
        gap = row["out"] + row["in"] - crossing - 2 * k
        assert gap >= 0
        admissibility.append({"shore": sorted(shore), "matching_crossings": crossing,
                              "gap": gap})
    eulerian_degrees = degrees(arcs, flips)
    for _, u, _ in matching:
        eulerian_degrees[u] += 1
    assert set(eulerian_degrees.values()) == {k + 1}
    return {"flips": sorted(flips), "outdegrees_G": degrees(arcs, flips),
            "oriented_matching": matching, "cut_rows": table,
            "pairing_admissibility": admissibility,
            "outdegrees_augmented": eulerian_degrees}


def certificate_history(k):
    arcs = family(k)
    lam = min(r["out"] + r["in"] for r in rows(arcs))
    assert lam == 2 * k + 1
    assert min(r["out"] for r in rows(arcs, {"e"})) < k
    assert min(r["out"] for r in rows(arcs, {"f"})) < k
    M0 = [("mwc", "w", "c"), ("myd", "y", "d")]
    M1 = [("mwc", "c", "w"), ("myd", "y", "d")]
    N1 = [("mwy", "y", "w"), ("mcd", "c", "d")]
    N2 = [("mwy", "w", "y"), ("mcd", "c", "d")]
    prescribed = [
        ("initial", set(), M0),
        ("physical g", {"g"}, M1),
        ("certificate re-pair only", {"g"}, N1),
        ("physical e", {"g", "e"}, N2),
        ("physical f", {"g", "e", "f"}, N1),
        ("certificate re-pair only", {"g", "e", "f"}, M1),
        ("physical g restored", {"e", "f"}, M0),
    ]
    history = [{"operation": op, **record(k, arcs, flips, matching)}
               for op, flips, matching in prescribed]
    return {"k": k, "lambda": lam, "labelled_arcs": arcs,
            "physical_word": ["g", "e", "f", "g"],
            "support_edges_both_initially_illegal": True, "history": history}


def root_signatures():
    k = 2
    arcs = family(k)
    root = "w"
    star = [(label, u, v) for label, u, v in arcs if root in (u, v)]
    internal = [(label, u, v) for label, u, v in arcs if root not in (u, v)]
    assert len(star) == len(internal) == 5
    root_labels = [item[0] for item in star]
    witnesses = []
    for root_bit, second_bit in itertools.product((0, 1), repeat=2):
        tau = [("mwc", "w", "c"), ("myd", "y", "d")]
        if root_bit:
            tau[0] = ("mwc", "c", "w")
        if second_bit:
            tau[1] = ("myd", "d", "y")
        target = {v: k + 1 for v in V}
        for _, u, _ in tau:
            target[u] -= 1
        for star_mask in range(1 << len(star)):
            star_flips = {label for i, label in enumerate(root_labels)
                          if star_mask >> i & 1}
            fixed_out_root = sum((v == root if label in star_flips else u == root)
                                 for label, u, v in star)
            if fixed_out_root != target[root]:
                continue
            found = None
            for internal_mask in range(1 << len(internal)):
                flips = star_flips | {label for i, (label, _, _) in enumerate(internal)
                                      if internal_mask >> i & 1}
                if degrees(arcs, flips) == target:
                    found = flips
                    break
            assert found is not None, (tau, star_flips)
            witness = record(k, arcs, found, tau)
            witness.update({"root_star_flips": sorted(star_flips),
                            "virtual_signature_bits": [root_bit, second_bit]})
            witnesses.append(witness)
    assert len(witnesses) == 40
    return {"kind": "40_prescribed_root_and_virtual_signature_queries",
            "root": root, "k": k, "labelled_arcs": arcs, "witnesses": witnesses}


def signed_mu2_control():
    k = 2
    arcs = family(k) + [("extra_cw", "c", "w"), ("extra_dy", "d", "y")]
    fixed = [a for a in arcs if a[0] not in {"e", "f"}]
    free = [a for a in arcs if a[0] in {"e", "f"}]
    lambda_value = min(r["out"] + r["in"] for r in rows(arcs))
    assert lambda_value == 2 * k + 2
    margins = []
    fixed_rows = rows(fixed)
    free_rows = rows(free)
    for shore, fixed_row, free_row in zip(SHORES, fixed_rows, free_rows):
        demand = k - fixed_row["out"]
        complementary_demand = k - fixed_row["in"]
        mu = free_row["out"] + free_row["in"] - demand - complementary_demand
        assert mu >= 2
        margins.append({"shore": sorted(shore), "p_J": demand,
                        "p_J_complement": complementary_demand, "mu": mu})
    assert next(r["p_J"] for r in margins if r["shore"] == ["c"]) == -2
    states = []
    for mask in range(4):
        flips = {label for i, label in enumerate(("e", "f")) if mask >> i & 1}
        table = rows(arcs, flips)
        legal = all(min(r["out"], r["in"]) >= k for r in table)
        states.append({"bits_ef": [(mask >> i) & 1 for i in range(2)],
                       "legal": legal, "rows": table})
    assert {tuple(s["bits_ef"]) for s in states if s["legal"]} == {(0, 0), (1, 1)}
    return {"kind": "specified_signed_mu2_scope_control", "k": k,
            "lambda": lambda_value, "labelled_arcs": arcs,
            "free_labels": ["e", "f"], "signed_margins": margins,
            "restricted_states": states, "minimum_mu": min(r["mu"] for r in margins),
            "restricted_components": 2, "ambient_counterexample": False}


def main():
    raw = {"kind": "specified_controls_and_signature_witnesses_only",
           "families": [certificate_history(k) for k in (2, 3, 4, 5)],
           "root_signature_audit": root_signatures(),
           "signed_mu2_frozen_control": signed_mu2_control()}
    output = ROOT / "data" / "pairing_bridge_controls_raw.json"
    output.write_text(json.dumps(raw, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8")
    hashes = {"algorithm": "SHA256", "files": {
        Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        output.name: hashlib.sha256(output.read_bytes()).hexdigest()}}
    (ROOT / "data" / "pairing_bridge_controls_sha256.json").write_text(
        json.dumps(hashes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"k_values": [r["k"] for r in raw["families"]],
                      "all_lambda": [r["lambda"] for r in raw["families"]],
                      "canonical_history_states_per_case": 7,
                      "root_signature_witnesses": len(raw["root_signature_audit"]["witnesses"]),
                      "signed_control_mu": raw["signed_mu2_frozen_control"]["minimum_mu"],
                      "signed_restricted_components": 2,
                      "result": "PASS"}))


if __name__ == "__main__":
    main()
