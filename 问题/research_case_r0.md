# Pure extra cycle, common fiber R0: rigorous closure

Date: 2026-10-02. This note is a new mathematical derivation, not a promotion of assertions in the pasted research prompt. The master archive has not been edited by this worker.

## Reading and provenance

- Read master archive lines 1–890, its entire current-status layer.
- Read master archive lines 2901–5500 in full as allocated historical coverage.
- Read the pasted long research prompt. Its claims beyond the current layer are treated as unverified prior assertions.
- A full-file text search found `source-free`, `zero-extreme`, and `essential private witness` only in the current layer, without complete formal definitions.
- For this note, `cross-free` means that any two rows are disjoint, nested, or co-cover A. The only `zero-extreme` input used is the explicit current-layer assertion Q ⊆ union of MAIN rows. No source-free premise is needed for the theorem below.

## Definitions

Let A be a finite ground set and D an orientation of H on A. For every nonempty proper Y ⊂ A, define

    q(Y) = min{R(Y), S(A−Y)},
    p(Y) = k−q(Y),
    s(Y) = d_D^+(Y)−p(Y),
    μ(Y) = |δ_H(Y)|−p(Y)−p(A−Y).

Assume R,S are nonnegative integer modular boundary-count functions, their totals are (k,k+1) or (k+1,k), every residual cut is feasible s(Y)≥0, and μ(Y)≥1 for every nonempty proper Y. Call Y actual-tight if s(Y)=0.

Let X_1,…,X_r be pairwise disjoint nonempty proper actual-tight MAIN rows, and put R0=A−union_j X_j. Let Z_1,…,Z_t be pairwise disjoint nonempty proper actual-tight extra rows, where t≥2. Put Q=A−union_i Z_i. Assume

1. every MAIN/extra pair is cross-free;
2. R0 meets every Z_i;
3. Q is nonempty and Q⊆union_j X_j.

The common-fiber-R0 three-cycle of the current layer has these properties: each Z_i contains an endpoint of its private edge h_i in R0, and t=3.

## Lemma 1: exact terminal partition skew

For any nontrivial partition A=P_1⊔…⊔P_m, write

    Φ(P) = sum_a [q(A−P_a)−q(P_a)].

Then Φ∈{0,1} if (R(A),S(A))=(k,k+1), and Φ∈{−1,0} if the totals are reversed.

Proof for totals (k,k+1). Set r_a=R(P_a), s_a=S(P_a), t_a=r_a+s_a. Directly from the two minima,

    q(A−P_a)−q(P_a)
      = s_a−r_a−1_{t_a≥k+1}.

For t_a≤k both minima choose r_a and s_a, respectively. For t_a≥k+1 they choose k+1−s_a and k−r_a, respectively. Because all counts are integers these are exhaustive cases. Since sum_a t_a=2k+1, at most one part has t_a≥k+1. Therefore

    Φ = 1 − #{a:t_a≥k+1} ∈ {0,1}.

Swapping R and S changes the sign of q(A−Y)−q(Y), proving the reversed case. □

## Lemma 2: no nontrivial actual-tight partition, including the sign audit

For every partition P as above,

    2 sum_a s(P_a) = sum_a μ(P_a) − Φ(P).

Indeed, if b_D(Y)=d_D^+(Y)−d_D^+(A−Y), then

    2s(Y)−μ(Y)=b_D(Y)+q(Y)−q(A−Y).

The divergence terms sum to zero over a partition. This establishes the stated identity; the sign of Φ is MINUS on the right. If all P_a are actual-tight, then sum_a μ(P_a)=Φ(P)≤1, while μ(P_a)≥1 and m≥2 force sum_a μ(P_a)≥m≥2, a contradiction. □

## Theorem 3: common-R0 disjoint-extra cover is impossible

Under the definitions and assumptions above, no such system exists. In particular, the pure ALL-D three-extra common-fiber-R0 branch is impossible under the current layer's explicit geometry and tightness assumptions.

Proof. Fix X_j and Z_i. Since Z_i∩R0 is nonempty and X_j∩R0 is empty, Z_i cannot be a subset of X_j. Because t≥2, choose i'≠i. A point in Z_i'∩R0 lies outside both X_j and Z_i, so X_j∪Z_i≠A. Cross-freeness leaves only the possibilities X_j⊆Z_i or X_j∩Z_i=∅.

Consequently each X_j is contained in a unique Z_i if it meets any extra row, and otherwise X_j⊆Q. Let J_Q={j:X_j⊆Q}. The cover assumption Q⊆union_j X_j gives

    Q = disjoint union_{j∈J_Q} X_j.

As Q is nonempty, J_Q is nonempty. It follows that

    A = Z_1 ⊔ … ⊔ Z_t ⊔ disjoint union_{j∈J_Q} X_j

is a partition into at least t+1≥3 nonempty actual-tight rows. Lemma 2 rules it out. □

For t=3 the contradiction has at least four tight parts, hence sum μ≥4 while Φ≤1. There is no narrow equality case or dependence on k=2.

## Scope and unused assumptions

The proof needs none of the following: source-free arc directions, inclusion minimality of the family, essential/private status of a witness, MAIN cycle witness edges, the number of edges in the extra cycle, a fixed value of k, or the tentative assertion that two MAIN row types must both occur.

It only uses the explicit MAIN disjointness, extra disjointness, cross-freeness, R0∩Z_i≠∅, coverage of Q by MAIN, actual tightness in the SAME orientation, residual margins, and true-critical endpoint counts.

This is a branch closure, not a proof of the main connectivity conjecture. It also does not independently establish the asserted reduction that all three private edges must lie in one common MAIN fiber.

## Corollary 4: laminar actual-tight covers are impossible

In the same true-critical residual setting, a laminar family of nonempty proper actual-tight subsets cannot cover A. The inclusion-maximal rows in a finite laminar cover would give a nontrivial actual-tight partition. This explains the common-R0 contradiction geometrically: the given row family becomes laminar, and its maximal rows cover A.

More generally, any finite cross-free family of nonempty proper actual-tight rows covering A must contain a co-cover pair U,V with U∪V=A. Otherwise it is laminar and the same contradiction applies.

## Continuing direction

The proof automatically handles every t≥2 common-R0 disjoint-extra configuration that meets the same cover assumptions. The unresolved three-extra common-fiber case is F=X*. A further question is whether common-fiber equality is itself needed: this note suggests auditing whether any R0 intersections with all three extra rows already force the same maximal-tight-partition contradiction, regardless of selected witnesses.

## Lemma 5: common-fiber equality, now proved from set geometry

Assume only that MAIN rows X_1,…,X_r are pairwise disjoint, extra rows Z_1,…,Z_t are pairwise disjoint, and every MAIN/extra pair is cross-free. Define the MAIN fibers as X_1,…,X_r,R0 with R0=A−union_j X_j.

Consider any physical edges joining distinct extra rows, each of which is MAIN-neutral, meaning both its endpoints lie in one MAIN fiber. Build an undirected auxiliary graph on the extra rows by placing an edge i—j for every selected physical edge joining Z_i and Z_j. All selected edges in any connected component of this auxiliary graph with at least one edge have the SAME MAIN fiber.

Proof. It suffices to compare two selected edges e,f incident with a common extra row Z. Each has its other endpoint outside Z.

Suppose e lies in a MAIN row X and f lies in a different fiber F. The Z-endpoint of e belongs to X∩Z, the other endpoint of e belongs to X−Z, and the Z-endpoint of f belongs to Z−X. Thus X and Z intersect and neither contains the other. Cross-freeness forces X∪Z=A. But the OTHER endpoint of f lies outside Z, hence lies in X, contradicting f being wholly in a different MAIN fiber F, which is disjoint from X.

This handles distinct MAIN rows and MAIN versus R0 simultaneously. If the first edge lies in R0 and the second lies in a MAIN row, swap their names. Thus incident selected edges have the same fiber; propagate along the auxiliary component. □

No tightness, q arithmetic, source-free predicate, zero-extreme condition, edge directions, or nonempty Q is required for this lemma. In particular, for a directed extra cycle Z_1→…→Z_t→Z_1 with all private edges MAIN-neutral, all private edges lie in one common MAIN fiber. This independently proves the common-fiber assertion made in the pasted prompt, and generalizes it to every t≥2 and any connected inter-extra edge pattern.

## Combined conclusion for the current three-extra branch

The current-layer assumptions alone give common-fiber equality by Lemma 5. If that fiber were R0, each extra row meets R0, and Theorem 3 gives the forbidden tight partition. Hence every surviving connected MAIN-neutral extra-edge pattern on pairwise disjoint actual-tight extra rows must lie entirely in one MAIN row X*, provided Q is nonempty and covered by MAIN as in Theorem 3.

This deduction needs no interpretation of `source-free` beyond the statements already explicit in the archive.
