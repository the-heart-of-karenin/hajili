# B+ common-completion 与全局 contraction induction：完整审计

2026-10-03。状态：本文件给独立完整证明。它关闭旧主稿 B+ / nonboundary lift 的引用与 scope 债务；不声称 general μ=1 fiber connectivity 已证明。

## 1. Even balanced-root extension theorem

### 定理 1

G₀ 是 finite loopless physical multigraph，λ(G₀)≥2k，V=A∪{r}，root degree=2k。任意固定 root-edge orientation，只要其 root outdegree、indegree 均为 k，就有一个 G₀[A] 内部定向扩展，使全图 k-arc-strong。

这是任意指定 balanced root signature 的 extension，不是仅存在某个 signature。允许 parallel identities；k≥1。

### 1.1 Residual model 不需要事先有合法扩展

令 R(Y) 为 Y→r copies，S(Y) 为 r→Y copies，R(A)=S(A)=k。对 proper nonempty Y⊊A，定义

    q(Y)=min{R(Y),S(A−Y)}，p(Y)=k−q(Y)。

root-contracted 图只有两类 global cuts，即 Y 和 {r}∪Y，所以内部合法性与 out_H(Y)≥p(Y) 等价。q非负、submodular，p integer crossing-supermodular且非负。

令 b=R+S，总边界2k。直接 min 运算给

    q(Y)+q(A−Y)=min{b(Y),2k−b(Y)}，
    μ(Y)=δ_H(Y)−p(Y)−p(A−Y)
        =min{δ_G₀(Y),δ_G₀(A−Y)}−2k≥0。

balanced signature 还有 q(A−Y)−q(Y)=S(Y)−R(Y)。故每个非平凡 partition A=⊔P_i 的 Φ=0，并有

    2(M_P−Σ p(P_i))=Σ μ(P_i)≥0，
    2(M_P−Σ p(A−P_i))=Σ μ(P_i)≥0。

这些是无向边数和固定边界的恒等式，未使用一个尚未构造的合法内部定向。

### 1.2 Fractional existence：无须借用外部 orientation min-max

若 |A|=1，内部无约束，结论直接成立。否则在完整 fractional orientation box 中定义

    ε*=max_x min_{proper Y} [out_x(Y)−p(Y)]。

任意 box point 使某个足够小 ε 可行，因此 LP 非空；box compact 且 rows finite，最优值有限并 attained。这里不假设 ε=0 已可行。

反设 ε*<0。LP/minimax dual 给 y_Y≥0、Σy=1，使：positive rows在最优 x* 处 out=p+ε*；x* 最大化其 weighted outcut。选择最优 y 中 shore potential Σy_Y|Y||A−Y| 最小者。

两个 positive rows crossing 时，fractional cut submodularity和 p crossing-supermodularity使两个 corners同样 active，demand defect=0，petals间没有任何 physical edge。把共同权重转至 intersection/union 保持整个 weighted objective，而严格降 potential。因此 positive support F cross-free。

F 不含互补 rows：若两者 active，会给 μ(Y)=2ε*<0，与 μ≥0矛盾。它也不含 actual partition/cpartition at ε* level：该 partition的总 slack为 tε*<0，与1.1的无向恒等式矛盾。因此 split tree 的 empty nodes 均 mixed。

坐标最优性给：任意跨 F-atoms 的正方向质量，都必须 consumes至少一个 F-row；否则所有 y在F上 strictly positive，strict-source方向会增加 weighted outcut，不可能被最优 fractional orientation 采用。

写 t=|F|，n为 occupied atoms数，e=t+1−n，Q=Σ_Fq。按 fractional mass计 ν=negative row数、σ=Σ mass·(ν−1)。tight-row sum给

    M+σ=t(k+ε*)−Q。

已有 CFST 的两个 packings 在 fractional mass下不变：每个 q-row只付一个空节点；negative-negative相邻 pairs总数≤ν−1。每个 mixed empty union U_v 为 proper，LP约束给 out(U_v)+q(U_v)≥k+ε*。所以

    Q+σ≥e(k+ε*)，
    M≤(n−1)(k+ε*)。

另一方面，收缩 atoms与root所得图仍 λ≥2k，root degree=2k，每个atom degree≥2k，因此

    2M+2k≥2kn，M≥(n−1)k。

n≥2且 ε*<0使两界矛盾。故 ε*≥0，fractional orientation满足原 demand p。

### 1.3 Integer extraction

已独立证明的 orientation-box primal integrality适用于任何 integer crossing-supermodular proper-cut demand，包括本 p。非空 bounded box因而有 integer vertex，即所需内部物理定向。定理1完成。∎

证明不依赖 dual整数性、未定位的 min-max编号或初始合法扩展；它是 balanced even-root的新精确 corollary，不重证 odd μ≥2 reachability。

### 1.4 第二条独立证明：admissible pairing 与整数 Hall

另可用 research_pairing_lift_route.md 中核对的primary Claim4。对G₀选oddvertices的pairingM，使δ_M≤δ_G₀−2k。Root degree2k为even，所以M没有rootcopy。E=G₀+M是Eulerianundirectedgraph，λ(E)≥2k，rootdegree仍2k；指定rootstar仍balancedk/k。

令H′=E[A]，每个vertex需要internaloutdegree b_v=deg_E(v)/2−R(v)。Total b(A)=|E(H′)|，integerHall条件b(X)≥|E(H′)[X]|恰δ_E(X)/2≥R(X)，左侧≥k、右侧≤R(A)=k，因而成立。得到Eulerianextension F ofE。

投影F−M的outcut为(δ_G₀−δ_M)/2+in_M≥k；fixedrootstar不变。这独立核对了定理1的任意指定signature量词，不依赖前面的LP负ε与empty-node推导。

## 2. B+：quotient-legal boundary flip 有同一个 deletion completion

### 定理 2

G满足λ≥2k+1；A是critical shore，δ(A)=2k+1；D globally legal。收缩A后的 D/A 中，一条boundary physicalcopy e的单翻仍合法。则固定除 H=G[A] 与 e外的全部 directions，有一个 H内部定向 F，使删除e后的 G−e globally k-arc-strong。于是将e以任一方向加回同一个 F 都合法。

### 2.1 Quotient deletion 合法且边界 balanced

对任何 cut，删除当前arc与反转它的危险条件相同：只有它当前 leaves的 cuts会降低1；反转合法说明这些cuts旧值≥k+1。因此 (D/A)−e也合法。

其 contracted vertexdegree=2k，两向都≥k，所以边界恰k/k。G−e的无向cuts都≥2k。

把outside B=V−A再收成root r，删去outside内部loops，保留边界 identities。所得 G₀ 每个cut是 G−e的一个cut，所以λ(G₀)≥2k，rootdegree2k；固定根边 balanced。定理1给其合法 internalcompletion F。

### 2.2 检查所有 mixed cuts，不能只停在双重 contraction

记 σ⁰ 为 G−e 的固定非H directions。Quotient deletion legality使每个 pureoutsidecut的out、in都≥k。对 proper Y⊊A 和任意 Z⊆B，令 c(Y,Z) 为 fixed graph中从Y∪Z离开的copies数。

写 W=B−Z。若 W≠∅，pureoutside W 的incut≥k给

    c(Y,Z)≥k−R(A−Y)+fixed arcs Z→A−Y≥R(Y)，

因为R(A)=k。若W=∅，c(Y,B)=S(A−Y)。故

    c(Y,Z)≥min{R(Y),S(A−Y)}=q(Y)。

于是 F 的 residual inequality out_H(Y)+q(Y)≥k保护每个mixedcutY∪Z。若Y=∅或A，该cutrespect contraction，已由quotient deletion合法。所有 globalcuts已覆盖。

因此 σ⁰∪F是 G−e合法orientation；加回任一方向的e都不会降低任何cut，定理2完成。∎

## 3. Nonboundary quotient flip 在任意当前 extension 中直接 lift

### 定理 3

在同一criticalshore设置中，若surviving physicalcopyg两端都在B=V−A，且其quotientflip合法，则在任意当前globallylegalextensionD中翻g也合法，无须内部strictification。

若不合法，存在out-k-tight shoreX，g leavesX。若XrespectA，则直接给quotientblocker，矛盾。否则A∩X、A−X均非空；g的tail在X−A、head在B−X，使其它两个Vennregions也非空。

- 若out_D(A)=k，对X,A作tightoutuncross，X∪A同样outtight且g leaves它，得到quotientblocker。
- 否则in_D(A)=k，即B outtight。对X,B作同样uncross，X∩B同样outtight且g leaves它，得到quotientblocker。

两个corners均nonempty proper，所有co-cover/root-containing例外已由g两端的membership排除。定理3完成。∎

## 4. 机械的全局归约：Universal H1 单独足够

H1为：每个 genuine criticalshoreA、每个有合法扩展的固定outside signatureσ，其完整内部fiber在H physicalsingleflips下connected。

**定理4：H1 ⇒ 原始MAIN THEOREM。** 对|V|归纳。两顶点图为有身份parallelcopies，其合法方向数在[k,m−k]，m≥2k+1使至少两相邻weightlayers；这些layers组成connected hypercube slab。单顶点为空定向。

对更大的G：若λ≥2k+2，使用Ito基线；否则取δ(A)=2k+1的shore，选择|A|≥2的一侧。G/A更小且λ≥2k+1，其合法orientations由归纳connected。

给任意D,E，选quotientword D/A→E/A。非boundarystep由定理3直接lift。Boundarystep由定理2给一个同时适配e两方向的internalcompletion；H1在currentfixedoutsidefiber中把当前orientation连到该completion，然后翻e。每步逐physicalcopy合法。

quotient终点后，outside/boundary与E相同；用H1作最后internalrepair，即到E。此归纳明确减|V|，没有把frozen-sectorcomponent当ambientcomponent。∎

## 5. 最小反例进一步归约到一个根度数2k+1的初始fiber

采用 synthesis中固定的图minimality (|V|,|E|)。已知μ≥2contraction使该G的inclusion-minimalmincutshore是singleton，选criticalvertexr，A=V−{r}。

如果该A下的每个fixedrootboundaryfiber都connected，quotient是两顶点2k+1parallelcopies，其flipgraphconnected；定理2逐步提供commoncompletion即可连接G的任意D,E。因此最小G中必有某个fixedrootboundary的**初始完整fiber自身不连通**。

这一次fiberseparation的必要性不是任意freezing产生的假象：它由“若全部fibersconnected，则全图connected”的完整lift论证推出。可以在这个实际不连通fiber中另取最小Hammingpair；该pair使用fibercomponents，不宣称它们自动是原Gcomponents。

所以主问题当前可准确集中到：rootdegree2k+1、所有proper内部μ≥1、存在μ1criticalshore的完整fixed-rootfiber连通。B+和nonboundarylift不再是额外OPEN。

## 6. 更弱、与原定理精确等价的目标：same-root-star ambient mixing

§5的internal-onlyfiber theorem是充分的，但可能比原始MAIN更强。为了避免把主目标又降格/加强成不必要的freezing命题，改保留下列**允许rootbuffers**的接口。

**Root-star mixing lemma (RSM).** 若G满足λ≥2k+1、每个inclusion-minimalglobalmincutshore为singleton，且deg(r)=2k+1，则任何两个globallylegalorientations只要agree on全部r-incidentphysicalcopies，就属于同一个**ambient Ω_k(G) component**。允许连接词临时翻rootcopies，终态恢复给定star。

**RSM ⇒ MAIN，完整反证。** 若MAINfalse，取固定的vertex-minimumG，已完成contraction使其满足RSM的mincut条件，选criticalrootr。Rootstar的所有balanced signatures组成connected two-layercube。至少一个signature有合法extension；定理2沿starcube的每个neighborstep提供两个linkedcommoncompletions，因此所有balanced signatures都有extension。

RSM说同一signature的全部extensions有唯一ambientcomponentlabel。每对neighbor signatures有一个boundarysingleflip链接，故两个labels相同。Starcubeconnected使所有labels同一，涵盖所有globallylegalD，矛盾。∎

反向MAIN当然蕴含RSM。所以在已证明归约的基础上，**MAIN与这一reduced-class RSM等价**。它没有要求fixed-rootfiber本身connected，避免一个尚未必要的强化。

### 6.1 真正的ambient separation可以放到同一rootstar

同一个componentlabel论证的逆否给：若reduced-classG的ambientΩ不连通，必有某个σ的两个合法extensions属于不同ambientcomponents。这里不用断言任意fiberdisconnection都是ambientdisconnection。

在所有agree-rootstar的ambient-separatedpairs中，另定义h_r为最小Hammingdistance；σ可以在选取时变化。它不是synthesis §0 的原始h，明确另行命名。选到R,Q后，K⊂E(G−r)，共同copiesJ包含所有rootcopies。

固定共同copies所得descendant用ambientlabels最小化，仍有两antipodes、全部Kcopies在两端illegal、signed-coordinatefaceprimalintegrality、necessary circuit/vertex-disjointpaths support。

若K是physicalcircuit，任意J-word——**包括rootflips**——可同步lift到R,Q，因为整圈cutneutral。Pair一直agree当前rootstar，不要求等于初始σ。h_r minimality遂禁止任意pairedstate的K firstflip。故这个branch的K在两端整个ambientcomponents中immutable。这里没有把roottemporarysteps错误地排除在J之外。

Paths branch仍有endpoint-specificasymmetricguards，不能套circuit同步性。RSM必须同时解决这两个branches，或另建不依赖supportclassification的root-returnservice。
