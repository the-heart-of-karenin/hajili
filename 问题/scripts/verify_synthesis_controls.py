"""Audit two prescribed controls by direct physical-edge cut counts."""
from pathlib import Path
import hashlib
import json


def edges_from_groups(groups):
    return [dict(id=f"g{group}_{copy}", tail=tail, head=head)
            for group, (tail, head, count) in enumerate(groups)
            for copy in range(count)]


def audit(edges, names):
    rows = []
    for mask in range(1, (1 << len(names)) - 1):
        inside = lambda vertex: bool(mask & (1 << names.index(vertex)))
        rows.append(dict(
            shore=[name for name in names if inside(name)],
            out=sum(inside(e['tail']) and not inside(e['head']) for e in edges),
            undirected=sum(inside(e['tail']) != inside(e['head']) for e in edges)))
    return rows


def degrees(edges, names):
    return {v: dict(degree=sum(v in (e['tail'], e['head']) for e in edges),
                    out=sum(e['tail'] == v for e in edges),
                    incoming=sum(e['head'] == v for e in edges)) for v in names}


def flip(edges, identity):
    result = [dict(e) for e in edges]
    chosen = [e for e in result if e['id'] == identity]
    assert len(chosen) == 1
    chosen[0]['tail'], chosen[0]['head'] = chosen[0]['head'], chosen[0]['tail']
    return result


def main():
    root = Path(__file__).resolve().parents[1]
    names4 = ['w', 'y', 'c', 'r']
    original = edges_from_groups([
        ('w', 'c', 2), ('y', 'c', 1), ('c', 'y', 1),
        ('w', 'y', 1), ('y', 'w', 1), ('c', 'r', 2),
        ('r', 'w', 2), ('r', 'y', 1)])
    rows4 = audit(original, names4)
    assert len(original) == 11 and min(row['undirected'] for row in rows4) == 5
    assert min(row['out'] for row in rows4) == 2
    virtual = dict(id='virtual_yr', tail='y', head='r')
    extended_degrees = degrees(original + [virtual], names4)
    assert all(row['out'] == row['incoming'] == 3 for row in extended_degrees.values())
    assert all(int(('y' in row['shore']) != ('r' in row['shore'])) <= row['undirected'] - 4
               for row in rows4)
    bad_first = audit(flip(original, 'g4_0'), names4)
    assert next(row['out'] for row in bad_first if row['shore'] == ['y']) == 1
    rotation = ['g7_0', 'g4_0', 'g0_0', 'g5_0']
    state = original
    states = [dict(step=0, cuts=rows4)]
    for step, identity in enumerate(rotation, 1):
        state = flip(state, identity)
        rows = audit(state, names4)
        assert all(row['out'] >= 2 for row in rows)
        states.append(dict(step=step, flipped=identity, cuts=rows))
    assert [row['out'] for row in rows4] == [row['out'] for row in states[-1]['cuts']]

    names5 = ['a', 'b', 'c', 'd', 'r']
    control5 = edges_from_groups([
        ('a', 'b', 1), ('b', 'a', 2), ('a', 'c', 1),
        ('d', 'a', 1), ('r', 'a', 1), ('c', 'b', 1),
        ('d', 'b', 1), ('r', 'b', 1), ('c', 'd', 1),
        ('d', 'c', 1), ('c', 'r', 2), ('r', 'd', 1)])
    rows5 = audit(control5, names5)
    degrees5 = degrees(control5, names5)
    assert len(control5) == 14
    assert [degrees5[v]['degree'] for v in names5] == [6, 6, 6, 5, 5]
    assert all(row['out'] >= 2 and row['incoming'] >= 2 for row in degrees5.values())
    assert min(row['undirected'] for row in rows5) == 5
    mincut_shores = [row['shore'] for row in rows5 if row['undirected'] == 5]
    assert {tuple(shore) for shore in mincut_shores} == {
        ('a', 'b', 'c', 'd'), ('d',), ('a', 'b', 'c', 'r'), ('r',)}
    assert next(row['out'] for row in rows5 if row['shore'] == ['a', 'b']) == 1
    noncritical = [e['id'] for e in control5
                   if not any((e['tail'] in shore) != (e['head'] in shore) for shore in mincut_shores)]
    assert len(noncritical) == 5
    result = dict(
        scope='two prescribed controls; no orientation census and no component claim',
        eulerian_projection=dict(k=2, vertices=names4, edges=original, virtual=virtual,
                                 degrees=extended_degrees, illegal_first_cuts=bad_first,
                                 legal_rotation=rotation, word_states=states),
        five_vertex_degree_gap=dict(k=2, vertices=names5, edges=control5,
                                    degrees=degrees5, cuts=rows5,
                                    mincut_shores=mincut_shores,
                                    noncritical_physical_edges=noncritical),
        passed=True)
    destination = root / 'data' / 'synthesis_controls_certificate.json'
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    files = [Path(__file__).resolve(), destination]
    hashes = {str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest() for path in files}
    (root / 'data' / 'synthesis_controls_sha256.json').write_text(
        json.dumps(hashes, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(dict(passed=True, eulerian_control_edges=11,
                         legal_rotation_steps=4, degree_gap_control_edges=14,
                         five_vertex_mincut_count=len(mincut_shores),
                         degree_gap_pair_out=1, noncritical_edges=5)))


if __name__ == '__main__':
    main()
