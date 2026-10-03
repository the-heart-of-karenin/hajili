# 小型完整临界纤维：|A|≤3 的全 k 连通性

2026-10-03。状态：完整理论证明，任意 k≥1、任意 labelled multiplicities。不是有限 census。主问题的推进是：结合已闭合 boundary lift，任何原始反例至少有5个global vertices，剩余rootfiber至少4个internal vertices。

## 1. 定理与准确范围

在initial true-critical fixedoutsidefiber中，λ(G)≥2k+1、δ(A)=2k+1、fiber非空。若 |A|≤3，则完整内部physicalflipgraph connected。允许 μ=1。

|A|=1 空约束、空内部orientation。|A|=2 为parallelcopies的合法weightslab，两个degreebounds间宽度μ≥1，逐加减copy及借相邻weightlayer交换labels使其connected。

以下证明 |A|=3。它还证明一个可复用的degree-only serialization机制。

## 2. 全部 cuts 精确变成 degree intervals

令 b_v=d⁺_{D[H]}(v)、d_H(v)为内部undirecteddegree。三个vertices的每条propercut是singleton或cosingleton。因此全部residualconstraints恰为

    L_v=p({v})≤b_v≤U_v=d_H(v)−p(A−{v})。

width为

    U_v−L_v=μ({v})≥1。

本证明中任何prefix只要保持这三个intervals，就已经保护全部mixed/globalcuts；不遗漏更大cut，因为没有其它proper内部cuts。

初始p≥0、integer crossing-supermodular，已证明的macroconnectivity给任意两feasibleorientations间的合法终态single directed path/circuit macro序列。只需逐个把macro serialize。

## 3. 合法终态 path 可按 localprecedence serialize

取当前directed simple path，从s到t，整体reversal终态feasible。每个intermediatevertex的degree净变化0；source减1、target加1已由终态feasibility保护。

对一个intermediate v，有incoming pathcopy a、outgoing pathcopy b。翻a使b_v增1，翻b使b_v减1。

- 若b_v=L_v，要求a先于b；
- 若b_v=U_v，要求b先于a；
- 若严格介于bounds之间，无须precedence。

因为width≥1，lower/upper两要求不会同时发生。Edges形成一条chain，任意方向的相邻precedences均无有向cycle。按topologicalorder翻所有physicalcopies，任何vertex的部分degree变化均在interval内，所以每步全局合法。

## 4. Mixed circuit 同样可 serialize

对directed physicalcircuit使用同样localprecedences。只有两种方式会形成整圈precedencecycle：所有circuitvertices均atlower，或均atupper。

若lower/upper混合，或者至少一个vertex strictlyinterior，precedencegraph为DAG，直接topologicalserialize。Physicaltwo-cycle的parallelcopies各有独立身份，同样适用。

剩下两个monochromaticcases需要一个finite stem，而非在整圈上不合法地强行启动。

## 5. 全 lower circuit 的入口 stem 一定存在

令C全部vertices atlower。考虑仅沿atlowervertices组成的current directedgraph，令B为能到达C的所有atlowervertices（包含C）。

如果有currentarc从outsideB进入B，tail若atlower也能到达C，应已在B；因此tail必须有b_s>L_s。选这样的copy并接B内到C的directedpath，得到simple stem s→…→w，s sparelower，所有其余vertices atlower，内部vertices避开C。

若不存在这样的incomingarc，则F={ {v}:v∈B }是同一D的actual-tightproperrowfamily。任何F-positivephysicalcopy必从outsideB进入B，现已不存在；internalBcopy的positiveheadrow同时有negativetailrow。因此F source-free。

F非空且cross-free，CFST给relative source，矛盾。故上述stem必存在。这也排除B=A时整族singletons all-tight的情况；没有以总degree计数替代cut约束。

按forward order openstem：s减1合法，每个lowerintermediate先增1再减1，最后w增1。circuit于是mixed或有interiorvertex，按§4翻整圈；整圈不改变当前degrees。再reverseorder恢复制定stemcopies，全部intervals逐步合法。最终只reverseC。

## 6. 全 upper circuit 的出口 stem 一定存在

对偶地，令B为从C沿atuppervertices可到达的所有vertices。若有arc B→outsideB，head必有b_t<U_t，给stem w→…→t，除t外均upper。

若没有outgoingarc，F={A−{v}:v∈B}是actual-tightcosingletonfamily：b_v=U_v恰意味着out_H(A−{v})=p(A−{v})。F-positivecopy需tail在B、headoutsideB，已不存在；内部Bcopy另有negativeguard。因此source-free，仍被CFST排除。

openstem必须按**从t端逆序**执行：t可增1，upperintermediate先减1再增1，w最终减1。此时circuitmixed/interior，可serialize；再按originalstem的forwardindexorder恢复copies，deficit送回t，各degree均在bounds内。没有把forward与backwardopening混用。

## 7. 完成 fiber theorem 与全局 corollary

§3—§6把每个合法终态path/circuitmacro变成真正的singlephysicaledgeword，允许temporarystemcopies最终恢复。沿macrochain拼接即到任意target，证明 |A|≤3 的fiberconnected。∎

由 research_boundary_lift_audit.md 的contractioninduction，任意global |V(G)|≤4、λ≥2k+1的图，其Ω_k(G)connected：criticalshore选大侧，但始终|A|≤3；quotient更小，B+与nonboundarylift均已闭合。

因此固定的vertex-minimum原始反例必须有|V|≥5；选criticalroot r 后，真正不连通的initialfiber有|A|≥4。所有内部μ≥2的fibers已完成，所以剩余必须同时具有μ1shore和至少4个internalvertices。

## 8. Scope audit 与不能继续跳的箭头

本证明使用degree-only等价，明确依赖 |A|≤3。若|A|≥4，还有pair cuts等约束；localprecedence可能同时让一个largercut损失多于1。即便所有vertexdegrees合法，也不能假设同样stem/circuitword全局合法。

这一步不复活degree-only⇒globalcut-safe的错误推理。它给新的准确规模下界，尚不完成一般μ1的历史服务终止。
