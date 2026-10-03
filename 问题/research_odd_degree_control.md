# All-odd balanced-degree orientations：可证明的连通 control

2026-10-02。**PROVED，degree-only scope**。本文不声称这些orientations全都k-arc-strong；用来把一般µ1难点与单纯odd vertex degree约束分开。

## 1. Degree-only theorem

设H loopless finite multigraph，每个vertex的undirected degree为odd。要求orientation满足

    (deg(v)−1)/2≤b_D(v)=outdeg_D(v)≤(deg(v)+1)/2。

称vertex处于U状态若outdegree为upper、L状态若为lower。则 `outdeg−indeg=+1` at U、`−1` at L。Legal degree-only physical flip恰是当前arc从U指向L。

**Theorem.** 所有balanced-degree orientations在这些single-physical-edge flips下连通。

Proof分为degree-vector unit routing与same-degree circuits，并为每种macro给degree-only合法serialization。全部physical copies保留身份。

## 2. Feasible degree vectors与unit transfers

Orientation degree zonotope的integer points由

    b(V)=m，b(X)≥i_H(X) ∀proper X

刻画，Hakimi edge-to-tail matching给exact realization。再加singletonbounds `l_v≤b_v≤u_v`。

把这些nodebounds写为singleton lower / co-singleton lower rows，在所有shores上定义g为对应已增强RHS（其余g=i_H）；同一row若有多条约束取max。任何crossing pair都不可能是singleton或co-singleton，因此其两个left-side g值仍为i_H；intersection/union的g值只可能增大。故g是integer crossing-supermodular。

`research_global_scope.md` §14.1的degree-polytope proof因此适用：integer degree vectors在feasibleunittransfers下connected。一次transfer `b'=b−χ_s+χ_t` 必有s处U、t处L。当前realizerD与任意targetrealizerE的difference support按D方向含一条simple s→t path，其完整reversal实现该transfer。

## 3. 任意degree-feasible path macro可serialize

写当前directed path `v0=s→v1→⋯→vm=t`，edges为e1,…,em。Endpoint s是U、t是L。

对于internalvertexvi：

- 若vi起初U，必须先翻其outgoingedge e(i+1)，再翻incomingedge ei；
- 若vi起初L，必须先翻incomingedge ei，再翻outgoingedge e(i+1)。

这些constraints只位于一条line的adjacentedgepairs上，无directedcycle。按任意topologicalorder翻每条copy一次。At每个internalvertex，先做的是允许±1变化，第二次restore；endpoints也按允许方向变化。故所有flipsdegree-only合法，完整后degreevector是b′。

**不能扩大scope。** 被翻edge集合未必始终是单一pathinterval；多个packets可以同时打开。一般k-strong cut在这种partialword中可能损2或更多，此节不提供全局cut-safe serialization。

## 4. Mixed circuit直接serialize

对一条directedphysicalcircuit，建立相同localprecedence：U要求outgoing先incoming，L要求incoming先outgoing。若circuit同时含U与L，precedenceorientation在其edge-cycle上不是一整个directedcycle，因而acyclic；two-parallel-copy2circuit也一样，两种polarity给相同一致先后而非冲突。

Topologicalorder翻完整圈degree-only合法，终点degreevector完全恢复。

若circuit全部U或全部L，上述precedence构成directedcycle，必须从outside引入一个相反status；不能声称monotone circuitword总存在。

## 5. Monochromatic circuit的external stem

### 5.1 全部L

在D的L-inducedsubgraph中，从circuitvertices作backwardreachability，得到B⊆L。若没有U→B arc，则没有任何outside→B arc；但

    out(B)−in(B)=Σ_{v∈B}(out(v)−in(v))=−|B|<0，

矛盾。所以有一个directedstem P，从outsideU出发，interiors皆L，到circuit的首次触点c，且interiors不在circuit。

Forwardedgeorder翻P，每步是一条U→L，U状态向c移动。此时c是U、其他circuitvertices仍L。第4节serialize整圈；degreevectors仍保持opening后的值。最后从c端逆序翻已反向的P，各步仍U→L，restore全部stemcopies及所有degree值。

### 5.2 全部U

在U-inducedsubgraph从circuit作forwardreachability，得到B⊆U。若没有B→L arc则out(B)=0，与 `out(B)−in(B)=|B|>0`矛盾。故有从circuit首次点c到outsideL、interiors皆U的directedstemP。

先从outsideL端逆序翻P，把L状态带到c；混合circuit按第4节serialize；再按P原始forwardedgeindex关闭已反向的copies，把L移回outside端。每步tailU/headL。

两种stem均有限，可以选simple。Circuit与stem仅共享接点，不翻丢physicalidentity。

## 6. 完成degree-only connectivity

沿第2节feasibledegreechain，每条path用第3节serialize，到目标degreevector。剩余difference是Eulerian current-directed support，分解为physicalcircuits；各圈用第4或5节处理、完成一圈后same-degree值恢复。最终达到目标orientation。∎

## 7. 对main theorem的实际意义与明确缺口

当G是(2k+1)-regular，k-strong orientation确实对每vertex只能有outdegree k或k+1；degree-only theorem说明这个单独的约束不会造成disconnectedcomponents。

但balanced-degree orientation不自动globallyk-strong。第3节的multiplepacketpartialword，以及第5节stem，可被propernon-singletontightcuts挡住。All-critical-singleton minimum-counterexample reduction并没有删除这些当前orientation的noncriticaltightcuts。

因此当前需要的是：把degree-only routing的packets/monochromaticstem改成fullcut-safe finite history；或用global minimal-frontierledger证明criticalsingletonstatus交换必能服务某个noncriticalrow。两者仍OPEN；本文只消除了“odd node degree itself freezes a circuit”的误解。
