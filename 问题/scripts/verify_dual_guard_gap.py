"""One prescribed antipodal certificate: relative source != legal weighted source."""
import hashlib
import json
from pathlib import Path

from verify_terminal_unbounded_debt import build, audit, outgoing, reverse

ROOT = Path(__file__).resolve().parent.parent
names, edges, _, _, target = build(2, 2, optimized=True)
n = len(names)
index = {name: j for j, name in enumerate(names)}
weights = {1 << index["w"]: 1, 1 << index["y"]: 1}
phi = {j: sum(y for mask, y in weights.items() if mask & (1 << j)) for j in range(n)}
initial_audit = audit(edges, n, 2)
antipode = edges
for edge_id in target:
    antipode = reverse(antipode, edge_id)
antipode_audit = audit(antipode, n, 2)
for mask in weights:
    assert outgoing(edges, mask) == outgoing(antipode, mask) == 2

records = []
for edge in edges:
    if edge["kind"] == "B":
        continue
    new = reverse(edges, edge["id"])
    new_audit = audit(new, n, 2, True)
    signs = [int(bool(mask & (1 << edge["head"]))) - int(bool(mask & (1 << edge["tail"]))) for mask in weights]
    records.append({
        "id": edge["id"], "tail": names[edge["tail"]], "head": names[edge["head"]],
        "original_gradient": phi[edge["head"]] - phi[edge["tail"]],
        "relative_F_source": min(signs) >= 0 and max(signs) > 0,
        "globally_legal": new_audit["min_outgoing"] >= 2,
        "flipped_state_min_outgoing": new_audit["min_outgoing"],
    })
legal = [x for x in records if x["globally_legal"]]
sources = [x for x in records if x["relative_F_source"]]
assert len(legal) == 4 and all(x["original_gradient"] == 0 for x in legal)
assert len(sources) == 2 and all(not x["globally_legal"] for x in sources)
designated = next(e for e in edges if e["id"] == target[0])
p_e = sum(y for mask, y in weights.items() if mask & (1 << designated["tail"]) and not mask & (1 << designated["head"]))
l_k = sum(max(0, phi[e["head"]] - phi[e["tail"]]) for e in edges if e["kind"] == "K" and e["id"] != target[0])
l_j = sum(max(0, phi[e["head"]] - phi[e["tail"]] - 1) for e in edges if e["kind"] == "J")
assert (p_e, l_k, l_j, p_e - l_k - l_j) == (1, 0, 0, 1)

raw = {
    "status": "PASS: positive nonoptimal Debt, no legal positive original gradient",
    "scope": "genuine k2 L2 connected control; not optimal/minimum-origin counterexample",
    "vertices": names, "physical_edges": edges,
    "positive_rows": [[names[j] for j in range(n) if mask & (1 << j)] for mask in weights],
    "original_phi": {names[j]: value for j, value in phi.items()},
    "R_audit": initial_audit, "antipode_audit": antipode_audit,
    "internal_single_flip_records": records,
    "dual_terms": {"P_e": p_e, "S_R": 0, "L_K": l_k, "L_J": l_j, "Debt": p_e - l_k - l_j},
}
path = ROOT / "data" / "dual_guard_gap_certificate.json"
path.write_text(json.dumps(raw, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__), Path(__file__).with_name("verify_terminal_unbounded_debt.py"), path)}
(ROOT / "data" / "dual_guard_gap_sha256.json").write_text(json.dumps(hashes, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": "PASS", "cuts_per_state": (1 << n) - 2,
                  "internal_single_flip_checks": len(records), "legal_copies": len(legal),
                  "relative_sources_all_illegal": len(sources), "Debt": 1,
                  "maximum_original_gradient_on_legal": max(x["original_gradient"] for x in legal)}))
