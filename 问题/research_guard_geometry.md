# Guard geometry and source closure — 2026-10-02

Scope: this note uses revised B0.2: extra-negative rows block a relative source; MAIN positive service is a separate trigger. All rows and all signs below are evaluated at the same fixed orientation D. No assertion here identifies a relative source with a globally legal flip.

## 1. Exact logical representation

For a retained family S⊆E, source-freeness is exactly

`(P_E(g) ∩ S ≠ ∅ or M+(g)) ⇒ N_E(g) ∩ S ≠ ∅`

for every relevant physical edge g. In Boolean variables x_X=1 iff X∈S, each positive target Y∈P_E(g) supplies the dual-Horn clause `¬x_Y ∨ ⋁_{X∈N_E(g)} x_X`; MAIN supplies `⋁_{X∈N_E(g)} x_X`.

Consequences, without geometric hypotheses:

* Arbitrary unions of source-free families are source-free.
* Intersections need not be source-free. Thus source-free supersets of a seed need not have a least member.
* Subfamilies of original cross-free E remain cross-free, and original actual-tight rows remain actual-tight at the unchanged D.
* Every add-one-deleted-guard step strictly increases row cardinality. Since original E is source-free, an applicable source always has a deleted guard. Hence every such process terminates in at most |E−S| additions. The substantive questions are properness, usefulness and canonicality, not finiteness/cross-freeness/tightness.

In complementary deletion variables z_X=1−x_X, the clauses are Horn implications: deletion of every negative guard of g forces deletion of every positive target of g; a MAIN trigger forbids deletion of every negative guard.

Given a candidate universe U⊆E, start with all rows E−U deleted and saturate these Horn implications. If a MAIN forbidden clause is reached, no source-free subfamily of U exists. Otherwise the undeleted rows form the unique greatest source-free subfamily of U. Consequently there exists source-free T with seed S⊆T⊆U iff saturation does not fail and does not delete a seed row. This is an exact obstruction certificate, even though the smallest admissible enlargement of S can be nonunique.

## 2. Cross-free chains of guards

Let g:u→v. Then N_E(g) consists precisely of rows containing u and excluding v. Two such rows have nonempty intersection (u belongs to it) and proper union (v is outside it). Cross-freeness therefore forces them to be nested. Thus **N_E(g) is an inclusion chain**. The same proof with u,v exchanged shows P_E(g) is a chain.

For X∈N_E(g), Y∈P_E(g), the exclusive atoms X−Y and Y−X contain u and v respectively. Cross-freeness forces either X∩Y=∅ or X∪Y=A. In particular, negative and positive chains interact only through the disjoint/co-cover relation.

When N_E(g) is nonempty it has a unique smallest and largest row. These are canonical guard choices. A particularly robust canonical enlargement is the following *stronger-than-necessary* monotone rule: whenever P_E(g) meets the current set or M+(g)=1, add the smallest member of N_E(g), whether or not another guard is already present. Its least fixed point is finite, independent of rule order, and source-free. Original source-freeness ensures every triggered edge has nonempty N_E(g). The maximum-guard version has the same properties. Neither version is yet shown proper or terminally useful; both may overshoot.

## 3. Minimal source-free families versus minimal FULL-supportable cores

If T is inclusion-minimal among nonempty source-free families and |T|≥2, then deleting any row X leaves a nonempty family which is not source-free. Choose its resurrected source g. Since T was source-free, N_E(g)∩T={X}; since T−{X} has a source, P_E(g)∩(T−{X})≠∅ or M+(g)=1. Hence every X has a support-capable private witness relative to T: **T is FULL-SUPPORTABLE**.

This does not assert T is a *minimal* FULL-SUPPORTABLE family. Applying the exact minimal-FULL C_t theorem directly to T would be invalid.

If T is instead minimal among source-free supersets of a prescribed seed S*, the argument only applies to X∈T−S*. Thus the new guard rows have private support-capable witnesses, while seed rows need not gain this property from source-closure minimality.

## 4. ALL-D core localization

Suppose core shores Z_1,…,Z_t are pairwise disjoint, and a resurrected source g has P(g)∩core≠∅ but N(g)∩core=∅. Its head lies in exactly one core shore Z_i, and its tail lies in Q=A−⋃_j Z_j. In particular, P(g)∩core={Z_i}, and every negative guard contains the tail in Q and excludes the head in Z_i.

No negative guard can be a subshore of any Z_j. Cross-freeness with the disjoint core gives a sharper trichotomy for any additional shore W: W is contained in a core shore; A−W is contained in a core shore; or every core shore is either wholly included in W or wholly excluded from W. For a negative guard of g the first alternative is impossible; in the second alternative the omitted subshore must lie in Z_i and contain the head. In the third alternative W excludes all of Z_i.

This classifies where guard rows can live without asserting that their addition preserves zero-extreme or produces a terminal contradiction.

## Current frontier

The private-witness digraph of a minimal source-free T is FULL-supported, but the usual minimal-FULL Hamiltonian-cycle classification cannot yet be transferred. The next audit asks whether cross-free N-chain geometry forces its private-witness digraph to be strongly connected, or whether a multi-negative guarded edge can connect otherwise separate private SCCs. Pure sign hypergraphs permit the latter; their smallest examples violate the N-chain restriction.

## 5. Private SCC common-fiber lemma

Assume T is cross-free and contains no complementary pair. This last assumption follows for same-D actual-tight rows from `s_D(X)+s_D(A−X)=μ(X)≥1`.

Form the ALL-private service digraph: X→Y if some physical g has N(g)∩T={X} and Y∈P(g)∩T. Let C be a terminal strongly connected component of this digraph. Every private witness whose negative row is in C is neutral on all rows W∈T−C: it has no other negative row by privacy, and a positive outside row would create an outgoing arc of the terminal SCC.

For distinct cross-free, noncomplementary shores X,W, an edge crossing X and neutral on W has a forced W-side, independent of whether its sign on X is negative or positive:

* X⊊W or X∪W=A: both endpoints lie in W;
* W⊊X or X∩W=∅: both endpoints lie outside W.

These cases are mutually consistent precisely because complementary pairs were excluded. Thus if a private witness supplies X→Y inside C, the forced W-side of X equals that of Y. Strong connectivity propagates this equality to every row in C, for every W outside C. Hence **all private witnesses attached to a terminal SCC lie in one common atom of T−C**.

This is a localization theorem, not a source-free deletion theorem. Physical edges with multiple negative rows inside C can still leave the common fiber and provide omitted positive service.

## 6. Minimal source-free private digraph need not be strongly connected: exact geometric control

The tempting purely geometric assertion that a minimal source-free cross-free family has one private-witness SCC is false.

Let A={a,b1,b2,c,d} and

`Z1={a,c,d}, Z2={b1,b2,c}, Z3={b1}, W={d}`.

These four shores are cross-free and have no complementary pair. Use the following five physical directed edges:

| edge | negative rows | positive rows |
| --- | --- | --- |
| a→b1 | Z1 | Z2,Z3 |
| b2→a | Z2 | Z1 |
| b1→c | Z3 | Z1 |
| b1→d | Z2,Z3 | Z1,W |
| d→c | W | Z2 |

Every edge has a negative row, so T={Z1,Z2,Z3,W} is source-free. If a nonempty source-free subset contains any core row, the first three edges force it to contain all Z1,Z2,Z3. The last edge then forces W. If it only contains W, the edge b1→d forces Z2 or Z3 and the preceding argument applies. Hence T is inclusion-minimal among nonempty source-free families.

Its ALL-private digraph has terminal SCC C={Z1,Z2,Z3}, with W→Z2; no private arc leaves C. The return dependency uses b1→d, whose negative set has two nested guards Z3⊊Z2. Thus the inclusion-chain restriction alone does not force private strong connectivity.

**Scope:** this is an exact sign/geometric control, not a terminal-realization claim. It has five nonempty membership atoms and four rows. The root agent's new terminal atom-budget inequality `n≤t` therefore rules out same-D actual-tight true-critical terminal realization of this bare family for every k. The counterexample nevertheless closes the geometry-only SCC shortcut.

The common fiber in Section 5 is A−W={a,b1,b2,c}. The edge b1→d leaves it with two negative core guards. This makes the precise surviving question visible: can the true-critical surcharge force the multi-negative edge to expose an additional private outgoing interface after accounting for empty nodes or extra rows?

## 7. Tiny finite geometry check

`scripts/guard_scc_geometry_probe.py` checks all 552 cross-free no-complement families on four atoms, and 158 FULL-supported candidate terminal splits, with no MAIN triggers. It finds no minimal-source-free family with a proper terminal private split. The maximal allowed edge-set reduction makes this finite symbolic control exhaustive; its scope is only four-atom membership geometry. Raw output: `data/guard_scc_geometry_probe.json`.

The explicit five-atom construction above explains why extending this check into a larger census would not produce the missing terminal theorem; theoretical terminal inequalities are needed instead.

## 8. Empty-node interface in the split tree

Choose an arbitrary ground vertex r and replace each shore X containing r by A−X. Cross-free shores with no complementary pair become a laminar family, hence admit the standard tree of splits. There are t edges/rows and t+1 tree nodes; physical membership atoms occupy some of these nodes. Consequently the root agent's terminal atom bound n≤t forces at least one unoccupied node.

At an unoccupied node, incident branch sets U_1,…,U_d partition A. The corresponding actual-tight retained rows have the form U_i for i∈I and A−U_j for j∈J.

If J is empty, the incident rows form an actual-tight partition. If I is empty, they form an actual-tight co-partition. Both are excluded by the locked terminal theorem. Thus **every empty split-tree node of a hypothetical terminal source-free closure must be mixed**.

There is also an exact local conservation law, valid before any source-free argument. Write μ_i=μ(U_i). Tightness gives

`d_D^+(U_i)−d_D^−(U_i) = q(A−U_i)−q(U_i)−μ_i` for i∈I,

and

`d_D^+(U_j)−d_D^−(U_j) = q(A−U_j)−q(U_j)+μ_j` for j∈J.

Summing over the partition cancels internal arc divergence, so

`Σ_{i∈I} μ_i − Σ_{j∈J} μ_j = Φ`, where `Φ=Σ_i[q(A−U_i)−q(U_i)]`.

The critical boundary skew yields Φ∈{0,1} when (R(A),S(A))=(k,k+1), or Φ∈{−1,0} under the opposite signature. Hence a mixed empty node balances two positive integral μ-masses to within one unit. On the fully saturated face μ_i=1, its numbers of normal and complementary incident rows differ by at most one; the allowed sign of that difference is determined by the boundary signature.

An arc from a J-branch into an I-branch has positive sign on both incident rows and negative sign on neither. Source-freeness therefore requires at least one deeper negative guard within those two branches. This is a precise recursive interface: **mixed empty-node transit forces deeper guards**, while local μ-mass conservation prevents pure-star termination. A proof that this recursion must either produce an unguarded transit, a tight partition/co-partition, or a private SCC merge is still open.

No claim is made here that n≤t alone resolves this mixed-node recursion, or that source-free closure must contain only one SCC.

## 9. New restriction: a mixed empty node in a FULL-supported family has at least two branches of each polarity

Suppose every retained row has a support-capable private witness relative to the entire T. This follows from minimal nonempty source-freeness when |T|≥2, but does not automatically follow for a seeded minimal source closure.

At the empty node of Section 8, a private witness negative on the incident normal row U_i has its tail in branch i and its head in another branch. If the head belonged to a complementary branch j∈J, the edge would also be negative on A−U_j. Privacy forbids this. Therefore its head must lie in a different normal branch i'∈I. In particular |I|≥2.

A private witness negative on the incident complementary row A−U_j has its head in branch j and tail in another branch. If its tail belonged to a normal branch i∈I, it would also be negative on U_i. Therefore its tail lies in another complementary branch j'∈J, so |J|≥2.

Thus **every mixed empty node has degree at least four**, with at least two normal and two complementary incident branches. This is unconditional cross-free geometry plus FULL-supportability, and does not use residual demand or MAIN neutrality. In particular, every mixed trivalent empty-node configuration is impossible even when deeper guards are present.

For a hypothetical inclusion-minimal nonempty source-free terminal family, pure empty nodes are already excluded by no-tight-partition/co-partition. Consequently all empty nodes have degree at least four. If e is the number of empty split-tree nodes and n the number of occupied nodes, the tree degree sum implies

`n ≥ 2e+2`, and `t=n+e−1`.

This quantitatively restricts the terminal atom-budget frontier. It remains weaker than a complete exclusion, but identifies which signed empty-node degrees need further analysis.

## 10. Tree packing closes the general cross-free actual-tight source-free obstruction

This section supersedes the open mixed-node recursion in Sections 8–9 **within the initial true-critical, all-physical-edge scope below**. The counterexamples and logical closure results retain their stated abstract scope.

### Statement

Let A be a true critical shore in a global orientation D of G, with λ(G)≥2k+1 and |δ_G(A)|=2k+1. Let q(X)=min{R(X),S(A−X)} and assume D's internal restriction is residual feasible. Let T be a nonempty cross-free family of nonempty proper actual-tight shores of A. If source-freeness is checked on **every internal physical edge** as in revised B0.2, then T cannot be source-free.

Equivalently, some internal edge g has N_T(g)=∅ and P_T(g)≠∅. Its flip may still be blocked by omitted actual-tight rows; this conclusion alone does not give global connectivity or a globally legal flip.

The argument uses the locked no-tight-partition/co-partition consequence, but not minimal FULL-supportability, zero-extreme, selected witnesses, or MAIN-neutrality.

### Proof

Actual-tight complementary rows cannot both occur, because their two slacks sum to μ≥1. Represent T by its tree of splits. Its t row edges and t+1 nodes consist of n occupied membership atoms and e empty nodes, so t=n+e−1. Since T is nonempty and every row proper, n≥2.

Let M be the number of physical internal edges joining different membership atoms. For each such edge g, write ν(g)=|N_T(g)|. Its membership changes across at least one row. If ν(g)=0, it has a positive row and is a relative source. Under the hypothetical source-free assumption, ν(g)≥1. Put

`σ=Σ_{g interatom}(ν(g)−1)≥0`, and `Q=Σ_{X∈T}q(X)≥0`.

Summing tight outgoing-cut equations counts each physical interatom edge exactly ν(g) times:

`M+σ = Σ_X d_D^+(X) = tk−Q`.

Contract each membership atom and also contract B=V−A. The resulting n+1 vertex multigraph retains edge-connectivity at least 2k+1. It has M internal interatom edges and exactly 2k+1 boundary edges. Its degree sum implies

`M ≥ ceil((n−1)(2k+1)/2) = (n−1)k+ceil((n−1)/2)`.

Therefore

`Q+σ = tk−M ≤ ek−ceil((n−1)/2) < ek`.    (upper bound)

For each empty tree node v, remove v and let its incident branch sets partition A. Orient every tree edge toward the side equal to its original row shore. Let I_v be the outgoing incident edges, whose row shores are the corresponding branch sets. Let U_v be their union. A pure empty node would give an actual-tight partition or co-partition, which the locked terminal consequence excludes. Thus I_v and its complement among incident edges are both nonempty, and U_v is a nonempty proper shore.

First, q is submodular and q(∅)=0. Indeed, with nonnegative additive weights r(X)=R(X), s(X)=S(X) and S_0=S(A),

`q(X)=r(X)−[r(X)+s(X)−S_0]_+`.

The positive-part of a nonnegative modular sum is supermodular, so q is submodular. Since the outgoing branch shores at v are disjoint,

`q(U_v) ≤ Σ_{X∈I_v}q(X)`.

Crucially, a row edge is outgoing at exactly one of its two tree endpoints. Thus the sets I_v, over distinct empty nodes, are pairwise disjoint row sets. Since every q(X)≥0,

`Σ_{v empty} q(U_v) ≤ Q`.    (row-q packing)

Second, every physical edge g leaving U_v transits the empty node from an outgoing branch into an incoming branch. The two consecutive row edges of its tree path both have negative sign on g. For an interatom edge with ν(g) negative row crossings, the number of adjacent negative-negative pairs on its entire tree path is at most ν(g)−1. Each empty-node transit counted by d_D^+(U_v) is one such pair, and distinct empty nodes supply distinct adjacent pairs. Summing over g gives

`Σ_{v empty} d_D^+(U_v) ≤ σ`.    (negative-pair packing)

Residual feasibility at each proper U_v supplies `d_D^+(U_v)+q(U_v)≥k`. Sum over all e empty nodes and apply the two packing bounds:

`ek ≤ Σ_v[d_D^+(U_v)+q(U_v)] ≤ σ+Q`.    (lower bound)

This contradicts the strict upper bound. When e=0 the upper bound already contradicts Q+σ≥0. Thus no hypothetical source-free T exists. ∎

### Audit boundaries

* This is an initial true-critical theorem. It uses the original nonnegative q and all internal physical edges. It does not transfer to an abstract signed descendant checked only on K.
* Parallel physical edges retain identity throughout M, ν and degree sums.
* No assertion about source legality on the omitted full cut system is used.
* The split-tree representation must retain empty internal nodes. Erasing them would lose the deficit ek and the packing interface.
* No external orientation-polytope, integrality, or adjacency theorem enters the proof.

The remaining global gap is the necessity bridge: minimum full-fiber separation has not yet been shown to supply a cross-free actual-tight family which is source-free for all internal physical edges. The theorem excludes such a supplied family; it does not manufacture one.

## 11. Quantitative strengthening: many relative sources

The root agent's quantitative extension passes an independent audit of both packings. Drop the hypothetical source-free condition. Let Z count physical interatom arcs with ν(g)=0, and now define `σ=Σ_g max{ν(g)−1,0}`. Every ν=0 interatom edge has a positive row, hence is a strict source under revised B0.2.

The exact tight-row identity becomes

`M−Z+σ = tk−Q`.

The empty-node lower bound Q+σ≥ek is unchanged: an edge with ν=0 contributes no adjacent negative-negative pair, and the number of such pairs for every other edge is bounded by max{ν−1,0}. Thus

`M ≤ (n−1)k+Z`.

Combining with the quotient degree lower bound gives

**`Z ≥ ceil((n−1)/2)`**.

So every nonempty cross-free actual-tight family in the stated initial true-critical/all-H scope has at least ceil((n−1)/2) relative-source physical edges, where n is its number of nonempty membership atoms. The sources can all have omitted negative guards, so this still supplies no direct legal-path theorem.

The formal root write-up is `research_crossfree_source_theorem.md`; this note supplies the guard-chain, common-fiber and split-tree audit interfaces used in its derivation.

## 12. Negative-guard uncrossing yields a compatible actual-tight extension

This section stays in the initial true-critical/all-H scope of Section 10.

### Actual-tight crossing identity

For crossing actual-tight W,Y, put I=W∩Y and U=W∪Y. Both are nonempty proper shores. Directed outcut submodularity gives

`d^+(W)+d^+(Y) = d^+(I)+d^+(U)+m_H(W−Y,Y−W)`.

Since q is submodular, p=k−q is crossing-supermodular. Residual feasibility and tightness therefore force equality throughout:

`s_D(I)=s_D(U)=0`, `m_H(W−Y,Y−W)=0`, and the demand supermodular defect is zero.

In particular, no physical edge can have opposite signs on crossing actual-tight rows: that would be a physical petal edge.

### Guard-extension lemma

Let T be cross-free actual-tight, and let g satisfy N_T(g)=∅. A relative source is one possibility, but g may also be neutral on every retained row. If g has any negative actual-tight blocker W in the full residual cut system, it has such a blocker W' which is cross-free with every retained row of T.

Proof: choose W among negative actual-tight blockers to minimize its number of crossings with T. If W crosses Y∈T, g cannot be positive on Y by the zero-petal identity, and cannot be negative because N_T(g)=∅. Thus it is neutral on Y. If both endpoints lie in Y, replace W by W∩Y; if both lie outside Y, replace W by W∪Y. The chosen corner is actual-tight and remains negative on g.

The following elementary geometric fact makes the crossing count strictly decrease: if W crosses Y, and Z is cross-free with both W and Y, then each of W∩Y and W∪Y is cross-free with Z. For the intersection, inspect the four possibilities Z⊂Y, Y⊂Z, Y∩Z=∅, Y∪Z=A; the first and last cases use W crossing Y to exclude the otherwise problematic nesting/cover alternatives. The union follows by complementing all three sets. Consequently no previously compatible Z∈T becomes crossing, while the crossing with Y disappears. This contradicts minimality of W unless W was already compatible with all T. ∎

### Consequence for maximal cross-free tight families

Take a maximal cross-free family T of actual-tight rows, assuming at least one actual-tight row exists. Every relative source of T is globally legal in the residual fiber: otherwise the guard-extension lemma would add a new compatible actual-tight negative blocker. It cannot already belong to T because the edge is a relative source.

More generally, maximal T covers exactly the full illegal-edge set: a physical edge is globally illegal iff N_T(g)≠∅. The forward implication is guard extension and maximality; the reverse is immediate tightness. Consequently every physical edge lying within a membership atom of maximal T is also globally legal at D. If M_intra counts those internal-atom physical edges, the total number of legal internal flips is at least `M_intra+ceil((n−1)/2)`.

Thus Section 11 guarantees at least ceil((n−1)/2) globally legal internal physical flips at this maximal family, each improving some retained tight row. This is a **no-frozen-state statement for the initial full fixed-outside fiber**, not a connectivity theorem. A frozen-J descendant may retain no such legal edge in K, and components of the full fiber may still in principle have several states.

This consequence is conditional only on the initial endpoint formula, residual feasibility, μ≥1 and λ≥2k+1 used in Section 10. It does not rely on a source-preserving laminarization of an arbitrary whole blocker family: it uncrosses one blocker relative to an already cross-free retained family.

## 13. Exact update under one legal flip

Let g:u→v be globally legal at D and let D' reverse g. Every old actual-tight row has δ_g≥0. The old rows split into neutral rows (still tight) and positive rows (their slack becomes one). The genuinely newly tight rows are exactly those X with `s_D(X)=1` and `δ_g(X)=−1`. Reversing g back is legal by history, and is positive on every newly tight row.

For an old maximal cross-free blocker cover T, its neutral subfamily T^0 remains cross-free and actual-tight at D'. It can be extended to a maximal cross-free blocker cover at D' by the guard-extension theorem. Such an extension need not consist only of newly tight rows: old actual-tight rows omitted from T can become compatible after the positive chain P_T(g) is removed. This is a second, dynamical form of row resurrection.

For h≠g that was globally legal at D but becomes illegal at D', its blocking cut is necessarily genuinely newly tight: an old neutral tight row cannot block h because it would already have blocked h at D. Thus there is a row X with

`s_D(X)=1`, `δ_g(X)=δ_h(X)=−1`.

This is an exact one-slack collision. Both single flips are legal from D, but no ordering of just {g,h} can be completed through this row. A third move is needed to supply slack.

Conversely, if h was illegal at D and becomes legal at D', **every old actual-tight blocker of h must be positive on g**; an old neutral blocker would remain tight. For a retained maximal cover T this implies the necessary condition

`N_T(h) ⊆ P_T(g)`.

Since both sets are inclusion chains, a first-step unlock can only remove a chain of blockers serviced by g. This condition is not sufficient: omitted old blockers or newly tight rows can still obstruct h. In particular the update cannot be represented by simply deleting N_T(h) from the old cover.

## 14. Conditional common-balanced blocker cover for a line descendant

This proposition is conditional on the externally audited hypothesis that the frozen-J reversal polytope on K is exactly `[0,1]·1`, with |K|≥2. It does not reclassify the frozen-J face as an initial system.

Consider the two full residual endpoint orientations R and Rbar, differing on every K-edge and agreeing on J. Let F_c be their common actual-tight rows. Every X∈F_c is K-balanced: `Σ_{h∈K}δ_h(X)=0`.

At the midpoint of the line polytope, all box bounds are inactive. Its active cut inequalities are precisely F_c. Hence their tangent cone is the one-dimensional linear space span{1}. For each coordinate h, neither e_h nor −e_h lies in this tangent cone. Therefore some common row has δ_h<0 and another common row has δ_h>0. Thus every K-edge has both a negative and a positive common-tight blocker.

Common-tight rows are closed under crossing intersection/union: each corner is actual-tight at R by the initial uncrossing identity, and independently actual-tight at Rbar by the same identity. Take a maximal cross-free subfamily T_c⊆F_c. Apply the negative-guard extension lemma at R and at Rbar, with guards constrained to F_c; corner closure keeps that constraint. It follows that

`N_{T_c}(h)≠∅` and `P_{T_c}(h)≠∅` for every h∈K.

Thus the line descendant admits a **cross-free, common-tight, K-balanced blocker cover at both endpoints**. Source-freeness on every physical edge is not asserted. The source theorem implies that T_c has relative-source physical edges, necessarily outside K; these are ancestral candidates in J. They may still have endpoint-specific blockers, so common legal launch is not proved.

For an endpoint-specific row define the signed K-height `τ(X)=s_Rbar(X)−s_R(X)=Σ_{h∈K}δ_h(X)`. An R-tight noncommon row has τ>0; an Rbar-tight noncommon row has τ<0. Consequently any obstruction to an ancestral candidate which is a source on T_c comes from a nonzero-height endpoint row. This is the exact interface for a two-endpoint guard or launch argument; there is no generic sign reason forcing both endpoints to accept the same launch.

## 15. Single-path and physical-circuit endpoint distinctions

### One physical directed path

Suppose K is one directed physical path from s to t, in its R orientation. Then `τ(X)=1_X(t)−1_X(s)` for every row. A J-edge g which is illegal at both endpoints has a common actual-tight negative blocker.

To prove this, take an R-tight negative blocker X and an Rbar-tight negative blocker Y. If either is common, the claim is immediate. Otherwise τ(X)=1 and τ(Y)=−1. Thus t∈X−Y and s∈Y−X. Since g leaves both rows, its tail lies in X∩Y and its head outside X∪Y, making X,Y crossing. Their intersection I excludes both s,t and their union U includes both, so τ(I)=τ(U)=0. At R, s(X)=0 and s(Y)=1. The crossing identity and p-supermodularity give `s(I)+s(U)≤1`. Both slacks are nonnegative integers and unchanged between endpoints, so at least one of I,U is common actual-tight. The same g leaves both I and U, proving the claim.

Consequently an ancestral candidate with no common negative blocker is legal at at least one endpoint. This does **not** imply it is legal at both. Applied to the common maximal cross-free cover of Section 14, every relative-source J-edge can launch from at least one of the two endpoints. The two endpoint components may accept different launches.

### One physical directed circuit

If K is a directed physical circuit, τ≡0. Thus every residual cut has exactly the same slack at R and Rbar, the complete tight-row families coincide, and all J-edge legalities coincide. A maximal cross-free blocker cover supplies genuinely common legal J launches at the two endpoints.

This statement refers to a graph-theoretic physical circuit; it is unrelated to a row/service dependency C_t.

## 16. Minimum separated physical-circuit support is immutable throughout its full components

Assume R,Rbar are in distinct full fixed-outside components and the number m of differing physical edges is minimum among all component-separated pairs. Suppose their difference K is a directed physical circuit.

Along any J-only legal word from R, reversing the entire circuit K gives a simultaneously legal companion word from Rbar, because circuit reversal is cut-neutral at every J signature. The companion states remain in the respective original full components.

If a K-edge h became legal after such a J-only word, flip it from the R-side state to obtain W. The companion Rbar-side state is still feasible in another full component, and W differs from it on only m−1 K-edges. This contradicts the minimum choice.

Therefore no K-edge becomes legal anywhere reachable from R by a J-only word. Any full path containing a K move would have a first such move after a J-only prefix, also impossible. Hence the entire full component of R retains the initial signature on every K-edge. The component of Rbar retains the reversed signature.

The cycle branch thus demands exclusion of a **genuine globally immutable physical circuit**, not merely a frozen-J face. The source theorem ensures legal ancestral moves still exist, but does not by itself prove that one of them eventually unlocks K. An immutable-edge theorem or a component-wise tight-cut invariant is the next missing interface for this branch.

## 17. Exact replacement obligation under a common ancestral launch

For a minimum component-separated pair, any common legal ancestral word preserves the antipodal K difference and the two full components. At its final ancestral signature J', the feasible frozen-J' K-face still has exactly the two antipodal integer states. Otherwise a mixed third state agrees with one endpoint on at least one K coordinate; choosing an endpoint in another full component yields a component-separated pair with fewer than m differing edges.

If the line-polytope hypothesis continues to hold for this minimum descendant, its midpoint active common-tight normal cone must remain the entire `(span{1})^⊥`.

After one common ancestral flip g, the retained old common-tight rows are precisely those neutral on g; lost old common rows are positive on g; newly common-tight rows had slack one at both endpoints and were negative on g. Any directions missing from the cone generated by neutral old common rows must be supplied by normals of newly tight rows. This is stronger than a rank count: even a retained family of rank m−1 can generate only a one-sided cone and still require new blockers.

This gives a precise blocker-transfer necessity without assuming that a transfer decreases nesting depth or history length. The scalar signed K-height τ does not rank these transfers in the circuit branch (τ≡0), and in a path branch it has only the values −1,0,1. Thus τ alone cannot provide a strictly decreasing finite-unlock potential. A second quantity tied to boundary charge, ancestry, or physical path position is needed.
