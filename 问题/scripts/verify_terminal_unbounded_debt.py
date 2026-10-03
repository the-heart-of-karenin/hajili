"""Bounded exact checks of the analytically proved unbounded family.

No graph search: twenty-four prescribed cases with arm length=1..4.
Original k=4,5 family, optimized k=2,3 family, and their path splits.
All nontrivial cuts are audited.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


def build(k, length, split=False, optimized=False):
    w_arm = ["w"] + [f"w{i}" for i in range(1, length)] + ["c"]
    y_arm = ["y"] + [f"y{i}" for i in range(1, length)] + ["c"]
    names = w_arm[:-1] + y_arm[:-1] + ["c", "root"]
    if split:
        names[names.index("y")] = "u"
        names.append("v")
        y_arm[0] = "u"
    index = {name: position for position, name in enumerate(names)}
    result = []

    def add(kind, tail, head, count):
        for copy in range(count):
            result.append({"id": f"{kind}_{tail}_{head}_{copy}", "kind": kind,
                           "tail": index[tail], "head": index[head]})

    if split:
        add("K", "w", "v", 1)
        add("K", "u", "w", 1)
        add("J", "u", "v", k)
        add("J", "v", "u", k)
    else:
        add("K", "w", "y", 1)
        add("K", "y", "w", 1)
    for arm in (w_arm, y_arm):
        for position, (first, second) in enumerate(zip(arm, arm[1:])):
            add("J", first, second, k - 1)
            backward = (k - 1 if position == 0 else k) if optimized else k - 2
            add("J", second, first, backward)
    add("B", "c", "root", k)
    add("B", "root", "w", 2)
    if split:
        add("B", "root", "u", 1)
        if not optimized:
            add("B", "root", "v", 1)
    else:
        add("B", "root", "y", 1 if optimized else 2)
    add("B", "root", "c", k - 2 if optimized else k - 3)
    prefix_weights = {}
    for arm in (w_arm, y_arm):
        for end in range(1, length + 1):
            vertices = arm[:end]
            if split and arm is y_arm:
                vertices = vertices + ["v"]
            mask = sum(1 << index[name] for name in vertices)
            prefix_weights[mask] = 1
    opening = [f"J_{second}_{first}_0"
               for first, second in reversed(list(zip(w_arm, w_arm[1:])))]
    target = ["K_w_v_0", "K_u_w_0"] if split else ["K_w_y_0", "K_y_w_0"]
    return names, result, prefix_weights, opening, target


def reverse(state, edge_id):
    state = [dict(edge) for edge in state]
    selected = next(edge for edge in state if edge["id"] == edge_id)
    selected["tail"], selected["head"] = selected["head"], selected["tail"]
    return state


def outgoing(state, mask):
    return sum(bool(mask >> edge["tail"] & 1) and not bool(mask >> edge["head"] & 1)
               for edge in state)


def audit(state, n, k, allow_illegal=False):
    values = [outgoing(state, mask) for mask in range(1, (1 << n) - 1)]
    minimum = min(values)
    if not allow_illegal:
        assert minimum >= k
    return {"min_outgoing": minimum,
            "tight_masks": [mask for mask, value in enumerate(values, 1) if value == k],
            "ordered_full_cut_outgoing_values": values}


def verify(k, length, split=False, optimized=False):
    names, initial, weights, opening, target = build(k, length, split, optimized)
    n = len(names)
    index = {name: position for position, name in enumerate(names)}
    root = index["root"]
    full_audit = audit(initial, n, k)
    undirected = [sum(bool(mask >> edge["tail"] & 1) != bool(mask >> edge["head"] & 1)
                      for edge in initial) for mask in range(1, (1 << n) - 1)]
    assert min(undirected) == 2 * k + 1
    all_internal = ((1 << n) - 1) ^ (1 << root)
    boundary = [edge for edge in initial if edge["kind"] == "B"]
    internal = [edge for edge in initial if edge["kind"] != "B"]

    def q(mask):
        out_boundary = sum(edge["head"] == root and bool(mask >> edge["tail"] & 1)
                           for edge in boundary)
        in_complement = sum(edge["tail"] == root and not bool(mask >> edge["head"] & 1)
                            for edge in boundary)
        return min(out_boundary, in_complement)

    residual = []
    for mask in range(1, 1 << n):
        if mask & (1 << root) or mask == all_internal:
            continue
        complement = all_internal ^ mask
        slack = outgoing(internal, mask) - k + q(mask)
        mu = sum(bool(mask >> edge["tail"] & 1) != bool(mask >> edge["head"] & 1)
                 for edge in internal) - 2 * k + q(mask) + q(complement)
        assert slack >= 0 and mu >= 1
        if mask in weights:
            assert slack == 0 and (mu >= 1 if optimized else mu == 1)
        residual.append({"mask": mask, "slack": slack, "mu": mu})

    phi = {vertex: sum(weight for mask, weight in weights.items() if mask >> vertex & 1)
           for vertex in range(n) if vertex != root}
    designated = next(edge for edge in initial if edge["id"] == target[0])
    demand = sum(weight for mask, weight in weights.items()
                 if mask >> designated["tail"] & 1 and not(mask >> designated["head"] & 1))
    slack_cost = sum(weights.get(row["mask"], 0) * row["slack"] for row in residual)
    k_leak = sum(max(0, phi[edge["head"]] - phi[edge["tail"]])
                 for edge in initial if edge["kind"] == "K" and edge["id"] != target[0])
    j_leak = sum(max(0, phi[edge["head"]] - phi[edge["tail"]] - 1)
                 for edge in initial if edge["kind"] == "J")
    assert demand - slack_cost - k_leak - j_leak == length

    k_states = []
    for bits in itertools.product((0, 1), repeat=2):
        state = initial
        for bit, move in zip(bits, target):
            if bit:
                state = reverse(state, move)
        k_states.append({"bits": list(bits), "min_outgoing": audit(state, n, k, True)["min_outgoing"]})
    assert [row["bits"] for row in k_states if row["min_outgoing"] >= k] == [[0, 0], [1, 1]]

    state = initial
    word_states = [{"step": 0, "move": "initial", "audit": full_audit}]
    word = opening + target + list(reversed(opening))
    for step, move in enumerate(word, 1):
        state = reverse(state, move)
        word_states.append({"step": step, "move": move, "audit": audit(state, n, k)})
    for first, last in zip(initial, state):
        expected = (first["head"], first["tail"]) if first["kind"] == "K" else (first["tail"], first["head"])
        assert (last["tail"], last["head"]) == expected

    deletion = [dict(edge) for edge in initial if edge["id"] != target[0]]
    for move in opening:
        deletion = reverse(deletion, move)
    deletion_audit = audit(deletion, n, k)
    return {"k": k, "length": length, "split_to_physical_path": split,
            "optimized_base_k2": optimized,
            "vertices": names, "labelled_edges": initial, "edge_connectivity": min(undirected),
            "ordered_undirected_full_cut_values": undirected, "residual_cut_audit": residual,
            "dual": {"weights_by_mask": weights, "potential": {names[v]: value for v, value in phi.items()},
                     "D": demand, "S_R": slack_cost, "L_K": k_leak, "L_J": j_leak, "Debt": length},
            "K_states": k_states, "balanced_word": word_states,
            "deletion_completion": {"deleted": target[0], "reversed_J": opening,
                                    "cost": length, "audit": deletion_audit}}


def main():
    cases = [verify(k, length) for k in (4, 5) for length in range(1, 5)]
    cases += [verify(4, length, True) for length in range(1, 5)]
    cases += [verify(k, length, optimized=True) for k in (2, 3) for length in range(1, 5)]
    cases += [verify(2, length, True, True) for length in range(1, 5)]
    directory = Path(__file__).resolve().parents[1] / "data"
    destination = directory / "terminal_unbounded_debt_certificate.json"
    destination.write_text(json.dumps({"status": "PROVED unbounded terminal-antipodal Debt; CONNECTED CONTROL",
                                      "cases": cases}, ensure_ascii=False, separators=(",", ":")) + "\n",
                           encoding="utf-8")
    summary = [{"k": case["k"], "length": case["length"], "vertices": len(case["vertices"]),
                "physical_path": case["split_to_physical_path"],
                "optimized_base_k2": case["optimized_base_k2"],
                "edge_connectivity": case["edge_connectivity"],
                "min_mu": min(row["mu"] for row in case["residual_cut_audit"]),
                "Debt": case["dual"]["Debt"],
                "deletion_cost": case["deletion_completion"]["cost"],
                "word_min_outgoing_by_step": [state["audit"]["min_outgoing"]
                                               for state in case["balanced_word"]],
                "endpoint_states": case["K_states"]} for case in cases]
    summary_path = directory / "terminal_unbounded_debt_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    hashes = {"algorithm": "SHA256", "files": {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in (Path(__file__).resolve(), destination, summary_path)}}
    (directory / "terminal_unbounded_debt_sha256.json").write_text(json.dumps(hashes, indent=2) + "\n", encoding="utf-8")
    print(json.dumps([{"k": case["k"], "length": case["length"],
                       "physical_path": case["split_to_physical_path"],
                       "optimized_base_k2": case["optimized_base_k2"],
                       "edge_connectivity": case["edge_connectivity"],
                       "Debt": case["dual"]["Debt"], "deletion_cost": case["deletion_completion"]["cost"],
                       "all_word_cuts_legal": True} for case in cases]))


if __name__ == "__main__":
    main()
