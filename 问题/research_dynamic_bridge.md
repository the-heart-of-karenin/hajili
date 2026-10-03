# 动态桥接：安全 stem、cycle sheets 与仍缺的启动链

日期：2026-10-02。主问题仍 OPEN。本文件只记录量词明确的动态接口；不把初始 no-frozen theorem 递归套到 frozen-J faces。

## 1. 单边合法性只由当前 tight cuts 决定

在完整初始 fixed-outside 定向 D 中，令 T(D) 为全部非空真 residual actual-tight shores。对当前内部弧 g=u→v，翻转合法当且仅当不存在 X∈T(D) 满足 u∈X、v∉X。

整数 slack≥1 的割在一次翻转中最多损失 1，故不会单独阻止该步。删除 g 与翻转 g 具有相同的危险割，二者在当前定向中等价合法。每次合法翻转后，新 tight cuts 可能来自旧 slack=1 的割，不能只跟踪旧 tight family。

## 2. 安全 directed stem 可以一次搬运一单位 slack

以下 lemma 不依赖临界连通度；仅使用所有相关割当前的非负整数 slack。

取一个内部有向简单路径 P=(c=v0→v1→…→vℓ=w)，所有物理弧按 D 的方向。依次翻转 P 的弧，顺序从 c 到 w。翻转前 j 条弧后，对任意 shore X 的净 outcut 变化为

    1[vj∈X]−1[c∈X]。

因此，若每个当前 tight X 满足

    c∈X ⇒ {v0,…,vℓ}⊆X，

则每个 opening prefix 都合法：tight cuts 从不损失，其他割原有 slack≥1，而净损失最多 1。这不是假设每条 P 弧在原始 D 都合法；后续弧可能需要前一段留下的 slack。

定义 cl_D(c)=∩{X∈T(D):c∈X}；没有此类 X 时取 cl_D(c)=A。条件就是 P 的所有顶点都位于 cl_D(c)。这是一个可直接检查的有限路径条件。

### 2.1 翻转指定弧的充分条件

设 e=w→z 不在 P 中。若 P 安全，且每个 e-blocking tight X 都遗漏 c，则开满 P 后可合法翻转 e，也可删除 e。

证明：e-blocker 含 w 不含 z，而其遗漏 c，所以得到恰一单位 slack。任意其他 e-outgoing cut 含 w，其 opening 净变化为 1−1[c∈X]≥0；原本非 tight 的这些割仍至少有一单位 slack。故 e 的损失可全部支付。

这给一个逐割充分条件，并未证明每个 e 都有这样的 stem。

## 3. 安全 stem 序列化一整条 directed circuit

设 C 是 D 中的内部 directed physical circuit，取 w∈V(C)，P 是从 c 到 w 的有向简单路径，内部顶点不在 C，物理边与 C 不交。允许 ℓ=0。

假设

    对每个 X∈T(D)，c∈X ⇒ V(P)∪V(C)⊆X。              (SAFE-STEM)

则下列 balanced word 合法：

    从 c 开 P；从 w 沿 C 的方向依次翻转整圈；逆序关闭 P。

证明：在开 P 和走 C 的全过程，已翻转弧构成从 c 到当前 frontier v 的有向 walk（可能额外含一整圈）。每个完整 directed circuit 对所有 outcuts 的净变化为 0，故当前净变化仍为 1[v∈X]−1[c∈X]。SAFE-STEM 保证 tight cuts 不损失，其他割最多损失 1。走完 C 后所有割的值与开满 P 时相同；关闭 P 又逆序重现已知 opening states 的割值。因此每步合法，最终只反转 C。

占用的 ancestral copies 至多 |P|，word 长度 2|P|+|C|。这里没有常数宽度结论；|P| 可以任意大。

### 3.1 有限检查接口与量词障碍

能满足 SAFE-STEM 的起点必须属于

    U_C=A\(∪{X∈T(D):V(C)⊄X})。

对某个 c∈U_C，只需检查 D[cl_D(c)] 中是否有从 c 到 C 的有向路径，并取第一次碰到 C 的位置作为 w。若存在，就得到上述 word。

尚未证明 U_C 非空；即使非空，也尚未证明该 induced subdigraph 总能到达 C。cross-free source theorem 保证某条合法内部 launch，却没有要求它以 SAFE-STEM 的共同起点为尾，也没有要求所有 C 顶点都高于该起点的 tight membership。因此该 lemma 不能单独填上一般 connectivity。

## 4. Directed-cycle difference 的同步 sheets

若一对合法完整定向 R,Q 只在一个 directed physical circuit K 上不同，且 Q 反转整条 K，则每个全局 / residual cut 在两端的 outvalue 相同。原因是每个 directed circuit 跨任何割的进、出边数相等。

所以两端 tight families 完全相同；每条 J=H−K 的当前方向相同，其单边合法性也相同。任意只翻 J 的合法 word 都可从 R 和 Q 同步执行，所有中间定向的 cut values 保持相同，差异一直为 K。

若 R,Q 属于不同原始 components，且其 Hamming distance |K| 是跨 component pairs 的最小值，那么同步可达的每个状态均禁止 first-K-progress。否则在 R-sheet 翻转某条 K 边后，它与 Q-sheet 状态的距离变成 |K|−1，仍属于不同 components，矛盾。

因而，一个假想 minimum separating cycle 的必要结构是：两个由相同 J words 产生的同构 sheets；每个 paired state 的 K edges 全部非法；每个 paired state 又至少有一条合法 J edge。后一点由 initial no-frozen theorem 得到。这样的同步有限状态图可以有回路，目前没有证明其必产生 K-unlock。

这个必要结构比任意 frozen-J antipodality 强。显式 unbounded-Debt controls 在同步 J sheet 内已有 SAFE-STEM / 解析 opening word，所以不满足此必要的全程 K-frozen 条件。

## 5. Minimum completion 的静态 acyclic difference

固定一个 reference R、删除 e，并要求所有其余 K copies 保持 reference 方向。若存在合法 completion，取其中 J Hamming cost 最小者。按 R 的方向看，它所翻的 J copies 不含 directed physical circuit。

否则可把这条 directed circuit 的 copies 全部恢复成 reference 方向；反转一整圈保持所有 cut values，仍合法，却严格减少 J cost，矛盾。

此结论不证明存在可执行的 first flip。无有向圈的 difference 仍可能在 contraction atoms 间形成 guard dependencies；reference-tight 与 completion-tight 的量词也不同。若允许其余 K 自由翻转，只能排除完全位于 positive-cost J 的圈，不能无条件排除整个 difference support 中的圈。

## 6. 下一步的两个精确目标

1. 在 minimum separating cycle 的同步 J sheet 上，证明存在一个可达状态满足 SAFE-STEM，或给出更一般但可序列化的 finite service network。只证明任一点有 launch 不够。
2. 对 directed-path K，common tight cuts 与 endpoint-specific tight cuts须分开。它们的割变化为 τ(X)=1[t∈X]−1[s∈X]；两端 launch 可能只在一端合法，不能偷用 cycle-sheet 同步。

任何把 arbitrary frozen descendant 的 remaining K 无冻结 / RCD 当成输入的证明，都与已知 genuine counterexamples 冲突，须立即退出该路线。

## 7. 对偶 safe sink stem：opening 顺序必须反过来

取 D 中 P=w=v0→…→vℓ=c，内部顶点不在 directed circuit C中，物理边不交。假设每个 initial tight X只要与 V(P)∪V(C)有交，就含 c。

先从靠近 c 的最后一条 P弧开始，逆着 P的索引顺序开 path；再从进入 w 的 C弧开始，逆着 circuit索引顺序翻一整圈；最后按原 P的正向索引顺序关闭。每个 opening / circuit prefix的净变化是

    1[c∈X]−1[deficit-frontier∈X]。

若 tight X含 deficit-frontier，假设保证含c，所以 tight cuts不损；其他cuts最多损1。关path同样重现已知割值。word合法，最终只reverseC。

不可把长 P按 w→c 的正向顺序开：那时第一段净变化为 χ当前frontier−χw，与上述假设无对应，证明失效。

initial safe-stem起点集合 U_C可能为空。research_global_scope.md §12有 genuine k=2、λ=5 的解析 control：A={w,y,c}，初始tightrows为{c},{w,c},{y,c}；两边cycle w↔y 的 U_C为空，却可用长度1 safe-sink path w→c连接，且一次Jlaunch后forward safe-stem变可用。因此仅要求原始 state有forward stem太强；minimum-origin目标必须量化整个 paired orbit。

## 8. Dual reoptimization 的真实退化接口

固定 cut weights y与合法 Jflip g，记 Δ=φ(head)−φ(tail)按旧方向计量。reference改变后 slack weighted sum增加Δ；g的L_J penalty从[Δ−1]_+变成[−Δ−1]_+，所以

    Debt_(R⊕g)(y)−Debt_R(y)=−clip(Δ,−1,1)。

重新优化 y会改变梯度。若R是在Jcomponent内 deletion-LP value全局最小的reference，则在neighbor R'的optimaldual y'下，g旧方向的gradient非正；其合法 undo的新方向可成为positivegradient。只在每一步选positive source / 重新优化dual，不保证严格全局进展，可能 undo。

Δ=1另有互补退化：它不迫使最优 completion翻该 edge。一个 integer optimaldual与另一个strictly complementary（可能fractional）dual不能拼成同一证书。research_terminal_debt.md §10保存一个三变量 boxed LP精确control和完整代数审计；它仅是逻辑控制，不是graph counterexample。
