# 五顶点最小边数层：全 k 理论排除

2026-10-03。新结论：对任意 k≥1，λ(G)≥2k+1、|V|=5 且 |E|=5k+3 时，Ω_k(G) 连通。允许任意 labelled parallel multiplicities；这里不是图 census。

> 后续更新：k≥2的全部五顶点实例现已由research_five_vertex_full_theorem.md闭合。本文件的最小边数层proof保留；下面14-edge OPEN是历史frontier，已superseded。

## 1. 一个可复用的 degree-only serialization lemma

设 G 满足 λ≥2k+1，并且其 k-strong orientations 恰是全部满足

    k≤out_D(v)≤deg_G(v)−k，∀v

的 orientations。则 Ω_k(G) 连通。

Proof：global path/circuit macro connectivity 给任意两个合法端点间的合法终态宏链。每个 vertex 的 degree interval 宽度 deg−2k≥1。

一条合法终态 directed simple path 的内部顶点只有一次 +1、一次 −1：atlower 时 incoming copy 先翻，atupper 时 outgoing copy 先翻，strictlyinterior 时不加 precedence。相邻 path copies 的 precedence 形成无向 chain，无有向 cycle，所以 topologicalorder 逐边执行，所有 degreebounds 始终合法。两个 pathendpoints 的一次 degreechange 已由宏终态保护。

Directed circuit 同样处理，唯一 precedence cycle 是全圈顶点都 atlower，或都 atupper。处理全lower：令 B 为能沿 atlower vertices 到达该圈的所有 atlower vertices。若有 current arc outsideB→B，其 tail 必 sparelower，接 B 内首次到圈的路径给 stem，stem 内部避开圈。若没有 incomingB，则

    out_D(B)−in_D(B)=Σ_{v∈B}(2k−deg(v))≤−|B|<0，

但 in_D(B)=0 使左侧≥0，矛盾。故 stem 必存在。沿 forward order 开 stem，把圈上接点的 degree 提高1；圈不再 monochromatic，可按 precedence 翻完；reverseorder 关 stem。每一步保持 degreebounds。

全upper 完全对偶：对 forward-reachable upper B，每个 vertex 的 out−in=deg−2k≥1；若没有 outgoingB，求和却≤0，矛盾。得到从圈到 spareupper 的出口 stem，从 target 端逆序打开，翻圈，再正序恢复 stem。

全部词使用 original physical copies，stem 最终恢复。由 degree-only 等价，所有中间 degree-feasible states 都 globally k-strong。沿宏链拼接完成证明。∎

这个 lemma 不声称一般 degreebounds 足够保护全局 cuts；等价性是明确前提，下面只在五顶点最小边数层证明它。

## 2. 五顶点存在 nontrivial mincut 时已经闭合

若λ(G)≥2k+2，已由Ito基线完成。以下取λ(G)=L。若五顶点 G 有 global L-mincut 的 nontrivial shore，取大小 2 或 3 的一侧 A。research_small_fiber_theorem.md 已证明完整 true-critical fiber 在 |A|≤3 时连通；quotient G/A 至多4个 vertices，其 MAIN 已证明。由已审计 B+ / nonboundary lift，把 quotientword lift 后作最终内部 repair，得到 Ω_k(G) 连通。

所以五顶点真正未解决的图只可能所有 global mincuts 都是 singleton/co-singleton。

## 3. 最小边数层的 degree pattern

令 L=2k+1。五顶点 λ≥L 给每个 degree≥L，因此

    |E|≥ceil(5L/2)=5k+3。

若恰等号，总 degree=10k+6=5L+1。故恰一个 vertex c 的 degree=L+1=2k+2，其余四个的 degree 全是 L。

若有 nontrivial mincut，由§2完成。以下假定全局 mincuts 只有 singleton/co-singleton。两顶点 cut 因而严格大于 L。

写 m_uv 为两顶点之间的 physical copies 数。

- u,v 都不同于 c 时，δ({u,v})=2L−2m_uv 是 even 且大于 L，故至少 L+1=2k+2，给 m_uv≤k。
- u=c、v≠c 时，δ({c,v})=2L+1−2m_cv 是 odd 且大于 L，故至少 L+2=2k+3，同样给 m_cv≤k。

所以所有 vertexpairs 都有 m_uv≤k。

## 4. 逐割证明 degree-only 等价

给任意 orientation 满足所有 singleton out/in≥k。对任意 vertexpair {u,v}，exact identity 为

    out_D({u,v})=out_D(u)+out_D(v)−m_uv≥2k−k=k；
    in_D({u,v})=in_D(u)+in_D(v)−m_uv≥k。

五顶点的每个 proper cut 都是 singleton、pair，或其 complement。因此全部 global cuts 两向≥k，定向 globally合法。

反向 singletonbounds 是 k-strength 的直接必要条件。故本层确实满足§1的 degree-only 等价，Ω_k(G) 连通。∎

## 5. 更新真正最小未闭合模型

既有 |V|≤4 的全 multiplicity 定理，加上本文件，给：

    原始最小反例若 |V|=5，则 |E|≥5k+4。

尤其 k=2 的五顶点13边层全部由理论排除，而非仅那两个已 BFS 的正控制。最小尚未统一分类的五顶点层是14条 labelled edges。

14边、k=2 的总degree=28；在 degree≥5 下，可能 degree multisets 恰为

    (8,5,5,5,5)，(7,6,5,5,5)，(6,6,6,5,5)。

若有 nontrivial5-cut，§2同样排除；剩余只含 singleton5-cuts。上面的 m_uv≤k 证明不再成立，例如 higher-degree pair 允许3条 parallel copies而其cut仍大于5，因此 pairconstraints可能真实强于 degreebounds。

示例 family member：K₅ 上再加 ab 两条、cd 一条、cr 一条，degree(a,b,c,d,r)=(6,6,6,5,5)，14copies，只有 d/r singleton cuts为5，ab有3copies，其paircut为6。这里若 out(a)=out(b)=2，pairout=1；这说明不能省略 pairconstraints。本文不把这个具体图宣称为 disconnected counterexample；其整体连通性需要逐边证明或单独证书。

Degree-onlyshortcut的实际定向已构造并逐30cuts验证：a→b1、b→a2、a→c1、d→a1、r→a1、c→b1、d→b1、r→b1、c↔d各1、c→r2、r→d1。Outdegrees=(2,2,4,3,3)，所有singletonout/in≥2，却out(ab)=1；λ5、mincutshores只有d/r及补集，E°有5copies。核验文件data/synthesis_controls_certificate.json，脚本scripts/verify_synthesis_controls.py。没有环境分量结论。

## 6. 与 MAIN 的关系和下一步

这是进一步排除一个最小反例层，不是 MAIN 完成。剩余 root-star mixing lemma 仍须覆盖任意规模、任意 multiplicities。

该14边示例的 E° 包含 ab、ac、bc 的 copies，适合 testing research_deletion_component_anchor.md 中 C° 锚定的路径分支；另一部分所有copies属于mincut的模型仍须保留，不能把 E° 非空当作一般事实。
