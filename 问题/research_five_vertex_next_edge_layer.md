# 五顶点下一边数层：|E|=5k+4 的完整收缩与区间lift

2026-10-03。继续原始MAIN的理论研究；本文件关闭一个新的全参数边数层，不将它替代全局目标。

> 同次研究的进一步结果：research_five_vertex_full_theorem.md将本文件interval论证推广，闭合全部五顶点、任意edgecount；下面5k+5/15-edge frontier是中间阶段，现已superseded。原始一般MAIN仍OPEN。

## 1. 主结论

**Theorem 1.1.** 对任意k≥2、任意五顶点loopless labelledmultigraphG，若λ(G)≥L=2k+1且|E(G)|=5k+4，则Ω_k(G) connected。

结合research_five_vertex_minimum_edges.md已闭合的5k+3层，五顶点反例如果存在，至少有5k+5条physicalcopies。k=2时第一尚未统一闭合层从14条提高到15条。

既有输入仅为：全部四顶点MAIN、五顶点含nontrivialL-mincut时的small-fiber/contraction结果，以及degree-onlyserialization。本文新增结构与lift证明如下。

## 2. 剩余图与唯一可能的exceptional pairs

若G有nontrivialL-mincut，五顶点small-fiber归约已闭合。故只需处理全部L-mincutshores为singleton或其complement的情况。

写deg(v)=L+ε_v。Degree总量为10k+8，故Σ ε=3；所有ε≥0。只有三种patterns：

    (3,0,0,0,0)，(2,1,0,0,0)，(1,1,1,0,0)。

每pair{u,v}的cut严格大于L，所以δ≥L+1，并有

    m_uv≤k+floor((ε_u+ε_v)/2)≤k+1。

如果m_uv≤k，任意满足singletonout/in≥k的orientation自动满足该pair双向≥k，因为out({u,v})=b_u+b_v−m_uv≥2k−m_uv≥k。五顶点全部cuts都是singleton/pair或其complement。

称m_uv=k+1的pairs为exceptional。只有ε_u+ε_v≥2的pairs可能exceptional。

- Pattern(3,0,0,0,0)：全部exceptionalpairs共享ε=3的centera，至多2条；3(k+1)>2k+4=deg(a)。
- Pattern(2,1,0,0,0)：全部exceptionalpairs共享ε=2的centera，至多2条；3(k+1)>2k+3。
- Pattern(1,1,1,0,0)：exceptionalpairs只能在三个highvertices之间。三条全部exceptional会用尽它们全部degrees，与另外两vertex断开，故至多2条；两条必共享center。

所以全图合法性恰singletonbounds加至多两个共享center的pairconstraints。

## 3. 通用interval-fiber lift原则

收缩一个pair A={a,b}，删除它们之间的loops，记quotientQ=G/A。Physicalcopies保留identity；λ(Q)≥L，|V(Q)|=4，Ω_k(Q)已知connected。

固定Q的一个orientation F，相应冻结G的全部非abcopies。设u为a→b的internalcopies数，m=m_ab。若完整globallegality恰u属于一个integerinterval I(F)⊆[0,m]，且I(F)至少含两个consecutiveintegers，则这个fullfixed-outsidefiberconnected：内部physicaldirections是subsetweights落在I的cube，两个邻接weightlayers可交替add/delete实现identity交换，整个interval按层连接。

若对每条legalquotientsingleflip F↔F′都有I(F)∩I(F′)≠∅，可在当前fiber先走到某个共同weight的同一physicalassignment，翻那条outsidecopy，再继续。连接任意quotientword并在终点fiber对齐，即得整个G connected。

本节要求的是实际globalcuts的精确fiber，不使用signedprojection的虚构µ继承；下面逐案验证I及交集。

## 4. 恰一个exceptional pair

取m_ab=k+1，deg(a)=L+ε_a、deg(b)=L+ε_b。令R_a、R_b为fixedoutside中a、b的outgoingcopies数，T=R_a+R_b为F的contractedrootout。

Externaldegrees为k+ε_a、k+ε_b。Quotientlegal给

    0≤R_a≤k+ε_a，0≤R_b≤k+ε_b，
    k≤T≤k+ε_a+ε_b。

完整Gsingletonbounds等价于

    I(F)=[max(0,k−R_a,R_b−ε_b),
          min(k+1,k+1+ε_a−R_a,R_b+1)]∩Z。

其余pairs非exceptional自动合法，abpaircut就是Q-rootcut，因此这确实是fullglobalfiber。

每个uppercandidate减每个lowercandidate至少1：两原vertexbounds各自width1+ε；两个交叉差分别为T−k+1、k+1+ε_a+ε_b−T，均≥1；lower≤k、upper≥1还处理0与k+1。故I width至少1，非空且connected。

一次quotientflip至多改变R_a或R_b一个unit，或两者不变；所有intervalendpoints同向变动0或1。新旧interval都width≥1，故交集非空。§3完成lift。

若没有exceptionalpair，则既有degree-onlyserialization直接闭合。

## 5. 两个exceptional pairs且有critical邻居

取exceptionalpairsab、ac，且deg(b)=L。Pattern(3,0,0,0,0)必属此案；Pattern(2,1,0,0,0)若有两exceptionalpairs，其中必有critical邻居，可选它作b。

收缩ab，m_ab=k+1。Fixedoutside记R_b≤k，T为Q-rootout；令ε_a=deg(a)−L。

任意u∈{R_b,R_b+1}都使

    b_b=k+1−u+R_b∈{k,k+1}，
    b_a=T+(u−R_b)∈{T,T+1}⊆[k,k+1+ε_a]。

abcut由Q-rootcut保证。对另一个exceptionalpairac，注意Q的root+c对应G的{a,b,c}，有exactidentity

    out_G({a,c})=out_Q({root,c})+m_ab+m_bc−out_G(b)，
    in_G({a,c})=in_Q({root,c})+m_ab+m_bc−in_G(b)。

因为b的out/in均≤k+1=m_ab，两个附加项非负；Qlegal就保证ac双向≥k。其它pairs自动合法。所以fullfiber精确为

    I(F)={R_b,R_b+1}。

非boundaryquotientflip或incidenta的boundaryflip不改变I；incidentb的flip把R_b改变±1，新旧两层区间总在一个weight相交。§3完成lift。

此证明没有要求outsideinternalflip直接lift当前每个extension；允许在fiber内先prepare共同assignment，所以也覆盖全部quotientedges。

## 6. 两个exceptional pairs且三个highvertices均excess1

剩余pattern是deg(a)=deg(b)=deg(c)=L+1=2k+2，deg(d)=deg(e)=L，exceptionalab、ac各k+1copies。

a的全部edges已被ab、ac用尽。b、c的externaldegrees各k+1−m_bc。于是

    δ_G({a,b,c})=2k+2−2m_bc。

该nontrivialcut严格大于L，故m_bc=0；并由同一cut的complement{d,e}得m_de=k。

收缩ab。记

    R_a=#a→c，R_b=#b→{d,e}，R_c=#c→{d,e}，

均在[0,k+1]。Q-rootout为R_a+R_b，c-out为k+1−R_a+R_c，Q的root+c-cutout为R_b+R_c。三者各自boundarydegree2k+2，所以Qlegal蕴含

    k≤R_a+R_b≤k+2，
    |R_a−R_c|≤1，
    k≤R_b+R_c≤k+2。

FullGlegality对internalu恰三个intervals及copybounds：

    I(F)=[0,k+1] ∩ [k−R_a,k+2−R_a]
                  ∩ [R_b−1,R_b+1]
                  ∩ [k−R_c,k+2−R_c] ∩Z。

前两个vertexintervals保证a/bsingleton；第三R_c interval等价于acpairbound，因为out_G(ac)=u+R_c且δ_G(ac)=2k+2；abpair与outsidevertices由Q保证；其它pairs非exceptional自动满足。

令r=min(R_a,R_c)、s=max(R_a,R_c)。合并a/ac的interval为[k−r,k+2−s]，width2−(s−r)≥1。与b interval的两个交叉gap为

    (R_b+1)−(k−r)=R_b+r−k+1≥1，
    (k+2−s)−(R_b−1)=k+3−R_b−s≥1。

因为R_b+R_a、R_b+R_c都在[k,k+2]。再用r,s,R_b∈[0,k+1]知所有lowers≤k、所有uppers≥1，copybounds不将width降至0。故I width至少1。

任一quotientsingleflip至多改变R_a、R_b、R_c之一±1，或三者不变（d–e copy）。所有lower/upperendpoints同向变动0/1，新旧I都width≥1，所以必有共同integerweight。§3给完整physicalwordlift。

## 7. Scope与研究前沿

三种degreepatterns及所有exceptionalpairs数量已穷尽；非trivialmincut案在既有smallfiber定理范围。Theorem1.1成立于任意k≥2及全部labelledmultiplicities，没有用finitegraphcensus推断。

当前MAIN仍OPEN；RSM未关闭。新结果将五顶点第一未闭合边数层提高到5k+5（k2为15），并给一般route一个可执行模型：connectedintervalfibers加相邻区间intersection，而非单态gradient或signedµ继承。

指定算术与一个14-edgewitness的核验存scripts/verify_five_vertex_next_layer.py及data/five_vertex_next_layer_*。程序核验proof使用的profileinequalities和两个指定quotientstates，不枚举五顶点graphs或其fullorientationgraphs。
