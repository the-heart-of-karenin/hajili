# Relative one-unit augmentation — 2026-10-02

## 1. Existence under μ≥2 is proved

Work in the initial true-critical residual system. Let H=G[A], q(X)=min{R(X),S(A−X)}, p(X)=k−q(X), and suppose

`μ(X)=|δ_H(X)|−p(X)−p(A−X)≥2`

for every nonempty proper X⊂A. Then H admits an orientation D* with

**`d_D*^+(X)≥p(X)+1` for every nonempty proper X⊂A.**

This is relative augmentation with the original outside orientation unchanged. It is not global (k+1)-arc-strength, since the fixed critical cut A retains only 2k+1 edges.

### Partition proof

Take any nontrivial partition A=U_1⊔⋯⊔U_t. Let M be its number of physical cross-edges, and put

`a=Σ_i p(U_i)`, `b=Σ_i p(A−U_i)`.

Critical Boundary Skew gives `a−b=Φ`, with |Φ|≤1. Sum the assumed margin:

`2M−a−b = Σ_i μ(U_i) ≥2t`.

Hence `M≥a+t−Φ/2`. Since M and a+t are integers and |Φ|≤1, this implies

`M≥a+t=Σ_i[p(U_i)+1]`.

The same argument gives `M≥b+t=Σ_i[p(A−U_i)+1]`. These are exactly all partition and co-partition orientation inequalities for the augmented demand f(X)=p(X)+1.

### Orientation-theorem scope

Set f(∅)=f(A)=0 and f(X)=p(X)+1 on nonempty proper shores. The initial endpoint demand has 0≤q(X)≤k, so f is nonnegative integer-valued. The formula

`q(X)=R(X)−[R(X)+S(X)−S(A)]_+`

shows q is submodular, and f is crossing-supermodular. Thus it is also crossing H-supermodular. Frank's nonnegative crossing-supermodular orientation theorem applies. The author-hosted primary research paper [Singh–Végh, Theorem 2.1, printed page 276](https://www.laszlovegh.eu/papers/singh-vegh.pdf) explicitly states the partition/co-partition criterion, and its definitions on printed page 273 explicitly note that ordinary crossing-supermodularity implies crossing-G-supermodularity. Their citation is A. Frank, *On the orientation of graphs*, JCTB 28 (1980), 251–261.

The source uses incoming-cut convention. Globally reversing its feasible orientation gives the outgoing-cut convention here with the same f. Parallel edges can be treated as physical copies throughout the partition counts; the cited paper explicitly uses the orientation theorem on multigraphs in its scaling argument immediately after Theorem 2.1.

Therefore the existence conclusion is not conditional on an arbitrary signed-descendant theorem or on a global (k+1)-orientation claim.

## 2. What existence does and does not supply

D* has at least one unit of slack on every proper internal residual cut. Thus every internal physical edge is initially a legal single-edge flip from D* under the original demand p.

This does not prove that an arbitrary residual-feasible D can reach D* by legal physical flips. A monotone sequence using only disagreement edges can fail in generic connectivity-improvement settings; a proof here must exploit the initial true-critical structure and the uniform μ≥2 margin.

The margin μ≥2 also gives every proper membership atom global degree at least 2k+2: writing w(X)=R(X)+S(X), one has q(X)+q(A−X)≤w(X), hence

`|δ_G(X)|=|δ_H(X)|+w(X)≥2k+2+w(X)−q(X)−q(A−X)≥2k+2`.

The outside root still has degree 2k+1. Thus the quotient degree-sum lower bound becomes M≥(n−1)k+n, yielding the stronger cross-free relative-source bound Z≥n. This counts available relative sources; it does not yet identify a progress source which increases a chosen deficient cut.

## Current task

**SUPERSEDED 2026-10-02:** Legal reachability under all proper µ≥2 is now proved in `research_relative_reachability_audit.md`. Its fixed-boundary safe-endpoint paths, HEAVY exception, and ancestor-label phase descent give an actual legal physical word. Combining with the unique strict component in `research_global_scope.md` §14 closes H1 for this µ≥2 initial subcase. General µ=1 remains open. The earlier existence proof and its scope notes above are retained independently.

## 4. Independent audit of the root's fractional empty-tree existence proof

The following gives a second proof of fractional existence, without the partition/co-partition orientation theorem.

Maximize ε over fractional physical-edge orientations with every proper cut satisfying `d_t^+(X)+q(X)≥k+ε`. Suppose the optimum ε*<1. Its optimal dual has nonnegative cut weights summing to one. Choose an optimal dual minimizing `Σ_X y_X |X||A−X|`. Positive-weight cut rows are active at the fractional optimum.

Crossing active rows X,Y force their intersection/union active, zero physical petal multiplicity, and zero q-submodular defect. This follows from the fractional directed-cut identity exactly as in Section 12 of the guard note. Thus moving a common positive weight α from X,Y to X∩Y,X∪Y preserves both the dual objective and normal vector. It strictly decreases the chosen secondary objective by `2α|X−Y||Y−X|`. The dual support is therefore cross-free.

At the fractional optimum, every positive-mass directed copy maximizes the dual-weighted outgoing cuts. If φ(v)=Σ_{X∋v}y_X, this gives φ(tail)≥φ(head). A relative-source directed copy for the positive-weight support would instead have φ(head)>φ(tail). Hence the support is source-free on all positive-mass directed copies.

Complementary active rows are impossible because their two original slacks would sum to 2ε*<2≤μ(X). Pure empty split-tree nodes are impossible: the partition budgets established in Section 1 give `M−Σp≥t`, while activation at ε* gives `M−Σp=tε*<t`.

The q row-packing and negative-pair surcharge packing apply unchanged to fractional directed masses. They imply `Q+σ≥e(k+ε*)`, while tight-row counting gives `M+σ=t(k+ε*)−Q`. Thus `M≤(n−1)(k+ε*)`.

The stronger quotient degree bound from μ≥2 gives `M≥(n−1)(k+1)+1`. This contradicts ε*<1. Therefore a fractional orientation covering p+1 exists.

Audit detail: vertex potentials alone do not make the dual outcut objective invariant under uncrossing, because outgoing cuts contain an orientation-independent petal-edge constant. The active-crossing identity kills this constant; it must be included explicitly.

## 5. Direct integer extraction from cross-free active network matrices

Consider the nonempty p+1 orientation polytope in reversal coordinates x∈[0,1]^m. Every cut RHS is integral. The following active-dual argument proves every vertex integral, and supplies the integer orientation needed after Section 4.

Take any vertex x*. Choose a cost vector c which uniquely exposes x* and avoids the span of every rank-deficient subset of the finite collection of cut normals and unit box normals. Such a c exists: the vertex normal cone has nonempty interior, and finitely many proper linear subspaces cannot cover this interior.

Take an optimal LP dual for c and minimize `Σ_X y_X |X||A−X|` over optimal duals. All positive dual cut rows are active at x*. Crossing active rows have active intersection/union and zero physical petals/demand defect; hence the same uncrossing preserves the dual cut-normal sum, its RHS value, and all box dual variables. The positive cut support is cross-free.

Because c avoids all rank-deficient normal spans, the positive-support cut normals together with positive-support box normals span the entire reversal-variable space. Choose a full-rank active constraint basis from them.

The cross-free cut coefficient matrix is a signed network matrix. Represent its splits by a tree; for a physical edge u→v the reversal coefficients `1_X(v)−1_X(u)` form the signed incidence vector of the unique tree path from the atom of u to the atom of v. These are the fundamental-path columns of a network matrix, which is totally unimodular. Empty tree nodes cause no difficulty. Complementary cut rows have opposite normals and can both be present in the support, but at most one can enter an independent basis; alternatively adding a negative duplicate row preserves total unimodularity. Adding unit box rows also preserves total unimodularity.

The selected active basis therefore has determinant ±1 and integer RHS. Its unique solution x* is integral. Choosing a vertex of the nonempty p+1 polytope gives the required physical orientation.

This proof uses ordinary crossing-supermodularity of the initial augmented demand and does not invoke an unverified signed partition/co-partition criterion. Box-integrality alone still does not imply single-edge connectivity or common deletion completion.
