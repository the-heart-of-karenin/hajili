# Pure three-extra common-fiber case F = X*: symbolic audit

Date: 2026-10-02. Research subtask: `/root/three_cycle_xstar`.

## Scope and provenance

Read the main archive's complete 2026-10-02 current layer, and read historical lines 5501–8000 in full. The historical range concerns degree/quotient formulations, blocker birth, tight-Q entrants, macro-path serialization, auxiliary width, and older search programs; none supplies a fuller definition of the present source-free closure. The user-pasted sprint prompt supplies the more advanced common-fiber geometry. Consequently the theorem below explicitly takes that geometry as an assumption; it does not claim to have proved the common-fiber reduction.

Inputs from the current layer:

- `B0.1`: q(Y) = min{R(Y), S(A−Y)}, p(Y) = k−q(Y), residual feasibility and μ(Y) ≥ 1.
- `C0`: critical boundary totals (k,k+1) or (k+1,k), and partition skew |Φ| ≤ 1.
- `E0.1–E0.3`: actual-tight MAIN/extra rows, ALL-D extra partition Z1,Z2,Z3,Q, Q nonempty, and zero-extreme coverage.
- User-pasted Priority 1 case B: X* = P ⊔ Z2 ⊔ Z3 ⊔ Q, Z1 = C ⊔ P, C = A−X*, and all other MAIN rows and R0 lie inside C.

Here source-free has the following explicit meaning, agreed with the coordinating agent: no physical arc has nonnegative reversal incidence on every family row and strictly positive reversal incidence on at least one row. For an arc u→v the incidence is δ(Y)=1[v∈Y]−1[u∈Y]. Thus an arc from a membership pattern to a strict superset of that pattern is forbidden. No stronger unrecorded meaning of zero-extreme is used.

## Theorem: the supplied F = X* geometry is terminally impossible

### Assumptions

Let H be a directed loopless multigraph on A, with nonnegative integer additive boundary functions R,S and critical totals (k,k+1) or (k+1,k). For every nonempty proper Y⊂A put

    q(Y)=min{R(Y),S(A−Y)}, p(Y)=k−q(Y),
    s(Y)=d_H^+(Y)−p(Y),
    μ(Y)=|δ_H(Y)|−p(Y)−p(A−Y).

Assume s(Y)≥0 and μ(Y)≥1 for all these Y. Suppose the family consists of pairwise disjoint MAIN rows X*=X0,X1,…,Xm, all actual-tight, plus the pairwise disjoint actual-tight rows Z1,Z2,Z3. Write O=R0=A−⋃MAIN. Assume

    A = C ⊔ P ⊔ Z2 ⊔ Z3 ⊔ Q,
    C = O ⊔ X1 ⊔ … ⊔ Xm,
    X* = P ⊔ Z2 ⊔ Z3 ⊔ Q,
    Z1 = C ⊔ P,

where P,Z2,Z3,Q are nonempty. Assume the family is source-free in the explicit sense above. (The private directed triangle ensures P,Z2,Z3 are nonempty, but its actual arcs will not otherwise be needed.)

Then no such system exists.

### Proof

**1. Partition slack and the two remainder slacks.** For every nontrivial partition A=⊔Y_i, set Φ=Σ_i(q(A−Y_i)−q(Y_i)). Directly summing directed cuts gives

    2 Σ_i s(Y_i) = Σ_i μ(Y_i) − Φ.       (1)

The sign in (1) is important. Since |Φ|≤1 and every μ≥1, an actual-tight partition is impossible. Thus O is nonempty: if O were empty, the MAIN rows would form a forbidden actual-tight partition. For the partition into MAIN rows and O, equation (1) gives

    s(O) ≥ 1.                             (2)

For the four-part partition Z1,Z2,Z3,Q, equation (1) gives 2s(Q)≥4−1=3; since slack is integral,

    s(Q) ≥ 2.                             (3)

If there is only one MAIN row, X* is still proper, so O=C is nonempty and the same two-part partition proves (2). Thus no lower bound on the number of other MAIN rows is needed.

**2. Source-free restrictions.** Vertices of Q belong only to X*. Vertices of P,Z2,Z3 belong to X* and an additional extra row. Therefore source-free forbids every arc from Q to P∪Z2∪Z3. Put W=Z2⊔Z3⊔Q. Then

    d_H^+(Q)=e(Q,C) ≤ d_H^+(X*)=k−q(X*).   (4)

Vertices of O belong only to Z1. Vertices of every Xi (i≥1) belong also to their MAIN row, and vertices of P belong also to X*. Hence source-free forbids all O→Xi and O→P arcs. Consequently

    d_H^+(O)=e(O,W) ≤ d_H^+(Z1)=k−q(Z1).   (5)

Here e(U,V) counts arcs directed from U to V.

**3. Forced endpoint branches.** Equations (2)–(5) imply

    q(Q) ≥ q(X*)+s(Q) > q(X*),
    q(O) ≥ q(Z1)+s(O) > q(Z1).             (6)

But Q⊂X* and q(Q)≤R(Q)≤R(X*). Therefore q(X*) cannot equal the R(X*) branch of its minimum. Similarly q(Z1) cannot equal R(Z1). The endpoint formula therefore forces

    q(X*)=S(C),   q(Z1)=S(W).               (7)

This inference is strict and does not assume a preselected R/R/S signature.

**4. Co-cover tightness puts an upper bound on C–W capacity.** The two tight rows X* and Z1 co-cover A, intersect in P, and have exclusive parts W and C. The ordinary directed-cut identity says

    d_H^+(X*)+d_H^+(Z1)
       = d_H^+(P) + m_H(C,W),              (8)

where m_H counts physical edges in both directions. Thus, using (7),

    d_H^+(P)=2k−S(C)−S(W)−m_H(C,W).

Feasibility of P and q(P)≤S(A−P)=S(C)+S(W) give

    m_H(C,W) ≤ k−S(C)−S(W)+q(P) ≤ k.       (9)

**5. The two remainders exceed that capacity.** Every arc leaving Q goes to C, and every arc leaving O goes to W. Both sets of arcs cross C|W, and no physical arc is counted twice. Consequently

    m_H(C,W) ≥ d_H^+(Q)+d_H^+(O)
       = 2k−q(Q)−q(O)+s(Q)+s(O)
       ≥ 2k−R(Q)−R(O)+s(Q)+s(O)
       ≥ 2k−R(A)+s(Q)+s(O).

For R(A)=k this is at least k+3. Even for the opposite boundary orientation R(A)=k+1 it is at least k+2. In either case

    m_H(C,W)>k,                            (10)

contradicting (9). ∎

## Status and limits

This is a symbolic impossibility result for the explicitly stated F=X* terminal geometry, all k, under either critical boundary orientation. It uses neither exhaustive search nor an assumption about full-fiber connectivity. It is stronger than needed inside that geometry: the physical private 3-cycle is used only to guarantee nonempty named atoms.

It does **not** prove the main connectivity theorem. To apply it to the complete three-extra classification, one still needs the common-fiber/geometric reduction supplied by the later sprint prompt, whose full proof is absent from the main archive. The source-free operational definition is stated explicitly to make that interface auditable.

## Earlier partial route, superseded by the capacity contradiction

Before (8) was used, the remainder inequalities suggested that both X* and Z1 must use their S-complement branch and that S(P)−R(P) must absorb several units of pressure. That gives low-k exclusions but does not alone exclude large k. The successful proof avoids a large-k case split: the same two remainder outcuts are disjoint demands on the single C–W physical-edge capacity, and co-cover feasibility caps that capacity at k. This is an exact counting contradiction, not a failed-route assertion.
