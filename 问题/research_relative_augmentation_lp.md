# µ≥2 的相对严格定向：独立 LP / 树预算证明

日期：2026-10-02。这是 existence theorem，不是单边可达性 theorem。证明经 guard_geometry 与 global_scope 两支独立审计。

## 1. 结论

在初始 true-critical fixed-outside system 中，假设

    µ(Y)≥2，∀∅≠Y⊊A。

则存在完整内部定向 D*，保持 boundary / outside signature，满足

    d_D*^+(Y)≥p(Y)+1=k+1−q(Y)，∀∅≠Y⊊A。

因此所有 proper internal residual cuts 都有至少一单位 slack。outside critical cut 本身仍只能处于 (k,k+1)；这里没有要求全局 (k+1)-arc-strong。

## 2. 有限 LP

允许每条内部物理边分数定向。令 z 属于 orientation box，解

    maximize ε
    subject to d_z^+(Y)+q(Y)≥k+ε，∀∅≠Y⊊A。

若 |A|≥2，ε 上界有限；初始合法定向使 ε=0 可行。以下证明 ε*≥1。|A|=1 没有待提升的内部 cuts，结论空真。

假设 ε*<1。有限 LP dual 提供 y_Y≥0、Σy_Y=1，且：

1. positive-weight rows 在同一 z* 处 active，即 out_z*(Y)=k+ε*−q(Y)；
2. z* 最大化 weighted outcut Σy_Y d_z^+(Y)。

在全部 optimal y 的 compact simplex 中，取使 Σy_Y|Y||A−Y| 最小者。

若两个 positive-support rows W,Y crossing，crossing-supermodularity of p+ε* 与 fractional directed-cut submodularity迫使 I=W∩Y、U=W∪Y 都 active，两个 petals 间没有任何 physical edge，且 q(W)+q(Y)=q(I)+q(U)。把 min(y_W,y_Y) 从 W,Y 移到 I,U，保持 weighted cut coefficients、weighted constants、Σy 和 dual objective，却严格降低该 potential。因此其 positive support F cross-free。

## 3. 支持上的 source-free 是坐标最优性的后果

定义 φ(v)=Σ_{X∈F:v∈X}y_X。weighted outcut 对一条 physical edge 的最优方向必须满足 φ(tail)≥φ(head)。若一条边分数定向且两种方向都获得正质量，则两端 φ 相等。

跨 F membership atoms 的 strict-source direction，对每个 row 都无负号且至少一正。因为 F 中每个 row weight 严格正，它必满足 φ(head)>φ(tail)。故这样的方向不可能获得正质量。

因此，所有正质量的跨 atom directed copies 至少 consumes 一个 active row。这里把每条物理边分成质量 α 与 1−α 的两个方向；质量总和仍是一个 physical copy，不增加 M。

## 4. Split tree 仍可使用

Complementary active rows 会给 µ(X)=2ε*，但 µ≥2、ε*<1，故不存在。distinct rows 代表 distinct splits。

任何 partition A=⊔Pi 的 interpiece physical edge count M_P 是整数，且

    2(M_P−Σp(Pi))=Σµ(Pi)−Φ，
    2(M_P−Σp(A−Pi))=Σµ(Pi)+Φ。

若有 t≥2 blocks，µ≥2、|Φ|≤1 与整数性给两种总 slack 都至少 t。若所有 normal rows（或所有 co-rows）在 ε* level active，则总 slack=tε*<t，矛盾。因此 split tree 的每个 empty node仍 mixed。

## 5. 将 CFST budget 延伸到分数质量

令 t=|F|，n 为 occupied atoms，e=t+1−n，Q=Σ_{X∈F}q(X)。对方向质量 α 计量 ν=负号个数，定义

    σ=Σ_direction mass α·max(ν−1,0)。

Section 3 给 ν≥1 对所有正质量跨 atom 方向成立。紧行总消耗为

    M+σ=t(k+ε*)−Q。

每个 empty node 的 U_v 仍 proper，LP feasibility 给 out_z*(U_v)+q(U_v)≥k+ε*。原 CFST 两个 packings不变：每个 q row 只支付一个 empty endpoint；每条方向质量的 negative-negative pairs 至多 max(ν−1,0)。所以

    Q+σ≥e(k+ε*)，
    M≤(n−1)(k+ε*)。                                  (upper)

µ(atom)≥2 的精确 cut formula意味着每个 proper atom 在 G 中的 undirected degree至少2k+2。收缩 atoms 与 outside 后，outside degree仍2k+1，故

    2M+(2k+1)≥n(2k+2)，
    M≥(n−1)(k+1)+1。                                  (lower)

family 非空，n≥2；两界对 ε*<1 不相容。因此 ε*≥1，得到 fractional strict orientation。

## 6. Integer extraction

orientation box 的需求 f(Y)=p(Y)+1 是 integer crossing-supermodular。该 polytope 的所有 vertices integral；同一证明也适用于任意 integer crossing-supermodular proper-shore demand，不要求 demand 非负。

简述独立证明：在任意 vertex 的 fractional coordinates K 上，active cut normals张成满秩。选 generic exposing objective，避开有限 normal 集合的每个 proper span；在 positive conic representation 中最小化 shore potential。active crossing cuts 用 intersection / union替换时，cut identity和 crossing-supermodularity迫使 physical petals 为零，故 normal、RHS 与 objective均保持。得到 cross-free full-rank active basis；删去 complementary split 的线性冗余，root-complement 仅作为 normal 的符号变换，给 laminar split-tree fundamental-cut/network matrix。它是 TU；integer RHS 扣除 fixed integer box coordinates后，方阵 basis 给所有 K coordinates integer，矛盾 fractional vertex。

于是 ε=1 的非空 bounded polytope有整数 vertex，即所需 D*。完整 general integrality证明与适用域补充见 research_global_scope.md §13；另一条使用 primary orientation min-max 的独立证明见 research_relative_augmentation.md。

## 7. 可使用与不可使用的接口

可使用：当所有内部 µ≥2 时，存在 relative strict target orientation，不需提高 critical boundary 的两向强度。

**后续更新：** 本文只证明 existence，不独自承担动态结论；但 `research_global_scope.md` §14已证明全部strict targets处于同一原始component，`research_relative_reachability_audit.md` 又证明任意initial D在all-proper-µ≥2范围可合法augment到strict。组合后该范围H1已闭合。一般µ=1以及signed descendants仍OPEN。

µ=1 在当前全边 source budget 中是精确的临界现象；它迫使 dual active family 可出现 opposite tight shores，阻断 Section 4 的树表示接口。存在性结论将研究焦点进一步压向 µ=1 shores 的服务与转移，而不是恢复常数 Debt conjecture。
