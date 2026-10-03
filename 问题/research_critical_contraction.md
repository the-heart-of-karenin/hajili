# Odd critical-cut contraction 与一般 µ=1 前沿

2026-10-02，接续 µ≥2 relative augmentation。本文区分已证明 reduction 与尚未完成的一般动态结论。

## 1. Odd global mincuts 必 cross-free（已证明）

设 λ(G)=2k+1=L。若两条 mincut shores X,Y crossing，四个 Venn regions I=X∩Y、P=X−Y、Q=Y−X、O=V−(X∪Y) 都非空。

Undirected cut identities 与每个 region 的 cut≥L 给

    δ(X)+δ(Y)=δ(I)+δ(O)+2m(P,Q)，
    δ(X)+δ(Y)=δ(P)+δ(Q)+2m(I,O)。

两边都是2L，因此 m(P,Q)=m(I,O)=0，四块 δ 恰L。记 remaining cycle links `a=m(I,P), b=m(P,O), c=m(O,Q), d=m(Q,I)`。Region cuts给 a+d=a+b=c+b=c+d=L，故 a=c、b=d。但 δ(X)=b+d=2b=L，与L odd矛盾。∎

因此全部undirected mincut splits有cross-free tree representation。该静态结构不独自给flipgraph connectivity：tree的empty nodes仍可能代表由多个odd-degree blocks组成的高阶quotient。

## 2. Strict critical block 上的所有tight globalcuts都 respecting contraction（已证明）

设 A是critical shore，δ(A)=2k+1。当前D globally k-arc-strong，且所有∅≠Y⊊A都有

    o(Y),i(Y)≥k+1。                                (S)

**Lemma 2.1.** 任意global out-k-tight shore X要么包含整个A，要么与A disjoint。

若X⊊A或V−X⊊A，(S)直接排除。其他partial-A情形满足 A∩X、A−X、X−A、V−(A∪X)都非空。

- 若o(A)=k，out submodularity给 `2k≥o(A∩X)+o(A∪X)≥(k+1)+k`，矛盾。
- 若i(A)=k，mixed posimodularity给 `2k≥o(X−A)+i(A−X)≥k+(k+1)`，矛盾。

criticalcut在这两种polarity中必有一个恰k。因此lemma闭合；对in-tightshore通过complement同理。∎

**Corollary 2.2（one-step quotient lift）.** 收缩A成a，删除H内部loops、保留其他physical copy身份。若D满足(S)，则D/A中的任意legal single-edge flip，在D中翻同一条copy也globally legal。

Proof：若原图翻转失败，旧D有一个tail-in/head-out actualtight blocker。Lemma2.1使它respect contraction，遂给quotient中的同一blocker，与quotient flip合法矛盾。∎

这个结论覆盖boundary edges及完全outside edges。Boundary flip之后(S)可能丢1单位，下一次quotient move前需要重新augment；没有声称(S)自动永久保持。

## 3. µ≥2 fiber theorem 给无内部criticalcut的block收缩（已证明）

设A是inclusion-minimal nonempty globalmincut shore，且|A|≥2。则每个proper nonempty Y⊊A不是mincut，故δ(Y)≥2k+2；A−Y也一样。于是A内部全部µ≥2。

若Ω_k(G/A)connected，则Ω_k(G)connected：

1. 给任意端点D,E，quotient orientations均合法，选quotient legal word从D/A到E/A。
2. 每一步前，在当前fixed outside signature下用relative augmentation theorem把H内部augment到(S)；outside/quotient orientation不变。
3. 用Corollary2.2 lift该quotient flip。当前原图仍合法，A boundary的两向仍k/k+1；下一步可以再次augment同一block。
4. 到quotient目标后，outside/boundary copies与E相同。allµ≥2 initial full fiber H1给内部word达到E。

所有moves都有原始physical copy身份；quotientword中不会翻被删除的Hloops。G/A的每条cut是原图cutpreimage，因此λ(G/A)≥2k+1。

**Minimum-counterexample reduction.** 若按|V|选一个主定理最小反例，λ必2k+1（2k+2 baseline已知），则每个inclusion-minimal globalmincut shore都是singleton。否则G/A顶点更少，归纳假设和本节lift立即排除该反例。

这是一个scoped reduction，不等于“所有nontrivialmincuts均可直接收缩”：若A包含criticalsingleton，其内部µ1，本文第3节augmentation前提失败。

## 4. 同一global frontier中的critical minimal shore必是undirected最小shore（已证明）

令M为当前global O∪I的inclusion-minimal proper shores，假设δ(T)=2k+1且T∈M。若有∅≠Y⊊T、δ(Y)=2k+1，D的k-strength迫使Y有一种polarity恰k。因此Y∈O∪I，违反T∈M。故T是inclusion-minimal undirectedmincutshore。

组合第3节：在minimumcounterexample中，每个critical M-row必为singleton。每个nonsingletonM-row有δ≥2k+2。实际上一个noncriticalM-row也不可能含odd-min-degreevertex，因为其singletondegree2k+1必在O∪I中。

这把一般动态难点压向：如何穿过critical singleton的polarity交换，服务一个noncriticalminimal row，或直接解除minimumdifference宏的封锁。

## 5. Global proper safe-endpoint lemma也能扩至λ≥2k+1（新证明）

这里只谈global graph，不固定一个odd-boundaryroot。设S globally inclusion-minimal in-k-tight，λ(G)≥2k+1。则仍可找到proper safe source：对s∈X且S−X非空，o(X)≥k+1；若o(X)=k+1，X−{s}含out-tightshore。对minimalOUT有safe sink。

与µ2 proof的差别必须明确：out(S)可能只有k+1，out-tight Y的incut可能只有k+1；原proof中的“至少2”收费降成“至少1”。Near-out Z proper contained in S有incut≥k+1，原因是S的IN-minimality，而不是所有global cutsµ2。

在S内取maximalOUT Yj，pairwise disjoint：overlapping union proper仍tight，union=S会因out(S)≥k+1不可能。再在S−∪Yj内取maximal proper near-outZj。

普通overlap union⊊S时，intersection不含outtightshore，故out≥k+1，submodularity使unionnear，与maximality冲突。唯一新风险是overlapping union=S。如果out(S)≥k+2，立即不可能；剩余out(S)=k+1，此时S是真正criticalcut，boundary out=k+1、in=k。

设Z1,Z2 co-coverS，intersectionJnearoutk+1、two petals P,Q无physicaledge。三个out等式给 `m_D(J→P)=R_S(P)`、`m_D(J→Q)=R_S(Q)`，因此

    i(P)=w_S(P)，i(Q)=w_S(Q)。

S最小IN使i(P),i(Q)≥k+1，而w_S(S)=2k+1，矛盾。故nearZ仍pairwise disjoint。

若Y/Zblocks覆盖S，total账本为 `Σ(i−o)=i(S)−o(S)≤−1`；每个Y贡献≥1，每个Z贡献≥0，矛盾。选择s在覆盖外。Proper-subset-S与outside-S的nearcut证明沿用relative审计的intersection/mixed identity，全部合法。∎

此lemma并不证明全局(k+1)augmentation；critical服务只换polarity，不能消灭criticalcut。

## 6. Anchored odd-boundary clean macro在µ1时发生什么（精确ledger；终止仍OPEN）

这里重新固定一个critical singleton root r，取A=V−{r}，boundary为k/k+1；O/I仅含不经过r的proper X⊊A，另有A sentinel。在minimumcounterexample中必存在这样的r，因为第3节把inclusion-minimalglobalmincutshores压到singletons。

第5节proper safe endpoints对这些shores同样适用：S的proper subsets均不经过r，minimality所用范围不变。C proper的prefixcut检查及C=A两族非空的backwardsearch，与relative审计相同。C=A只有normal I的分支概念reverse后，A是actualin-tight，且proper I为空；A因此本身是globalminimalINshore，直接用第5节safe-source lemma即可。H强连通及Q1/Q2构造仍成立。

**必须记录的scope修正。** 不能把relative no-leaving route直接套到包含root的全部global OUT shores：两条globalOUTshore可能co-coverV，submodularity中的out(V)=0，此时intersection未必tight。Root-excluded families则union最多A、真实out(A)≥k，tightintersectionproof有效。因此本节不声称有一个对所有globalOUTrows同时no-leaving的unanchoredroute。

服务一个minimalOUT T后：

- δ(T)≥2k+2：out从k升k+1，in仍≥k+1，T退出M；
- δ(T)=2k+1：out从k升k+1，in从k+1降k，T保留同一shore但从OUT切换为IN。

若properminimalIN S也在M，其变化完全对偶。Newminimalrows若strictcontains一个保留、已换polarity的oldrow，仍有tightchild而不能minimal；只有真正退出的noncriticaloldrow能被enlarge/merge/drop替代。因而v不增，至少一个noncriticalendpoint退出时严格下降。

但服务两个criticalendpoints时，M可以完全不变、仅颜色交换，v不降。一个proper mixed C的minimalIN source若等于C而不在M，服务criticalT也可能只把T换色。不能由“每次合法服务”直接推断有限terminalprogress。

**当前OPEN接口。** 在minimumcounterexample中，零下降阶段的criticalMrows全是singletons。需要证明这些polarity交换的history能把safe path导向一个noncriticalMrow / 指定difference支撑，或给另一个严格下降量。尚未得到该全量词结论。把finite状态空间与公平选点并列，并不排除循环；不能冒充terminationproof。

## 7. No-I弱source在µ1时的精确失败层（已证明）

继续root-excluded odd-boundary模型，正常方向out(A)=k、in(A)=k+1，properI为空。MaximalproperOUT Yj仍pairwise disjoint：overlap union proper由tightunion排除，overlap co-coverA由zero-petal / boundary-weight contradiction排除，后者只需I为空、不需要µ2。剩余region中的maximalnearOUT Zj也disjoint。

若所有Y/Zblocks覆盖A，账本要求

    Σ_blocks(i−o)=1。

每个Y贡献至少1，每个Z贡献至少0。因此cover只可能有**恰一个**maximalOUT Y，且

    δ(Y)=2k+1、i(Y)=k+1；
    每个Z都有out=in=k+1、δ(Z)=2k+2。             (COVER-EXCEPTION)

所以当有至少两个maximalOUTblocks，或唯一maximalOUT的undirectedcut≥2k+2时，仍有weaksource s遗漏全部OUT/nearblocks。对这种s，relative审计的WS proof沿用；唯一nearcut例外仍是w(X)=k+1的HEAVY shore。

FreshHEAVY row一定noncritical：它旧时nearOUT k+1，而oldI为空使oldIN≥k+1，故δ(X)≥2k+2。这使其服务时可以真实退出tightfrontier。

但weakmacro若只服务criticalT，它只把T换色，originalT-label不strictgrow/drop。即使freshHEAVY在回到No-I前必灭，original-labelpotential也只能不增，不能复制µ2 theorem的strictdescent。COVER-EXCEPTION之外，“有weaksource”仍不足以排除zero-progress历史循环。

## 8. Critical singleton 的标签永久性（已证明的障碍）

若vertexx的undirecteddegree=2k+1，则任意globallyk-strongorientation中它恰有一种polaritytight；singleton{x}在root-excluded模型中（x≠r）始终属于M。它不能whole-contained in任何另一个minimalrow，不能通过frontiergrowth或drop消灭，只能OUT/IN换色。

因此allµ2 theorem的“每个servicedlabel必grow/drop”对minimumcounterexample中的criticalsingleton不能补一个小技术修正就复用；必须改用noncriticallabel推进、指定macro支撑的进度，或控制colour交换本身。当前本文把这点作为真实结构障碍，不将它标为算法失败或counterexample。
