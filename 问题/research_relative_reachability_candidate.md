# Relative augmentation 的分阶段历史标签证明候选

日期：2026-10-02。**历史 PROOF-CANDIDATE；现已被完整审计稿 SUPERSEDED。** 本文保留研究分支 outline 与 root 首轮推导。第二轮逐项核验、路径构造的简化、retained minimality 的反查，以及正式 theorem见 `research_relative_reachability_audit.md`。全部内部 µ≥2 的 single-flip augmentation / H1 已在该范围升级为 PROVED；一般 µ=1 主问题仍 OPEN。下文原有未闭合状态只作 provenance，不再是 current 状态。

本文与已证明的 existence / unique strict component不同；目标是从任意初始合法定向出发，确实产生一条内部单物理边 word。研究来源之一是 [Ito 等的原始论文 §4](https://arxiv.org/pdf/2110.11585) 的 safe-source / minimal-tight-set 方法；下面针对固定 root、odd boundary、禁翻 boundary新增例外处理和标签账本，并不直接引用其 global augmentation theorem。

## 1. Root-contracted 模型与候选结论

把 outside收缩成 r，内部顶点为 A，n=|A|。固定所有 r-incident labelled arcs，令

    R(A)=k，S(A)=k+1。

允许所有 H=G[A] 的 physical edges翻转。当前 contracted D globally k-arc-strong。额外假设

    |δ_G(X)|≥2k+2，∀∅≠X⊊A。                         (MARGIN)

这等价于 initial residual全部 proper µ≥2。交换方向时只是概念上反转整个模型，再翻同一批内部 copies；不实际改变固定 boundary。

候选 theorem：从任意 D有有限 legal internal word到达 D*，使每个 proper X⊊A的 global outcut与incut均至少 k+1，即所有 proper residual slacks至少1。结合 research_global_scope.md Theorem14即可得该 MARGIN子类的 H1。

## 2. Families与精确 cut identities

设 O={proper nonempty X⊊A:d_D^+(X)=k}，I={proper nonempty X⊊A:d_D^−(X)=k}。另将 A作为两族的人工 sentinel。M为O∪I∪{A}的 inclusion-minimal shores；若O=I=∅，M={A}。定义

    v(D)=Σ_{X∈M}(n−|X|)。

proper同一 polarity的两 tight shores相交时，其 intersection仍tight；proper union若不是A也tight。若union=A，intersection tight仍由 d±(A)≥k保证；actual polarity的A值为k+1时两tight shores不可能 co-cover A。

对于 X∈O、Y∈I，若 X−Y、Y−X均非空，mixed cut identity给 X−Y∈O、Y−X∈I。因此 M中的proper shores两两不交。MARGIN也保证一个proper shore不能同时在O和I。于是 v是非负整数，v=0 iff O=I=∅，并有 v≤n²。

记边界权重 w(X)=R(X)+S(X)。在当前约定 R(A)=k,S(A)=k+1 下，有

    d_D^−(A−X)=d_D^+(X)+(k+1)−w(X)。                 (B1)

因此 I=∅时，每个 X∈O都满足 w(X)≤k；反之，若w(X)=k+1且X∈O，则A−X∈I。

## 3. Proper safe endpoints 与内部路径

若 S是proper inclusion-minimal I shore，可选s∈S，使对任意proper X含s但不包含整个S：

    d_D^+(X)≥k+1；
    若等于k+1，X−s内包含某个O shore。               (SS)

proper minimal O shore T有对偶safe sink t：把out/in交换得到相同两条条件。该proper lemma在两种 boundary方向都成立。

### 3.1 Safe endpoint 的独立 budget证明

在proper S内取 inclusion-maximal O shores Y_i；它们不交，因为 union=S会与 out(S)≥k+2冲突，其他 overlapping union仍O并违背maximality。再在S−∪Y_i内取 maximal near-out shores Z_j（out=k+1）；它们也不交：若overlap，intersection没有O subset所以out≥k+1，cut identity迫使union near-out，与maximality冲突。

若Y_i、Z_j覆盖S，交叉边的out / in计数相等，扣除S外边得到

    Σout(Y_i)+Σout(Z_j)−out(S)
    =Σin(Y_i)+Σin(Z_j)−in(S)。

每个Y_i有in≥k+2，每个Z_j有in≥k+1，in(S)=k、out(S)≥k+2，右减左至少2·#Y_i+2，矛盾。选s在覆盖外。

若near-out X⊆S含s，X必与某Y_i相交，且X∪Y_i proper、不再tight，所以intersection tight并遗漏s。若X−S非空，mixed identity与S的minimality迫使X−S out-tight，亦遗漏s。这证明(SS)；第一条由tightX若含s则违反选点或mixed minimality得到。safe sink对偶证明相同。

### 3.2 Tight-containing vertex 的内部 route lemma

对某polarity的proper tight-containing shore C，取其中包含x的最小tight shore C_x。其 induced digraph可从x到达任意C_x顶点（out polarity），或任意顶点到达x（in polarity）。否则 reachable / backward-reachable proper subset具有full out / in至多k，因legality恰k，违背C_x最小。

沿一次这样的路径，在第一个遇到strictly smaller tight-containing shore处递归，得到从x到某minimal O shore任意顶点、且不 leaves任何O shore的路径；对I反向。这项递归局限于proper tight container时无需任何A强连通假设。若out(A)=k，out route lemma也允许container=A：reachable proper subset的fullout≤R(A)=k即给contradiction。

## 4. I非空阶段的 clean macro

选 inclusion-minimal mixed container C：它属于一族（含sentinelA），且包含另一族的proper shore。若C proper，必要时概念reverse orientation，使C∈I且含proper O shore。

可构造P=s→t⊂D[C]，s是minimal I shore S⊆C的safe source，t是minimal O shore T⊊C的safe sink。P分成Q1,Q2：Q1除最后一点外不触碰任何C内proper O shore；Q2不leaves任何O shore。用第3.2节的反向I route先到一个C内O shore，再在首次O触点改接正向O route即可。

### 4.1 Artificial C=A 两种情况单独核验

若O、I都proper非空、最小mixed container只能是A，保持当前 R(A)=k方向。从proper O目标t按“禁止enter所有proper I shores”的arcs反向搜索B：

- 若B触到proper I shore，proper-container route给minimal proper I source及到t的内部路径；
- 若B与全部proper I shores不交，所有A−B→B arcs均未被禁，故此类内部arc不存在。L=A−B非空proper，其fullout=R(L)≤k，legality使L∈O；L包含proper I shore，违背mixed container A最小。

所以可取proper S，而不是把in(A)=k+1当成k。后续Q1/Q2构造不变。

若只有I proper非空，概念reverse：此时in(A)=k、out(A)=k+1，proper I为空而proper O非空。D[A]强连通，否则backward-reachable proper B没有内部incoming，fullin(B)≤in(A)=k，于是出现proper I，矛盾。允许S=A，safe-source cover budget的严格差变成2·#Y_i+1；co-cover near-out union A的out=k+1也保证intersection tight。因此A是真实in-tight source sentinel，strong (SS)成立。

### 4.2 Serialization与frontier更新

从t端逆序翻P。每个prefix净outcut变化为 χ_t−χ_frontier，incoming为反号。只有旧tight shores可能失败。Q2的O-no-leaving、Q1的首次O触点、minimal mixed container和 mixed difference identity排除out失败；若旧I含t不含frontier，则它与T的nested/crossing关系给一个更小mixed container或T的proper O subset，矛盾。C=A时out失败已由Q1避开全部proper O排除；无需假装A in-tight。

整个P结束后，被服务的proper T退出两tight族；若S proper且本身minimal union shore，则S也退出。原因是out(T)或in(S)升到k+1，MARGIN使相反方向仍≥k+1。

每个新minimal shore必严格包含其中一个退出的old minimal shore：

- 原来已tight但非minimal者，若现在变minimal，必含一个退出的old minimal shore；
- 新incoming-tight含t不含s，safe sink条件使其包含T，或含一个不变的old incoming-tight子集而不能minimal；
- 新outgoing-tight含s不含t，safe source条件使其包含S，或含一个不变的old outgoing-tight子集而不能minimal；S=C时包含S又必含t，这种新minimal outshore根本不能发生。

其余old minimal shores保持。因此v严格下降，且新minimal frontier只 enlarge / merge / drop被服务的old frontier。没有spawn全新无祖先shore。

重复clean宏直到I为空或O=I=∅；因v每次降至少1，该段有限。若概念反向运行，返回原方向检查I是否为空；每次clean仍同一个v严格下降。

## 5. No-I阶段的weak source与重边界例外

现在I=∅、O≠∅，恢复约定R(A)=k,S(A)=k+1。O的inclusion-maximal proper shoresY_i不交。若两者co-coverA，out identity给两个petals之间无内部edge。由(B1)，两个非空petals P=A−Y_2、Q=A−Y_1分别有fullin=w(P)、w(Q)；I为空使两者w≥k+1，而boundary total仅2k+1，矛盾。其他overlap则proper union O违背maximality。

在A−∪Y_i内取maximal near-out Z_j，out=k+1；同一cut identity使Z_j不交。若这些blocks覆盖A，扣boundary的in/out账本之差至少

    2·#Y_i−1>0，

因为O≠∅。故可取s遗漏全部Y_i,Z_j。它遗漏所有O shores；所有含s的proper cuts out≥k+1。

### 5.1 唯一类型的weak safety exception

若near-out X含s，必与某Y_i相交。若X∪Y_i proper，其intersection是out-tight且遗漏s。若union=A，则

    out(X∩Y_i)+m_H(X−Y_i,Y_i−X)=k+1。

如果intersection tight，仍有同样证书。唯一剩余是intersection near-out且petal multiplicity为0。

写I0=X∩Y_i、P=Y_i−X、Q=X−Y_i。三者partitionA且P,Q非空，P↔Q没有内部edge。记I0→P数为b，I0→Q数为d。三个out等式给

    b=R(P)+1，d=R(Q)。

于是fullin(P)=w(P)+1、fullin(Q)=w(Q)。I为空⇒w(P)≥k、w(Q)≥k+1。与total2k+1合成

    w(P)=k，w(Q)=k+1，w(I0)=0，w(X)=k+1。          (HEAVY)

所以weak source只允许一种失败：near-out X的boundary weight恰k+1。

## 6. Weak macro 的frontier变化

由out(A)=k的内部route lemma，从s可到minimal O shore T的safe sink t，取P且不leaves任何O shore。从t端逆序翻P，每prefix的旧O不损；没有proper I可损；非tight cuts最多损1。因此word合法。

P结束后T退出两tight族。其他old minimal O shores不含s,t，保持tight。新minimal incoming shore必严格包含T（safe sink，且原I为空）；新minimal outgoing shore若不包含old不变tight subset，则只能是第5.1节的HEAVY exception。原来tight而非minimal的新frontier也必严格包含T。

所以新minimal shores只可能：

    原来的未服务T_i；
    至多一个strict superset of T；
    至多一个HEAVY shore X。

最后一项的“至多一个”来自新M rows互不交，而两块w≥k+1超过total boundary。HEAVY若出现，out_new(X)=k、w(X)=k+1，(B1)使A−X∈I，从而强制进入clean阶段。即使A−X不是minimal，proper I family仍已非空。

## 7. 标签宏循环与候选严格下降

在一次No-I起点D0，给全部minimal O shores T_1,…,T_a各一个label，label目前的container就是该shore。

弱宏后，label若其oldshore被某新minimal row整个包含，则转入那个row；否则drop。其container只严格enlarge或不变。给HEAVY新row（若存在）另一个fresh heavy label。

随后执行第4节clean宏，直到I再次为空或strict。每个被服务oldminimal row的labels只转入whole-shore-containing newminimal row；merge时携带所有labels。newminimal rows两两不交，所以一个label不会fork。第4.2节保证每个newrow都有旧祖先，因此所有frontier rows始终有至少一个label。

回到No-I时，每个minimal row属于O且w≤k。fresh heavy label的所有后继container都包含原HEAVY shore，boundary weight≥k+1；因此它不可能存活到这个No-I endpoint。每个remaining frontier row于是都有至少一个原始label。

按每个原始label计量

    Ψ=Σ_alive original labels (n−|current container|)，

drop后贡献0。所有container只grow或drop，Ψ不增；被弱宏服务的T label在第一步就grow或drop，所以Ψ严格下降。初始Ψ=v(D0)。endpoint一个row可能有多个labels，但每row至少一个，故

    v(Dend)≤Ψ_end<Ψ_start=v(D0)。                    (DESCENT)

因此，No-I→weak macro→有限clean phase→No-I / strict的完整阶段严格降低v。最初有I时先运行clean phase；之后反复这些No-I循环，最终达到strict。

本节的风险点不是简单“某个label总增长”：必须同时保留每个frontier row至少一个祖先label、fresh heavy label在回到No-I前必灭、label不fork，以及服务T的strict增长。以上分别依赖第4.2、6、B1及minimal rows不交。缺任一项，DESCENT都不能引用。

## 8. 尚需独立逐行核验的事项

1. 第4.2节clean宏的所有新minimal-row分类，特别是old minimal row还tight但可能因新小row而失去minimal的反向影响；必须用新row包含已服务oldrow、oldminimal两两不交排除此情形，不能只说“slack不变所以minimal不变”。
2. 第4.1节proper / artificial mixed container的route选点，确保两种 conceptual reversal后仍只翻internal labelled copies，且不对root cut加需求。
3. 第7节label可merge但不能fork的形式化映射，及HEAVY complement入紧割非minimal时clean程序仍可启动。

root目前逐条得到上述接口，没有做重型枚举；三顶点weak-source control以及本轮既有小证书只作sanity checks，不代替该一般proof。若独立复核通过，可将MARGIN子类H1升级；在此之前保持PROOF-CANDIDATE，主2k+1一般问题仍OPEN。
