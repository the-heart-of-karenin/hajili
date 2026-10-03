# Source-free actual-tight family 的 membership-atom 边数预算

日期：2026-10-02。状态：符号定理，适用 initial true-critical residual system。它不是 full-fiber connectivity theorem。

## 1. 精确假设

G 为有限无自环多重图，λ(G)≥2k+1，A 为边界大小恰为 2k+1 的非空真 shore；固定 outside signature 有 k-arc-strong 扩展。H=G[A] 的当前完整定向 D 合法，q(X)=min{R(X),S(A−X)}，p(X)=k−q(X)。

取 t 个互不相同的非空真 actual-tight rows F={X1,…,Xt}，全部在同一个 D 中紧，即 d_D^+(Xi)=k−q(Xi)。

本定理只需下述较弱 source-free 条件：不存在某条内部物理边 u→v，使其在 F 全部 rows 上 reversal signs 非负且至少一正。新版 B0.2 的 extra-negative / MAIN-positive source-free 蕴含这一条件，因此可把 F 取为 MAIN 与 extra 的全体 distinct rows 使用。

令 n 为 F 的非空 Boolean membership atoms 个数：两个 A 顶点属于同一个 atom 当且仅当它们在每个 Xi 上的成员资格完全相同。这里计入存在的 all-zero/all-one atoms；无需假设 zero-extreme，也无需 cross-free。

令 M 为 H 中跨不同 atoms 的物理边总数。

## 2. Atom Budget Theorem

必有

    ceil((n−1)(2k+1)/2) ≤ M ≤ tk−Σ_i q(Xi).                (AB)

特别地，n≤t。更精确地，

    Σ_i q(Xi) ≤ (t−n+1)k − ceil((n−1)/2).                (AB2)

### 证明

将每个非空 membership atom 收缩为一个顶点，并将 outside B 收缩为一个 root；删除收缩产生的自环，保留所有平行边身份。每个 quotient 非平凡割都对应 G 的非平凡割，因此 quotient 的边连通度仍至少 2k+1。root 恰有 2k+1 条 incident edges。其它 n 个 atom 顶点的总度至少 n(2k+1)，但该总度恰为 2M+(2k+1)。故

    2M≥(n−1)(2k+1),

得到下界。

另一方面，对每条跨 atom 当前弧 u→v，至少有一个 row 成员资格发生变化。如果它不 leaves 任何 Xi，则所有 reversal signs 都非负且至少一正，与 source-free 矛盾。因此每条跨 atom 物理边至少在一个 Xi 的当前出割中计数，故

    M≤Σ_i d_D^+(Xi)=tk−Σ_i q(Xi),

得到上界。q≥0；若 n≥t+1，则下界至少 tk+ceil(t/2)>tk，与上界矛盾，因而 n≤t。整理得到 AB2。证毕。

## 3. 预算中遗漏的真正 guard surcharge

令 ν_F(g)=#{Xi:g leaves Xi}。跨 atom edges 满足 ν_F(g)≥1，且紧割出度总和精确给

    Σ_i d_D^+(Xi)=Σ_cross-atom g ν_F(g)=M+σ,
    σ:=Σ_cross-atom g (ν_F(g)−1)≥0。

因此 AB 还可加强为

    Σ_i q(Xi)+σ ≤ (t−n+1)k − ceil((n−1)/2).             (AB3)

多负号 guard 边不是免费的：每一条同时 leaves 两个 tight rows 的边给 σ 至少一单位。这为 guarded core 的 terminal 容量论证提供了一个明确的计量对象。

## 4. 修订版最小 normalization-failure 几何的准确范围

修订版 D0.6 的三行

    Z1={a,c}, Z2={b1,b2,c}, Z3={b1}

在四个非空 atoms {a},{b1},{b2},{c} 上给 membership words

    a:100, b1:011, b2:010, c:110。

因此 bare three-row family 有 n=4,t=3。若要求它本身 source-free、actual-tight 且来自 initial true-critical residual system，AB 排除其实现，对所有 k 都成立。原因是 source-free 把 M 压至 ≤3k，底图临界连通度却要求 M≥3k+2。

这不否定 D0.6 的 sign normalization counterexample，也不否定加入 MAIN 或更多 guards 后的实现。它说明 bare sign/geometry counterexample 本身尚未穿过 terminal atom budget；若附加 distinct actual-tight MAIN/guard rows，总行数 t 及 membership atoms n 会改变，必须重新计数。

同样，五个非空 atoms、四行的 bare abstract minimal-source-free multi-SCC example 满足 n=t+1，亦不能直接升级为 true-critical terminal witness。

## 5. 对 cross-free tree 的启示与未证明接口

cross-free t-row split system 可以用 t-edge tree 表示；若其 t+1 个 node regions 全非空，则 n=t+1，AB 直接排除。任何 genuine source-free actual-tight system 必须有 empty tree-node region，或有其它使非空 membership atoms 减少的退化。

该预算尚未证明 empty-node geometry 必须形成 tight partition/copartition，也尚未证明 minimal source-free family 的 private dependency graph 强连通。后续应使用 σ 的多负号 surcharge、empty-node 的混合方向和 boundary q 总量来分析这一步。不能把 AB 当作 arbitrary-size closure exclusion。
