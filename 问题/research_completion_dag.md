# Optimal deletion-completion difference 的无环性

2026-10-02。**PROVED necessary structure**。仅假设该completion问题有可行integerorientation；不把无环性当singleflipserialization。

## 1. Setup

固定referenceR、designateddeletedphysicalcopye。允许若干剩余copies反向，其中J每条cost1、K−e可cost0。对candidatecompletionC，changedcopy集合Z按R当前方向组成directedgraph。Completion要满足完整residual/globalcuts，fixedoutsidecopies不在Z。

ChooseC先minimumcost，再在minimumcost者中minimum|Z|。Primalcut-orientationbox integral已由`research_global_scope.md`证明；但本文也可直接在有限integercompletions中选这个lexminimum，不另假设dualTDI。

## 2. DAG lemma

**Lemma.** 这个Z没有directedphysicalcircuit。

若存在R-directedcircuitB⊆Z，则在C中它的copies全部反向，仍是一条opposite-directedcircuit。把B全部restore到R方向，保持C的每vertexoutdegree；每个cutoutvalue因此不变。Physicaldeletededgee不在Z、也不在B；outside/fixedcopies不变，所以restore后的completion仍legal。

若B含J-copy，cost严格减少，矛盾。否则全部B的cost0，cost不变但|Z|减少，违反secondaryminimum。∎

更弱但适用于任意costminimumC的结论：Z中任何directedcircuit都只能由cost0copies组成。特别地，当freeK−e本身是一个directedpath的子图时，任何minimumcostcompletion的全部Z自动DAG，无需secondaryselection。

## 3. Tight blocker的selected gain-chain

若selectedg∈Z从reference-tightshoreU leaves，则δ_g(U)=−1。Completionfeasibility要求

    Σ_{h∈Z}δ_h(U)≥1[e leaves U]。

因此至少另一selectedcopyh进入U，其δ_h(U)=+1。可以从每条illegalselectedg的blocker追到selectedgaincopy；若所有selectedcopies都illegal，这产生finite edge/rowdependencycycle。

**这个dependencycycle不是physicaldirectedcycle。** 不同依赖transition只要求两条edges对同一shore符号相反，未必共享physicalvertex；也可能在membershipatom内从不同vertex进出。DAG lemma不会自动排除它。

## 4. Genuinepathcontrol说明scope不能扩大

`research_terminal_debt.md` §8的split-tipconstruction中，K是currentdirectedpath `u→w→v`，两端orientation合法、每条K copy初始均illegal。在仅允许K的restriction里，支撑DAG也不能启动任何singleflip；允许J history才可连接。这不是optimaldeletion-completion反例，只是“DAG⇒可直接serialize”的真实反例control。

因此当前仍需证明的精确primalextraction目标是：在minimumcomponentreference的一个lexoptimalcompletionDAG里，selected blocker/gain dependency能通过ancestor/history合法地解开，或至少存在一条legal selected ancestralcopy。本文没有关闭这条全量词。

## 5. 与weightedguardclosure结合的新可检查接口

`research_dual_guard_gap.md` §5给positiveoptimalguard iff universallytight on optimalcompletionface。若一个reference-tightblockerU不能被赋positiveoptimalweight，就存在optimalcompletion使U有positive surplus；这个surplus必须由selectedDAG的enteringcopies支付。

于是有两种可分开研究的objects：universallytightguard可进入optimaldualsupport（仍需cross-free选择）；non-universallytightguard具有primalselectedgainwitness。两者的交替closure比“所有guard随便加ε”精确，但finiteprogress尚未证明。无界terminalwidth要求该closure允许任意长有限history。
