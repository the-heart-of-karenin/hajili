"""Exact certificate verifier; no search and no external dependencies.

Six vertices, 62 nontrivial full cuts, four K states, seven word states.
The general k >= 4 theorem is proved in research_terminal_debt.md by
adding k-4 copies of a bidirected spanning tree to this k=4 certificate.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

NAMES = ("w", "y", "a", "b", "c", "r")
A = frozenset(range(5))
ROOT = 5
BASE_K = 4


def edges(k: int):
    result = []

    def add(kind, tail, head, count):
        for index in range(count):
            result.append({"id": f"{kind}_{NAMES[tail]}{NAMES[head]}_{index}",
                           "kind": kind, "tail": tail, "head": head})

    add("K", 0, 1, 1)
    add("K", 1, 0, 1)
    for core, ring in ((0, 2), (1, 3)):
        add("J", core, ring, k - 1)
        add("J", ring, core, k - 2)
        add("J", ring, 4, k - 1)
        add("J", 4, ring, k - 2)
    add("B", 4, ROOT, k)
    add("B", ROOT, 0, 2)
    add("B", ROOT, 1, 2)
    add("B", ROOT, 4, k - 3)
    return result


def shore(mask, n=6):
    return frozenset(v for v in range(n) if mask >> v & 1)


def outgoing(edge_list, mask):
    return sum(bool(mask >> e["tail"] & 1) and not bool(mask >> e["head"] & 1)
               for e in edge_list)


def cut_size(edge_list, mask):
    return sum(bool(mask >> e["tail"] & 1) != bool(mask >> e["head"] & 1)
               for e in edge_list)


def reverse(edge_list, edge_id):
    result = [dict(e) for e in edge_list]
    e = next(e for e in result if e["id"] == edge_id)
    e["tail"], e["head"] = e["head"], e["tail"]
    return result


def audit(edge_list, k):
    rows = [{"mask": mask,
             "shore": [NAMES[v] for v in sorted(shore(mask))],
             "outgoing": outgoing(edge_list, mask),
             "undirected": cut_size(edge_list, mask)}
            for mask in range(1, 63)]
    assert all(row["outgoing"] >= k for row in rows)
    return {"min_outgoing": min(row["outgoing"] for row in rows),
            "min_undirected": min(row["undirected"] for row in rows),
            "cuts": rows}


def residual_rows(edge_list, k):
    internal = [e for e in edge_list if e["kind"] != "B"]
    boundary = [e for e in edge_list if e["kind"] == "B"]
    result = []
    for mask in range(1, 31):
        complement = 31 ^ mask

        def q(current_mask):
            r_count = sum(e["head"] == ROOT and bool(current_mask >> e["tail"] & 1)
                          for e in boundary)
            s_complement = sum(e["tail"] == ROOT and not bool(current_mask >> e["head"] & 1)
                               for e in boundary)
            return min(r_count, s_complement)

        q_here, q_complement = q(mask), q(complement)
        slack = outgoing(internal, mask) - k + q_here
        mu = cut_size(internal, mask) - 2 * k + q_here + q_complement
        assert slack >= 0 and mu >= 1
        result.append({"mask": mask,
                       "shore": [NAMES[v] for v in sorted(shore(mask, 5))],
                       "q": q_here, "q_complement": q_complement,
                       "slack": slack, "mu": mu})
    return result


def word_audit(initial, k, word):
    state = initial
    states = [{"step": 0, "move": "initial", "audit": audit(state, k)}]
    for index, move in enumerate(word, 1):
        state = reverse(state, move)
        states.append({"step": index, "move": move, "audit": audit(state, k)})
    final = {e["id"]: (e["tail"], e["head"]) for e in state}
    for e in initial:
        expected = (e["head"], e["tail"]) if e["kind"] == "K" else (e["tail"], e["head"])
        assert final[e["id"]] == expected
    return states


def main():
    initial = edges(BASE_K)
    base = audit(initial, BASE_K)
    assert base["min_undirected"] == 2 * BASE_K + 1
    residual = residual_rows(initial, BASE_K)
    tight_masks = [row["mask"] for row in residual if row["slack"] == 0]
    assert tight_masks == [1, 2, 5, 10]

    k_edge_ids = [e["id"] for e in initial if e["kind"] == "K"]
    k_states = []
    for bits in itertools.product((0, 1), repeat=2):
        state = initial
        for bit, edge_id in zip(bits, k_edge_ids):
            if bit:
                state = reverse(state, edge_id)
        minimum = min(outgoing(state, mask) for mask in range(1, 63))
        k_states.append({"bits": list(bits), "min_outgoing": minimum,
                         "feasible": minimum >= BASE_K})
    assert [row["bits"] for row in k_states if row["feasible"]] == [[0, 0], [1, 1]]

    weights = {mask: 1 for mask in tight_masks}
    phi = {v: sum(weight for mask, weight in weights.items() if mask >> v & 1)
           for v in A}
    designated = next(e for e in initial if e["id"] == "K_wy_0")
    demand = sum(weight for mask, weight in weights.items()
                 if mask >> designated["tail"] & 1 and not(mask >> designated["head"] & 1))
    slack_cost = sum(weights.get(row["mask"], 0) * row["slack"] for row in residual)
    k_leak = sum(max(0, phi[e["head"]] - phi[e["tail"]])
                 for e in initial if e["kind"] == "K" and e["id"] != designated["id"])
    j_leak = sum(max(0, phi[e["head"]] - phi[e["tail"]] - 1)
                 for e in initial if e["kind"] == "J")
    debt = demand - slack_cost - k_leak - j_leak
    assert (demand, slack_cost, k_leak, j_leak, debt) == (2, 0, 0, 0, 2)

    deletion_state = [dict(e) for e in initial if e["id"] != designated["id"]]
    deletion_state = reverse(deletion_state, "J_aw_0")
    deletion_state = reverse(deletion_state, "J_ca_0")
    deletion_audit = audit(deletion_state, BASE_K)
    assert deletion_audit["min_outgoing"] == BASE_K

    requested_word = ["J_ca_0", "J_aw_0", "K_wy_0", "K_yw_0", "J_aw_0", "J_ca_0"]
    alternate_word = ["J_aw_0", "J_ca_0", "K_wy_0", "K_yw_0", "J_ca_0", "J_aw_0"]
    requested_states = word_audit(initial, BASE_K, requested_word)
    alternate_states = word_audit(initial, BASE_K, alternate_word)

    # Only four specified k values are checked; this is not a parameter search.
    parameter_checks = []
    for k in (4, 5, 6, 10):
        instance = edges(k)
        instance_audit = audit(instance, k)
        instance_residual = residual_rows(instance, k)
        assert [row["mask"] for row in instance_residual if row["slack"] == 0] == tight_masks
        word_audit(instance, k, requested_word)
        parameter_checks.append({"k": k,
                                 "min_outgoing": instance_audit["min_outgoing"],
                                 "edge_connectivity": instance_audit["min_undirected"]})

    payload = {"status": "TRUE-CRITICAL TERMINAL ANTIPODAL Debt=2; CONNECTED CONTROL",
               "not_established": "actual minimum component-separating descendant",
               "vertices": list(NAMES), "k": BASE_K, "labelled_edges": initial,
               "base_full_cut_audit": base, "residual_cut_audit": residual,
               "K_states": k_states,
               "dual": {"weights_by_mask": weights, "potential": {NAMES[v]: x for v, x in phi.items()},
                        "D": demand, "S_R": slack_cost, "L_K": k_leak, "L_J": j_leak, "Debt": debt},
               "deletion_completion": {"deleted": designated["id"],
                                       "reversed_J": ["J_aw_0", "J_ca_0"],
                                       "cost": 2, "audit": deletion_audit},
               "requested_balanced_word": requested_states,
               "alternate_balanced_word": alternate_states,
               "parameter_checks": parameter_checks}
    directory = Path(__file__).resolve().parents[1] / "data"
    directory.mkdir(exist_ok=True)
    destination = directory / "terminal_antipodal_debt2_certificate.json"
    destination.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    digests = {"algorithm": "SHA256",
               "files": {str(path.name): hashlib.sha256(path.read_bytes()).hexdigest()
                         for path in (Path(__file__).resolve(), destination)}}
    (directory / "terminal_antipodal_debt2_sha256.json").write_text(
        json.dumps(digests, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"edge_connectivity": base["min_undirected"],
                      "minimum_outgoing": base["min_outgoing"],
                      "Debt": debt, "deletion_cost": 2,
                      "legal_K_states": [[0, 0], [1, 1]],
                      "balanced_word_legal": True, "alternate_order_legal": True,
                      "parameter_checks": parameter_checks,
                      "output": str(destination)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
