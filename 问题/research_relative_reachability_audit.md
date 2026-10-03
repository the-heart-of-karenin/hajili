# Fixed-boundary relative augmentation：完整证明与第二轮审计

2026-10-02。状态：**PROVED（root 两轮逐项理论审计；无重型枚举）**。

本文件替代 `research_relative_reachability_candidate.md` 的未闭合接口；候选原稿保留，不删除其中的风险记录。这里的结论只覆盖全部内部 residual margins `µ≥2`，主问题中允许 `µ=1` 的一般 true-critical fiber 仍然 OPEN。

## 1. 定理与适用范围

令图的顶点为 `A∪{r}`，`n=|A|`，允许有身份的平行物理边，不允许 loops。所有 root-incident copies 的方向固定，内部 `H=G[A]` 的 copies 可以逐条翻转。固定边界满足

    R(A)=k，S(A)=k+1，k≥1。

从任意 globally k-arc-strong 的定向 D 出发。假设

    |δ_G(X)|≥2k+2，∀∅≠X⊊A。                       (M)

**Relative augmentation theorem.** 存在一个只翻 H 中 physical copies 的有限 word，每一个中间定向仍 globally k-arc-strong，终态满足

    d⁺(X)≥k+1，d⁻(X)≥k+1，∀∅≠X⊊A。              (STRICT)

可以选择 word 长度不超过 `n²(n−1)²`；此处只断言 word 存在及长度界，不未经论证声称 cut-family selection 算法已实现。

当 `n=1` 时 STRICT 没有 proper rows，空 word 即可。以下取 `n≥2`。

在原始 true-critical residual system 中，STRICT 恰为所有 proper residual slacks 至少 1，且 (M) 恰为所有 proper `µ≥2`。概念上反转所有 directions 只用于对偶证明：实际执行仍只翻同一批 H-copies，root boundary 从不被翻。

## 2. Cut identities 与最小紧割 frontier

写 `o(X)=d⁺(X)`、`i(X)=d⁻(X)`。对 `X,Y⊆A`，exact identities 为

    o(X)+o(Y)=o(X∩Y)+o(X∪Y)+m_G(X−Y,Y−X)，        (2.1)
    o(X)+i(Y)=o(X−Y)+i(Y−X)
               +m_G(X∩Y,(A∪{r})−(X∪Y)).         (2.2)

`m_G` 是两块之间全部物理 copies 的数目，方向不计。第二式的 outside 确实包括 r，不得只算 H。

令 O、I 分别为所有 nonempty proper out-k-tight、in-k-tight shores。为定义 frontier，把 A 作为两族的人工 sentinel，但在任何 cut identity 中使用 A 的**真实** cut value。令 M(D) 为 `O∪I∪{A}` 的 inclusion-minimal shores，定义

    v(D)=Σ_{X∈M(D)}(n−|X|)。

**Lemma 2.1.** M 中 proper shores 两两不交；每块只属于一种 polarity。`v=0` iff `O=I=∅`，且 `v≤n(n−1)`。

证明：同 polarity 的两个 intersecting tight shores，由 (2.1)、所有 nonempty cuts≥k 和 A 的真实 cut≥k，得到 intersection 同样 tight；若 A 的该 polarity cut 是 k+1，co-cover 的情形更直接不可能。intersection 与 minimality 排除两个不同最小 shores 相交。不同 polarity 的两个 shores 若相交且互不包含，(2.2) 使两个 nonempty differences 分别 out/in-tight，严格缩小原 shores，矛盾；nested 情形本身与 union-family minimality 矛盾。(M) 排除一个 proper shore 同时 out/in-k-tight。于是至多 n 个不交非空块，其他断言随定义成立。∎

记 `w(X)=R(X)+S(X)`，始终固定不随内部翻转改变。正常方向下

    i(A−X)=o(X)+(k+1)−w(X)。                       (2.3)

因此 `I=∅` 时，任何 X∈O 都满足 `w(X)≤k`。一个 boundary weight 为 k+1 的 proper out-tight shore 会强制其 complement 属于 I。

## 3. Proper safe source / sink：所有量词展开

**Lemma 3.1.** 若 S 是 globally inclusion-minimal 的 proper in-tight shore，则存在 s∈S，使对于每个 proper X，若 `s∈X`、`S−X≠∅`，则

    o(X)≥k+1；
    o(X)=k+1 ⇒ X−{s} 包含一个 proper out-tight shore。 (SS)

对 globally minimal proper out-tight T，有完全对偶的 safe sink t：含 t 而不包含 T 的 near-in shore，其 `X−{t}` 包含一个旧 in-tight shore。

**证明。** 在 S 内选所有 maximal out-tight shores Y₁,…,Yα。它们两两不交：overlapping pair 若 union proper，则 union tight；若 union=S，则 `o(S)≥k+2` 与 (2.1) 直接矛盾。再在 `S−∪Yj` 内选所有 maximal near-out shores Z₁,…,Zβ，near-out 指 o=k+1。这个剩余 region 不包含任何 out-tight shore，所以 intersecting Z-pair 的 intersection out≥k+1；(2.1) 迫使其 union near-out，违反 maximality（若 union=S 则 o(S)≥k+2 同样排除）。Z 块因而也不交。

若这些 Y/Z 块 partition S，内部 cross-block arcs 在总 out/in 计数中抵消，从而

    Σ_blocks(i(B)−o(B))=i(S)−o(S)≤−2。

每个 Y 有 `i(Y)−o(Y)≥2`，每个 Z 有 `i(Z)−o(Z)≥0`，矛盾。取 s 不在所有 Y/Z 中。

若 X⊊S 含 s 且 out-tight，它应包含于某个 maximal Y，矛盾。若 X⊊S near-out，它必与某个 Y 相交，否则会包含于一个 Z。这个 Y 不含 s，且 X∪Y 不是 out-tight；(2.1) 给 X∩Y out-tight，位于 X−{s} 内。

若 X−S、S−X 都非空，(2.2) 和 S 的 in-minimality 给

    o(X)+k≥o(X−S)+i(S−X)≥k+(k+1)。

所以 o(X)≥k+1；等号时 X−S out-tight，仍遗漏 s。SS 的全部情形已经覆盖。safe sink 逐方向对偶。∎

注意这里 S 必须是该 polarity globally minimal，不必预先是 union-family M 的成员。后面只有当它也属于 M 时才给它记一次 frontier removal。

## 4. Tight container 内部路径与 no-leaving route

**Lemma 4.1.** 取一个 actual out-tight container C（允许 C=A，但此时必须真实 o(A)=k），以及 x∈C。所有 out-tight shores 中，取包含 x、contained in C 的 inclusion-minimal shore Cx。则 D[Cx] 中 x 可到达所有 vertices。

证明：若 reachable set B⊊Cx，则 H 中没有 B→Cx−B arcs；所有离开 B 的 arcs 都是离开 Cx 的 arcs，故 `o(B)≤o(Cx)=k`。Legality 给 equality，B 是更小、仍含 x 的 out-tight shore，矛盾。∎

任何 proper out-tight W 含 x，都包含整个 Cx：若不然，tight intersection `W∩Cx` 又给更小 container。这句话同样适用于 Cx=A 且实际 o(A)=k。

**Lemma 4.2（no-leaving route）.** 在 Lemma 4.1 的条件下，有一条从 x 到某个 globally minimal out-tight shore T 的 safe sink t 的 directed simple path，contained in C，而且从不 leaves 任何 proper out-tight shore。

若 Cx 自身 minimal，在其内从 x 到指定 safe t 即可。否则选 Cx 内任一 smaller out-tight shore，以 Lemma 4.1 到达其中一点；在这条路径第一次触碰任意 smaller out-tight shore的位置 x′ 截断，并在 x′ 递归。

第一次触碰之前，若某个 out-tight W 已含某个 path vertex：含 x 的 W 包含 Cx，无法被 leaves；不含 x 的 W 与 Cx 的 intersection 是 smaller tight shore，第一次触碰条件禁止提前遇到它。递归 suffix 从 x′ 出发，contained in 新的 Cx′；Cx′ 又被所有含 x′ 的 tight shores 包含。因此整条 route 一旦 enter 任意 out-tight shore，就永不 leaves。每次 container 严格缩小；各 prefix 与其 suffix 只共享接点，可以选 simple path。对 in-tight container 的对偶 statement 给从某个 minimal in-tight S 的任意指定 safe source s 到 x 的内部 path。∎

## 5. Clean macro：只要 I 非空便有 frontier 下降

mixed container 指 O/I 中的 proper shore，包含一个另一 polarity 的 proper tight shore；若没有 proper mixed container，则把 A 作为最小 mixed container。若有 proper mixed container，选 inclusion-minimal 的 C，必要时概念反向，使 C∈I。

### 5.1 C proper

取 C 内一个 globally minimal out-tight T₀。它不能包含任何 in-tight shore，否则 T₀ 是更小 mixed container，因此 T₀∈M。

对任何 in-tight W touching T₀，(2.2) 与 T₀ 的 out-minimality 迫使 `T₀⊆W` 或 `W⊆T₀`；后者被更小 mixed container 排除。再对 W、C 做 same-polarity intersection，得到包含 T₀ 的 in-tight `W∩C`。C 的选择迫使 `C⊆W`。所以对 t₀∈T₀，最小 in-tight container 正是 C。由 Lemma 4.1 的 in-dual，C 内每个 vertex 都可到达 t₀。

选 C 内 globally minimal in-tight S（它可能等于 C），取 Lemma 3.1 的 safe s∈S。s 不属于 C 内任何 proper out-tight U：若 s∈U，mixed difference identity 和 S 的 minimality 迫使 S⊆U 或 U⊆S；SS 排除 U⊊S，另一情形产生 smaller mixed container。故可以从 s 到 t₀ 的 path 上，截到第一次碰到 C 内 proper out-tight shore的位置 x，再用 Lemma 4.2 接到某个 globally minimal out-tight T 的 safe sink t。这产生 simple P=s→t⊂C，分为：

- Q1：接点前不属于任何 C 内 proper out-tight shore；
- Q2：从不 leaves 任何 global proper out-tight shore。

对于这个新的 T，相同 argument 仍给：每个 in-tight shore containing t 都包含 C。

### 5.2 C=A，proper O、I 均非空

此时不存在任何 proper mixed container。任取 minimal out-tight T₀ 与 safe t₀。任何 proper in-tight W 都与 T₀ disjoint：若 touching，mixed differences / minimality 会迫使 nested，继而给 proper mixed container。

在 H 中从 t₀ 作普通 backward reachability，记 B。若 B 不触碰任何 proper in-tight shore，则 L=A−B 非空 proper；H 中没有 L→B，故

    o(L)=R(L)≤R(A)=k。

Legality 使 L∈O，而所有 proper in-tight shores 全部 contained in L，矛盾。因此 B 触到某个 W∈I，取 x∈B∩W。用 proper in-route 从某个 globally minimal in-tight S 的 safe s 到 x，再接 x→t₀ 的 directed path，得到 s→t₀ walk；erase loops 得 simple path。

s 所在的 minimal in-tight S 与所有 proper out-tight shores disjoint（同一 no-mixed-container argument），所以它在途中确有首次 O 触点。按前节截前缀、接 no-leaving route，得到 P=s→t。其 safe T globally minimal，而所有 proper I shores 都遗漏 t。

这一证明不需要 candidate 原稿中“删去 enter-I arcs”的过滤搜索；普通 backward reachability 已足够。并且完全没有把真实 `i(A)=k+1` 误用成 k。

### 5.3 C=A，原方向只有 proper I 非空

概念反向。反向模型中 proper I 为空、proper O 非空，而真实 `i(A)=k`、`o(A)=k+1`。

H 强连通：否则某个 proper backward-reachable B 没有 internal incoming，`i(B)≤i(A)=k`，给 proper I，矛盾。在 A 内做 Lemma 3.1 的 Y/Z cover selection，此时覆盖总账本为

    Σ_blocks(i−o)=i(A)−o(A)=−1，

而 block 左侧仍至少 2α≥0。因而存在 s∈A 遗漏全部 Y/Z。对于 near-out X 含 s，与 maximal out-tight Y 相交；proper union 情形照旧，若 union=A，实际 o(A)=k+1 也使 intersection out-tight。故人工 S=A 在此分支是**真实 in-tight** safe source，SS 对全部 proper X 成立。

H 强连通给从 s 到 O 的 path；首次 O 接点之后接 Lemma 4.2。Proper I 为空，所以 incoming prefix 没有 tight blockers。

### 5.4 每个 physical prefix 合法

三种情形中都从 t 端逆序翻 P。某一 suffix 被翻后，其 frontier 为 f，净 cut 变化是

    Δo(X)=1[t∈X]−1[f∈X]，Δi(X)=−Δo(X)。          (5.1)

非tight cuts 最多损 1，仍≥k。Root cut不变，因为每条 copy 都内部。

对 proper C，若 out-tight W 含 f 不含 t：W⊆C 被 Q1/Q2 性质排除，C⊆W 不可能遗漏 t；若 W crossing C，T 与 W 的 out-minimal intersection 性质给 T∩W=∅，(2.2) 给 proper in-tight C−W，其中包含 T，形成 smaller mixed container，矛盾。任何 in-tight W 含 t 都包含 C，故也含 f，排除 incoming 损失。

对 C=A、两族非空，Q1 避开全部 proper O，Q2 不 leaves O，排除 out 损失；所有 proper I 都遗漏 t，排除 in 损失。

对反向模型 C=A、proper I 空，out 用同一 Q1/Q2，incoming 没有 proper tight blocker。因此所有 flips 合法。

### 5.5 Frontier transition 的完整证明

整个 P 翻完，净变化把 (5.1) 中 f 换成 s。T 的 outcut 从 k 升到 k+1，incut 原≥k+2、降 1 后仍≥k+1，故 T 离开两族。若 S 是 proper 且 S∈M，则 S similarly 离开两族。记实际退出的 old minimal shores 为 B；B 包含 T，且至多另有 S。

若 proper S 不属于 M，那么 S 必等于所选 proper mixed C；s 不在任何 old minimal row 中。人工 S=A 的分支也如此。因此 B 之外的 old minimal shores 全部遗漏 s,t，cut values 不变。

现在逐类看一个**新** minimal proper shore X：

1. 若它旧时已经 tight 但不 minimal，选其中一个 old minimal U。若 U 未退出，U 仍 tight 且 U⊊X，X 不可能新 minimal。所以 X 必含一个退出的 old minimal shore。
2. 若它由 near-in 变为 in-tight，则 t∈X、s∉X。Safe sink 保证 T⊆X，或 X−{t} 含一个旧 in-tight U。后者遗漏 s,t，仍 tight，排除 minimality；前者必须 strict，因为旧 i(T)≥k+2。
3. 若它由 near-out 变为 out-tight，则 s∈X、t∉X。Proper safe source 保证 S⊆X，或含一个旧不变 out-tight U。后一情形不 minimal。前一情形 S=C 时含 t 而矛盾，S∈M 时必须 strict，因为旧 o(S)≥k+2。Artificial S=A 不能 contained in proper X，只有 retained-tight-child 情形。

因而每个 new minimal row **strictly contains** 至少一个 B 中的 whole old shore。

还必须反查 retained old minimal U 是否可能被新小 tight row Z⊊U 夺去 minimality。若如此，取 Z 内的 new minimal X，则 X 不是 old M row，按刚才分类它包含一个 exited old minimal V。旧 M 的 disjointness 给 V∩U=∅，与 V⊆X⊊U 矛盾。因此所有 retained old minimal shores确实保留 minimality，而非仅保留 cut equality。

这些 strict containment、disjointness 表明：新 rows 只能使 removed old rows enlarge、merge 或 drop，不能 fork，也不能出现没有 old ancestor 的 fresh row。每个新 row 分配一个它包含的旧 B-row（不同新 row 不能分配同一个），有

    n−|X|<n−|assigned old shore|。

B 非空，所以 `v_new<v_old`。达到 strict 时 M={A}、v=0，同样下降。∎

只要正常方向 I 非空，就能用上述三分支进行 clean macro；每次 v 降至少 1。有限 clean phase 最终得到 strict，或正常方向 I 为空。

## 6. No-I weak source：唯一失去祖先的例外

恢复正常方向 R(A)=k、S(A)=k+1。设 I=∅、O≠∅。

所有 maximal proper out-tight Yj 两两不交。只需排除 overlapping pair：proper union 违背 maximality；若 overlapping union=A，(2.1) 使 intersection tight且两个 nonempty petals P、Q 之间没有 physical edge。由两个 out-tight 等式，`i(P)=w(P)`、`i(Q)=w(Q)`。I 空给两者 w≥k+1，违反 total boundary 2k+1。注意此 zero-petal argument 只用于 **overlapping** co-cover pair；disjoint pair 不需要也不能引用它。

在 remainder A−∪Yj 中选 maximal near-out Zj，它们 disjoint。若 Y/Z blocks partition A，总账本为

    Σ_blocks(i−o)=i(A)−o(A)=1，

而 Y blocks 各贡献至少 2、Z 各至少 0，且 Y 至少一块，矛盾。选 s 在这些块外，故 s 不属于任何 O，含 s 的 proper cuts out≥k+1。

**Weak-source dichotomy.** 若 proper near-out X 含 s，则：

    X−{s} 含一个 out-tight shore；或 w(X)=k+1。     (WS)

证明：X 必触某个 Y。若 X∪Y proper，则 intersection tight；若 union=A，(2.1) 给

    o(X∩Y)+m_H(X−Y,Y−X)=k+1。

Intersection tight 时已有证书。否则 intersection near-out且 physical petals 之间无 edge。令 J=X∩Y、P=Y−X、Q=X−Y，三个 nonempty blocks partition A。记 b=m_D(J→P)、d=m_D(J→Q)。三个 out 等式分别给

    b=R(P)+1，d=R(Q)，i(P)=w(P)+1，i(Q)=w(Q)。

I 空强制 `w(P)≥k`、`w(Q)≥k+1`。Total 2k+1 随即给

    w(P)=k，w(Q)=k+1，w(J)=0，w(X)=k+1。          (HEAVY)

这覆盖全部 exception。∎

## 7. Weak macro 的新 frontier

因为实际 o(A)=k，Lemma 4.2 从这个 s 给一条 no-out-tight-leaving P 到某个 globally minimal out-tight T 的 safe t。从 t 端逆序翻，(5.1) 的 out 损失被 no-leaving 排除，incoming 无 proper tight blockers，所以 word 合法。

T 退出两族；其他 old M rows 不含 s,t。新 near-in→tight row 由 safe sink 必 strict contains T，因为 old I 空。新 near-out→tight row 若含 old tight child，则 child 遗漏 endpoints、仍 tight，不能 minimal；否则由 WS 它的 w=k+1。旧时 tight 而非minimal的新row，若出现，也必须 strict contains T（一般分类已足够，无需优化）。

因此新 M 只可能含：retained old rows、至多一个 strict superset of T、至多一个 HEAVY row。后两种不能重合，因为 HEAVY out-tight row遗漏 t，而 T含t。Retained minimality 用5.5的反查：新 grown row contains T，不可能藏在 retained disjoint old row；HEAVY 新 out-tight row含s，retained old row遗漏s，新 in-tight row含t，也不可能藏进去。

HEAVY 至多一块，因为新 M disjoint，两块各w=k+1会超过 boundary total。若 HEAVY X 出现，(2.3) 给 A−X∈I，于是下一阶段必可运行 clean macros；complement 无需自身是 minimal row。

## 8. 历史标签证明：No-I 宏循环严格下降

在 No-I、非strict 起点 D₀，给每块 old M=T₁,…,Ta 一个 original label，它的 container 是该 whole shore。

weak macro 后，若某 new minimal row whole-contains 一个 old shore，就把其 label 转入该 row；否则 drop。Retained label 不变；T 的 label 必 strict enlarge 或 drop。一个 old shore 不会 whole-contained in 两个 disjoint new rows，所以 label 不 fork。若有 HEAVY fresh row，给它一个额外 heavy label。这时每个 frontier row 至少有一个 label。

随后运行有限 clean phase，直到正常方向 I 再次为空或达到 strict。5.5证明每个 new minimal row whole-contains exited old shore；沿同一规则转移所有 labels、merge 时一起携带。各 container 单调 enlarge；no-fork、每row至少一label均持续成立。

若结束于 strict，定理已完成。若结束于 No-I 非strict，所有 minimal rows 是 out-tight、且由 (2.3) 有 w≤k。Heavy label 的每个后继 container 都包含最初 w=k+1 的 HEAVY shore，故这个 label 不可能仍存活。每个 endpoint row因此至少携带一个 original label。

按 original labels（不含 fresh heavy）计量

    Ψ=Σ_alive original labels(n−|current container|)，drop 贡献0。

所有 container 只 grow 或 drop，所以 Ψ 不增；T original label 在第一 weak step strict grow/drop，贡献严格下降。起点 Ψ=v(D₀)；终点每row至少一个 original label、每row贡献非负，故

    v(Dend)≤Ψend<Ψstart=v(D₀)。                     (8.1)

这是一整个 No-I→weak→clean→No-I 的下降，允许 weak step 本身因 HEAVY birth 暂时增加 v。

先运行初始 clean phase；然后重复8.1的阶段循环。v 非负整数，所以 finite termination，只能落在 strict。Relative augmentation theorem 的存在部分完成。∎

## 9. 有限 word 长度界

每条 macro path 可以选 simple，至多 n−1 physical flips。设初始 v₀≤n(n−1)，W 为 weak macros数，C 为 clean macros数。

完整阶段下降给 W≤v₀。一次 weak macro，old labels 至少因 T 少贡献1；至多额外一条 fresh HEAVY row贡献≤n−1，故

    v_after−v_before≤n−2。

clean 每次降至少1；把所有阶段的 v 变化 telescope 至最终0，得到

    C≤v₀+(n−2)W；
    C+W≤nv₀≤n²(n−1)。

因此全部 flips≤`n²(n−1)²`。这不把 degree-polytope connectivity 混成 physical prefixes；本 proof每个 prefix都用5.1或7的 old-tight-cut检查。

## 10. µ≥2 initial full fiber 的 H1 闭合

`research_global_scope.md` Theorem14已证明：一个 initial true-critical fiber 内所有 strict orientations都在同一个 original physical flip component；degree unit transfers在strict起点可serialize，且 macro终点恢复strict。

本定理证明任意合法 initial state到某个strict state。将两个 arbitrary endpoints 各自augment、在unique strict component内连接、再倒放第二个augmentation word，即得到

    全部proper µ≥2 ⇒ initial full fixed-boundary fiber connected。

该结论不限制intermediate paths的buffer width为常数，也不要求monotone翻指定K；没有与固定k=2的无界 terminal width controls冲突。

## 11. 两轮审计实际修正了什么

1. C=A、两族非空的路径存在性不需要 filtered graph；普通 backward reachability给更短、量词更明确的证明。
2. Proper C 情形，新 target T 可以因 splice变化；已重新对这个 T证明每个含t的in-tight shore contains C，不能只对最初T₀证明后直接复用。
3. retained old minimal shore的 minimality必须反向检查；cut equality保持本身不够。5.5、7已分别证明不会被new subset夺去minimality。
4. No-I maximal O 的zero-petal co-cover论证只用于overlapping pair；disjoint pair无需该论证。
5. Artificial A只有在真实polaritycut等于k时才允许route/safe-source lemma。5.2始终使用真实 o(A)=k；5.3概念反向后只把真实 i(A)=k当source sentinel。
6. Fresh heavy label只在No-I endpoints必灭；clean阶段中允许merge、暂存，不把“weight≥k+1”误当立即无法legal。
7. 存在性与长度界已闭合；选择所有tight shores的高效算法、一般µ=1历史动力学、signed descendant H1均不随本定理自动完成。

与 [Ito 等的原始论文](https://arxiv.org/pdf/2110.11585) 的关系只在方法层面：使用minimal tight shores及safe endpoints处理path prefixes。本证明新增fixed odd-boundary的HEAVY例外和ancestor-label阶段账本，不把原论文的global `(2k+2)` theorem直接当relative theorem引用。

## 12. 指定 HEAVY birth 实例：阶段势确实可以暂时上升

`k=2,A={a,b0,b1,c}`。初始内部 copies 为 `a→b1`2条、`b1→a`2条、`a→c`1条、`c→a`3条、`b0→b1`2条、`b1→b0`4条。Boundary 为 `b1→r,c→r,r→b1`各1条、`r→c`2条。

所有proper内部 µ≥2，root cut5。初始 O 为 `{b0}`及`{a,b0,b1}`，I 空；M只有`{b0}`，v=3。Weak source取c，safe sink取b0，path为 `c→a→b1→b0`。从target端逆序翻指定copies，得到 HEAVY minimal OUT `{a,c}`（w=3），及minimal IN `{b0,b1}`；此时v=4，旧b0标签grow到后一块，HEAVY块获得fresh label。

再翻一条指定 `b1→a` copy，所有proper cuts都out/in≥3，v=0。宏端点势为 `3→4→0`。它明确表明不能要求每个weak macro自身使v下降；需要第8节的阶段账本。

独立逐割核验：5个prescribed states，各检查全部30个global proper cuts与14个residual µ rows；全部PASS。没有枚举其他orientations。脚本 `scripts/verify_relative_heavy_phase.py`；raw `data/relative_heavy_phase_certificate.json`；SHA256 `data/relative_heavy_phase_sha256.json`。

## 13. Whole-fiber diameter的显式上界

`research_global_scope.md` §17进一步证明degreepolytopeintegerpoints有targetedunitchain长度恰L1/2。两个strict states因此可用word长度≤nm连接（unitpaths≤n−1、最后Eulerian difference≤m）。任意两个initialendpoints各用本定理augment，再走strictcomponent，倒放另一endpointaugmentation，得到

    diam≤2n²(n−1)²+nm，n=|A|、m=|E(H)|。

这保留parallelphysicalcopy身份。界不追求最优；其用途是说明本子类的finitehistory不只来自finite-statepigeonhole，而有明确polynomial-lengthcertificate。
