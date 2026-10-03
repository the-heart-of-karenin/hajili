# 边最小性的新用途：非临界边的共同环境分量

2026-10-03。主目标仍为原始 Ω_k(G) 连通性。这里显式使用已经固定的反例图字典序最小性 (|V|,|E|)，而非只用顶点最小性。所有 parallel copies 保留身份。

## 1. 删除与单翻的同一个危险割

在合法定向 D 中，当前 physical arc f=u→v 可单翻，当且仅当删除 f 后 D−f 仍 k-arc-strong。两种操作只会使含 u、不含 v 的割减 1；反转对另一些割增加 1，删除对那些割不变。故两种操作的失效条件相同。

下文把这样的 f 称为 D-deletable，未添加任何方向无关的假设。

## 2. 非临界边集合与一个边的分量

在 λ(G)=L=2k+1 的最小反例图中，定义

    E°={f∈E(G): f 不属于任何大小为 L 的全局无向割}。

这是原图物理边集合，不是某个定向中的合法边集合。对 f∈E°，所有含 f 的原割至少 L+1，故 λ(G−f)≥L。图 G−f 的顶点数不变、物理边数减少 1；按固定的字典序最小性，Ω_k(G−f) 连通。

令 U_f 为 G 中全部 f-deletable 合法定向。它非空：G−f 满足 λ≥L≥2k，有 k-strong 定向，将 f 以任一方向加回即得 U_f 中状态。

**命题 2.1.** U_f 中所有状态处于 Ω_k(G) 的同一个环境分量 C_f。

证明：给 D,E∈U_f，D−f,E−f 都合法。沿 Ω_k(G−f) 的合法 physical word 连接它们，加回并暂固定 f 的 D 方向，每步仍合法；最后若需要翻 f，在一个删 f 后合法的状态上翻它也合法。因此 D,E 相连。这里连接词未假设始终停留在 U_f，但实际构造的所有状态均在 U_f。∎

因此任何其它环境分量 C≠C_f 中，f 永远不可合法翻；f 的方向在 C 上恒定。

## 3. 不同非临界边共用同一个分量

**命题 3.1.** 对任意不同 f,g∈E°，λ(G−{f,g})≥2k。

逐割证明：若割不含这两条边，删除不改变它；若只含一条，原割至少 L+1，删除后至少 L；若含两条，原割至少 L+1，删除后至少 L−1=2k。所有 cuts 已覆盖，parallel identities 不合并。∎

由 Nash–Williams orientation existence，G−{f,g} 有 k-strong 定向。将两边以任意方向加回，两边都可单独合法删除，所以 U_f∩U_g 非空。由命题 2.1，C_f=C_g。

于是只要 E° 非空，就有唯一的共同环境分量

    C°，包含所有定向中至少一条 E°-copy 可合法翻的状态。

任何其它环境分量的全部 E°-copies 都永远冻结，其所有合法翻边必须属于某个 L-mincut。

这是 genuine ambient component 结论，不是 frozen sector 的计算分量。证明允许 C° 内其它状态临时没有任何合法 E°-copy。

## 4. 在 C° 上锚定最小差异：排除 circuit branch

本节另定义 h°，不覆盖 synthesis 中 h，也不覆盖 boundary audit 中 h_r：

    h°=min{dist_H(R,Q): R∈C°，Q∉C°，R,Q 都合法}。

如果原图不连通且 E° 非空，这个集合非空；选 attaining pair R,Q，K 为差异 copies，J 为共同 copies。相对于二元标签“在 C° / 不在 C°”取最小 coordinate restriction，既有 elementary two-antipode lemma 与 integral-face support classification 仍适用。固定 J 的可行 cube 恰两端，K 在两端全部不可单翻；必要 support 是单 directed physical circuit 或若干 vertex-disjoint directed paths。

**定理 4.1.** h° 的 K 不可能是 directed physical circuit。

证明：若 K 是圈，全圈反向不改变任何全局 cutout。故任意 J-word 可在两个端点同步合法执行，两条 sheet 的每个对应状态仍相差同一 K。

在 R 的整个环境分量中 K 永远不可首次翻动：若一个 J-prefix 后首翻 e∈K 合法，同步得到的 Q-sheet 状态仍在 C° 外；翻 e 后 Hamming distance 降为 h°−1，违反 h° 最小性。于是从 R 到 C° 内任意状态的全部合法词都只翻 J。

任选 f∈E°，C° 含某个 F∈U_f。取 R→F 的合法词；它只用 J，因此同步给 Q→F′，F′ 仍在 C° 外，而 F,F′ 的所有割值相同。

若 f∈K，F 的 f 单翻已由上一段禁止，与 F∈U_f 矛盾。若 f∈J，f 在两端方向相同，删除危险割相同，所以 F′∈U_f。命题 2.1 又给 F′∈C°，矛盾。∎

因此在 E° 非空时，可以选一个真正环境分量分离的最小对，其 support 必为若干 vertex-disjoint directed paths。圈分支不再需要任意服务历史。这不是断言原先另一个最小 h 或 h_r 的圈也被自动排除。

## 5. 精确的作用和剩余范围

对原始 MAIN 的推进：最小反例若含非临界边，可用 C° 锚定，消去 circuit-support branch，把问题压向路径端点的非对称守卫。不能把路径支撑强行收成一条路径；必要分类仍允许多条 vertex-disjoint paths。

若 E°=∅，上述锚分量不存在；所有物理边都属于某条全局 mincut。这包含 odd-regular 图，不能由当前证明排除。并不由此推出每个 vertex degree=L，也不推出 quotient 为一棵物理树。

路径情形不能同步：全部路径反向对 cutout 的净变化为其各端点 imbalance 总和；两端实际 tight rows 可以不同。一条在 C° 端合法的 J-copy 未必在另一端合法。命题 4.1 的证明明确依赖圈 cut-neutral，不能直接复用。

### 5.1 用另一个最小对象，确实可以选到 single-path macro

另定义 ℓ° 为全部合法终态 single-path/circuit macros 中，两端分别在 C° 内、外的最小 physical length。已有 global macro connectivity 保证存在跨 C° 的 macro，故该定义有意义。

若最小 macro 是圈，任一 K-copy 的首翻会留下长度 ℓ°−1 的合法终态 single-path macro，仍跨 C°，矛盾。因此其 K 在两端都不可首翻。任意共同 J-word 同步合法，圈 support 及 ℓ° 保持，所以整个 C° 中 K 仍不可首翻。再走到某个 f-deletable 状态，命题 4.1 的同一锚分量证明给矛盾。

所以 E° 非空的最小反例必有一个跨 C° 的 **single directed path macro**，可取其 physical length 最小。其首、尾 K-copy 在两端不可单翻：翻任一端边会留下更短的 directed path macro。Interior K-copy 的首翻却会把 support 切成两段，不能用 ℓ° 最小性宣称其也被冻结。

这里 h° 与 ℓ° 是不同的最小对象：h° 的 necessary support 允许 path collection；ℓ° 给 single path，但只直接冻结首尾。没有把两种好处不经证明同时加在一个 pair 上。

该结果没有完成 root-star mixing。它给下一次 proof attack 一个可用的环境分量锚，和明确不能再使用的圈/路径混同。

## 6. 外部输入位置

本文件只在两边同时删除后使用 [Nash–Williams orientation existence（Ito 等原始论文 Theorem 1 也包含这一存在性）](https://arxiv.org/pdf/2110.11585)。边最小性、共同分量、h° 与圈分支排除都是本次推导，不从该论文引用 reconfiguration 结论。
