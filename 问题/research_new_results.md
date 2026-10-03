# 本次研究的新结果

> 2026-10-03最新综合报告：[五顶点原定理全闭合续报](研究续报_五顶点原定理已闭合_2026-10-03.md)。全部|V|≤5 PROVED，六顶点oddregular最小边数层也闭合；原始任意规模MAIN仍OPEN，主链RSM未关闭。下面早期OPEN按新proof scope更新，下载原稿未改。

## 1. Canonical source-free 删除约简（符号定理）

新版精确 source 定义下，source-free 子族是 dual-Horn models；补集是 Horn 删除传播系统。任意候选 universe U 内存在唯一最大的 source-free 子族（若 MAIN 硬约束导致不可行则不存在）。其计算不依赖 guard 选择顺序。

这不能直接给一个包含指定 core 的最小 canonical guard closure；后者仍可能有多种 minimal choices。完整推导见 `research_guard_geometry.md`。

## 2. Membership-Atom Budget（符号定理）

initial true-critical system 中，t 个 distinct actual-tight source-free rows 若有 n 个非空 membership atoms，则

    ceil((n−1)(2k+1)/2) ≤ M ≤ tk−Σq(X)。

故 n≤t；计入多负号 surcharge σ 后，Σq(X)+σ≤(t−n+1)k−ceil((n−1)/2)。这一结论不要求 cross-free 或 zero-extreme。

修订版 bare three-row / four-atom normalization-failure 因 n=t+1 不能直接 terminal-realize。sign counterexample 仍成立；加入更多 MAIN/guard 后须另行分析。完整证明见 `research_atom_budget.md`。

## 3. 小规模精确算法核验

三行抽象逻辑 universe 中全部 38 个允许的 signed-edge signatures、741 个二-signature systems，经直接 truth-table 穷举核对：5928 个 candidate universe 的 canonical maximum 完全一致，15903 对 source-free models 的 union 全部保持 source-free。

代码：`scripts/guard_closure_verify.py`；原始结果与 SHA-256：`data/guard_closure_verify.json`、`data/guard_closure_verify.sha256`。这是逻辑算法有限核验，未枚举 terminal graphs，未证明一般连通性。

## 4. 本轮独立重建的已有结果

- true-critical endpoint / μ 的无向割精确式、heavy-block skew、partition slack 恒等式：`research_foundation_audit.md`。
- common-fiber equality 与 R0 / X* pure-cycle terminal exclusion：`research_case_r0.md`、`research_case_xstar.md`。修订版已将 all-t selected program 列为完成，因此这里不把独立重建冒称新的前沿结论。

## 5. Critical Cross-Free Source Theorem（已证明、独立复核）

initial true-critical system 中，任意非空 cross-free actual-tight family F，若有 n 个非空 membership atoms，则至少有 ceil((n−1)/2) 条 full-family strict-source physical edges。不要求 selected core、FULL-support、minimality 或 zero-extreme。

证明保留 split tree 中的 empty nodes。若有 t rows、e=t+1−n 个 empty nodes，记 Q=Σq(X)，σ=Σmax(ν(g)−1,0)。每个 empty node 的 mixed branch union U_v 可用 feasibility 收费 k；row-q 每行只支付一个 empty endpoint，多负号沿物理边 tree path 支付相邻 negative-negative transitions，故 Q+σ≥ek。紧行总消耗与 quotient atom-degree lower bound 随后给 source 数下界。

这闭合 same-D、initial、all-H-edge scope 的 arbitrary-size cross-free actual-tight source-free exclusion。完整证明：`research_crossfree_source_theorem.md`；独立审计：`research_guard_geometry.md` §10–§11、`research_global_scope.md` §7。不能套到仅允许 K 翻转的 signed descendant。

## 6. Compatible negative guard 与初始 full fiber 无冻结状态（已证明）

若 T cross-free actual-tight，g 对 T 没有 negative row，而 full tight system 中有 g-blocker，则可 uncross 出与整个 T compatible 的 actual-tight g-blocker。crossing tight cuts 的两个 petals 之间没有 physical edge；g 因而对被 crossing 的旧 row 中性，取 intersection 或 union 保留 negative g。corner compatibility lemma 保证 crossing count 严格下降。

所以 maximal cross-free actual-tight T 精确覆盖所有 illegal internal arcs。其 relative sources 与 intratom edges都 globally legal；legal internal flips 至少 M_intra+ceil((n−1)/2)。若没有 tight row，则每条内部边都合法。

特别地，|A|≥2 的初始 full fixed-outside fiber 中，每个合法完整定向均有内部 legal flip。另一个独立证明通过 uncross 全局 tight-cut cover，再调用第 5 节。该结论排除 isolated states，尚不排除多个非平凡 components。

## 7. 真临界 antipodal Debt 与 temporal width 在固定 k=2 时无界（已证明）

对任意 L≥1、任意 k≥2，有 genuine true-critical construction，λ=2k+1、|K|=2，frozen-J feasible face 恰为两个 antipodes，reversal polytope 是 diagonal segment，且所有 K edges 两端均非法。两条长 L 的臂上，每个 prefix 都 actual-tight；给 2L 个 prefixes 各 weight 1 得到 complement-pair-free laminar dual。

精确值是

    c*(e)=max Debt=β_first=β_bal=temporal width=L。

显式 legal word 为从中心朝 tip 开 L 条 backward copies、翻 K 两边、逆序关闭。端点由此在 full fiber 中连通，属于 CONNECTED CONTROL，不是主问题反例。把另一 tip 分成 u,v、加 k copies 各 u→v 与 v→u，K 可改成 genuine physical path u→w→v，保持上述全部精确值；固定 k=2、L=2 给 |A|=6、m=2、Debt=width=2。

完整解析证明在 `research_terminal_debt.md` §8（§5–§7 为先前较弱 k≥4 模板）。24 个预指定小案例已逐割核验，包括所有 word 中间状态、删除 completion、端点 assignments、dual terms、residual μ；只是证书核验，不是图搜索。raw 和 SHA256：`data/terminal_unbounded_debt_certificate.json`、`data/terminal_unbounded_debt_sha256.json`。

本构造关闭 revised H0.4 的 TRUE-CRITICAL TERMINAL ANTIPODAL Debt=2 OPEN，并更强地否定 terminal-only 常数 Debt / buffer-width 上界。ACTUAL minimum-component origin 尚未实现，不能将其冒充 minimum-disconnected counterexample。

## 8. Dual 量词修正（已证明）

对 arbitrary nonnegative y，旧 positive-incidence inequality 本身不成立：给互补 cuts 同加权 T，会保持 φ 的梯度为零而使 P_e=T，Debt=T(1−μ)≤0。若 μ=1，这是不改变 dual objective 的 neutral ray。因此即便“optimal y”也不能无条件断言旧 P_e 上界；需选择归一化 certificate。

准确 antipodal identity 含 −S_barR：

    Debt=P_e−S_barR−Σ_(K−e)[−Δ]_+−L_J。

原版省略该项得到的 upper bound 正确，但把它当 equality 或据此控制每个 y 错误。第 7 节无界构造已 complement-pair-free、全部 weighted rows 两端 tight、S_R=S_barR=0，因此只去 neutral pairs 仍不能救活 terminal-only Debt-One。

## 9. Minimum descendant / polyhedral scope 与新的动态接口

`research_global_scope.md` 给出 minimum **ambient original-component-separating** cube restriction 的两对跖态证明；不能只最小化某个 restriction 自身的 disconnectedness。

同档独立证明全局 physical reversal polytope 的 primal integrality 及 long-edge support 必要条件，避免把 signed p_J 误当非负 demand；固定 J 是原 polytope 的 coordinate face。support theorem 是必要条件，不是充分条件（regular K7 tournament 的 triangle full-cube control 已写出）。没有声称 dual-TDI 自动完成。

对于 directed-circuit difference，两端 cut values 恒同，任意 J word 可以同步 lift。minimum inter-component distance 强迫整个同步 orbit 不得出现 first-K-progress；这才是比 frozen-J antipodality 更强的 minimum-origin 条件。

`research_dynamic_bridge.md` 新写 SAFE-STEM lemma：若从 c 开到 circuit 的 directed path 及 circuit 全部顶点，都在每个包含 c 的 initial tight shore 内，则 opening / circuit / closing word 逐步合法。允许任意长 path，不承诺这种 path 总存在。剩余目标是从 minimum-origin 的 immutable circuit / path，制造有限可执行服务链。

## 10. Strict component 与 single-path/circuit macro connectivity（已证明）

`research_global_scope.md` §14独立证明crossing-supermodular degree polytope integral、edge directions为unit roots、integer degree points在unit transfers下连通。Strict起点的directed path可逐边serialize，终点degree合法strict；Eulerian differences逐圈serialize。因此全部strict orientations属于同一个original flip component，允许不同degree vectors。

同档§15证明initial nonnegative crossing-supermodular demand fiber在合法终态single directed path/circuit macros下连通；不要求macro prefixes合法。一般动态目标可只研究single path/circuit，不必先处理多条disjoint paths。§16给一个genuine k2、minµ1的node-gradient局部陷阱；greedy单步不成立，但不否定component-level reachability。

## 11. 全内部 µ≥2 的 relative single-flip augmentation / H1（已证明）

固定odd boundary，所有proper内部µ≥2时，任意初始合法D有internal single-physical-edge word到strict target，长度可取≤n²(n−1)²。Proper safe source/sink、actual-tight-container route保证每个path prefix合法；I非空的clean macro使minimal mixed frontier v下降。No-I弱source唯一例外是boundary weight k+1的HEAVY新out-tight块；它强制进入I阶段。

历史labels只whole-shore enlarge/merge/drop，不能fork。HEAVY标签在回到No-I前必灭；所有剩余frontier rows保留original ancestor，因此完整阶段严格降v。这闭合了candidate中的retained-minimality及人工A接口。

完整证明 `research_relative_reachability_audit.md`；候选原稿仅保留provenance。配合第10项unique strict component，all-proper-µ≥2 initial full fiber connected。主2k+1问题仍允许µ=1，未解决。

指定HEAVY phase核验：k2、4个internal vertices、19条physical copies；5个prescribed states逐一检查30个global cuts，µmin2、宏势3→4→0、word长度4，PASS。只核验证书，没有orientation enumeration。raw及SHA在`data/relative_heavy_phase_*`。

## 12. Critical contraction 与 minimum-counterexample新归约（已证明）

`research_critical_contraction.md`证明odd global mincut splits全部crossfree；若criticalblock A所有properglobalcuts严格，则所有actualtightglobalrows respect contraction，quotientlegaledgeflip可直接lift。对inclusion-minimalcriticalshore|A|≥2，其内部µ2，前一项augmentation能在每个quotientstep前恢复strictblock。

故Ω_k(G/A)connected⇒Ω_k(G)connected；按顶点数minimumcounterexample的所有inclusion-minimalglobalmincutshores必须singleton。Anchoredµ1 cleanmacros仍可合法服务，但criticalminimalrows只换polarity、不退出；这些criticalrows在minimumcounterexample中为permanent singletons。No-I weak-source cover失败只能有唯一criticalmaxOUTblock、其余nearblocks全部out/in=k+1，已明确分类；general termination仍OPEN。

## 13. Degree-only control 与 weightedguard新缺口（已证明、严格区分scope）

`research_odd_degree_control.md`证明所有vertexdegreeodd时balanced-degree orientations的singleflipgraphconnected：unit-degreepath按localprecedenceserialize，mixedcircuits直接serialize，monochromaticcircuits用外部相反statusstem。这个degree-only word可能违反globalcutconstraints，不填mainH1。

`research_dual_guard_gap.md`给genuine k2,L2 connectedcontrol：crossfree antipodal-tightpositiveweights、Debt=1>0，但全部4条globallylegalinternalcopies的originalgradient为0；2条relativeF-sources被omittedguards挡住。Certificate非optimal（V=2），不能当minimum-origincounterexample。Focused12singleflip、每state62cuts核验PASS。CFST+zero-weightguard closure不单独保证原weightedgradientpositive。

同档证明：一条guard可在某optimaldual中positive iff它在所有optimalprimalcompletions中tight；simultaneouspositivecertificate可以fractional，crossfreepreservation仍需另证。`research_completion_dag.md`证明lexoptimaldeletioncompletion的R-directedchangedsupport必DAG；selected blocker/gain dependencycycles未必physicalcycles，因此无环性仍不是serialization。

## 14. 原始 MAIN 综合更新（2026-10-03）

本轮正式交付《原定理综合研究与唯一剩余接口_2026-10-03.md》，类型FINAL C。MAIN未证明、没有ambientcounterexample；当前唯一主接口为reduced-class的same-root-star ambientmixing（RSM），允许临时rootflips。其单独成立机械完成MAIN；B+、nonboundarylift不再是额外OPEN。

新proof：任意actualtight同态sourcefree族排除；globalCFST sourcebound为k+ceil(n/2)；atomproduct正确而localμ继承false；balancedevenroot任意signatureextension；|A|≤3完整fiber及global|V|≤4；五顶点最小边数5k+3全部multiplicities层；非mincutcopies的共同删除环境分量C°及锚定singlepathmacro。

新certificate：atomgap为μ_min2/localμ0/sectordisconnected/ambientfourstepconnected；两个13edge五顶点positivecontrols完整检查，legalcounts1288/1204；Eulerianbadprefix与legalrotation；14edgedegreegap全部singleton合法但pairout1。全部raw/SHA在data。本轮计算只核验指定控制与两预选图，没有重型graphsearch。

k2五顶点最小未统一分类层更新为14edges，degreepatterns为(8,5,5,5,5)、(7,6,5,5,5)、(6,6,6,5,5)，且只有singletonmincuts。13edge层现在由理论排除，不再依赖有限BFS结果。
