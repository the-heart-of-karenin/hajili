# 本轮依赖图与状态来源

> 2026-10-03 网页端交接入口：[本轮研究总结与审计状态](本轮研究总结与审计状态_2026-10-03.md)、[问题引入与继续研究交接](网页版Work研究交接_问题引入与继续任务_2026-10-03.md)。六顶点 nontrivial critical cut、6k+3边层及6k+4边单高点模式已证明；双高点模式仍OPEN。交接稿第11节的候选续推不进入PROVED依赖图。当前文件快照见data/research_checkpoint_manifest.json，带时间戳的旧快照只作溯源。

> 2026-10-03 最新状态：原始 MAIN 尚未证明；全部|V|≤5、任意k≥2及multiplicities已闭合。一般最小反例至少六顶点，且m_ab≤deg(b)−k−1。当前综合归约的主接口仍是允许临时 root flips 的 same-root-star ambient mixing（RSM）。最新证明见 [五顶点全闭合续报](研究续报_五顶点原定理已闭合_2026-10-03.md)，完整主架构见 [原定理综合研究与唯一剩余接口](原定理综合研究与唯一剩余接口_2026-10-03.md)。下文旧 priority 与 OPEN 保留为历史，已被新证明关闭的接口不自动恢复。

## 2026-10-03 当前 MAIN 依赖链

1. all-proper μ≥2 physicalaugmentation/H1 → nontrivial inclusion-minimal criticalshore contraction → vertex-minimum counterexample全部minimalmincutshores singleton。
2. evenbalancedrootextension（LP与pairing/Hall两条证明）→ B+共同deletioncompletion；globaltightuncross → outside nonboundaryflip直接lift。两处旧audit debt均CLOSED。
3. 上述结果 + **RSM（唯一主链OPEN）** → 每balancedrootstar只有一个ambientcomponentlabel → starcube邻步labels相同 → MAIN。
4. MAIN⇒RSM直接，所以这是reduced-class上的精确等价，不必另证强版本fixed-rootfiberH1。
5. arbitrarysame-stateactualtightsourcefree排除、globalCFST sourcebound k+ceil(n/2)均PROVED。历史rows归一化未完成，不把不同time的族直接套静态定理。
6. common-S条件不变性、atomproduct PROVED；全Jclosed+全部Kblocked在完整initialscope前提为空。Global μ不继承projected μ_B，反例为μ_min2/local μ_B0的15copycontrol。
7. |A|≤3fullcriticalfiber → 全局|V|≤4；dominant-neighbor contraction + heavy-star interval/intersection lift + heavy-triangle C°/CFST budget → 全部|V|=5 PROVED，任意k≥2及multiplicities。旧14/15-edge frontier完全superseded。
8. 使用图的edge-minimality，非mincutcopies的deletable states共用C°；E°非空时可按ℓ°选singlepath跨锚macro，circuitbranch排除。E°空的图仍保留；路径endpointguards不对称，不能circle同步。
9. Minimumambientpair first-asynchrony face → one-sided共同launch endpoint-compatible；parallelclass冻结与criticalshore同步锁。h_r rootflip例外保持。
10. 完整admissiblepairing signature + 任意compatiblecriticalrootstar Eulerianextension PROVED；matchinghead→tail pathmacro终态合法。Smoothinversepairing为已核对primaryinput；generalphysicalserialization未关闭。
11. 全部五顶点MAIN + |A|≤3 fullcriticalfiber + B+ → 六顶点全部nontrivialcriticalcut案PROVED；degree-onlyserialization → 六顶点L-regular / 6k+3层及6k+4边excess(2,0,0,0,0,0)PROVED。excess(1,1,0,0,0,0)OPEN，异常三点割候选待审计，不作为已关闭接口。

最新proofnodes：research_five_vertex_full_theorem.md、research_dominant_neighbor_contraction.md、research_first_asynchrony_geometry.md、research_pairing_signature_bridge.md、research_canonical_cycle_controls.md。research_five_vertex_next_edge_layer.md保留为通向fullfivevertex theorem的中间证明。

新增proofnodes：research_boundary_lift_audit.md、research_main_theorem_synthesis.md、research_atom_product_audit.md、research_global_source_theorem.md、research_pairing_lift_route.md、research_small_fiber_theorem.md、research_deletion_component_anchor.md、research_five_vertex_minimum_edges.md。各文件scope以最新正文为准。

## 2026-10-02 开始研究

主问题：有限无环多重图 G 满足 λ(G)≥2k+1、k≥2 时，其 k-弧强定向的合法单物理边翻转图是否连通。

本轮以完整主档案为研究数据库。阅读分工：协调者读取 1–2900 行；R0 分支读取 current layer 与 2901–5500 行；X* 分支读取 current layer 与 5501–8000 行；基础审计读取 current layer 与 8001–10224 行。分块读取遇到工具截断时补读相应片段。

## 需要严格区分的来源

1. 主档 2026-10-02 前页：项目当时的最新结论摘要，尚需为本轮使用的重要结论补完整证明。
2. 主档历史层：保留机制、反例、计算记录与文献线索，旧 OPEN 优先级不自动恢复。
3. 用户附加提示：含比主档前页更进一步的断言，例如三条 extra 边的 common-fiber equality、H1 死亡、H3 equality core、96 个候选 census、D1 complete-rewind 反例。当前主档未保存这些断言的完整证明或原始数据，故先作为待核验线索或显式条件。

## Priority 1 的形式化接口

- MAIN rows X_i 非空、真、两两不交且 actual-tight；R0=A\(∪X_i)。
- Extra rows Z1,Z2,Z3 两两不交且 actual-tight；Q=A\(Z1∪Z2∪Z3) 非空。
- Cross-free：任意两 rows 不同时具有四个非空 Venn 区域，即不 crossing。
- 当前所用 zero-extreme 仅为档案明示条件 Q⊆∪X_i 与 R0⊆∪Z_i，等价于 family 覆盖 A。不得擅自补入更强条件。
- 对当前有向边 u→v，δ_e(Y)=1[v∈Y]−1[u∈Y]。
- 本轮 source-free 的显式工作定义：不存在某条 physical edge，其对 family 所有 rows 的 δ 都非负且至少一个严格为正。主档未保存更正式定义；任何依赖此条件的定理均明确写出。
- “每条 h_i 位于某一个 MAIN fiber”由 MAIN-neutral 得到；“三条 h_i 共用同一 fiber”是附加提示里的更强条件，须单独审计。

## 底层审计所得精确等式（独立证明正在归档）

令 R,S 为 critical boundary 的出、入计数，b(Y)=R(Y)+S(Y)。

q(Y)=min{R(Y),S(A\Y)}。

q(Y)+q(A\Y)=min{b(Y),2k+1−b(Y)}。

μ(Y)=min{|δ_G(Y)|,|δ_G(A\Y)|}−2k≥1。

对 partition A=⊔P_i，令 Φ=Σ[q(A\P_i)−q(P_i)]。正确的 slack 账本是

2Σs(P_i)=Σμ(P_i)−Φ，

2Σs(A\P_i)=Σμ(P_i)+Φ。

由于 |Φ|≤1，任何非平凡 partition 或 copartition 都不可能全部 actual-tight。注意 Φ 的符号必须按本文件定义，不可反写。

## 当前待闭合依赖

Priority 1：先独立排除/实现 common-fiber 的 R0 和 X* 两分支，再审计 common-fiber reduction 本身。

主定理仍需要全局动态桥：排除某一静态族，不等于排除 minimum disconnected descendant，更不等于一般连通性证明。

## 修订版新的精确定义接口

取 extra universe E，当前内部边 g 的 N(g)、P(g) 分别为 extra rows 上 δ=−1 与 δ=+1 的集合；M(g)=1 表示有 MAIN 正作用。子族 S source-free 当且仅当对每条相关内部物理边

    (P(g)∩S≠∅ or M(g)=1) ⇒ N(g)∩S≠∅。

这比旧“full-row membership 严格增加才为 source”的谓词强。以下新的 guard 结论一律采用这个准确版本。

删除集 D=E\S 的等价规则：

    N(g)⊆D ⇒ P(g)⊆D，
    若 M(g)=1，则禁止 N(g)⊆D。

原始 E 是 source-free 时，这些规则对 E 的任意子族给出精确可行性检查，不涉及对 full cut system 的全局翻转合法性判断。

## 本轮最新依赖：静态程序关闭，动态 bridge 尚缺

1. foundation endpoint / q submodularity / µ / skew → split tree no complementary pair、no pure empty node。
2. q one-endpoint packing + negative-pair surcharge → CFST quantitative sources。
3. actualtight crossing zero-petal identity + corner compatibility → maximalcrossfreeblockercover → initial nofrozenlegalflipbound。
4. minimum ambient original-component-separating cube + primalintegrality → exactlytwoantipodes segment → necessary circuit / disjointpathsupport。
5. circuit support → allcutvaluesidentical → synchronousJwords → actual minimumintercomponentdistance makesKimmutablethroughwholecomponent。
6. µ≥2 onallinternalshores → relativep+1 existence（minmax与独立fractionalLP两条proof）；现由safe endpoints + HEAVY ancestor-label phases闭合singleflipaugmentation，unique strict component再给该initial子类H1。
7. unbounded k2 terminal-antipodal controls → terminal-onlyconstantDebt / width FALSE；不否定minimum-originfiniteescape。

第3项仅给每state合法Jlaunch；第5项仍允许Jcomponent内launch/undo循环。新问题是让有限service链真正unlockK。SAFE-STEM / SAFE-SINK给明确可执行充分条件，但未证明在第5项的全orbit中必出现；对physicalpaths的两色endpointguards也未合成一般escape。

当前不再依赖：properminimalguardcore的选择、terminalDebt≤1、genericboundedpacket、arbitrarysignedRCD。仍需独立audit：B+与quotientlift、dual-TDI / normalizeddualcertificate selection、pathcollectionendpoint-specificguards。

最新proof节点：`research_relative_reachability_audit.md`（all-proper-µ≥2 augmentation与H1）；`research_global_scope.md` §14（unique strict component）、§15（nonnegative-demand singlepath/circuit macroconnectivity）、§16（degree-image接口）。当前一般frontier转向µ1 critical cuts、boundary lifting、及没有nontrivial mincut时的vertex degree障碍。

新增精确依赖：µ2 dynamic theorem→strictcriticalblock quotientlift→minimumcounterexample的mincriticalshores singleton（`research_critical_contraction.md`）。Singletondegree2k+1使frontierlabel永久存在、只能换色，µ2 ancestrystrictdescent在此不自动继续。

Dual支线另有两道独立gap：relativeweightedsource→globallylegalpositiveoriginalgradient尚无generallemma（zero-weightguardcontrol已排除unqualified版本）；legalpositiveΔ≤1→optimalprimalmembership也不成立。Optimalpositiveguard必须universallytight于completionface；nonuniversalguard有某optimalcompletion的selectedgainwitness。LexoptimalcompletionDAG不能排除rowdependencycycle。对应proof见`research_dual_guard_gap.md`、`research_completion_dag.md`。
