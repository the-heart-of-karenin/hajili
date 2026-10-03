# Terminal Debt / positive-incidence audit — 2026-10-02

Task scope: the revised archive's B0.12, H0, K0.4. This note does not revive the false generic antipodal Debt-One assertion. It first audits the quantifiers in the proposed positive-incidence inequality, then isolates the terminal algebra that remains available.

## 1. A universal quantifier obstruction

For any cut (X\subsetneq A) crossed by the designated edge (e), set

\[
y_X=y_{A-X}=T,\qquad y_Z=0\text{ otherwise}.
\]

Then \(\phi_y(v)=T\) for every internal vertex. Every physical edge gradient is zero. Consequently

\[
P_e(y)=D_e(y)=T,\quad
\sum_{f\in K-e}[-\Delta_y(f)]_+=L_J(y)=0,
\quad S_R(y)=T\mu(X).
\]

Thus the proposed inequality

\[
P_e(y)\le1+\sum_{f\in K-e}[-\Delta_y(f)]_++L_J(y)
\]

fails for every (T>1), in **every** instance, independently of terminal realizability, antipodality, two-state normal form, or actual minimum-descendant origin. Both a laminar support condition and a cross-free support condition permit this complementary pair; neither repairs the quantifier.

This gives no high-Debt witness:

\[
\operatorname{Debt}_e(y)=T(1-\mu(X))\le0.
\]

If \(\mu(X)=1\), adding this pair with arbitrary (T) to *any* dual weight vector leaves every gradient and the Debt unchanged, but increases (P_e) by (T). In particular, if an optimal dual exists and (e) crosses a \(\mu=1\) cut, the proposed assertion also fails for **arbitrary optimal duals**. Merely changing “all dual weights” to “all optimal dual weights” does not resolve this.

Removing (a=\min\{y_X,y_{A-X}\}) from a complementary pair leaves gradients unchanged and improves the dual objective by

\[
a(\mu(X)-1)\ge0.
\]

Therefore an optimal certificate may always be selected with no complementary pair. This is a useful normalization; it is not a proof of the positive-incidence bound for normalized certificates.

## 2. Exact antipodal equality: the omitted term matters

Let \(\bar R\) reverse exactly (K) and keep (J) fixed. Define

\[
S_{\bar R}(y)=\sum_X s_{\bar R}(X)y_X,
\qquad B_K(y)=\sum_{f\in K-e}[-\Delta_y(f)]_+.
\]

Cut by cut,

\[
s_{\bar R}(X)=s_R(X)+\sum_{f\in K}\Delta_f(X).
\]

Hence

\[
S_{\bar R}=S_R+\Delta_y(e)+L_K-B_K,
\]

and the B0.12 formula becomes the **exact identity**

\[
\boxed{\operatorname{Debt}_e(y)=P_e(y)-S_{\bar R}(y)-B_K(y)-L_J(y).}
\]

H0.3 is obtained by dropping the nonnegative antipodal slack term. It is a valid bound, but its dropped term may absorb an arbitrarily large (P_e), as in Section 1.

The quantifier-safe exact target is therefore

\[
\boxed{P_e(y)\le1+S_{\bar R}(y)+B_K(y)+L_J(y).}
\]

For all (y\ge0), this is precisely equivalent to Debt-One; it is not an independent shortcut. The original target without (S_{\bar R}) can be used only after proving an additional **certificate selection theorem**, for example that some optimum has support entirely in antipodal endpoint-tight cuts. That selection theorem is presently unproved. “Optimal”, “extremal”, and “normalized” are different restrictions and must not be interchanged.

## 3. A completely explicit true-critical control

For arbitrary (k\ge1), use internal vertices (u,v) and external root (b). The fixed boundary has (k) copies (u\to b) and (k+1) copies (b\to v). Let (J) contain (k) copies (v\to u), and let (K=\{e=u\to v\}).

The undirected graph has cut sizes (2k+1,2k+2,2k+1), so its edge connectivity is (2k+1), and (A=\{u,v\}) is a true critical shore. Both (R) and \(\bar R\) are globally (k)-arc-strong. The residual data are

\[
q(\{u\})=k,\quad q(\{v\})=0,
\quad p(\{u\})=0,\quad p(\{v\})=k,
\quad\mu=1.
\]

For (y_{\{v\}}=T), one has (P_e=T), all penalties zero, (S_R=0), and (S_{\bar R}=T). Thus Debt is zero for every (T). Deleting (e) already leaves a legal orientation without changing (J), so this is an optimal dual ray for a cost-zero primal.

This control is terminal and antipodal but **not** an endpoint-illegal / component-separating minimum descendant: (e) itself is legal. Its purpose is to prevent replacing a carefully scoped certificate-selection claim by a broad terminal-plus-antipodal claim. The universal complementary-pair calculation of Section 1 applies even in the minimum-descendant scope.

## 4. Exact terminal root budget

Suppose the boundary totals are (R(A)=k,S(A)=k+1). Put

\[
a_X=R(X),\quad b_X=S(X),\quad t_X=a_X+b_X,
\quad h_X=\mathbf1\{t_X\ge k+1\}.
\]

Since (t_X) is integral, the endpoint-minimizer formula gives

\[
q(X)=a_X-[t_X-k-1]_+,
\qquad q(A-X)=b_X-[t_X-k]_+.
\]

In particular,

\[
\boxed{q(X)+q(A-X)=\min\{t_X,2k+1-t_X\}\le k,}
\]

\[
\boxed{q(A-X)-q(X)=b_X-a_X-h_X.}
\]

Writing (m_H(X)=|\delta_H(X)|), the symmetric slack is

\[
\boxed{\mu(X)=m_H(X)-2k+\min\{t_X,2k+1-t_X\}.}
\]

The two full undirected cut lower bounds (m_H(X)+t_X\ge2k+1) and (m_H(X)+(2k+1-t_X)\ge2k+1) give \(\mu(X)\ge1\) immediately.

Let \(\gamma_R(v)=d_R^+(v)-d_R^-(v)+R(\{v\})-S(\{v\})\) be the full oriented divergence at internal vertex (v). Then

\[
s_R(A-X)-s_R(X)=-\sum_{v\in X}\gamma_R(v)-h_X.
\]

For any nonnegative (y), set (M(y)=\sum_X\mu(X)y_X) and (H(y)=\sum_Xh_Xy_X). Combining this difference with (s_R(X)+s_R(A-X)=\mu(X)) yields

\[
\boxed{2S_R(y)=M(y)+\sum_{v\in A}\gamma_R(v)\phi_y(v)+H(y).}
\]

Replacing (R) by \(\bar R\) gives the analogous exact identity for (S_{\bar R}). This is genuine terminal information, unlike generic antipodal feasibility. It is not by itself an inequality in the needed direction: divergences can have either sign, and (H(y)) is a majority-cut charge that is not determined by the internal potential alone.

All formulas above are initial-system formulas evaluated on full internal orientations (J\cup K); they remain valid when (J) is designated ancestral. They do not require pretending that the signed descendant demand (p_J) is nonnegative.

For the opposite boundary totals (R(A)=k+1,S(A)=k\), retain (t_X=a_X+b_X\) and (h_X=\mathbf1\{t_X\ge k+1\}\). Direct algebra, with no signed-reroot black box, instead gives

\[
q(X)=a_X-[t_X-k]_+,\qquad
q(A-X)=b_X-[t_X-k-1]_+,
\]

\[
q(A-X)-q(X)=b_X-a_X+h_X,
\qquad q(X)+q(A-X)=\min\{t_X,2k+1-t_X\},
\]

\[
\boxed{2S_R(y)=M(y)+\sum_{v\in A}\gamma_R(v)\phi_y(v)-H(y).}
\]

The only change in the weighted identity is the sign of the majority-cut term.

## 5. Terminal antipodal Debt two: an explicit infinite family

**NEW PROVED RESULT.** The previously open `TRUE-CRITICAL TERMINAL ANTIPODAL Debt=2` target has a positive realization for every (k\ge4). This family is a **CONNECTED CONTROL**, not an actual minimum component-separating descendant. It closes the terminal-plus-antipodal target without resolving the main connectivity conjecture.

### 5.1 Physical edge certificate

Take

\[
A=\{w,y,a,b,c\},\qquad V=A\cup\{r\}.
\]

The two designated physical edges are

\[
K=\{e=w\to y,\ f=y\to w\}.
\]

They are distinct labelled copies of one undirected pair. They form a directed physical two-cycle. The ancestral edges (J) have the following multiplicities:

| Arc | Copies |
|---|---:|
| (w\to a) | (k-1) |
| (a\to w) | (k-2) |
| (a\to c) | (k-1) |
| (c\to a) | (k-2) |
| (y\to b) | (k-1) |
| (b\to y) | (k-2) |
| (b\to c) | (k-1) |
| (c\to b) | (k-2) |

The fixed boundary signature is

\[
c\to r\ (k\text{ copies}),\qquad
r\to w\ (2),\quad r\to y\ (2),\quad r\to c\ (k-3).
\]

Thus \((R(A),S(A))=(k,k+1)\) and \(|\delta(A)|=2k+1\). Let (R) be exactly this orientation. Reversing both labelled (K)-copies produces \(\bar R\). The directed multiplicities of (R) and \(\bar R\) agree, so all their cut values agree.

### 5.2 Undirected connectivity and global arc connectivity: an analytic proof

Let (T) be the spanning tree with edges

\[
wa,\ ac,\ yb,\ bc,\ cr,
\]

and let \(\triangle\) be the triangle on leaves (w,y,r). The underlying multigraph is

\[
\boxed{G_k=(2k-3)T+2\triangle.}
\]

For a proper nonempty full shore (C\subset V), write (d=|\delta_T(C)|\ge1) and \(\ell=|\delta_\triangle(C)|\in\{0,2\}\). Then

\[
|\delta_{G_k}(C)|=(2k-3)d+2\ell.
\]

If (d=1), removing a tree edge separates one of the three leaves from the other two, so \(\ell=2\) and the cut size is exactly (2k+1). If (d\ge2), the cut size is at least (4k-6\ge2k+1\), because (k\ge4\). Therefore

\[
\boxed{\lambda(G_k)=2k+1.}
\]

The full oriented divergences are

\[
\gamma(w)=\gamma(y)=-1,\quad
\gamma(a)=\gamma(b)=0,\quad
\gamma(c)=\gamma(r)=1.
\]

Consequently

\[
d_R^+(C)=\frac{|\delta_{G_k}(C)|+\gamma(C)}2,
\qquad -2\le\gamma(C)\le2.
\]

For (d=1), \(\gamma(C)=\pm1\), giving outgoing value (k) or (k+1). For (d\ge2),

\[
d_R^+(C)\ge\frac{4k-6-2}{2}=2k-4\ge k.
\]

Thus both endpoints are globally (k)-arc-strong. Since the outside consists of the single root (r), the endpoint-minimizer formula is exact with no further mixed-cut issue. The residual system is genuine true-critical, and its \(\mu\ge1\) property follows from Section 4 or directly from the full cut bounds.

The full (R)-tight shores are exactly

\[
\boxed{\{w\},\ \{w,a\},\ \{y\},\ \{y,b\},\ A.}
\]

To verify that no (d\ge2) cut is tight, if \(\ell=2\) its outgoing value is at least (2k-2>k). If \(\ell=0\), all three leaves are on the same side. If (c) is on that same side, \(\gamma(C)=0\) and (d\ge2\), giving outgoing value at least (2k-3>k\). If (c) is on the opposite side, (d\ge3\) and \(\gamma(C)=\pm1\), giving outgoing value at least (3k-5>k\). The listed five shores are the (d=1,\gamma=-1\) cases.

For proper residual shores, the four tight cuts are

\[
X_1=\{w\},\quad X_2=\{w,a\},\quad
Y_1=\{y\},\quad Y_2=\{y,b\}.
\]

Each has (q=0\), original demand (p=k\), internal outgoing value (k\), and symmetric slack \(\mu=1\).

### 5.3 Two-state antipodality and endpoint illegality

Freezing (J\) leaves four labelled (K\)-states. Reversing only (e\) decreases the outgoing value of both (X_1,X_2\) to (k-1\). Reversing only (f\) decreases the outgoing value of both (Y_1,Y_2\) to (k-1\). Reversing both preserves all multiplicities and is feasible. Hence

\[
\boxed{S_J=\{R,\bar R\},}
\]

and every (K\)-edge is illegal at both endpoints. The reversal polytope is also exactly \(\{t(1,1):0\le t\le1\}\), since the (w\)-tight and (y\)-tight constraints give the two opposite inequalities (x_e\le x_f\) and (x_f\le x_e\).

### 5.4 Debt and deletion cost are exactly two

Give each of (X_1,X_2,Y_1,Y_2\) weight one. The potential is

\[
\phi(w)=\phi(y)=2,\qquad
\phi(a)=\phi(b)=1,\qquad\phi(c)=0.
\]

Every (K\)-gradient is zero. Every ancestral gradient belongs to \(\{-1,1\}\). The four shores are endpoint-tight. For deleting (e=w\to y\),

\[
D_e=P_e=2,\quad S_R=S_{\bar R}=0,
\quad L_K=L_J=B_K=0.
\]

Therefore

\[
\boxed{\operatorname{Debt}_e(y)=2.}
\]

This dual is supported on a laminar, cross-free, complement-pair-free family and is tight at **both** antipodal endpoints. Restricting to such support does not restore Debt-One in a merely terminal-antipodal system.

For an upper bound, delete (e\), reverse one copy (g=a\to w\), and reverse one copy (h=c\to a\). Exactly two ancestral copies move. This completion is legal by the word proof below, because after moving (g,h\) both (e\)-blocking shores have at least one unit of slack. Thus

\[
\boxed{c^*(e)=2,\qquad \max_{y\ge0}\operatorname{Debt}_e(y)=2.}
\]

The lower bound uses elementary LP weak duality. The upper bound is an explicit integer completion. No box-integrality theorem is used.

### 5.5 A legal balanced word proves the full fiber is connected between the endpoints

Choose one physical copy of each (g=a\to w\) and (h=c\to a\). The word

\[
\boxed{h,\ g,\ e,\ f,\ g^{-1},\ h^{-1}}
\]

reverses the designated edges once each and restores both ancestral copies. Every step is legal.

* Moving (h\) could only lower cuts containing (c\) and omitting (a\). None of the five listed initial tight shores has this membership, so (h\) is legal.
* Moving (g\) next could only lower cuts containing (a\) and omitting (w\). No initial tight shore has this membership. Any newly tight cut created by (h\) omits (a\), so it cannot block (g\). Hence (g\) is legal.
* For an (e\)-outgoing cut, (w\in C,y\notin C\). The net slack change caused by (h,g\) is always zero or one: if (a\notin C\), the gain from (g\) compensates any loss from (h\); if (a\in C\), (g\) is neutral and (h\) is neutral or helpful. The two initially tight (e\)-blockers (X_1,X_2\) each gain exactly one. Every other (e\)-outgoing cut starts with at least one unit of slack and loses none during opening. Therefore flipping (e\) is legal. The same statement proves that **deleting (e\)** at the open state is feasible.
* After moving (e\), moving (f\) restores the original directed multiplicities on the pair (wy\). The resulting cut values equal those at the known feasible open state before (e\). Thus (f\) is legal.
* Closing (g\), then (h\), retraces the feasible opening states in reverse, as far as all cut values are concerned. The physical (K\)-labels have exchanged directions, but their multiplicities agree with the corresponding opening states. Both closing steps are legal.

The alternate order (g,h,e,f,h^{-1},g^{-1}\) is also legal; it is independently checked in the saved finite certificate.

The word has ancestral occupancy at most two. Occupancy one cannot precede first (K\)-progress: to release (e\), both nested blockers (\{w\}\) and (\{w,a\}\) must gain slack. The only available (J\)-types entering the first are (a\to w\), which are neutral on the second; the only types entering the second are (c\to a\), which are neutral on the first. One moved ancestral copy cannot service both. The symmetric argument applies to (f\). Thus this control has

\[
\boxed{\beta_{\rm first}=\beta_{\rm bal}=w=2.}
\]

This explicitly explains why two-state antipodality and all-(K\)-edge endpoint illegality do **not** imply actual minimum-component origin. The full legal fixed-outside fiber contains the displayed connection, although the frozen-(J\) face consists of two isolated states.

### 5.6 Saved verification artifacts

* Verifier: `scripts/verify_terminal_antipodal_debt2.py` — no search, standard library only.
* Raw labelled-edge / all-cut / dual / deletion / word certificate: `data/terminal_antipodal_debt2_certificate.json`.
* SHA256 values for the verifier and raw certificate: `data/terminal_antipodal_debt2_sha256.json`.

The base (k=4\) checks inspect all 62 nontrivial full cuts, all 30 residual cuts, all four frozen-(J\) endpoint assignments, every intermediate state of both six-step words, and the explicit deletion completion. Separate checks at (k=5,6,10\) agree with the analytic family. The general proof does not rely on extrapolating these checks: increasing (k\) by one adds one copy of a bidirected spanning tree (T\), increasing every directed full-cut value by at least one and every undirected full-cut value by at least two.

## 6. Unbounded Debt and temporal width at fixed (k\ge4\)

**NEW PROVED FAMILY, extending Section 5.** Let \(L\ge1\) be arbitrary. Replace the two length-two tree arms by

\[
w=w_0,w_1,\ldots,w_{L-1},w_L=c,
\qquad
y=y_0,y_1,\ldots,y_{L-1},y_L=c.
\]

Keep one tree edge (cr\), the same boundary signature (c\to r\) (k\) times, (r\to w,r\to y\) twice each, and (r\to c\) (k-3\) times. On every arm link, orient (k-1\) ancestral copies toward (c\) and (k-2\) copies away from (c\). Keep (K=\{e=w\to y,f=y\to w\}\).

The resulting graph still satisfies

\[
G_{k,L}=(2k-3)T_L+2\triangle(w,y,r),
\]

where (T_L\) is a three-leaf tree with the two arms subdivided. The proof of Section 5.2 uses only the three leaves and the number of tree edges crossing a cut; it is independent of arm length. Hence

\[
\boxed{\lambda(G_{k,L})=2k+1,\qquad R,\bar R\text{ globally }k\text{-arc-strong}.}
\]

The full divergence remains (-1\) at (w,y\), (+1\) at (c,r\), and zero elsewhere. The complete full-tight family is

\[
W_i=\{w_0,\ldots,w_{i-1}\},\quad
Y_i=\{y_0,\ldots,y_{i-1}\}\quad(1\le i\le L),
\quad A.
\]

Each proper prefix has (q=0\), demand (k\), outgoing value (k\), and \(\mu=1\). Freezing all ancestral copies again leaves exactly the two antipodal labelled (K\)-states, and each individual (K\)-flip is endpoint-illegal.

Give every one of the (2L\) prefix cuts weight one. Then

\[
\phi(w_i)=\phi(y_i)=L-i,\qquad \phi(c)=0,
\]

every (K\)-gradient is zero, every ancestral gradient is (+1\) or (-1\), and all weighted cuts are tight at both endpoints. Consequently

\[
\boxed{D_e=P_e=L,\quad S_R=S_{\bar R}=L_K=L_J=B_K=0,
\quad\operatorname{Debt}_e=L.}
\]

### 6.1 Exact completion cost and a legal balanced word

Choose one physical backward copy on each (w\)-arm link. Open them in the order from (c\) toward (w\):

\[
c\to w_{L-1},\ w_{L-1}\to w_{L-2},\ldots,w_1\to w_0.
\]

After (j\) opening steps, the selected copies form a directed path from (c\) to (w_{L-j}\) that has been reversed. Its net change in outgoing cut value is

\[
\mathbf1\{w_{L-j}\in C,c\notin C\}
-\mathbf1\{c\in C,w_{L-j}\notin C\}.
\]

This change is at least (-1\), and none of the initial tight shores loses slack: the proper prefixes omit (c\), while (A\) contains the whole path. Every other initial cut has at least one unit of slack. Therefore every opening prefix is legal.

After full opening, every (W_i\) has gained one unit of slack. On any (e\)-outgoing shore (w\in C,y\notin C\), the opening change is zero or one. The initially tight (e\)-blockers are exactly the (W_i\). Thus moving (e\) is legal, and deleting (e\) at that open state is also feasible.

Moving (f\) restores the initial (wy\)-multiplicities, so it is legal. Closing in the reverse of the opening order retraces known feasible cut values. This gives a balanced legal word of length (2L+2\), using exactly (L\) ancestral copies. Dual weak duality and this completion prove

\[
\boxed{c^*(e)=\max_{y\ge0}\operatorname{Debt}_e(y)=L.}
\]

### 6.2 Exact temporal width

Before first (K\)-progress, (K\) retains its original directions. To move (e\), all (L\) initially tight (W_i\) must have gained at least one slack unit simultaneously. Every physical ancestral edge crosses at most one of these prefixes; only a backward copy on that prefix's unique arm link can supply its positive slack. Therefore at least (L\) ancestral copies must differ from their reference directions. The symmetric argument holds if (f\) is the first (K\)-move.

Together with the word above,

\[
\boxed{\beta_{\rm first}=\beta_{\rm bal}=w=L.}
\]

In particular, already at fixed (k=4\), true-critical antipodal systems with exactly two frozen-(J\) states and directed-cycle support have arbitrarily large deletion Debt, balanced completion size, and temporal width. All these endpoints remain connected in the full fixed-outside legal fiber. A uniform bounded-depth/width theorem cannot follow from these terminal and endpoint assumptions.

## 7. The same unbounded family with a two-edge directed path

The unbounded phenomenon is not a peculiarity of labelled opposite copies. Split the (y\)-tip of Section 6 into two vertices (u,v\). Attach all former ancestral links incident with (y\) to (u\), and replace the two root copies (r\to y\) by one each (r\to u,r\to v\). Add (k\) ancestral copies (u\to v\) and (k\) ancestral copies (v\to u\). Replace (K\) by

\[
\boxed{K:\ u\to w\to v.}
\]

For a cut keeping (u,v\) on the same side, all cut values agree exactly with the corresponding coarse two-cycle construction. For a cut separating (u,v\), the untouched bidirected ancestral pair supplies at least (k\) outgoing arcs at every state of the proposed word and deletion completion. Thus those cut orientations are always feasible. Its undirected cut has at least (2k\) copies between (u,v\), at least one crossing edge of the physical path (u-w-v\), and at least one crossing root edge among (ru,rv\). Its undirected size is therefore at least (2k+2\).

It follows that the split system is again genuine true-critical with \(\lambda=2k+1\), and both antipodal endpoints are feasible. Replace the (y\)-prefixes in the dual family by prefixes containing (u,v\) together. Give (u,v\) the same potential (L\). The added ancestral pair has zero gradient, and all other gradients agree with Section 6. Deleting (w\to v\) therefore again has

\[
\boxed{\operatorname{Debt}=c^*=L.}
\]

The frozen-(J\) feasible states are exactly (00\) and (11\): the (w\)-prefix cuts block moving only (w\to v\), and the split (y\)-prefix cuts block moving only (u\to w\). Their two inequalities also force the reversal polytope to be the diagonal segment.

Use the same (w\)-arm opening, then move (w\to v\), then (u\to w\), and close. Coarse cuts follow the already-proved cycle word; split cuts remain protected by the (k\) untouched outgoing copies between (u,v\). Hence the word is legal throughout. The first-progress lower bound on (L\) occupied ancestral copies remains valid: the new (uv\)-copies are neutral on every relevant prefix.

Thus for every fixed (k\ge4\), genuine terminal-antipodal systems with **exactly a two-edge directed physical path** already satisfy

\[
\boxed{c^*(e)=\operatorname{Debt}_{\max}=\beta_{\rm first}=\beta_{\rm bal}=w=L\to\infty,}
\]

while the two endpoints are connected in the full fiber. The cycle family has \(|A|=2L+1\), and the path family has \(|A|=2L+2\). This does not overlap the closed (k=2,|A|=5\) finite path universe.

### 7.1 Additional saved verification artifacts

* `scripts/verify_terminal_unbounded_debt.py` checks twelve prescribed cases: (k=4,5\), (L=1,2,3,4\) for the cycle family, and (k=4\), (L=1,2,3,4\) for the path family. This is deterministic verification, not graph search.
* `data/terminal_unbounded_debt_certificate.json` saves labelled physical edges, every ordered full-cut value, every residual slack / \(\mu\), all four frozen-(J\) assignments, exact dual terms, deletion completion, and all word states.
* `data/terminal_unbounded_debt_sha256.json` saves verifier and raw-certificate SHA256 values.

Every prescribed case passed. The arbitrary-(L\) theorem follows from the analytic proof, not extrapolation from these finite checks.

## 8. Stronger optimization: unbounded Debt already at fixed (k=2\)

**STRONGEST CURRENT CONSTRUCTION.** The (k\ge4\) threshold in Sections 5–7 belongs only to the uniform heavy-tree template. A different asymmetric root signature and stronger non-tip backward links give the same unbounded phenomenon for every (k\ge2\), including (k=2\).

Use the two length-(L\) arms of Section 6. For every arm link, put (k-1\) copies forward toward (c\). Put (k-1\) backward copies on each first link incident with its tip, and (k\) backward copies on all remaining arm links. Keep (K=\{w\to y,y\to w\}\). The boundary is

\[
\boxed{c\to r\ (k),\quad r\to w\ (2),\quad
r\to y\ (1),\quad r\to c\ (k-2).}
\]

Again (R(A)=k,S(A)=k+1\). The following direct proof starts with (k=2\). Raising (k\) adds (k-2\) copies of a bidirected spanning tree and therefore transfers the cut and word proof to every larger (k\).

### 8.1 Undirected base connectivity

At (k=2\), tree links incident with (w,y,r\) have weight two, and all remaining arm links have weight three. The low triangle has (wy\) weight two, (rw\) weight two, and (ry\) weight one.

If a full cut crosses one tree link, its size is at least five: a (w\)-prefix has low crossing weight four, a (y\)-prefix low crossing weight three, and a root shore low crossing weight three. If it crosses at least two tree links and the three leaves are not all on the same side, its low crossing weight is at least three, giving size at least seven.

If the leaves are all on one side, a leafless component on an arm has two boundary links, including a non-tip link of weight three and another link of weight at least two; its boundary therefore has at least five physical copies. If (c\) is on the opposite side from all leaves, at least three tree links cross and give at least six copies. These cases exhaust full proper cuts. The root cut has size five exactly. Hence

\[
\boxed{\lambda(G_{2,L})=5.}
\]

### 8.2 Every full directed cut has at least two outgoing arcs

At the base, arm forward multiplicities are one; backward multiplicity is one on the first tip link and two on non-tip links. The root has (c\to r\) twice, (r\to w\) twice, and (r\to y\) once.

* If (c\in C,r\notin C\), the two copies (c\to r\) already give outgoing value at least two.
* If (c,r\notin C\), two included tips give at least one forward exit on each arm. Exactly one included tip gives one (K\)-exit and one forward arm exit. No included tip means a nonempty leafless arm interval, whose outgoing boundary contains a backward exit of multiplicity at least one and a forward exit of multiplicity one.
* If (c\notin C,r\in C\), two included tips give two forward arm exits. Two excluded tips give three root exits. Included (w\) and excluded (y\) give (r\to y\) and (w\to y\), one each. Excluded (w\) and included (y\) give the two root copies (r\to w\).
* If (c,r\in C\), excluding (w\) gives the two root copies (r\to w\). Including (w\) and excluding (y\) gives (r\to y\) and (w\to y\). If both tips are included, a proper cut must omit a leafless interior interval. Its incoming boundary from (C\) contains a forward copy on its tip side and two backward copies on its center side, giving at least three outgoing arcs from (C\).

Thus (R\) and its multiplicity-identical antipode are both globally two-arc-strong.

### 8.3 Opening and serialization: a direct proof that does not assume a complete tight list

Open one backward copy on each (w\)-arm link in order from (c\) toward (w\). After each partial opening, only cuts containing (c\) and omitting its current frontier can lose outgoing value, and their loss is exactly one.

Every such cut has initial outgoing value at least **three**:

* If (r\notin C\), the two copies (c\to r\) plus a backward crossing of the arm path give at least three.
* If (r\in C,w\notin C\), the two copies (r\to w\) plus a backward crossing toward the omitted frontier give at least three.
* If (r,w\in C\) but the frontier is omitted, a leafless excluded arm interval lies between included tip and center. One forward arc enters it from its tip side, and two backward arcs enter it from its center side, giving at least three outgoing arcs from (C\).

Therefore every opening prefix is legal. This argument handles all tight cuts, including extra leafless-interval tight shores; it does not incorrectly import the five-shore tight list of the uniform (k\ge4\) construction.

After full opening, an (e=w\to y\)-outgoing shore gains one if it omits (c\), so moving or deleting (e\) is safe there. If it contains (c\), its initial outgoing value is at least three: for (r\notin C\), use the two rootward copies (c\to r\) and the (K\)-copy (w\to y\); for (r\in C\), use (r\to y\), (w\to y\), and a backward crossing from included (c\) toward excluded (y\). Thus moving or deleting (e\) is safe on these shores as well.

Moving (f\) restores the coarse (wy\)-multiplicities, and closing retraces the legal opening states. The same balanced word is therefore legal at (k=2\). Increasing (k\) adds a bidirected tree without changing any selected physical copy, so each full outgoing cut value grows by at least (k-2\), and each undirected cut grows by at least (2(k-2)\). The root cut remains exactly (2k+1\). This proves the full construction for every (k\ge2\).

### 8.4 Exact dual, completion cost, and width

All (2L\) arm prefixes remain actual-tight: they have (q=0\), internal outgoing value (k\), and demand (k\). Weight them by one. The potentials and edge gradients are exactly those of Section 6, giving Debt (L\). The explicit deletion completion moves exactly (L\) ancestral copies. The unique-link service requirement for all (L\) nested blockers proves the same first-progress lower bound. Hence

\[
\boxed{\lambda=2k+1,\quad c^*(e)=\operatorname{Debt}_{\max}
=\beta_{\rm first}=\beta_{\rm bal}=w=L\quad(k\ge2).}
\]

The endpoint support is a directed physical two-cycle, the frozen-(J\) polytope is the diagonal segment with exactly two antipodal integral states, and both endpoints are connected by the displayed balanced word. The family has unbounded width **at fixed (k=2\)**.

### 8.5 Optimized two-edge physical path

Split (y\) into (u,v\), attach former ancestral (y\)-links to (u\), attach the single former root copy (r\to y\) to (u\), and add (k\) copies each (u\to v,v\to u\). Replace (K\) by

\[
u\to w\to v,
\qquad e=w\to v,\quad f=u\to w.
\]

There is no extra root copy at (v\). Cuts keeping (u,v\) on the same side reproduce the optimized cycle construction. Cuts separating them have at least (k\) untouched outgoing ancestral copies and at least (2k\) undirected ancestral copies, plus at least one crossing copy of the physical path (u-w-v\). Thus their directed values are at least (k\) and their undirected sizes at least (2k+1\). All word states and the deletion completion are therefore legal, and \(\lambda=2k+1\).

The dual (y\)-prefixes now contain (u,v\) together; the two new vertices both have potential (L\). The added ancestral pair has gradient zero. The same exact Debt / cost / width value (L\) follows. In particular,

\[
\boxed{k=2,\quad |A|=6,\quad m=2\text{ directed path},\quad c^*=w=2}
\]

is a genuine terminal, antipodal, endpoint-illegal **CONNECTED CONTROL**. Larger (L\) gives unbounded values with \(|A|=2L+2\). This leaves the closed (k=2,|A|=5\) path universe untouched.

The verifier now checks **24** prescribed cases: the original 12 cases from Section 7.1, plus optimized (k=2,3\), (L=1,2,3,4\) cycle cases and optimized (k=2\), (L=1,2,3,4\) path cases. Every full cut, residual \(\mu\), endpoint assignment, dual term, deletion completion, and intermediate word state passed. The same raw-certificate and SHA256 filenames are updated. A compact summary is saved at `data/terminal_unbounded_debt_summary.json`, with each case's connectivity, \(\mu\), Debt, endpoint audit, and minimum outgoing value at every word step.

### 8.6 Why the reference minimum condition still has content

Let (R_j\) be the reference after (j\) legal opening flips, (0\le j\le L\). Keep the original optimal prefix weights. Each selected ancestral gradient was (+1\) and becomes (-1\) after its reversal; the slack sum grows by one per flip, and both leak terms stay zero. Thus the same certificate has Debt (L-j\). Finishing the remaining (L-j\) opening flips makes (e\) deletable. Weak duality and this completion give the exact identity

\[
\boxed{c^*_{R_j}(e)=L-j.}
\]

At the fully opened reference the deletion cost is zero. Therefore the high-Debt reference in these controls is **not** a deletion-cost minimum on its legal ancestral-only component. The new family decisively refutes terminal-only constant bounds while illustrating precisely how a minimum-reference origin might add real structure: it must rule out all such legal optimal-completion extraction paths.

## 9. A finite guarded-path serialization lemma

The unbounded controls point toward **existence of finite service**, rather than a constant service-cost bound. The following sufficient criterion works in an arbitrary globally (k\)-arc-strong orientation; it uses no terminal-only assumption.

For a full orientation (D\) and vertex (c\), define its guarded set

\[
\mathcal G_D(c)=\{c\}\cup\{x:\ d_D^+(C)\ge k+1
\text{ for every }C\ni c\text{ with }x\notin C\}.
\]

Equivalently, no full (D\)-tight shore contains (c\) while omitting (x\). All shores here are full global shores, so mixed residual cuts are covered automatically.

### 9.1 Directed-circuit criterion

Let the designated support (K\) be a directed physical circuit in (D\), starting at vertex (u\). Let (P\) be a directed physical ancestral path (c\to u\), with physical edges disjoint from (K\). Assume every vertex of (P\cup K\) belongs to \(\mathcal G_D(c)\).

Then there is a balanced legal word:

1. open (P\) in its directed order from (c\) to (u\);
2. reverse (K\) in its directed circuit order starting at (u\);
3. restore (P\) in reverse of the opening order.

For an opening frontier (x\), reversing the directed prefix changes outgoing cut value by

\[
\mathbf1\{x\in C\}-\mathbf1\{c\in C\}.
\]

It can lose one only on a (c\)-containing, (x\)-omitting shore, which has the assumed (k+1\) guard. During the circuit phase, the opened path followed by the reversed circuit prefix has the same net cut change, with (x\) now the circuit frontier. The same guard proves every intermediate state legal. A complete directed circuit reversal preserves all outgoing cut values, so closing retraces known legal opening values. The certificate has ancestral occupancy at most \(|P|\), with no claimed constant bound.

In a genuine actual component-separating descendant with one-circuit support, the existence of such a path is impossible: its balanced word would join the two proposed components. This is an exact **minimum-origin obstruction**, stronger than mere high Debt. It says that the minimum-origin engine must force an actual missing guarded route, not merely a large deletion cost.

### 9.2 Directed-path criterion

Let the designated support (K\) be a directed physical path (u\to v\), and suppose its full reversal gives another feasible endpoint \(\bar D\). Let (P:c\to u\) be an ancestral directed path, physically disjoint from (K\). Assume

\[
V(P)\cup V(K)\subseteq\mathcal G_D(c),
\qquad V(P)\subseteq\mathcal G_{\bar D}(c).
\]

Opening (P\), reversing (K\) from (u\) toward (v\), and closing (P\) in reverse opening order is legal. Opening and target progress have net change from (c\) to the current frontier, so the first guard suffices. During closing, relative to \(\bar D\), the remaining opened prefix of (P\) again has net change from (c\) to its frontier, so the second guard suffices. This again gives finite balanced support with occupancy \(|P|\).

The criterion is conditional. It has **not** been proved that a suitable (c,P\) always exist, either for terminal systems or actual minimum descendants. A collection of vertex-disjoint target paths also requires additional coordination; applying this single-path lemma to each component without verifying intermediate endpoint feasibility would exceed its scope.

### 9.3 Deletion-completion consequence

If (P:c\to u\) and the head (v\) of a designated edge (e=u\to v\) are guarded in (D\), opening (P\) makes (e\) deletable. An (e\)-outgoing shore omitting (c\) gains one from opening; one containing (c\) and omitting (v\) has at least one initial slack by the guard on (v\). Hence

\[
c^*(e)\le |P|.
\]

If such a path has length exactly the minimum deletion cost, its first arc is a legal member of an optimal deletion-completion difference set. Thus a reference selected to globally minimize deletion cost over its legal ancestral-only component cannot be positive-cost and simultaneously admit this optimal guarded-path completion. This gives a concrete extraction target: obtain a guarded path, or an analogous finite service certificate, **inside an optimal completion**, rather than infer forced membership from a positive dual gradient alone.

## 10. Complementarity audit for the proposed minimum-reference / CFST bridge

Suppose a reference (R\) is chosen to minimize integer deletion-completion cost over its legal ancestral-only component. If (g\in J\) is immediately legal at (R\), then no minimum completion difference set can contain (g\): flipping (g\) first gives a reference in that component with a completion costing one less. This assertion is valid for integer optimal completions. Extending it to every LP optimum requires an applicable integrality theorem; it cannot be assumed merely from weak duality.

For an optimal primal and optimal dual, the edgewise complementary-slackness rule is exactly

\[
\Delta_y(g)>1\Rightarrow z_g=1,\quad
\Delta_y(g)<1\Rightarrow z_g=0,\quad
\Delta_y(g)=1\text{ leaves }z_g\text{ unrestricted by this rule}.
\]

For free-cost (K\)-coordinates, replace threshold one by zero. These statements follow directly from equality in

\[
c_fz_f\ge\Delta_y(f)z_f-[\Delta_y(f)-c_f]_+,
\qquad0\le z_f\le1.
\]

Therefore CFST's legal **positive**-gradient edge does not automatically belong to a minimum completion. Even if the dual is integral, positivity gives only \(\Delta_y(g)\ge1\), and the equality case can have (z_g=0\) in every optimum.

A basic LP illustrates the strictness issue:

\[
\min h+g_1+g_2,
\quad h+g_1\ge1,\quad h+g_2\ge1,
\quad0\le h,g_1,g_2\le1.
\]

Its unique optimum is (h=1,g_1=g_2=0\). After eliminating upper-bound multipliers, its boxed dual objective is

\[
y_1+y_2-[y_1+y_2-1]_+-[y_1-1]_+-[y_2-1]_+.
\]

The dual optimal face is (0\le y_1,y_2\le1\), (y_1+y_2\ge1\). Its three integral extreme optima ((1,0),(0,1),(1,1)\) give positive gradient exactly one to some (g_i\), while no optimal primal uses either (g_i\). A strict complementary certificate is (y_1=y_2=3/4\): its two (g_i\)-gradients are strictly between zero and one, and its (h\)-gradient is (3/2>1\), matching the active upper bound (h=1\). This example is an **LP degeneracy control only**, not a terminal graph realization or an actual minimum-descendant counterexample.

If all optimal primal solutions have (z_g=0\) for a collection of coordinates, strict complementarity can select a dual with \(\Delta_y(g)<1\) on all of them simultaneously. It generally selects a fractional point in the dual optimal face. Ordinary integral-dual existence does not imply that this simultaneous strict certificate is integral. Combining “some integral optimum” with “some strict optimum” as though they were the same certificate is invalid.

Two possible genuine missing lemmas are now explicit:

* a geometric theorem selecting one optimal dual with the needed reference-tight support **and** simultaneous strictness on the legal coordinates, compatible with the integer thresholds; or
* a primal extraction theorem finding at least one legal ancestral copy inside some optimal deletion completion, perhaps by guarded-path decomposition as in Section 9.

Neither has been proved here. In particular, antipodal-tight support alone is insufficient: the families in Sections 5–8 already have optimal cross-free duals tight at both endpoints and arbitrarily large Debt.

### 10.1 Exact transport across a legal ancestral reference flip

There is a useful dynamic identity. Keep a fixed cut-weight vector (y\), and change the reference from (R\) to (R'=R\oplus g\) for one ancestral copy (g\). The designated (e\) and all (K\)-directions stay fixed. Let (\Delta=\Delta_y(g)\) in the old reference. Then

\[
S_{R'}=S_R+\Delta,\qquad
L_{J,R'}=L_{J,R}-[\Delta-1]_++[-\Delta-1]_+.
\]

Therefore

\[
\boxed{\operatorname{Debt}_{e,R'}(y)-\operatorname{Debt}_{e,R}(y)
=-\operatorname{clip}(\Delta,-1,1).}
\]

This formula is exact for every nonnegative (y\); legality is needed only to treat both reference states as feasible. In particular, a positive integral gradient lowers this particular certificate's value by exactly one, even when the optimized deletion cost does not decrease.

Let (V(R)=\max_y\operatorname{Debt}_{e,R}(y)\), and suppose (R\) minimizes (V\) on its legal ancestral-only component. For a legal (g\), one has (V(R')\ge V(R)\). If (y'\) is optimal at (R'\), the transport formula and optimality at (R\) give

\[
\operatorname{clip}(\Delta^{R}_{y'}(g),-1,1)
\le V(R)-V(R')\le0.
\]

Thus every new optimal certificate satisfies \(\Delta^{R}_{y'}(g)\le0\). If the optimized value rises by one, it satisfies \(\Delta^{R}_{y'}(g)\le-1\). Relative to the **new** orientation of (g\), these gradients reverse sign. The history-certified legal undo edge can therefore immediately become a positive-gradient service edge for the new dual.

This is a concrete reason why repeated “select an optimal dual, apply CFST, flip a positive legal edge” can oscillate. The optimized dual may switch polarity after every step. A real dynamic argument needs a history/closure rule that proves progress despite this switch; static positive incidence and complementarity do not supply that rule.

## 11. Current useful frontier

**2026-10-02 接口补充：** `research_dual_guard_gap.md` 给genuine k2,L2 connectedcontrol，crossfree antipodal-tight weightedrows、Debt=1>0，但全部globallylegalinternalcopies的originalgradient为0。CFST relative sources被omittedguards阻止；加zero-weightguards后出现legalT-sources，仍不保证originalweightedgradientpositive。本certificate非optimal（V=2），不能升级为optimal/minimum-origin反例。上节提及“legalpositivegradient”的推理只有在另行证明该存在性后才适用；CFST单独不提供它。

1. Prove a certificate-selection / uncrossing theorem for a minimum-descendant deletion LP. No current result permits assuming antipodal-tight support.
2. Alternatively keep the exact (S_{\bar R}) term, and use the majority-cut charge (H(y)), minimum origin, and ancestor service closure jointly to bound Debt.
3. Sections 5–8 now supply genuine terminal-antipodal examples with **unbounded** Debt and width at fixed (k=2\), even for a two-edge directed physical path. They refute every terminal-only constant-bound version and leave **ACTUAL MINIMUM-DESCENDANT Debt=2** open. The generic antipodal Debt-two example already in H0.2 must not be recycled as new progress.

Status: Sections 1–10 contain direct proved algebra, explicit controls, and precisely scoped conditional lemmas. Section 11 contains open targets. No assertion here settles the main connectivity conjecture.
