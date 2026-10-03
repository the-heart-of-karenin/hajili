# Common-tight atom product 与 contraction 接口审计

2026-10-03。主目标仍为 λ≥2k+1 的原始 physical flip connectivity。本文证明 product 输入的准确版本，并用真正 μ≥2 临界实例隔离它与现有 augmentation theorem 之间的失败箭头。

## 1. 准确的 product theorem

设 H=(A,E) 是 finite loopless physical multigraph，p 为 integer crossing-supermodular proper-cut demand。允许 p 为 signed。取一个 p-feasible orientation D 和任意 actual-tight family S。此处 S 不必 cross-free、source-closed 或 progress-blocking。

令 B₁,…,B_t 为 S 的 Boolean atoms。固定全部 cross-atom physical copies 的当前方向，记其有向图为 Q₀。注意 Q₀ 不仅是压缩后的计数商图；它保留原 endpoints 和物理身份。

对 atom B、非空真 U⊊B，定义

    p_B(U)=max_{Z 为其它 atoms 的 whole-union}
           [p(U∪Z)−d⁺_{Q₀}(U∪Z)]。

那么全局 p-feasible orientations 在该 fixed-Q₀ sector 中，恰为各 atom 的 p_B-feasible orientations 的 Cartesian product；逐物理边 legal flip graph 同样为 Cartesian product。因此 sector 内的 connected components 为局部 components 的 product。

这里仅断言固定 Q₀ 的 sector，未断言其分量就是允许翻 cross-atom edges 的 ambient components。

### 1.1 Common-S 条件不变性通过审计，但不是 existence theorem

在任意 proper-cut demand system 中，若 S actual-tight 且对全部允许 J-copies满足 P_S(g)≠∅ ⇒ N_S(g)≠∅，则每条 legal J-flip对 S 都 neutral：合法排除所有 negative tight rows，source-closed 再排除 positive rows。

neutral 等价于两个 endpoints 对 S 的 Boolean signature相同。翻转这样的 copy 后，全部 S-rows仍 tight；其它 copy的 signs不变，该 copy仍 neutral。因此同一 S 的 source-closed性逐步保持，任何固定 K-blocking也保持。沿整个 J-connected component归纳，所有 moves都 atom-internal，全部 cross-atom J-copies冻结。

结合 product theorem，**在这些明确假设下**，J-component确为局部 component的 product。证明没有把 conditional S 的存在当作已知。

在 genuine initial complete true-critical system、J∪Wrong_K=H、全部 Wrong_K都被 S负号阻挡时，这些假设由 synthesis §2 排除。所以这里的形式定理在一般 signed/受限模型有意义，却不能制造初始主问题中的 obstruction。

## 2. 为什么 multi-atom cuts 冗余

每个 Y∈S 是 whole-atom union；固定 Q₀ 后其 cutout 固定，内部 atom orientations 对它中性。所以对任何候选内部定向都有 s(Y)=0，哪怕候选尚未证全局可行。

对一个同时 partial-splits 至少两个 atoms 的 cut X，选 S-row Y 分开其中两个 atoms。因为每个 atom 对 Y 要么全包含、要么全遗漏，X∩Y、X∪Y 都是 nonempty proper cuts；它们分别保留 Y 内、Y 外的 split atoms，每个 split 数严格少于 X。

由 cut submodularity 和 p crossing-supermodularity，有

    s(X)+s(Y) ≥ s(X∩Y)+s(X∪Y)。

若两个 corners 已可行，则 s(Y)=0 立即给 s(X)≥0。递归归约到 zero-split 与 one-partial-atom cuts。

zero-split cuts 的值只由 Q₀ 决定，原 D 可行保证它们可行。one-partial cut X=U∪Z 的 atom-internal贡献恰 d⁺_{D[B]}(U)，其余为 d⁺_{Q₀}(X)；取所有 Z 的最大需求正是 p_B。故 product 等式在所有 cuts 上成立。

## 3. 局部需求的 supermodularity 与 integrality

取在 B 中 crossing 的 U,V，分别选 attaining maximizers Z_U,Z_V。全局 X=U∪Z_U、Y=V∪Z_V 仍 crossing，因为 B 自身四区域都非空。

p supermodular、d⁺_{Q₀} submodular，所以 p−d⁺_{Q₀} crossing-supermodular。取 global intersection/union，把其其它 whole-atom 部分作为 U∩V、U∪V 的允许 Z，得到

    p_B(U)+p_B(V)≤p_B(U∩V)+p_B(U∪V)。

p_B 是有限个 integers 的最大值，故 integer。可能为 negative。其 orientation box 继承已证明的 primal integrality；这种 integrality 没有提供 local physical connectivity。

## 4. Phase 3 的失败箭头：global μ≥2 不变成 local μ_B≥2

### 真正临界的 4 顶点控制

k=2，V={a,b,c,r}，A={a,b,c}。所有 copies 有独立身份：

- a→b、b→a 各 1 条；
- a→c、b→c 各 1 条；
- c→a、c→b 各 3 条；
- c→r 2 条，r→c 3 条。

总共 15 条 physical edges。无向 degrees 为 a,b 各6、c为13、r为5；root cut 恰5，其他 full cuts均≥5，所以 λ(G)=5，A 为 genuine critical shore。

当前 D 合法。全部 proper internal residual μ 最小为2；特别 a,b 的 global singleton cuts 各6，没有 μ=1 藏在 B={a,b} 内。S={B} 是 actual-tight：q(B)=0，p(B)=2，d_H⁺(B)=2。其 atoms 为 B 和 {c}。

固定 cross-atom quotient Q₀ 后，B 的局部 demands却是

    p_B({a})=p_B({b})=1，δ_{G[B]}({a})=2，
    μ_B({a})=2−1−1=0。

所以 B 内两条 labelled copies 必须一条 a→b、一条 b→a，恰有两个合法 local orientations；交换它们必须同时反转两条，单翻任一条都会违反 local singleton demand。local flip graph为两个孤立点，fixed-Q₀ sector也不连通。

这严格否定：

    atom B 每个 proper global μ≥2
    ⇒ 可对 B 直接套 fixed-critical-boundary μ≥2 connectivity。

失败原因不是 hidden critical singleton。B 的 boundary 大小为8，当前 out=2、in=6，根本不是 2k+1 临界边界；从 whole-other-atom cuts 做最大投影，制造了 local μ_B=0。

### Ambient connectivity 并没有失败

选一条 g=c→a physical copy，e=a→b、f=b→a。word

    g,e,f,g

逐步合法，最后只交换 B 内两条 copies，同时恢复同一 g。因此 fixed quotient sector 的两个 local components 在 ambient full fiber 中相连；这正处于已证明的全内部 μ≥2 fiber 范围。

S 不是 J-source-closed：g positive on B，却没有 S-negative row。故该实例不反驳条件式 common-S theorem，也没有制造主定理反例。它只击穿未经审计的“atom projection 保留 genuine critical μ≥2”以及“sector 分离自动 ambient 分离”两个箭头。

指定证书已独立逐割检查：scripts/verify_atom_scope_gap.py，4vertices、15copies、每状态14global cuts；固定 sector的4个 assignments中恰00/11合法，ambient word的5states全部合法，global μ_min=2、local μ_B=0、λ=5。raw和SHA在 data/atom_scope_gap_*。未枚举全图全部orientations，也未将该控制称为主定理反例。

## 5. 对主定理的作用与保留的路线

Atom product theorem 本身可使用，且不需要 common-S 不变性。但其局部 fibers 是 arbitrary projected signed-demand systems；要用现有 μ≥2 theorem，必须另证具体 atom 的 boundary signature genuinely critical 和 exact endpoint representation。

不能从 whole-atom quotient的 q、μ继承，推导 atom 内 p_B 的 q、μ继承。二者是不同方向的投影。

因此用户建议链中 Phase 3 的一般 connectivity 箭头暂时停止使用。若能提取真正 source-closed S，其 existence 在初始完整系统中已由 research_main_theorem_synthesis.md §2 排除，可以直接反证，不必经 atom contraction。若 S 只 universally-tight、不是 source-closed，product sector 则仍可能需要 cross-atom history才能连接。
