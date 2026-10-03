"""Independent cut-based verification of a 32-state environment test."""
import hashlib
import json
import platform
import subprocess
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CPP = DATA / "environment_probe.exe"


def main():
    DATA.mkdir(exist_ok=True)
    n, k = 2, 2
    edges = [(0, 1)] * 5  # List positions identify physical edges.
    m = len(edges)
    legal = []
    for mask in range(1 << m):
        arcs = [(u, v) if mask & (1 << i) else (v, u)
                for i, (u, v) in enumerate(edges)]
        cut_counts = [sum(bool(shore & (1 << u)) and not bool(shore & (1 << v))
                          for u, v in arcs)
                      for shore in range(1, (1 << n) - 1)]
        if min(cut_counts) >= k:
            legal.append(mask)

    legal_set = set(legal)
    adj = {mask: [mask ^ (1 << i) for i in range(m)
                  if mask ^ (1 << i) in legal_set] for mask in legal}
    component_sets = set()
    diameter = 0
    for start in legal:
        distances = {start: 0}
        pending = deque([start])
        while pending:
            here = pending.popleft()
            for nxt in adj[here]:
                if nxt not in distances:
                    distances[nxt] = distances[here] + 1
                    pending.append(nxt)
        component_sets.add(frozenset(distances))
        diameter = max(diameter, max(distances.values()))

    result = {
        "vertices": n,
        "physical_edges": m,
        "k": k,
        "orientations_checked": 1 << m,
        "legal_orientations": len(legal),
        "reconfiguration_edges": sum(map(len, adj.values())) // 2,
        "components": len(component_sets),
        "maximum_component_diameter": diameter,
    }
    expected = dict(vertices=2, physical_edges=5, k=2,
                    orientations_checked=32, legal_orientations=20,
                    reconfiguration_edges=30, components=1,
                    maximum_component_diameter=5)
    if result != expected:
        raise RuntimeError(f"Python result differs from expectation: {result}")

    completed = subprocess.run([str(CPP)], check=True, capture_output=True, text=True)
    cpp_result = json.loads(completed.stdout)
    if cpp_result != result:
        raise RuntimeError(f"C++/Python disagreement: {cpp_result} vs {result}")

    (DATA / "environment_probe_cpp.json").write_text(completed.stdout, encoding="utf-8")
    report = {
        "classification": "ENVIRONMENT_TEST_ONLY; exact finite result for one tiny graph",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": platform.python_version(),
        "result": result,
        "cpp_python_agree": True,
        "legal_masks": legal,
        "adjacency": adj,
    }
    output = DATA / "environment_probe_python.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if json.loads(output.read_text(encoding="utf-8")) != json.loads(json.dumps(report)):
        raise RuntimeError("Saved JSON did not round trip")

    files = [ROOT / "scripts" / "environment_probe.cpp",
             Path(__file__).resolve(), CPP,
             DATA / "environment_probe_cpp.json", output]
    manifest = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in files}
    (DATA / "environment_probe_sha256.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "result": result,
                      "cpp_python_agree": True,
                      "file_read_write_verified": True,
                      "hashed_files": len(files)}, indent=2))


if __name__ == "__main__":
    main()
