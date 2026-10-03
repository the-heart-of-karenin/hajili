"""Verify a prescribed atom-projection control; not graph search."""
from pathlib import Path
import hashlib
import itertools
import json


def main():
    names = ['a', 'b', 'c', 'r']
    k, a_mask, b_mask = 2, 7, 3
    edges = []
    for prefix, tail, head, count in (
        ('ab', 0, 1, 1), ('ba', 1, 0, 1),
        ('ac', 0, 2, 1), ('bc', 1, 2, 1),
        ('ca', 2, 0, 3), ('cb', 2, 1, 3),
        ('cr', 2, 3, 2), ('rc', 3, 2, 3),
    ):
        for index in range(count):
            edges.append({'id': f'{prefix}{index}', 'tail': tail, 'head': head})

    def inside(mask, vertex):
        return bool(mask & (1 << vertex))

    def out(state, mask):
        return sum(inside(mask, edge['tail']) and not inside(mask, edge['head']) for edge in state)

    def cut(state, mask):
        return sum(inside(mask, edge['tail']) != inside(mask, edge['head']) for edge in state)

    def reverse(state, identity):
        result = [dict(edge) for edge in state]
        chosen = [edge for edge in result if edge['id'] == identity]
        assert len(chosen) == 1
        chosen[0]['tail'], chosen[0]['head'] = chosen[0]['head'], chosen[0]['tail']
        return result

    def audit(state):
        return [{'mask': mask, 'out': out(state, mask), 'undirected': cut(state, mask)}
                for mask in range(1, 15)]

    def q(mask):
        outgoing = sum(edge['head'] == 3 and inside(mask, edge['tail']) for edge in edges)
        incoming_complement = sum(edge['tail'] == 3 and inside(a_mask ^ mask, edge['head']) for edge in edges)
        return min(outgoing, incoming_complement)

    p = {mask: k - q(mask) for mask in range(1, 7)}
    internal = [edge for edge in edges if 3 not in (edge['tail'], edge['head'])]
    mu_rows = [{'mask': mask, 'p': p[mask], 'q': q(mask),
                'slack': out(internal, mask) - p[mask],
                'mu': cut(internal, mask) - p[mask] - p[a_mask ^ mask]}
               for mask in range(1, 7)]
    assert min(row['mu'] for row in mu_rows) == 2
    assert out(internal, b_mask) == p[b_mask]
    quotient = [edge for edge in internal if not (inside(b_mask, edge['tail']) and inside(b_mask, edge['head']))]
    projected = {mask: max(p[mask | whole] - out(quotient, mask | whole) for whole in (0, 4))
                 for mask in (1, 2)}
    assert projected == {1: 1, 2: 1}
    b_edges = [edge for edge in internal if edge['id'] in ('ab0', 'ba0')]
    mu_local = cut(b_edges, 1) - projected[1] - projected[2]
    assert mu_local == 0
    assignments = []
    for bits in itertools.product((0, 1), repeat=2):
        state = edges
        for bit, identity in zip(bits, ('ab0', 'ba0')):
            if bit:
                state = reverse(state, identity)
        full = audit(state)
        assignments.append({'bits': list(bits), 'minimum_out': min(row['out'] for row in full),
                            'legal': all(row['out'] >= k for row in full), 'cuts': full})
    assert [row['bits'] for row in assignments if row['legal']] == [[0, 0], [1, 1]]
    assert sum(abs(a - b) for a, b in zip([0, 0], [1, 1])) == 2
    states = []
    state = edges
    for move in ('initial', 'ca0', 'ab0', 'ba0', 'ca0'):
        if move != 'initial':
            state = reverse(state, move)
        full = audit(state)
        assert all(row['out'] >= k for row in full)
        states.append({'move': move, 'cuts': full, 'minimum_out': min(row['out'] for row in full)})
    for original, final in zip(edges, state):
        if original['id'] in ('ab0', 'ba0'):
            assert (final['tail'], final['head']) == (original['head'], original['tail'])
        else:
            assert final == original
    full_initial = audit(edges)
    connectivity = min(row['undirected'] for row in full_initial)
    assert connectivity == 5
    result = {'status': 'PASS; CONNECTED CONTROL, not main-theorem counterexample',
              'vertices': names, 'physical_edges': edges, 'k': k, 'lambda': connectivity,
              'actual_tight_family': [b_mask], 'atoms': [b_mask, 4],
              'global_residual': mu_rows, 'projected_demand': projected, 'local_mu': mu_local,
              'fixed_sector_assignments': assignments, 'fixed_sector_components': 2,
              'ambient_connecting_word': states}
    base = Path(__file__).resolve().parents[1]
    raw = base / 'data/atom_scope_gap_certificate.json'
    raw.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    hashes = {str(path.relative_to(base)): hashlib.sha256(path.read_bytes()).hexdigest()
              for path in (Path(__file__).resolve(), raw)}
    (base / 'data/atom_scope_gap_sha256.json').write_text(json.dumps(hashes, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'vertices': len(names), 'physical_copies': len(edges),
                      'lambda': connectivity, 'global_min_mu': min(row['mu'] for row in mu_rows),
                      'local_mu': mu_local, 'fixed_sector_components': 2,
                      'ambient_word_length': len(states) - 1, 'cuts_per_state': 14}))


if __name__ == '__main__':
    main()
