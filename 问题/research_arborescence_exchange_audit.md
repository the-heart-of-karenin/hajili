# Arborescence exchange路线审计：可借用的动态模式与physical兼容义务

2026-10-03。目标仍为原始MAIN；本文不将另一种reconfiguration定理直接代入。

## 1. 精确外部输入

Kobayashi–Mahara–Schwarcz，*Reconfiguration of the Union of Arborescences*，[原始论文 arXiv:2304.13217](https://arxiv.org/pdf/2304.13217)，Theorem1.1给固定root、k个arc-disjoint outarborescences之union在单arc exchange下连通。其Lemma3.13通过一次实际可行exchange缩短动态auxiliarydigraph的最短directedcycle；该值随当前state重新定义。

这里只引用这个定理与动态shortest-cycle机制。论文的arc exchange不是用户要求的physicaledge反转，不能将结论直接叫MAIN。

## 2. 一个original orientation的两份证书

固定rootr。D k-strong等价于存在k个arc-disjoint rootedOUTarborescences，以及另有k个arc-disjoint rootedINarborescences。两套packing分别存在，允许相互重叠。

Physicalarc e在D可单翻等价于D−e k-strong，因而等价于两套packing都可重新选为避开e。这里的避开是同时满足两个存在性条件，不能只调整OUT证书。

不能要求两套packing之间也arc-disjoint。例如k=2，四顶点五正则无向多重图只有10copies，而两套各含2个spanningarborescences共需12copies；λ=5仍可能。因此joint-disjoint强化会排除合法原问题。

## 3. 三道不能省略的lift问题

1. 在固定D中重选arborescence certificate不改变orientation；不能把证书exchange次数记成physicalprogress。
2. 放到G的bidirectedexpansion后，一套可行packing可能同时用某个physicalcopy的两个方向；OUT/IN的独立exchange也可能要求相反physicaldirections。必须保持每条copy仅一个实际方向。
3. 将一个certificateexchange实现成physicalflip时，还要保留另一套packing，并核验所有mixed/root-containing cuts；rootreturn更要求最终恢复labelledstar。

以上是定义层的实质差异，不是复杂度或常数问题。只证明某个completiondifference DAG也不能代替actualhistory。

## 4. 为什么动态shortest cycle仍值得尝试

现有guard路线的失败主要在静态closure不提供finitehistory。文献机制说明一条不同的证明形态：保持目标差异规模，允许暂时换掉commoncertificatearc，同时让当前辅助图的最短cycle缩短；到self-loop后再减少目标差异。

要在原问题中使用它，必须先给可由当前actual-tight rows定义、经过每次physicalmove可重新计算的dependencygraph，并证明实际可执行的shortening。暂时增加Debt或endpointdistance可以允许，不能把它们每步单调当作前提。

本次first-asynchrony theorem已把最小环境分离对的one-sidedlaunch限制到路径端点；配对signature theorem又给smoothstates统一certificate与虚拟head→tail路径。这些是候选建图素材，尚未得到物理shortening lemma。

## 5. 根排除条件必须保持

定向tightcontainer的intersection/union closure需要共同rootexcluded，使union仍proper。原globalOUTtightrows可以co-coverV，此时out(V)=0，不能套同一个最小container证明。

所以建图若混合OUT/IN与root-containing rows，必须使用补岸的符号并检查corner；“每条边任选一个minimalblocker”本身不足以保证文献中的uniquecontainer与更新性质。当前没有忽略这一差异的完整移植。
