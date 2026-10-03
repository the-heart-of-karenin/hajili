# Critical-shore 基础独立审计

日期：2026-10-02。状态：本文件证明的结论均为局部基础结论；主连通性问题仍未解决。

## 0. 阅读范围与审计范围

已逐段读取主档案 `graph_orientation_reconfiguration_progress_2026-10-02.md` 的 current layer 第 1–883 行、历史 residual formulation 附近第 1001–1182 行，以及完整历史段第 8001–10224 行。历史段中的有限搜索数字只按档案记录读取，本次未重新运行，因此不将其标为独立计算核验。

本次独立证明以下四项：端点公式、对称余量、Critical Boundary Skew、actual-tight partition/copartition 排除。它们无需假设 minimum component-separating descendant、source-free closure 或特定 blocker history。后文给出精确适用范围与固定内部边后的继承关系。

## 1. 假设与统一记号

令 G 为有限无自环多重图，k≥1，λ(G)≥2k+1。取非空真子集 A⊂V，满足 |δ_G(A)|=2k+1，令 B=V\A、H=G[A]。

固定所有非 H 边的定向 σ，并假设它可以扩展成一个 k-arc-strong 定向 D=F∪σ。非空 fiber 的假设很重要；任意任性指定的 σ 不自动满足后续结论。

对 Y⊆A，令 R(Y) 为 Y→B 的边数，S(Y) 为 B→Y 的边数，b(Y)=R(Y)+S(Y)。R、S、b 都是关于 A 上顶点的非负整数模函数。由 D 合法与 critical cut 大小可知：

\[
(R(A),S(A))\in\{(k,k+1),(k+1,k)\},\qquad b(A)=2k+1.
\]

K_σ 是删去 H 内部边之后的固定有向图。对 ∅≠Y⊊A 定义

\[
q(Y)=\min_{Z\subseteq B}d^+_{K_\sigma}(Y\cup Z),\qquad
p(Y)=k-q(Y),\qquad s_F(Y)=d_F^+(Y)-p(Y).
\]

每一条物理平行边分别计数。以下证明不识别平行边的身份，因此也不丢失它们。

## 2. 端点公式：完整直接证明

**命题 2.1（成立）。** 对上述任意可扩展 σ，

\[
q(Y)=\min\{R(Y),S(A\setminus Y)\}.
\]

上界来自 Z=∅ 与 Z=B。下面证明下界。令 W=B\Z，写

\[
c(Z)=d^+_{K_\sigma}(Y\cup Z)
=a(Y,W)+a(Z,A\setminus Y)+a(Z,W),
\]

其中 a(U,W) 记 σ 中 U→W 的边数。

若 R(A)=k：只要 W≠∅，纯 outside cut W 的入度至少 k，故

\[
a(Z,W)+a(Y,W)+a(A\setminus Y,W)\ge k.
\]

因此

\[
c(Z)\ge k-a(A\setminus Y,W)+a(Z,A\setminus Y)
\ge k-R(A\setminus Y)=R(Y).
\]

剩下的 W=∅ 即 Z=B，恰有 c(Z)=S(A\Y)。这给出所需下界。

若 S(A)=k：只要 Z≠∅，纯 outside cut Z 的出度至少 k，所以

\[
a(Z,W)+a(Z,Y)+a(Z,A\setminus Y)\ge k.
\]

于是

\[
c(Z)\ge k-a(Z,Y)+a(Y,W)\ge k-S(Y)=S(A\setminus Y).
\]

剩下的 Z=∅ 恰有 c(Z)=R(Y)。证毕。

**实际使用的最弱假设。** 此证明只使用一个方向的 boundary total 等于 k，以及对应纯 outside cuts 的 k 入度/出度下界；不使用 G 的全局 λ 下界，也不使用内部 F 的具体形状。全局合法扩展保证这些条件。

**推论 2.2。** 固定 boundary directions 后，critical fiber 的内部可行性不依赖 B 内部 σ 的具体结构，只要 σ 的 outside cuts 合法。把 B 收缩成一个 root 后，内部 fiber 的约束完全不变。

**推论 2.3（chain quasi-concavity）。** 若 E⊆F⊆T⊆A，则 R(F)≥R(E)，S(A\F)≥S(A\T)，故

\[
q(F)\ge\min\{q(E),q(T)\}.
\]

## 3. 对称余量其实是无向割大小的精确函数

**命题 3.1（成立，强于档案的 μ≥1）。** 对 ∅≠Y⊊A，

\[
q(Y)+q(A\setminus Y)
=\min\{b(Y),b(A\setminus Y)\}.
\]

证明：端点公式及恒等式 min(a,b)+min(c,d)=min(a+c,a+d,b+c,b+d) 给出左边等于

\[
\min\{R(A),S(A),R(Y)+S(Y),R(A\setminus Y)+S(A\setminus Y)\}
=\min\{k,b(Y),b(A\setminus Y)\}.
\]

两项 b 的和为奇数 2k+1，故其中至少一项≤k；因此 k 项可以删去。

令 m(Y)=|δ_H(Y)|，则

\[
\boxed{\mu(Y)=m(Y)-p(Y)-p(A\setminus Y)
=\min\{|\delta_G(Y)|,|\delta_G(A\setminus Y)|\}-2k.}
\]

这里 |δ_G(Y)|=m(Y)+b(Y)，另一边同理。因此 λ(G)≥2k+1 立即给 μ(Y)≥1。特别地，μ 只依赖无向图 G 与 shore A，完全不依赖 boundary orientation。

并且

\[
\mu(Y)=1\iff
\min\{|\delta_G(Y)|,|\delta_G(A\setminus Y)|\}=2k+1.
\]

所以 μ=1 必且仅当 Y 或 A\Y 本身为 global minimum cut shore。档案的“是某个 mincut 的 trace”在这里可具体到这两个直接候选。

同时 q(Y)+q(A\Y)≤k，且 q≥0，故每个 initial p(Y)=k-q(Y) 非负。

## 4. Critical Boundary Skew 的精确式

取任意非平凡 partition A=P₁⊔⋯⊔P_t，t≥2，所有块非空。定义

\[
\Phi=\sum_i\bigl(q(A\setminus P_i)-q(P_i)\bigr),\quad
h=\#\{i:b(P_i)\ge k+1\}.
\]

由于 Σ_i b(P_i)=2k+1，h 只能为 0 或 1。

若 R(A)=k、S(A)=k+1，写 r_i=R(P_i)、s_i=S(P_i)、b_i=r_i+s_i，则

\[
q(P_i)=r_i-(b_i-k-1)_+,\qquad
q(A\setminus P_i)=s_i-(b_i-k)_+.
\]

整数性给 (b_i-k)_+−(b_i-k-1)_+=1_{b_i≥k+1}，所以

\[
\boxed{\Phi=1-h\in\{0,1\}.}
\]

若 R(A)=k+1、S(A)=k，则相同计算给

\[
\boxed{\Phi=-1+h\in\{-1,0\}.}
\]

此处 skew 的方向不仅受 boundary totals 控制，还由 partition 中是否有唯一 heavy boundary block 精确决定。这一证明在取得端点公式后是纯 boundary arithmetic，不使用 source-free 或最小性。

## 5. 完整 partition slack 恒等式与两个排除结论

**命题 5.1（成立）。** 对任意合法 F 与上述 partition，

\[
\boxed{2\sum_i s_F(P_i)=\sum_i\mu(P_i)-\Phi,}
\qquad
\boxed{2\sum_i s_F(A\setminus P_i)=\sum_i\mu(P_i)+\Phi.}
\]

证明：每个内部跨块 arc 在 Σ_i d_F^+(P_i) 中计一次，在 Σ_i d_F^+(A\P_i) 中也计一次，故两个总和相同。因此

\[
\sum_i\bigl(s_F(A\setminus P_i)-s_F(P_i)\bigr)=\Phi.
\]

再利用逐块恒等式 s_F(P_i)+s_F(A\P_i)=μ(P_i)，相加相减即可。

于是总 slack 满足

\[
\boxed{\sum_i s_F(P_i)\ge\left\lceil\frac{t-1}{2}\right\rceil,
\qquad
\sum_i s_F(A\setminus P_i)\ge\left\lceil\frac{t-1}{2}\right\rceil.}
\]

所以任意 t≥2 的 partition 不可能所有 P_i 都 actual-tight；其 copartition 也不可能所有 A\P_i 都 actual-tight。此处 actual-tight 必须是完整 residual slack 等于 0，而不能是仅跟踪若干行之后的局部记账值。

例如 A=Z₁⊔Z₂⊔Z₃⊔Q，前三块 actual-tight 时，必有 s_F(Q)≥2。这一结论不需要 Z_i 间存在 private directed 3-cycle；private cycle 是后续额外结构。

精确式还给 parity 约束 Σ_i μ(P_i)≡Φ (mod 2)，可在等号分支中直接使用。

## 6. 固定内部边后的继承：哪些可用、哪些不能直接照搬

固定内部有向边集 J，remaining graph K=H−J，令

\[
p_J(Y)=p(Y)-d_J^+(Y),\qquad q_J(Y)=q(Y)+d_J^+(Y).
\]

若 remaining orientation 为 L，则

\[
s_L^J(Y)=d_L^+(Y)-p_J(Y)=s_{J\cup L}(Y),
\quad \mu_J(Y)=\mu(Y).
\]

对任意 partition，

\[
\Phi_J=\sum_i[q_J(A\setminus P_i)-q_J(P_i)]
=\Phi,
\]

因为 J 中跨块弧在两侧各计一次。由此可知，整个第 5 节的 partition/copartition slack 恒等式与排除结论严格 hereditary，即使 p_J 取负值也成立。

但是 q_J 逐项一般不再等于 min{R(Y),S(A\Y)}，也不能把它当作新的 true-critical endpoint function；chain quasi-concavity 亦不应未经独立证明转用给 q_J。p_J 的非负性不继承。特别地，这些 hereditary 结论仍不能推出 descendant fiber connected：它们只排除某种 tight-family 形状。

## 7. 文献基线与旧历史层的表述修正

已直接打开并核验作者原始论文 [Monotone edge flips to an orientation of maximum edge-connectivity à la Nash-Williams, arXiv:2110.11585](https://arxiv.org/pdf/2110.11585)，Theorem 2（PDF 第 3 页）及 §3（PDF 第 7–8 页）。该论文明确允许多重边，证明 λ(G)≥2k+2 时 k-arc-strong 单边翻转图连通。正式 [SODA 2022 论文页](https://epubs.siam.org/doi/10.1137/1.9781611977073.56) 也确认这一结论。

其 connectivity 证明先把两个给定定向分别通过单边翻转提升为 (k+1)-arc-strong；接着使用 Frank 的宏路径/环翻转连接它们，再逐边序列化；宏路径的前缀使任一割最多损失一个出弧，所以中间保持 k-arc-strong。

审计修正：旧历史层第 13.1 节把 2k+2→2k+1 描述成 safe-source counting 的 strict inequality 变 equality，这只能是待分析的研究设想，并不是 §3 证明的实际差异。λ=2k+1 时 global (k+1)-arc-strong orientation 被该最小割直接禁止，所以已知证明最先失去的是全局提升步骤。需要一种局部余量/不同桥接结构来替代它。

本次定向检索没有发现直接解决 2k+1 的来源；这一有限检索不构成完整截至日期文献调查。

## 8. 当前审计结论

四个指定基础结果均可独立证明，未发现它们在正确 critical fiber 假设下的漏洞。最值得后续直接引用的是更强的 μ 无向割精确式、heavy-block skew 精确式、partition 总 slack 恒等式，以及 Φ_J=Φ 的固定边继承关系。

额外 terminal 假设并不需要；必要的实际条件是 |δ(A)|=2k+1、底图 λ≥2k+1，以及 outside σ 有合法扩展（或显式满足端点证明需要的纯 outside cut 下界）。没有这些条件时不能照搬。

这些结论均不填补 minimum component separation ⇒ closed temporal obstruction 的全局必要性桥。后续使用时应保留这一界限。
