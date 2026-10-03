# 原始 2k+1 连通性定理：综合证明工作档

2026-10-03。主目标固定为：finite loopless multigraph、k≥2、λ(G)≥2k+1 ⇒ Ω_k(G) connected。保留 parallel physical copy 身份。本文连续记录综合、归约、失败箭头和当前证明接口；主定理尚未标为完成。

最新补充：research_five_vertex_full_theorem.md已闭合全部|V|≤5；research_dominant_neighbor_contraction.md给一般最小反例m_ab≤deg(b)−k−1。原始MAIN与RSM仍OPEN；后文旧规模frontier按这两项更新理解。

## 0. 固定最小对象，不静默更改

反设主定理失败。在反例图中按 (|V|,|E|) 字典序取 G。对这个 G，在跨原始 physical components 的合法定向对中取 Hamming distance h 最小的 R,Q，写 K 为其差异边、J 为共同边。

已有结果给 h≥2、固定 J 的 K-face 恰有两 antipodes、且对应 polytope 是线段。其 physical support 为单有向圈或若干 vertex-disjoint 有向 paths。不能未经论证把最小 Hamming pair 改成一个 single-path pair。

如果另外使用 degree/path/circuit macro 理论，另定义 ℓ 为跨原始 components 的合法终态 single-path/circuit macros 的最小 physical length；ℓ 的选取不改变 G 或 h 的 minimality。最小 path macro 只直接冻结首尾边，不能冻结 interior edges。后面每次下降注明减少的是 (|V|,|E|)、h 还是 ℓ。

已完成的 μ≥2 contraction 给：G 的每个 inclusion-minimal global mincut shore 是 singleton；critical minimal frontier rows 也是 singleton。

## 1. 首先审计新输入的逻辑地位

用户新输入的 common-S component 定理是条件命题：假设已经存在 actual-tight、source-closed、K-progress-blocking S。它没有自动给 S 的存在。source-closed 的边 universe 必须注明；这里先使用物理翻边意义的条件：对每条允许 J-copy，P_S(g)≠∅ ⇒ N_S(g)≠∅。

如果每条 Wrong_K copy 都有 N_S(g)≠∅，且 Wrong_K=K，则 S 对全部 H=J∪K 的 copies source-free。下面证明，这样的非空 S 在初始 true-critical 完整系统中即使不 cross-free 也不可能存在。因此不能把该条件输入当作已经提取到了一个可收缩的 obstruction。

## 2. 新推导：任意 actual-tight source-free 族排除（不预设 cross-free）

### 定理 2.1

在初始 true-critical 固定外部纤维中，取任意非空 actual-tight proper-shore family F，同一合法完整内部定向 D。若对每条 H-physical copy g 都有

    P_F(g)≠∅ ⇒ N_F(g)≠∅，

则矛盾。即不存在这样的 F；不需要预设 F cross-free。

### 证明架构

1. 令 C 为 F 在 crossing intersection/union 下的闭包。只对四个 Venn regions 均非空的 crossing pairs 加 corners。初始 q submodular、p crossing-supermodular 和 D 可行使两个 corners 都 actual-tight，且两个 petals 间没有 physical edges。因此 C 的所有 rows 仍 actual-tight、proper；A 有限使 C 有限。

2. C 的每条 row 是 F 的 indicators 经有限次 AND/OR 得到的。若 g 对 F 全中性，则对 C 全中性。更精确地，若 g 对 C 的某 row positive，则 g 对 F 的某 row positive：否则对所有原 rows 均有 χ_X(head)≤χ_X(tail)，AND/OR 保持这个坐标序，无法得到 positive corner。

3. 在 C 中取非空 inclusion-maximal cross-free family T。若 g 是 T-relative strict source，则 P_T(g)≠∅、N_T(g)=∅。由第 2 步和 F 的 source-freeness，存在 W∈F⊆C negative on g。

4. 在 C 中对 W 使用 compatible negative-guard uncrossing。其每次只取 W∩Y 或 W∪Y，Y∈T，且仅在 W,Y crossing 时操作，所以仍留在 C。已有 corner-compatibility lemma 保证 crossing count 严降。得到 W′∈C negative on g 且 compatible with 全 T。

5. W′不在 T，因为 N_T(g)=∅。于是 T∪{W′} 是 C 内更大的 cross-free family，与 maximality 矛盾。

6. 所以 T 没有 relative strict source。但 CFST 对非空 cross-free actual-tight T 给至少 ceil((n_T−1)/2)≥1 条这样的 physical copies，矛盾。∎

### Scope audit

- 用的是初始完整 H 和 true-critical endpoint q；未把 signed descendant p_J 当成初始需求。
- 未断言普通 source-preserving laminarization 保持原 F 的 signs；改用有限 corner closure 与“positive corner ⇒ positive ancestor”。
- compatible guard extension 被约束在 C 内，corner closure 明确保证这个约束。
- 此定理是 source-free family 排除，不是“每个指定 row 都有合法 incoming service”。后者已被 tip-only weighted guard 控制否定。
- 这里所有 F-rows 在同一个 D actual-tight；不能把不同历史时刻的 blockers 拼起来套用。

### 第二种证明审计：直接保留物理负号覆盖

source-free F 负号覆盖每条 F-nonneutral physical copy。对 crossing X,Y∈F，用 I=X∩Y、U=X∪Y 替换。tightness 强迫两个 petals 间无任何 physical copy。

一条原来 negative on X 或 Y、替换后却不 negative on I/U 的弧，只能从一个 petal 指向另一个 petal，已被排除。因此原全部 negative-edge cover 被保留。另一方面，new positive on I/U 必然 old positive on X 或 Y；原来对整个 F neutral 的边在新族仍 neutral。所以新族的每条 positive copy 仍有一个 negative guard，source-freeness 保留。

每次替换使 Σ_X |X||A−X| 严格下降，若 corner 已存在就只会进一步下降。有限终止给非空 cross-free actual-tight source-free T，再被 CFST 排除。此证明不使用 source-preserving row deletion；实际执行的是 tight-corner uncrossing，零 petal 物理边条件是关键。

两种证明在有限 corner closure 和直接 physical negative-cover 两个层面相互核对。没有把 cut-normal 的线性 span 当作 edge-sign cover。

### 对主定理的推进

若能从真正的 minimum ambient separation 提取这样的同态 source-closed blocker family，就立即结束主定理；不再需要先证明该族 cross-free 或做 atom 收缩。新的瓶颈是该族的存在/历史归一化，不是 arbitrary-size static source-free 排除。

也因此，如果新输入的 common-S 假设把 source-closed 检查于全部 J，并把全部 K 阻挡，那么其初始真临界前提不能同时实现。条件不变性命题可有正确的形式证明，但在该 scope 中前提为空。若其模型用了更小边 universe、signed p_B 或只阻挡 K 的子集，必须单独注明，不能用于主定理捷径。

## 3. 下一步审计计划（随推导更新）

1. 完成 atom product 的精确证明，区分固定 quotient sector 与 ambient components。
2. 核对 atom 局部需求是否 genuinely critical；不能只看 whole-atom quotient μ。
3. 尝试把最小分量的历史 blockers 变成同一 D 的闭族，或证明这个提取箭头需要额外动态量。
4. 并行于理论思考的替代路线：admissible odd-vertex pairing / Eulerian lift，明确逐物理边投影是否合法。

所有局部结果必须继续接回 Ω_k(G) 的全局连通性；本文不以一项新的静态 theorem 作为研究终点。

## 4. 本轮综合之后的状态更新

上节审计计划已执行：atomproduct完整证明通过，projected μ继承箭头由真临界15copycontrol否定；B+及nonboundarylift均独立闭合；pairing给每balancedrootstar canonicaltarget，但prefixshortcut被具体控制否定。

当前主归约使用允许temporaryrootflips的RSM，完整statement和MAIN等价证明见research_boundary_lift_audit.md §6。|A|≤3fiber已完成，global|V|≤4完成；五顶点最小边数5k+3层也完成。边最小性给C°删除锚，存在非mincutcopy时最短跨C°macro可选singlepath；它只直接冻结首尾，不能与h/h_r的全部K冻结混同。

正式综合交付为《原定理综合研究与唯一剩余接口_2026-10-03.md》。MAIN仍OPEN；不以静态source供给、atomsector分离或positivecontrol的BFS冒充全局证明。
