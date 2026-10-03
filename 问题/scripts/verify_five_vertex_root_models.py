"""Exact checks of two prescribed five-vertex models, no graph census."""
from collections import deque
from pathlib import Path
import hashlib
import json


def verify(name, groups):
    edges = [(u, v, f'g{group}_{u}{v}_{index}') for group, (u, v, count) in enumerate(groups) for index in range(count)]
    assert len({edge[2] for edge in edges}) == len(edges)
    n, k, m = 5, 2, len(edges)
    root = 4
    all_bits = (1 << m) - 1
    cut_rows = []
    for shore in range(1, (1 << n) - 1):
        leave = enter = 0
        for index, (u, v, _) in enumerate(edges):
            u_in, v_in = bool(shore & (1 << u)), bool(shore & (1 << v))
            if u_in and not v_in:
                leave |= 1 << index
            elif v_in and not u_in:
                enter |= 1 << index
        cut_rows.append((shore, leave, enter))

    def legal(state):
        return all(((leave & (all_bits ^ state)).bit_count() + (enter & state).bit_count()) >= k
                   for _, leave, enter in cut_rows)

    valid = {state for state in range(1 << m) if legal(state)}
    root_mask = sum(1 << index for index, (u, v, _) in enumerate(edges) if root in (u, v))
    internal_positions = [index for index in range(m) if not root_mask & (1 << index)]

    def components(universe, positions):
        remaining = set(universe)
        output = []
        while remaining:
            initial = min(remaining)
            remaining.remove(initial)
            queue, component = deque([initial]), [initial]
            while queue:
                state = queue.popleft()
                for index in positions:
                    neighbour = state ^ (1 << index)
                    if neighbour in remaining:
                        remaining.remove(neighbour)
                        queue.append(neighbour)
                        component.append(neighbour)
            output.append(sorted(component))
        return output

    global_components = components(valid, range(m))
    fibers = {}
    for state in valid:
        fibers.setdefault(state & root_mask, set()).add(state)
    fiber_certificates = []
    for signature, states in sorted(fibers.items()):
        local_components = components(states, internal_positions)
        fiber_certificates.append({'root_signature': signature, 'states': sorted(states),
                                   'component_sizes': [len(c) for c in local_components],
                                   'components': local_components})
    # Independent direct endpoint counting, rather than reusing cut bitmasks.
    for state in valid:
        for shore, _, _ in cut_rows:
            direct = 0
            for index, (u, v, _) in enumerate(edges):
                if state & (1 << index):
                    u, v = v, u
                direct += bool(shore & (1 << u)) and not bool(shore & (1 << v))
            assert direct >= k
    degree = [sum(vertex in (u, v) for u, v, _ in edges) for vertex in range(n)]
    connectivity = min((leave | enter).bit_count() for _, leave, enter in cut_rows)
    assert connectivity == 5 and degree[root] == 5
    return {'name': name, 'k': k, 'vertices': ['a', 'b', 'c', 'd', 'r'],
            'edges': edges, 'lambda': connectivity, 'degrees': degree,
            'orientations_checked': 1 << m, 'proper_cuts': len(cut_rows),
            'legal_states': sorted(valid),
            'ambient_components': global_components,
            'root_fibers': fiber_certificates,
            'independent_endpoint_cut_audit': 'PASS'}


def main():
    models = [
        ('K5-plus-three-copies',
         [(u, v, 1) for u in range(5) for v in range(u + 1, 5)] + [(0, 1, 1), (2, 3, 1), (2, 4, 1)]),
        ('critical-pair-ac',
         [(0, 2, 3), (0, 4, 1), (0, 1, 1), (2, 4, 1),
          (2, 3, 2), (1, 3, 2), (3, 4, 1), (1, 4, 2)]),
    ]
    results = [verify(name, groups) for name, groups in models]
    base = Path(__file__).resolve().parents[1]
    raw = base / 'data/five_vertex_root_models_certificate.json'
    raw.write_text(json.dumps({'status': 'EXACT PRESCRIBED MODELS; no extrapolation', 'models': results},
                              ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
    paths = [Path(__file__).resolve(), raw]
    hashes = {str(path.relative_to(base)): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
    (base / 'data/five_vertex_root_models_sha256.json').write_text(json.dumps(hashes, indent=2) + '\n', encoding='utf-8')
    print(json.dumps([{'name': result['name'], 'physical_edges': len(result['edges']),
                       'orientations_checked': result['orientations_checked'],
                       'lambda': result['lambda'], 'legal_orientations': len(result['legal_states']),
                       'ambient_component_sizes': [len(c) for c in result['ambient_components']],
                       'nonempty_root_fibers': len(result['root_fibers']),
                       'maximum_fiber_component_count': max(len(f['components']) for f in result['root_fibers']),
                       'fiber_sizes': [len(f['states']) for f in result['root_fibers']],
                       'independent_all_cut_audit': 'PASS'} for result in results]))


if __name__ == '__main__':
    main()
