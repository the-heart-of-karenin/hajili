# 五顶点原定理全闭合：heavy-star interval lift 与 heavy-triangle 删除锚预算

2026-10-03。这里证明原始MAIN的全部五顶点实例，任意k≥2与全部labelledmultiplicities。不是仅某个边数层，不是finitecensus外推。原始任意vertexcount MAIN仍OPEN。

## 1. 结论与既有独立输入

**Theorem1.1.** 若G为五顶点finite loopless labelledmultigraph、k≥2、λ(G)≥2k+1，则Ω_k(G)connected。

使用已经归档的四项独立输入：

1. 全部|V|≤4的原定理，以及五顶点有nontrivial(2k+1)-mincut时的small-critical-fiber归约：research_small_fiber_theorem.md与research_main_theorem_synthesis.md；degree-onlyserialization见research_five_vertex_minimum_edges.md §1。
2. 全部properµ≥2的genuinefixedcriticalrootstarfiberconnected，以及B+邻星commoncompletion：research_relative_reachability_audit.md、research_boundary_lift_audit.md。
3. Edge-minimalcounter中的非mincutcopies共享删除分量C°：research_deletion_component_anchor.md。
4. 全局maximalcross-free actual-tight family覆盖全部illegalcopies，且atomtree预算M≤(n−1)k+Z：research_global_source_theorem.md。其中n是membershipatoms数，不是直接代入graphvertexcount。

此外，λ≥2k+2的已知全局reconfiguration定理可排除该范围，原始输入已在前稿核对；本证明不由它推出2k+1一般情形。

## 2. Heavy pairs与singleton合法性

令L=2k+1。称multiplicity m_uv≥k+1的pair为heavy。任意singleton双向≥k的orientation，对非heavy pair都自动有

    out({u,v})=out(u)+out(v)−m_uv≥2k−m_uv≥k，

in同理。五顶点的全部propercuts都是singleton/pair或其complement。

因此只有heavy pairs需要额外pairbounds；全部globallegality恰degreebounds与这些heavy pairbounds。Parallelcopies全程保留identity。

## 3. General heavy-star lemma

**Lemma3.1.** 五顶点G λ≥L，若heavy pairs至多两条且共享一个vertex，则Ω_k(G)connected。不限制edgecount、degrees或heavy multiplicities。

Zero heavy案由degree-onlyserialization闭合。One heavy案见research_dominant_neighbor_contraction.md §6。下面证明two heavy案ab、ac，记m_1=m_ab≥k+1，m_2=m_ac≥k+1；其它pairs包括bc皆≤k。

收缩ab得四顶点Q，λ(Q)≥L，故Ω_k(Q)connected。固定任意Q-legalorientationF。记

    R_a=#a向b之外vertices的outgoingcopies，
    R_b=#b向a之外vertices的outgoingcopies，
    q=#a→c，t=#a→{d,e}，R_a=q+t，
    R_c=#c向a之外vertices的outgoingcopies，W=t+R_c。

记d_a,d_b,d_c为原graphdegrees，D_ac=d_a+d_c−2m_2。内部u=#a→b。

完整fiber精确为integerinterval

    I(F)=[0,m_1]
       ∩ [k−R_a,d_a−k−R_a]
       ∩ [m_1+R_b−(d_b−k),m_1+R_b−k]
       ∩ [k−W,D_ac−k−W]。

四组分别为physicalcopybounds、a singleton、b singleton、ac pair。Outsidevertices及ab pair由Q保证，其余pairs非heavy自动合法，故没有漏mixedglobalcuts。

### 3.1 所有upper/lower交叉差至少1

用L_a,U_a、L_b,U_b、L_c,U_c表示后三intervals的lower/upper。各自width分别d_a−2k、d_b−2k、D_ac−2k，均≥1。

令T=R_a+R_b。Q-rootcut双向≥k给T∈[k,D_ab−k]，其中D_ab=d_a+d_b−2m_1。所以

    U_b−L_a=m_1+T−2k≥m_1−k≥1，
    U_a−L_b=D_ab+m_1−2k−T≥m_1−k≥1。

Q的root+c-cut对应G的abc；令m_3=m_bc（可为0），其degree

    D_abc=D_ac+d_b−2m_1−2m_3，

cutout为R_b+W−m_3。故

    U_b−L_c=m_1+R_b+W−2k≥m_1+m_3−k≥1，
    U_c−L_b=D_ac+d_b−m_1−2k−R_b−W
              ≥m_1+m_3−k≥1。

再用c的singletondegree（Q与G相同），out(c)=m_2−q+R_c=m_2+W−R_a。于是

    U_a−L_c=d_a−2k+W−R_a
              ≥d_a−m_2−k≥m_1−k≥1，
    U_c−L_a=D_ac−2k−W+R_a
              ≥d_a−m_2−k≥m_1−k≥1。

最后全部lowers≤k≤m_1−1，全部uppers≥m_1−k≥1：前两vertexintervals由outsideprofilebounds直接得到；对第三，W≤(d_a−m_1−m_2)+(d_c−m_2)=D_ac−m_1。这同时处理copybounds0与m_1。

因此maxlower+1≤minupper，I(F)必含两个consecutiveintegers，整个labelledinternalfiberconnected。

### 3.2 相邻quotientfibers必相交

将b singleton换写为其complement的OUTcut。所有涉及u的rows变成nestedchain

    {a} ⊂ {a,c} ⊂ V−{b}，

它们的cutout都为u加一个outsideconstant。任一outsidephysicalarc的singleflip，对这条chain各row的cutout变化全在{0,1}或全在{0,−1}，不能一行增加而另一行减少。

所以全部intervalendpoints同向移动0或1；0与m_1不变。新旧I均width≥1，故必共享integerweight。可先在当前fiberprepare同一internalassignment，再执行Q指定copyflip，再在新fiber继续。

逐步lift完整Q-word并在终点fiber对齐，即证Lemma3.1。没有假设quotientoutsideflip直接lift任意extension，也没有用signedµ继承。

## 4. Critical leaf主邻居归约

已有research_dominant_neighbor_contraction.md证明：若某vertexb degree d≥L、某邻居a有m_ab≥d−k，则fullfixed-outsidepairfiber为width d−2k≥1的interval，全部mixedcuts自动合法，且quotientflip可lift。

所以五顶点反例中任何criticalvertexdegree=L都不能incidentheavy pair：m≥k+1=L−k就可收缩到四顶点，立即connected。

这一步用一般dominant-neighbor定理，不能只由critical-criticalpaircutbound推到critical–noncriticaledges。

## 5. 最小五顶点反例必须有恰两个criticalvertices和heavy triangle

反设Theorem1.1，固定五顶点反例中physicaledgecount最小的G。

若λ≥L+1，既有2k+2定理已闭合。若有nontrivialL-mincut，smallfiber归约已闭合。因此λ=L且所有mincutshores是criticalsingleton或其complement。

若只有一个criticalvertexr，固定任意balancedrootstar。A=V−r的properresidualshores的µ≥2：它们与A内complement都不是r或V−r这两个mincutshores。已证明µ2fiberconnected；B+让相邻balancedrootstars有commoncompletion，根星的weight-k/k+1 cubeconnected，因此整个Ωconnected。故不能恰一个criticalvertex。

若至少三个criticalvertices，§4排除incident它们的heavy pairs；heavy pairs只能在至多两个noncriticalvertices之间，故至多一个，Lemma3.1闭合。

于是恰两个criticalverticesr,s；其它a,b,c noncritical。Heavy pairs只可能在abc内。若至多两条，仍Lemma3.1闭合。所以必须

    m_ab,m_ac,m_bc≥k+1。

这是仅剩的heavy triangle，不由finitegraphsearch选出。

## 6. Heavy triangle给删除锚，并迫使全部membershipatoms为singleton

所有mincutshores仅r、s单tons及complements。所以E°精确为abc内部的全部copies，非空。由edgecountminimality，每个G−f（f∈E°）仍λ≥L且Ωconnected，删除分量锚C°存在。

如果Ω(G)不连通，选D在C°以外。所有E°copies在D都不可合法flip，所以全部legalcopiesincidentr或s。

取D中r的actualOUTtightshore：rout=k时为{r}，rout=k+1时为V−{r}；s同理。这两rows互compatible，并与任何properrow都cross-free。扩成maximalcross-freeactualtightfamilyT；compatibleguardextension使T覆盖全部illegalcopies。

每条abc-edge都illegal，故有T-negative rowseparates它的endpoints；triangle三个pairs均有copy，所以a、b、c处于三个distinctmembershipatoms。Retainedcriticalrows又将r、s各自与其余vertices区分开。

因此T恰有n=5个非空atoms，全部singleton。这里是正式证明n=5，不能直接把graphvertexcount代入CFST。

## 7. 最后一个budget contradiction

所有physicalcopies都跨T-atoms，故globalatomtreebudget的M=|E(G)|。相对strictsources全部globallylegal，数Z满足

    |E(G)|≤4k+Z。

另一方面criticalr,s每个仅有k+1条majority-directioncopies可能合法flip，故D的globallegalcopies总数≤2(k+1)，于是Z≤2k+2。

记p=m_rs。由r,s degree=L及λ≥L，p≤k。令m_H=m_ab+m_ac+m_bc≥3(k+1)。Rootincidentcopies计数给

    |E(G)|=m_H+2L−p
          ≥3(k+1)+4k+2−k=6k+5。

合并预算则

    6k+5≤|E(G)|≤4k+Z≤6k+2，

矛盾。故不存在五顶点反例，Theorem1.1成立。∎

## 8. 当前主目标状态与下一范围

原始MAIN现已闭合全部|V|≤5，任意k≥2、全部multiplicities。此前“k2五顶点第一未闭合层14/15edges”的frontier已被本定理完全supersede。

一般最小反例若存在，至少六顶点，并且满足dominant-neighbor multiplicity约束。RSM仍为一般充分且必要主接口，没有因五顶点闭合而自动解决六顶点及以上。

本proof的关键新桥是actualconnectedintervalfibers及neighborintersection；最后才使用删除锚与静态数量矛盾。没有把一般source数本身当动态terminationmeasure，也没有冒称所有mincutshores的内纤维都connected。

指定smallarithmetic与witness核验继承five_vertex_next_layer证书；generalheavy-star的额外交叉gap、nestedchain及heavytrianglebudget核验见scripts/verify_five_vertex_star_algebra.py与data/five_vertex_star_algebra_*。理论证明不依赖有限参数外推。
