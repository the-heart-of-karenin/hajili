# Critical Cross-Free Source Theorem：guard 的统一树预算

日期：2026-10-02。状态：符号证明，已由两个独立研究分支逐项审计。适用 initial true-critical residual system、完整内部定向和所有内部物理边。主连通性问题仍 OPEN。

## 1. 假设、量词和结论

G 为有限无自环多重图，λ(G)≥2k+1，k≥1。A 为非空真 shore，|δ_G(A)|=2k+1；固定 outside orientation σ 有 global k-arc-strong 扩展，当前完整内部定向 D 合法。

对非空真 Y⊂A，

    q(Y)=min{R(Y),S(A−Y)}, p(Y)=k−q(Y),
    s_D(Y)=d_D^+(Y)−p(Y), μ(Y)≥1。

取任意非空、distinct、cross-free actual-tight family F={X1,…,Xt}，即每个 Xi 非空真且在同一 D 中 d_D^+(Xi)=k−q(Xi)。不要求 zero-extreme、FULL-SUPPORTABLE、minimality 或事先 source-free。

令 n 为 F 在 A 上的非空 Boolean membership atoms 数。因为 family 非空且 rows 真、非空，n≥2。

对跨不同 atoms 的当前物理弧 g=u→v，令

    ν(g)=#{X∈F:u∈X,v∉X}。

称 ν(g)=0 的跨 atom 边为 full-family strict source：它不 consumes 任何 F row，却正向 service 至少一行。

**定理 CFST（定量版本）。** 这样的 strict source 物理边至少有

    ceil((n−1)/2)

条。特别地，不存在非空 cross-free actual-tight、对全部内部物理边 source-free 的族。

新版 B0.2 若把 MAIN 与 extras 合并为 F，其更强 source-free 条件蕴含“无 full-family strict source”，因此也被本定理排除。若只对某个 K/J 子集 source-free，则不得照搬此结论。

## 2. 三项基础事实

### 2.1 q 非负、q(∅)=0 且 submodular

令 b(Y)=R(Y)+S(Y)。端点函数可写成

    q(Y)=R(Y)−[b(Y)−S(A)]_+。

R 为模函数，b 为非负权重模函数；正部函数对非负模权重是 supermodular，因此 q submodular。特别地，对任意互不相交 Ui，

    q(∪Ui)≤Σ q(Ui)。

此处使用的是 initial q；不能直接把 signed descendant p_J 当成同样的端点函数。

### 2.2 Complementary actual-tight pair 不存在

    s_D(X)+s_D(A−X)=μ(X)≥1。

故 F 不含一对 complementary rows。distict rows 因而也代表 distinct splits。

### 2.3 Actual-tight partition / copartition 不存在

对 partition A=⊔Pi，Φ=Σ[q(A−Pi)−q(Pi)] 满足 |Φ|≤1，且

    2Σs(Pi)=Σμ(Pi)−Φ,
    2Σs(A−Pi)=Σμ(Pi)+Φ。

至少两块时全部 tight 会与 Σμ≥2 矛盾。完整独立基础证明在 `research_foundation_audit.md`。

## 3. Split tree：只变换集合表示，不偷换 tightness

选任意 a0∈A。仅为构建 splits，把包含 a0 的 rows 取补，得到不含 a0 的 laminar shore system；不宣称这些 complemented shores actual-tight。原 row Xi 的方向仍单独保留。

标准 laminar inclusion tree 有 t 条边、t+1 个节点；每条边删除后将 assigned original vertices 分成 Xi 与 A−Xi。给边定向，方向指向原始实际 row Xi 的那一侧。

把每个原顶点赋给包含它的最小 laminar shore node，若没有则给 root node。非空 assigned node regions 恰为 membership atoms，故有 n 个 occupied nodes 与

    e=t+1−n

个 empty nodes。每条树边的两侧均有 assigned vertices，因为每个原 row 非空真；因此 empty node 的每个 incident branch shore 非空。

在 empty node v，incident branches U_{v,i} 不交且 partition A。设

    I_v={i:原始 tight row 恰为 U_{v,i}},
    J_v={i:原始 tight row 恰为 A−U_{v,i}}。

若 I_v 或 J_v 为空，incident rows 构成 actual-tight copartition 或 partition，被 2.3 排除。因此每个 empty node 都 mixed。

令

    U_v=∪_{i∈I_v}U_{v,i}。

它非空真，故 residual feasibility 给

    q(U_v)+d_D^+(U_v)≥k。                              (1)

## 4. q packing：一个 row 的预算只在一个树端点使用

定义 Q=Σ_{X∈F}q(X)。对每个 empty v，disjoint subadditivity 给

    q(U_v)≤Σ_{i∈I_v}q(U_{v,i})。

一条 tree edge 的原 row Xi，在该 edge 的 outside endpoint 被看作 normal branch Xi，在 inside endpoint 被看作 co-branch A−Xi。因此它至多在一个 empty node 的 I_v 中出现。

因 q≥0，各 empty v 的这些 row subfamilies 不交，故

    Σ_empty v q(U_v)≤Q。                               (2)

这一步没有要求 source closure 的选 guard 顺序；它直接对完整 retained cross-free family 计量。

## 5. 多负号 surcharge packing

令 M 为全部跨 membership atoms 的内部物理边数，

    Z=#{跨 atom g:ν(g)=0},
    σ=Σ_cross-atom g max{ν(g)−1,0}。

沿 g 的 tail-atom 到 head-atom 的唯一 tree path，负号恰为路径逆着 oriented tree edge 走，负号总数为 ν(g)。

若 g leaves U_v，它从一个 I_v branch 进入 empty node v，再离开进入 J_v branch。这两条连续的 incident tree edges 在 g 的方向上均为负号。

因此每个被 g leaves 的 U_v 对应 path 的一对相邻负号。一个有 ν 个负号的路径，相邻负号对数至多 max{ν−1,0}。逐边相加得

    Σ_empty v d_D^+(U_v)≤σ。                           (3)

结合 (1)–(3)，

    Q+σ≥e k。                                          (4)

## 6. 紧行总消耗与 critical atom-degree lower bound

在同一 membership atom 内的边不 crosses 任何 row。跨 atom边被计入恰 ν(g) 个当前紧行出割。因此

    tk−Q=Σ_{X∈F}d_D^+(X)=Σ_cross g ν(g)=M−Z+σ。

由 (4)，

    M=tk−Q−σ+Z≤(t−e)k+Z=(n−1)k+Z。                  (5)

另一方面，将所有 atoms 与 outside 分别收缩，root degree 恰为 2k+1，n 个 atom vertex 各 degree 至少 2k+1。故

    2M+(2k+1)≥n(2k+1),
    M≥ceil((n−1)(2k+1)/2)。                            (6)

(5)、(6) 给

    Z≥ceil((n−1)/2)。

这证明定理，且完全不需事先假设 source-free。∎

## 7. 解决了哪一层，尚未解决哪一层

**本定理解决的静态层。** 在上述 initial、same-D、all-H-edge scope 下，arbitrary-size cross-free actual-tight source-free family 不存在；source-resurrection 不必通过选择 proper minimal core 来处理，直接对原始完整族的 tree guards 计量即可。

**不能推出的结论。** 一个相对 source 未必对 omitted full tight cuts globally legal；若所有实际 tight cuts不能被 source-preserving 地表示成同一个 cross-free族，一般 temporal/global necessity bridge仍未完成。signed descendant 或只检查 K/J 的 source-free也不在定理范围。

**后续独立接口已闭合。** 全局 tight-cut cover uncrossing给 initial no-frozen theorem；更强的 compatible negative-guard lemma使 maximal cross-free tight family精确 covers全部 illegal internal edges。两种证明分别归档于 research_global_scope.md §8、research_guard_geometry.md §12。仍不推出一般 connectivity。

## 8. Root 独立 audit：corner compatibility 和 maximal blocker cover

若 W,Y crossing，而 Z 与 W,Y 均 cross-free，则 I=W∩Y 与 U=W∪Y 均与 Z cross-free。对 I，按 Z 与 Y 的四种关系证明：

- Z⊆Y：若 I∩Z非空，则 W−Y 和 A−(W∪Y) 的非空性分别排除 W⊆Z 与 W∪Z=A。W/Z compatibility因此迫使 Z⊆W，故 Z⊆I；若交空则本来 compatible。
- Y⊆Z：直接有 I⊆Z。
- Y∩Z为空：直接有 I∩Z为空。
- Y∪Z=A：W−Y⊆Z保证 W∩Z非空；A−(W∪Y)⊆Z−W排除 Z⊆W。剩下 W⊆Z（故 I⊆Z）或 W∪Z=A。后一种有 A−Z⊆W∩Y=I，故 I∪Z=A。

U 的结论用同时 complement W,Y,Z 后的 intersection结论得到；cross-free 对 complement不变。

现在 T cross-free actual-tight，g无 negative row。取任意 full tight g-blocker W，若 W crossing Y∈T，tight uncross identity迫使 I/U actual-tight且无 petal physical edge。g正于Y会连接 W−Y 与 Y−W，故不可能；g负于Y被假设排除。g于是对Y中性：两端都在Y则取I，都在Y外则取U。corner仍negative于g。上述 lemma保证所有原来不 crossing W 的 T rows仍 compatible，Y自身的 crossing消失。最小 crossing count 的 W因此必 compatible全部T。

故 maximal T中每条 globally illegal arc都有 retained negative row，反向显然。relative sources 与 intratom physical edges全合法，CFST quantitative count亦成为 legal-flip lower bound。该证明检查所有 full H physical edges，未使用或证明 frozen-J connectivity。
