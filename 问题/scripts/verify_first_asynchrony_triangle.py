"""Check one specified labelled 4-vertex control, not an orientation census."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V = ("s", "v", "t", "z")
K = 2
ARCS = [
    ("e", "s", "v"), ("f", "v", "t"), ("g", "s", "t"),
    ("ts1", "t", "s"), ("ts2", "t", "s"), ("sz", "s", "z"),
    ("h", "z", "t"), ("zt2", "z", "t"), ("vz", "v", "z"),
    ("zv1", "z", "v"), ("zv2", "z", "v"),
]
SHORES = [frozenset(V[i] for i in range(4) if mask >> i & 1)
          for mask in range(1, 15)]


def cut_record(flips):
    rows = []
    for shore in SHORES:
        out = inc = 0
        for label, u, v in ARCS:
            if label in flips:
                u, v = v, u
            out += u in shore and v not in shore
            inc += u not in shore and v in shore
        rows.append({"shore": sorted(shore), "out": out, "in": inc})
    return rows


def state(flips):
    rows = cut_record(flips)
    return {
        "flips": sorted(flips),
        "legal": all(min(row["out"], row["in"]) >= K for row in rows),
        "outdegrees": {v: next(row["out"] for row in rows
                               if row["shore"] == [v]) for v in V},
        "rows": rows,
    }


def main():
    base = state(set())
    lam = min(row["out"] + row["in"] for row in base["rows"])
    restricted = []
    for mask in range(8):
        flips = {label for i, label in enumerate(("e", "f", "g"))
                 if mask >> i & 1}
        restricted.append({"bits_efg": [(mask >> i) & 1 for i in range(3)],
                           **state(flips)})
    legal_bits = {tuple(record["bits_efg"]) for record in restricted
                  if record["legal"]}
    assert lam == 5
    assert legal_bits == {(0, 0, 0), (1, 1, 0), (0, 0, 1)}
    flips = set()
    word = [state(flips)]
    for label in ("h", "e", "f", "h"):
        flips.symmetric_difference_update({label})
        record = state(flips)
        assert record["legal"], (label, record)
        word.append(record)
    assert flips == {"e", "f"}
    raw = {"kind": "specified_control_only", "k": K, "vertices": V,
           "labelled_arcs_at_R": ARCS, "lambda": lam,
           "restricted_cube": restricted,
           "ambient_word": ["h", "e", "f", "h"], "ambient_states": word,
           "ambient_minimum_separation_origin": False}
    output = ROOT / "data" / "first_asynchrony_triangle_raw.json"
    output.write_text(json.dumps(raw, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8")
    hashes = {
        "algorithm": "SHA256",
        "files": {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  output.name: hashlib.sha256(output.read_bytes()).hexdigest()},
    }
    (ROOT / "data" / "first_asynchrony_triangle_sha256.json").write_text(
        json.dumps(hashes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"lambda": lam, "legal_cube_vertices": sorted(legal_bits),
                      "ambient_word": raw["ambient_word"],
                      "outdegrees_along_word": [s["outdegrees"] for s in word],
                      "output": str(output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
