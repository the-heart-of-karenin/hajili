# Global scope audit and elementary long-edge proof

日期：2026-10-02。对应修订档 C0.3、C0.4、K0.6。本文独立工作，不修改总档案。

## 0. 本轮结论与适用域

1. **PROVED / elementary**：cardinality-minimum component-separating descendant 恰有两个 antipodal feasible states；每条 remaining physical edge 在两端都 individually illegal。这里只需要 hypercube restriction 和 original flip-component labels，完全不用 orientation existence / integrality theorem。
2. **SCOPE CLOSED / also elementary primal proof**：把 true-critical descendant 当作 full global orientation polytope 的固定 0/1-coordinate face，即可继承 integrality，推出 two-state descendant polytope 为 segment。无需对 signed demand `p_J` 本身另行套用非负 demand theorem。Section2.1还独立证明了所需global primal integrality。
3. **PROVED / independent necessity**：对本项目的 full global cut polytope，若两个 0/1 orientations 的最小面是一条 edge，则 difference support 在任一端为一个 directed physical circuit，或若干 vertex-disjoint directed physical paths。下面给出完整 proof，替代无编号的 Lovász citation debt。
4. **SCOPE REPAIR**：不能把 support 为 circuit / vertex-disjoint paths 当作 adjacency 的充分条件。slack-rich examples 中这种 support 也可以形成 cube diagonal。历史段落中的 `if and only if` 不应在项目中作为充分方向引用。
5. common-tight cross-free **spanning** family 只保留线性 rank；它不自动保留 source-free，也不提供 source guards。它足够完成 long-edge support classification，但仍不能解决 guarded closure / H1。

## 1. 完全初等的 minimum descendant normal form

设 `S` 是有限 hypercube `{0,1}^E` 中的可行状态集合。以 Hamming-distance-one 的可行边定义原始 flip graph，`c(s)` 表示原始 connected component label。一个 descendant 是固定若干 coordinate 所得的 restriction；它 component-separating 当且仅当包含不同 `c` 标签的状态。

在所有 component-separating descendants 中，取 remaining coordinate set `K` cardinality 最小的一个，记其可行状态集为 `T`。以下的“component”始终指**原始 flip graph**，而不是 restriction 中另算的 component。

### Proposition 1

存在 `R,Q` 属于 `T`，满足

\[
T=\{R,Q\},\qquad Q=\bar R\quad\text{on }K,
\]

且 `|K|>=2`，every `K`-edge reversal 在 `R,Q` 都不可行。

**Proof.** 选 `c(R) != c(Q)`。若某 coordinate `e in K` 在 `R,Q` 相同，则继续固定它仍得到 component-separating descendant，反于最小性。因此 `R,Q` 在 every coordinate 相反。

对任意 `e`，两个 slices `T[e=R_e]` 和 `T[e=Q_e]` 均非空，并分别包含 `R,Q`。每个 slice 比原 descendant 少一个 variable coordinate，因此每个 slice 的所有状态只有一个原始 component label；两个标签分别为 `c(R),c(Q)`。

设有第三个状态 `U`。若它既在某 coordinate 与 `R` 相同，又在另一 coordinate 与 `Q` 相同，那么 slice monochromaticity 同时给 `c(U)=c(R)` 和 `c(U)=c(Q)`，矛盾。所以 `U` 必须等于 `R` 或 `Q`。

若 `|K|=1`，`R,Q` 是可行 Hamming neighbors，必属相同原始 component，矛盾。于是 `|K|>=2`。任何单 `K`-edge reversal 若可行，会产生不同于 `R,Q` 的第三个状态，已被排除。证毕。

**Scope note.** 若只最小化“restriction 自己 disconnected”，上述 proof 无效：进一步 fixing coordinate 后可能把原本同一 ambient component 的状态人为分开。必须最小化 **original-component-separating** descendants。

## 2. Integrality 应在 full global cut polytope 上应用

固定一个任意 reference global orientation `D`。对每条 physical edge 使用独立 reversal coordinate `x_e`。定义

\[
Q_D=\{x\in[0,1]^{E(G)}:
x(\delta_D^+(U))-x(\delta_D^-(U))\le d_D^+(U)-k,
\quad\varnothing\ne U\subsetneq V(G)\}.
\]

整数点恰好对应 global `k`-arc-strong orientations。这里 parallel copies 保留 coordinate 身份。

Edmonds--Giles 的 cut-difference system 对 integer crossing-submodular RHS 是 box-TDI / box-integer。具体本例：domain 是 all nonempty proper shores（一个 crossing family），RHS

\[
f(U)=d_D^+(U)-k
\]

在 crossing pairs 上 submodular，因为 directed outcut function submodular，而两边各减去相同的 `2k`。`f` integer；无需 `f>=0`。因此 `Q_D` integer。

固定 outside orientation `sigma` 和 ancestral internal orientation `J` 等于把一批 global reversal coordinates 固定到 0 或 1。由于已有 bounds `[0,1]`，这是 `Q_D` 的一个 face，故该 face integer。删除固定 coordinates 是 affine isomorphism，保留 integrality。

而 residual inequalities `d_K^+(Y)>=p_J(Y)` 正是该 face 的 exact description：对于固定 outside orientation，所有 global shores `Y union Z` 的最强要求为 `k-q(Y)`；再减去固定 `J` 的 cut contribution 得 `p_J`。这一描述可能 signed，但不影响它的 global face origin。

现在 Proposition 1 给 descendant only two integer points `0,1`。有界 integer polytope 的 every vertex integer，因此

\[
P_R=\operatorname{conv}\{0,1\}=\{t\mathbf1:0\le t\le1\}.
\]

**进一步缩小引用需求。** 这一步实际上只需要 full `Q_D` 的 ordinary integrality，不需要 descendant 的 standalone box-integrality。global box-integrality 是更强工具，但 signed residual theorem scope 并非这里的债务。

### 2.1 完全独立的 primal integrality proof

本节把Section3.2的cross-free spanning argument用到任意vertex，因而本轮所需primal integrality也可以不用外部theorem。

设`z`是`Q_D`任意vertex；把active box bounds上的coordinates记为`I`，其值均为0或1；其余coordinates记为`K`。若`K`为空则已integer。vertex条件给tight cut normals限制到`K`后rank等于`|K|`。

tight cut family的crossing closure不用fractional图解释也可直接验证。令`f(U)=d_D^+(U)-k`，`n_U`为完整signed cut normal。若`U,W` crossing且tight，则

\[
f(U)+f(W)=(n_U+n_W)z=(n_{U\cap W}+n_{U\cup W})z
\le f(U\cap W)+f(U\cup W)\le f(U)+f(W).
\]

故intersection/union也tight。用Section3.2的generic objective与minimum potential uncross，得到cross-free tight normals，在`K`上仍rank`|K|`。

root-complement后laminar normals组成一个tree fundamental-cut matrix。该矩阵是network matrix并且totally unimodular，下面补其determinant理由，避免把该性质另当未审计black box：

令`A_T`为rooted laminar node tree的reduced node-incidence square matrix，`A_T`有determinant`+1`或`-1`。令`A_Q`为physical-edge quotient arcs的reduced node incidence。tree fundamental-cut matrix，差至多row signs，为

\[
N=A_T^{-1}A_Q.
\]

对于任意equally-sized row-index set`P`与arc-column set`Q`，把`A_T`中columns`P`替换为`A_Q`的columns`Q`。所得matrix仍由reduced directed incidence columns组成，其determinant为0、1或-1（incidence矩阵的标准leaf elimination / column-sum argument）。basis replacement determinant identity给

\[
\det N[P,Q]=\pm\frac{\det A_{\rm replacement}}{\det A_T}\in\{0,1,-1\}.
\]

故`N`TU。选`|K|`条linearly-independent active cut rows得到square nonsingularTU submatrix，其det为±1。它的RHS是integer `f`减去fixed integer coordinates的贡献，故唯一解`z_K`integer。

every vertex integer，证明所需`Q_D`integrality。相同proof允许additional arbitrary integer coordinate bounds，只需active bounds的值integer；所以还能直接得cut-difference polyhedron的primal box-integrality。其TDI / integer-dual最优性仍是另一项theorem，本文没有把primal proof冒充dual证明。

## 3. Long-edge support：不依赖外部 adjacency theorem 的完整必要方向

以下证明适用于任意 finite loopless undirected multigraph 的 `k`-arc-strong orientation polytope。设 `R,Q` 是不同可行 0/1 orientations，二者在 polytope 中 adjacent。记 difference physical support `K`，`m=|K|`，用 `R` 作 reference。除 `K` 外所有 coordinates 在两端相同，`K` coordinates 在两端为 `0` 与 `1`。令 midpoint 为 `z`。

若 `m=1`，support 已是一条 directed single-edge path。以下设 `m>=2`。

### 3.1 Midpoint common-tight cut normals

把 midpoint 看成 fractional orientation `F`：一条 fixed edge 的方向权重为 1；每条 `K` edge 两个方向各有权重 `1/2`。令

\[
h(U)=d_F^+(U).
\]

记 tight shores family

\[
\mathcal T=\{U:\varnothing\ne U\subsetneq V,\ h(U)=k\}.
\]

对 `U in T`，restricted cut normal 为

\[
n_U(e)=\mathbf1_U(\operatorname{tail}_R e)
-\mathbf1_U(\operatorname{head}_R e),\qquad e\in K.
\]

midpoint tight 的任何 inequality 在两个 feasible endpoints 都 tight，所以

\[
n_U\cdot\mathbf1=0.
\]

midpoint 在一条 polytope edge 的 relative interior，故所有 active constraint normals 的 rank 为 full dimension减1。把 common fixed coordinates 去掉，`K` 上没有 active box bound，故

\[
\dim\operatorname{span}\{n_U:U\in\mathcal T\}=m-1.
\]

### 3.2 找到 cross-free tight family，仍然 span 全部 rank

对于 crossing `U,W in T`，intersection 和 union 都 nonempty proper。fractional directed outcut submodularity 给

\[
2k=h(U)+h(W)\ge h(U\cap W)+h(U\cup W)\ge2k.
\]

故 intersection 和 union 也在 `T`。signed normals 满足 exact modular identity

\[
n_U+n_W=n_{U\cap W}+n_{U\cup W}.
\]

设 `L=span{n_U}`，其维数 `r=m-1`。在 cone `C=cone{n_U}` 的 relative interior 选 `w`，并让它避开由所有 rank `<r` 的 tight-normal subsets 张成的 finitely many proper subspaces。这样的 `w` 存在，因为 `span C=L`，而 finite proper subspaces 不覆盖 `C` 的 relative interior。

在所有 nonnegative representations

\[
w=\sum_{U\in\mathcal T}\lambda_U n_U
\]

中，最小化

\[
\Phi(\lambda)=\sum_U\lambda_U|U|\,|V-U|.
\]

minimum attained：所有 coefficient 的 potential factors strictly positive，因此有界 sublevel set compact。若 positive support 包含 crossing `U,W`，令 `alpha=min(lambda_U,lambda_W)>0`，从两者各移去 `alpha`，给 intersection 和 union 各加 `alpha`。representation 不变；potential 降低

\[
2\alpha|U-W|\,|W-U|>0.
\]

矛盾。因此 positive support `F` cross-free。由 `w` 的 generic choice，它的 normals span `L`，rank 仍为 `m-1`。

注意这里保留的是 **linear span**。不能因此宣称新 family 与全部 tight cuts 具有相同 conic hull，或同样 source-free。

### 3.3 Cross-free family 的 laminar tree / atom quotient

选 root vertex `r0`。把 `F` 中含 `r0` 的 shore 替换为 complement，并相应把其 normal 乘 `-1`；去除 duplicate shores。cross-free 变为 laminar family `L0`，normals rank 与 `n_U·1=0` 性质保持。

用节点集合 `L0 union {V}` 建 rooted inclusion tree `T0`：每个 laminar shore 的 parent 是最小 proper containing shore，若无则 parent 是 `V`。每个 original vertex `v` 赋予最小 containing shore node，若不属于任何 shore则赋给 root `V`。节点可能没有 assigned vertices；这不影响 argument。

把 every physical `K` arc `u->v` 替换为从 assignment node of `u` 到 assignment node of `v` 的一条有身份 quotient arc，得到 directed multigraph `QK`。对 tree edge对应的 shore，cut-normal column 正是该 quotient arc 在 tree fundamental cut 上的 signed incidence。

Tree fundamental cuts 是 node divergence space 的一个 basis。因此 cut-normal matrix `M` 与 quotient node-incidence matrix `B` 通过可逆 row transformation 对应，给

\[
\operatorname{rank}B=\operatorname{rank}M=m-1,
\qquad B\mathbf1=0.
\]

`QK` 是 positive Eulerian directed multigraph。若它有 loop，对应 column为0，则该 coordinate unit vector在 `ker M`；但 `ker M=span{1}` 且 `m>=2`，矛盾。所以无 quotient loop。

每个 nontrivial weak component Eulerian，因而各含 cycle。incidence nullity

\[
m-\operatorname{rank}B=1
\]

说明只有一个 nontrivial component，且其 undirected cycle-space dimension恰为1。设该 component 有 `n` vertices，则 `m=n`；每个 vertex positive indegree与outdegree至少1，而两种degree总和分别等于`m=n`，故每个 node恰有一入一出。

所以 **quotient support 是一个 directed circuit**。

### 3.4 从 quotient circuit 拉回 physical vertices

每个 quotient node只有一条 entering `K` arc和一条 leaving `K` arc。故该 node中每个 original vertex至多一条 entering arc和一条 leaving arc。原 physical support每个vertex的in/outdegree都至多1。

沿 quotient circuit依次查看 entering arc的physical head与下一条 leaving arc的physical tail：若每个node两者为同一vertex，全部support是one directed physical circuit。否则在不同vertex的node处断开，得到若干vertex-disjoint directed physical paths。

不能同时存在一个physical circuit和额外paths：任一physical circuit在quotient中已必须遍历唯一quotient circuit的全部edges。

这完成必要方向：

\[
\boxed{\text{adjacent global feasible orientations}
\Longrightarrow K\text{ is one directed circuit or vertex-disjoint directed paths}.}
\]

特别地，该结论对 Proposition 1 的 minimum separating descendant 自动成立，因为 Section 2 已给其 segment 是 full global polytope的一条face edge。

## 4. 为什么不能引用“充分方向”

给一个不依赖程序的 `k=2` simple-graph control。令 `G=K_7`，vertices为`0,...,6`，采用circulant regular tournament `i->i+1,i+2,i+3 (mod 7)`。每vertex indegree和outdegree均为3，因此任何size `s` cut有

\[
d^+(X)=3s-\binom{s}{2}=\frac{s(7-s)}2\ge3.
\]

其中 `0->1->4->0` 是一个directed triangle。翻转该triangle的任何subset，对每个cut的outdegree降低至多1：triangle穿过一个cut时恰一条arc进入、一条arc离开。故全部`2^3` orientations仍为2-arc-strong。

固定其他edges后得到完整3-cube。原orientation与full triangle reversal的orientation位于cube两端，差异support是one directed circuit，却不是polytope adjacent。

因此支持分类在本项目只作为 **necessary condition**。这个control没有否定Section 3，亦未否定主connectivity问题。

## 5. Primary-source scope record

- Edmonds, J.; Giles, R. (1977), *A Min-Max Relation for Submodular Functions on Graphs*, Annals of Discrete Mathematics 1, pp.185--204. Publisher primary record and DOI: [Elsevier original chapter](https://doi.org/10.1016/S0167-5060(08)70734-9). 本轮publisher页面确认bibliography；未能读到原paper全部pages，故不声称原paper theorem numbering。
- Schrijver, *Combinatorial Optimization*, Ch.60: Theorem60.1 gives crossing-submodular signed cut-difference system box-TDI; Corollary60.1a gives integer-RHS box-integrality. Ch.61 equation(61.36) explicitly gives global physical reversal formulation. 这些是本轮实际核对的scope anchors。本文数学使用Section2的具体mapping，避免把signed `p_J`本身当standalone crossing-submodular demand。
- 原书Ch.61.4d确有无year/no bibliography key的 Lovász adjacency-result描述。本轮没有定位可靠原始Lovász paper；因此不为它虚构publication/year。实际核读的是Schrijver原书文本的大学课程托管副本：[book primary text, university mirror](https://www.lamsade.dauphine.fr/~cornaz/Enseignement/M2_MODO/DATA/B5.PDF)。书正式作者页面：[Schrijver book corrections](https://homepages.cwi.nl/~lex/co/)。版本页码有差异；托管副本printed page1048，而作者2002目录给Ch.61起始page1038，不能混用page numbers。

上面没有长篇转录。Section1--4为本轮独立proof与control，外部adjacency结果不再是logical dependency。

## 6. 对 source-guard bridge 的精确启示与剩余缺口

Section3提供一族 common-tight cross-free rows，其 **linear rank** 足以强迫difference support。它没有保存all-tight row signs：一个edge在新family中没有negative action，却仍可能被omitted actual-tight row阻塞。这与修订档的source-resurrection gap一致。

可以把guard问题压成明确矩阵要求：若 retained tight-normal matrix为`M_F`，省略tight cut row为`n_Z`，只有当`n_Z`属于retained **nonnegative conic hull**时，才可从retained feasibility推出该guard row；仅有`n_Z in rowspan(M_F)`不够。Section3的generic objective uncross只保证rowspan。

对于minimum-descendant midpoint，all remaining coordinates同步且`ker M_F=span{1}`。但previously-fixed `J` 的columns没有被该kernel statement控制；service edge能在quotient cycle以外连接laminar atoms，也可能被omitted guard rows阻塞。要从support theorem到H1，仍需证明允许temporarily unfix `J` 的legal escape，并检查every actual-tight guard。

**可攻的新精确子问题。** 不是再证明quotient cycle存在，而是：能否在uncross过程中加入一个有限edge-sign guard certificate，使必要的`J` service source在被选cross-free rows中成立时也在full actual-tight系统中成立？目前本文未证明该guard-preserving uncrossing。不能把matrix rank closure冒充guard closure。

## 7. NEW: Empty-node guard charge 闭合 cross-free source-free exclusion

本节与本轮 `research_atom_budget.md` 的 AB3 结合，解决此前empty signed-tree node的计量缺口。适用域严格为 **initial true-critical residual system**：`p(X)=k-q(X)`、`q(X)=min{R(X),S(A-X)}`、every proper shore的`mu>=1`，以及actual-tight partition/copartition exclusion。允许全部内部physical edges；未减去ancestral `J`。

### Proposition 7 (cross-free actual-tight source-free family 不存在)

取非空distinct proper actual-tight rows `F={X_1,...,X_t}`，cross-free。假设不存在跨membership atoms的current internal arc，其对全部rows的reversal signs非负且至少一正。则这些假设不可能同时成立。

**Step 1: atom budget.** 记`n`为非空Boolean atoms个数、`M`为跨atoms physical edges数。对于current跨atom arc `g`，记`nu(g)`为它leaves的rows数。source-free给`nu(g)>=1`。因此

\[
M+\sigma=\sum_i d_D^+(X_i)=tk-Q,
\qquad
\sigma:=\sum_g(\nu(g)-1),\quad Q:=\sum_iq(X_i).
\]

收缩atoms与outside root，root degree为`2k+1`，every其他atom degree至少`2k+1`，故

\[
M\ge\left\lceil\frac{(n-1)(2k+1)}2\right\rceil.
\]

于是

\[
Q+\sigma\le(t-n+1)k-\left\lceil\frac{n-1}2\right\rceil.
\tag{AB3}
\]

**Step 2: signed-tree representation.** 选一个`A`内root vertex，把含root的shores complement，使family laminar。`mu>=1`禁止actual-tight complementary pair，所以不会出现duplicate split。其inclusion tree有`t+1`个nodes，非空node regions恰为`n`个membership atoms。记empty nodes个数为`e`，故

\[
t-n+1=e.
\]

保留每条tree edge对应的**原actual-tight row**身份。对empty node`v`，删除它后incident branches的ground-set regions `U_i`给`A`的一个partition，所有`U_i`非空。对应row恰为`U_i`或`A-U_i`。

记normal branch index set`I_v={i:actual row=U_i}`，co-branch index set`J_v={i:actual row=A-U_i}`。若`I_v`或`J_v`为空，则所有incident actual rows形成tight partition或tight copartition，已被initial true-critical skew排除。因此每个empty node是mixed，并且

\[
U_v:=\bigcup_{i\in I_v}U_i
\]

是nonempty proper subset of`A`。

**Step 3: q packing（每条row只在一个tree endpoint付款）.** 对disjoint sets，`q` subadditive。可直接写

\[
q(X)=R(X)-\big(R(X)+S(X)-S(A)\big)_+;
\]

`R,S`为nonnegative modular functions，positive-part threshold使

\[
q\left(\bigcup_iU_i\right)\le\sum_iq(U_i)
\quad\text{for pairwise disjoint }U_i.
\]

故`q(U_v)<=sum_{i in I_v}q(U_i)`。关键是不重复花费：同一tree edge在两个endpoints的branch shores互为complement；其固定actual row只能等于其中一个branch shore。因此该row最多被一个empty endpoint作为normal branch收入`I_v`。结合`q>=0`，得到

\[
\boxed{\sum_{v\text{ empty}}q(U_v)\le Q.}
\tag{QP}
\]

这里没有把`q(A-X)`偷换为`q(X)`；被计量的每个quantity始终是该edge的**原actual row**的`q`。

**Step 4: 多负号 surcharge支付empty nodes.** 若current internal arc`g` leaves`U_v`，其tree path从某normal branch进入`v`、从某co-branch离开`v`。它在这两条consecutive tree edges上都leaves对应actual row，故是two consecutive negative reversal signs。

一个tree path若总共有`nu(g)`条negative-sign edges，其相邻negative-edge pairs总数至多`nu(g)-1`。把每个empty `v`中`g` leaves`U_v`的事件向该pair收费，charges不重复。因此

\[
\sigma\ge\sum_{v\text{ empty}}d_D^+(U_v)
\ge\sum_v(k-q(U_v))
\ge ek-Q.
\tag{EC}
\]

最后一步用(QP)，中间一步用完整initial residual legality，且`U_v`已证明nonempty proper。所以

\[
Q+\sigma\ge ek.
\]

而AB3给`Q+sigma<=ek-ceil((n-1)/2)`。非空proper row family必有`n>=2`，产生严格矛盾。证毕。

**What changed.** Empty nodes无须用minimality全部删掉；mixed empty节点允许存在，但其two-negative consecutive passage必花费至少`k-q(U_v)`，每条row的`q`预算最多支付一个empty端点。该global charge闭合了all-`e`，不是只处理one-empty-node。

**Scope limit.** 这里`q>=0`与terminal endpoint formula不可丢；arbitrary signed descendant `p_J`中的ancestral contributions既改变row-demand，也改变多负号budget。因此本节没有复活历史FALSE strengthened RCD。

## 8. NEW: Initial fixed-root fiber 没有 wholly frozen internal orientation

### Proposition 8 (NO-FROZEN-INTERNAL)

在initial true-critical setting，若`|A|>=2`，则任何合法完整internal orientation都有至少一条legal internal single-physical-edge reversal，保持outside signature fixed。等价地，至少一条internal current arc可删除而保持相应root-contracted digraph `k`-arc-strong。

**Proof.** 把outside`B`收缩为root`r`，保留boundary physical edge identities。true-critical endpoint formula给：root-contracted orientation的`k`-arc-strong cut system与fixed-outside initial residual system完全等价。root degree为`2k+1`，所有quotient nontrivial undirected cuts至少`2k+1`。

若every internal current arc不可reverse，则every such arc`g` leaves某个global`k`-tight shore in the root-contracted digraph。理由是single physical reversal对每cut只改变`-1,0,+1`，当前integer slack至少1的row不会在一步后违反；唯一blockers就是当前tight且该arc leaves的rows。删除当前arc与反转它具有相同的危险cut集合，因此两种legality在此等价。收集一族tight shores覆盖全部internal arcs。

**这里可保留cover的uncrossing是确定的，不是generic source normalization假设。** 若global tight shores`X,Y` crossing，directed cut submodularity与all-cut legality给

\[
d^+(X\cap Y)=d^+(X\cup Y)=k,
\]

以及`X-Y`与`Y-X`之间两个方向都没有current arcs。把`X,Y`替换为intersection/union，任何原来被某row covered而新rows均不cover的arc必须从一个difference atom指向另一个，已不存在。所以全部current internal arc cover被保留。

用strictly decreasing potential`sum |X||V'-X|`得到cross-free tight cut cover。删除没有internal coverage的root-only / whole-`A` shore，并取inclusion-minimal cover。每row仍actual-tight，且有一条private covered internal physical arc。把global shores追踪到`A`：无rootshore`Y`给residual actual row`Y`，有rootshore`{r} union Y`也给residual actual row`Y`。traces cross-free，补集仅用于tree representation，不改变actual row身份。

覆盖every internal arc蕴含Section7所需source-free。因此Proposition7排除该cover，矛盾。

最后`|A|>=2`确有internal edges：

\[
2|E(H)|+(2k+1)=\sum_{v\in A}d_G(v)\ge|A|(2k+1).
\]

故不能用empty internal edge set规避命题。证毕。

**与H1的关系。** 本命题排除full initial fiber中的isolated state。它没有证明fiber connected：两个有多点的components仍可能存在。对于minimum separating descendant，它仅保证endpoint处至少有一条当前固定在`J`中的legal service edge；尚需证明service过程中能到达并跨过不同original components。

### 8.1 为什么单独Mader minimal-core theorem不够

本轮primary检索确认：Mader theorem保证任意minimally `k`-arc-connected digraph存在indegree与outdegree都为`k`的vertex。原作者论文的明确陈述可见 [Durand de Gevigney--Szigeti, On minimally 2-T-connected directed graphs](https://pagesperso.g-scop.grenoble-inp.fr/~szigetiz/articles/min_2-T-con_DAM.pdf), Theorem1；DOI [10.1016/j.dam.2018.04.003](https://doi.org/10.1016/j.dam.2018.04.003)。

若hypothetical frozen internal orientation删掉root incident arcs得到minimally`k`-strong core，该balanced vertex可能正是root（删去一条root arc后root degree可降到`2k`）。因此whole-global removable-arc conclusion不能直接推出internal removable arc。Section8使用的是terminal cut cover与empty-node charge，绕开这个root exception。

另有2025 primary论文 [Fan--Hu--Yang--Zhao, On vertices of outdegree k in minimally k-arc-connected digraphs](https://doi.org/10.1016/j.dam.2024.11.009)，讨论simple digraph与tree representation中的empty nodes；其simple scope不能未经证明移植到本项目physical multigraph。本文Section7--8未依赖该论文。

### 8.2 Minimal private cover 的独立empty-node几何

这不是Section7所需假设，但可复用作结构lemma：在cross-free inclusion-minimal internal arc cover中，每row有private internal witness。对signed tree empty node，若只有一条positive-direction outgoing edge，则这条edge的private witness经过该empty node时必须从另一incident edge进入；所有其他edges都positive-direction incoming，造成第二条covered row，矛盾。唯一incoming edge情形对称。

故empty tree nodes满足`indegree>=2`且`outdegree>=2`，特别degree至少4。若非空node regions数为`n`、empty nodes为`e`，tree degree counting还给`n>=2e+2`。一般mixed degree>=4节点并不能单凭minimality消除；Section7的预算charge才排除了它们与initial terminal feasibility同时实现的可能。

## 9. NEW: Minimum-pair 动态桥的可闭合弱形式

Section8只保证some legal launch，不能将它当作component escape。这里固定两个不同original components`C_1,C_2`，在`C_1 x C_2`中取Hamming distance最小的pair`(R,Q)`，记distance`m`、difference support`K`、common physical edge set`J`。固定outside signature不变。Section1--3仍给该minimum pair的path/circuit support与two-state fixed-J descendant。

### Proposition 9.1 (circuit case 的同步launch与整条word lift)

若`K`按`R`方向是one directed physical circuit，则对于**任意**`J` orientation`F`：把`F`分别与两个相反的`K` circuit orientations拼接所得`D_F^0,D_F^1`，每个residual/global cut的outdegree相同。因此二者同时可行，并且每条`J` physical edge在二者中的single-flip legality相同。

特别地，对任何仅翻`J`的legal word`w`从`R`出发，完全相同的physical word从`Q`出发也legal；每个prefix给一个新的pair`(R_i,Q_i)`，仍有

\[
R_i\in C_1,\qquad Q_i\in C_2,\qquad
\operatorname{diff}(R_i,Q_i)=K,\qquad d_H(R_i,Q_i)=m.
\]

**Proof.** directed circuit对every shore有equal numbers of entering与leaving physical edges。全cycle reversal故保持every cutout value。`J` edge在两端current direction相同，翻转对每cut改变也相同，因此所有prefix一步一步同步lift。证毕。

**Minimum-origin consequence.** 在该同步`J`-reachable orbit的every pair、every`K` edge都非法：否则在一端翻这条mismatch edge会得到distance`m-1`的inter-component pair，反于minimum choice。Section8又给每个pair至少一条legal`J` edge，所以该orbit始终有同步legal launches。

这给一个精确必要obstruction：**两个isomorphic circuit sheets，全部common-edge words可同步执行，而整个paired orbit没有first-K-progress。** 它仍可能作为有限`J` flip graph中的非平凡component存在；没有论证排除这种closed orbit。

### Proposition 9.2 (path case 的one-sided guards完全由端点imbalance定位)

对一般directed path collection support，定义

\[
b_K(v)=d_K^+(v)-d_K^-(v),\qquad b_K(X)=\sum_{v\in X}b_K(v).
\]

每条path的start贡献`+1`、end贡献`-1`，其他vertices贡献0。于是

\[
s_Q(X)=s_R(X)-b_K(X).
\tag{PD}
\]

若common current edge`g`在`R` legal而在`Q` illegal，则存在一个`g`-leaving actual-tight shore`X` at`Q`，满足

\[
s_Q(X)=0,
\qquad s_R(X)=b_K(X)\ge1.
\]

该blocker含有比path ends更多的path starts。反过来，若`g`在`Q` legal而在`R` illegal，则其某个`R`-tight negative blocker满足`b_K(X)<=-1`，即path ends较多。

因此common-tight rows（`b_K(X)=0`）不会造成one-sided launch asymmetry。若`K`是单条directed physical path，asymmetric guards在较松端的slack恰为1，并且严格分离该path的两个endpoints。Circuit case则`b_K=0` everywhere，恢复Proposition9.1。

**Scope.** 这些是minimum pair endpoints及其同步common-edge orbit的性质。未推出arbitrary one-sided launch存在可行rejoin word，更未把所有path collections压成single path。

## 10. NEW: Optimal deletion completion 可去掉所有ancestral directed cycles

### Proposition 10 (minimum service support is a DAG)

固定current orientation`R`，一条待删除physical edge`e`，以及任意必须保持方向的其他physical set`K-e`。假设存在orientation of`J`使删除`e`后完整cut system可行；这一existence是明确hypothesis，不由generic antipodality推出。

在全部这种completions中，按strictly positive physical costs`c_g>0`，最小化changed`J` copies成本。令optimal completion为`F`，令`T subset J`为相对`R`改变方向的physical edges，按`R`方向看`T`。

则`T`不含directed physical circuit，即difference digraph为DAG。

**Proof.** 若`T`含`R`-directed circuit`C`，在`F`中它全部反向，因此仍为directed circuit。把`C`在`F`中反转回`R`方向，every cutout value保持相同，所有fixed coordinates与deleted-edge状态保持，故仍是completion；成本严格减少`sum_{g in C}c_g`，矛盾。证毕。

这允许把optimal service support decomposition看成若干有向paths/branching DAG上的degree transfer，而不携带可消去的Eulerian cycles。它不推出monotone serialization：即便difference support是directed path，两个feasible endpoints之间也可能需要extra detours。当前最小服务completion是否在fixed-`K` common-edge reachable orbit中，仍是temporal necessity问题。

### 10.1 下一步精确弱目标

Cycle case可把未解接口写为：对于每个minimum inter-component pair的directed-circuit support`K`，Proposition9.1的paired`J`-reachable component必含某个state，使至少一条`K` arc可删除。若成立，则first-K-progress将minimum distance降1，直接矛盾。

这个目标没有假设constant buffer cost/width。已知terminal families的service DAG长度与occupied buffer copies可以任意大，故可行的证明必须允许长common-edge words。Proposition10只负责消去optimal completion里的cycles，不能提供reachability，也不能给该弱目标未经证明的completion existence。

## 11. SAFE-STEM audit 与一个对称的 SAFE-SINK theorem

本节审计 `research_dynamic_bridge.md` Section3 的充分条件，并给出其deficit对称版本。

### 11.1 Forward SAFE-STEM 审计通过

给定current orientation`D`，directed physical circuit`C`、directed simple stem`P=c->...->w`，`w in C`，stem内部vertices不在`C`，physical edge sets disjoint。若every initial tight shore`X`满足

\[
c\in X\Longrightarrow V(P)\cup V(C)\subseteq X,
\]

则从`c`开始按forward edge order开`P`，从`w`开始按forward circuit order翻`C`，逆序关`P`，所有prefix legal。每opening / circuit prefix净cut change是`1[frontier in X]-1[c in X]`。初始tight cuts均不损，其他cuts初始integer slack至少1且净损至多1。closing重现opening cut values，最终只反转`C`。

条件检查必须使用**全部initial actual-tight rows**，而非仅selected core。proof对later新tight cuts无需逐个假设：每个prefix已直接对全部cuts证明值>=demand。

### Proposition 11.2 (SAFE-SINK / backward deficit stem)

令`P=(w=v_0->v_1->...->v_l=c)`是current`D`中的directed simple path，从cycle vertex`w`到buffer vertex`c`；内部vertices不在`C`，physical edges与`C` disjoint，允许length0。假设every initial tight shore`X`满足

\[
X\cap(V(P)\cup V(C))\ne\varnothing\Longrightarrow c\in X.
\tag{SAFE-SINK}
\]

则以下balanced physical word legal，最终只反转`C`：

1. **逆序开P**：先翻最靠近`c`的edge，按`c`往`w`的索引逆序移动deficit；
2. **逆序走C**：从当前cycle中进入`w`的edge开始，按cycle edge索引逆序依次翻一整圈；
3. **正序关P**：按原`w`往`c`索引顺序恢复stem copies。

**Proof.** 逆序opening到frontier`v_i`时，已翻的是原directed suffix`v_i->...->c`，所以netcut change为

\[
1[c\in X]-1[v_i\in X].
\]

全stem开满后frontier是`w`。逆序翻cycle时，若当前deficit在`u`，下一条current baseline cycle arc是`z->u`；反转它给`+1[u in X]-1[z in X]`，deficit移到`z`，总变化仍为`1[c in X]-1[z in X]`。整圈后返回`w`；正序closing同样将deficit沿stem送回`c`。

每个possible deficit frontier都在`P union C`。SAFE-SINK保证初始tight cuts不损，其他cuts最多损1，全部prefix合法。copy identity由edge-disjointness与所选stem physical labels保留。证毕。

**顺序不可省略。** 只假设SAFE-SINK却从`w`正序open长stem不充分：initial tight cut可含`w,c`却遗漏中间vertex，第一次prefix便失1。必须使用上面的reverse opening。

### 11.3 两个可检查的membership reachability接口

定义`cl_D(c)=intersection{X tight:c in X}`，若无则为`A`。Forward stem要求`C subset cl_D(c)`，且在`D[cl_D(c)]`中有从`c`到`C`的directed path。

定义

\[
\operatorname{down}_D(c)=\{v:\forall X\in\mathcal T(D),\ v\in X\Rightarrow c\in X\}.
\]

Backward sink要求`C subset down_D(c)`，且在`D[down_D(c)]`中有从`C`到`c`的directed path。它的candidate endpoint set是

\[
V_C=\bigcap\{X\in\mathcal T(D):X\cap V(C)\ne\varnothing\}.
\]

Forward candidate set则是

\[
U_C=A-\bigcup\{X\in\mathcal T(D):V(C)\not\subseteq X\}.
\]

两者是tight membership的common lower bound与common upper bound；不能只要求one family中的相对包含，也不能未经证明假设任一set非空。

## 12. Exact genuine control：initial U_C 可以为空，仍一条J launch后SAFE

此例只反驳“terminal antipodal cycle在当前state必有forward-safe起点”的shortcut。它不是minimum-component-separating counterexample，因为下面给显式reconnecting word。

取`k=2`，root `r`，`A={w,y,c}`。所有parallel copies有身份。

- Boundary：`r->c`三条copies，`w->r`一条，`y->r`一条，总boundary5。
- Internal `K`：`e:w->y`与`f:y->w`各一条，构成directed physical two-cycle。
- Internal `J`：`c->w,c->y`各一条，`w->c,y->c`各两条。选一条`w->c` copy为`g`。

### 12.1 无向与cut certificate

Vertex degrees为`d(r)=5,d(w)=d(y)=6,d(c)=9`。无向两vertex cuts依次为

\[
|\delta(rw)|=|\delta(ry)|=9,\quad
|\delta(rc)|=|\delta(wy)|=8,\quad
|\delta(wc)|=|\delta(yc)|=9.
\]

三vertex cuts等于互补singleton cuts，故`lambda=5`，`A`是真critical shore。

Root-contracted current directed outdegrees为`d^+(r)=3,d^+(w)=d^+(y)=4,d^+(c)=2`。两vertex outgoing cuts为`6,6,2,6,3,3`，按`rw,ry,rc,wy,wc,yc`排列；互补singletons的三vertex outgoing值为`2,2,2,7`。因此current orientation为2-arc-strong。

Boundary signature为`R(w)=R(y)=1,R(c)=0,S(c)=3,S(w)=S(y)=0`。所有proper residual rows的exact initial slack为

| X | q(X) | d_H^+(X) | p(X) | slack |
|---|---:|---:|---:|---:|
| {w} | 1 | 3 | 1 | 2 |
| {y} | 1 | 3 | 1 | 2 |
| {c} | 0 | 2 | 2 | 0 |
| {w,y} | 2 | 4 | 0 | 4 |
| {w,c} | 0 | 2 | 2 | 0 |
| {y,c} | 0 | 2 | 2 | 0 |

所以全部actual-tight rows恰为`{c},{w,c},{y,c}`。三者均不包含整个`C={w,y}`，且其union为`A`；于是

\[
\boxed{U_C=\varnothing.}
\]

与此同时touches`C`的tight rows仅`{w,c},{y,c}`，故`V_C={c}`。`P=w->c`满足SAFE-SINK；前后opening顺序因length1相同。

### 12.2 Antipodality与显式reconnection

固定`J`时，单翻`e`破坏tight row`{w,c}`，单翻`f`破坏tight row`{y,c}`；两条全翻保持全部cut values。所以该frozen-`J` descendant恰有两个antipodal endpoints，且support是真directed circuit。

合法word为

\[
\boxed{g,\ f,\ e,\ g.}
\]

最后一项恢复同一physical copy`g`，不得误翻原有的另一条`c->w` copy。前三prefix的outdegree变化分别为

\[
\chi_c-\chi_w,\qquad
\chi_c-\chi_y,\qquad
\chi_c-\chi_w.
\]

其在三条initial tight rows上的变化分别为`(1,0,1)`、`(1,1,0)`、`(1,0,1)`；其他rows初始slack至少2而净变化最多损1。最后prefix为0。因此每一步legal，最终只反转`C`。

在第一步`g`后，唯一actual-tight row是`{w,c}`。此时`y in U_C`，且可用length0 forward SAFE-STEM从`y`沿`f,e`翻cycle。所以这个control也明确说明：**initial U_C为空，不排除一条legal J launch后进入SAFE-STEM state**。

### 12.3 当前necessity仍缺什么

Minimum separating cycle pair的同步`J` orbit必须排除所有可达SAFE-STEM与SAFE-SINK states；上述connected control并不满足这个全orbit禁令。欲证明main connectivity，仍需从terminal geometry与minimum-origin证明该orbit不能一直避开两种可序列化的buffer configurations，或提供更一般service network。本文没有以U/V候选集非空代替该proof。

## 13. NEW: 任意integer crossing-supermodular cut demand 的primal integrality

### Proposition 13 (general orientation-box integrality)

令`H=(A,E)` finite loopless physical multigraph，`f`定义于every nonempty proper subset of`A`，integer-valued，并对crossing pairs满足

\[
f(X)+f(Y)\le f(X\cap Y)+f(X\cup Y).
\]

用任意reference orientation与physical reversal coordinates描述cutout feasibility box

\[
\mathcal O_f=\{x\in[0,1]^E:d_x^+(X)\ge f(X)
\ \forall\varnothing\ne X\subsetneq A\}.
\]

则`O_f`每个vertex integer。`f>=0`不是必要hypothesis；complementary tight rows可以出现，proof中只删除它们的linear redundancy。

**Proof.** 对任意vertex`z`，记`K`为未位于active box bound的coordinates，其他coordinates皆integer 0/1。tight cut normals限制到`K`后rank`|K|`。

若`X,Y` crossing且tight，fractional directed outcut submodularity及demand supermodularity给

\[
d_z^+(X)+d_z^+(Y)=f(X)+f(Y)
\le f(X\cap Y)+f(X\cup Y)
\le d_z^+(X\cap Y)+d_z^+(X\cup Y)
\le d_z^+(X)+d_z^+(Y).
\]

全部相等，intersection/union同样tight，两个difference petals间total directed weight为0。restricted signed normals仍满足`n_X+n_Y=n_I+n_U`。

因此Section3.2的generic-cone objective与minimum positive potential uncrossing给cross-free tight normals，仍span fullrank`|K|`。允许`X,A-X`都tight；它们的restricted normals互为负，在线性span层保留一条即可，不必保持原cone representation。root-complement把这些splits转成unique laminar family，signed row changes不影响TU。

Section2.1的laminar tree-incidence determinant argument证明其cut matrix TU，即使tree nodes为空也成立。选fullrank square active submatrix，det±1。RHS由integer `f`、reference integer cut值及fixed 0/1 coordinates组成，所以`z_K`integer。证明完成。

**适用域区别。** 本命题是primal vertex integrality，不声称该特定inequality representation的integer dual optimum / box-TDI。minimum-cost primal=LP value可用integrality；LP dual strong duality本身成立；要进一步要求dual y integer，仍需另行TDI theorem。

### 13.1 Initial strict augmentation corollary

在initial true-critical系统，`q` submodular，所以

\[
f(X)=p(X)+1=(k+1)-q(X)
\]

integer crossing-supermodular（事实上every proper row均`>=1`）。如果有**独立的fractional strict-feasibility proof**，即存在physical fractional orientation满足`d_x^+(X)>=p(X)+1`全部proper rows，则Proposition13给一个integer strict orientation`D_*`：

\[
\boxed{s_{D_*}(X)\ge1\quad\text{for every nonempty proper }X\subset A.}
\]

这里fractional existence是明确premise；本节不把`mu>=2`单独当作未经证明的existence theorem。若另一个proof已由`mu>=2`得到fractional strict feasibility，即可组合，无需调用外部Frank partition min-max。

### 13.2 Strict orientation 的Eulerian class已可serialize

若一个合法initial orientation`D_*`所有proper residual cut slack至少1，则任意current directed physical circuit可按其forward edge order翻完整圈；每prefix净cut变化为`chi_frontier-chi_start`，最多损1，故legal；整圈后所有cut slack保持原值，仍strict。

因此任何两条**相同internal outdegree vector**的strict orientations可通过legal physical flips相连：按第一条方向，其difference digraph在每vertex balanced，分解为edge-disjoint directed physical circuits；逐圈serialize，完整每圈后仍strict，最终达到另一条。

同一proof允许从strict`D_*`逐边反转任意单条current directed physical path，得到一个合法终态（未必仍strict）。这不证明任意初始orientation都可到达strict state，也不证明不同degree vectors的strict states可通过保持strict的macro moves连接。故strict-state existence仍不能单独填上H1。

## 14. NEW: 所有strict orientations已属于同一个原始flip component

本节加强13.2：不同internal outdegree vectors的strict states也能连接。中间physical-flip states允许只有原始`p` feasibility；每个完整path/circuit macro后的state重新strict。仍不证明任意non-strict state能到达这一component。

### 14.1 Crossing-supermodular degree polytope 的edge directions

设`n=|A|`，integer crossing-supermodular `g`定义于nonempty proper shores，`m`为integer。考虑非空bounded polytope

\[
B_g=\{b\in\mathbb R^A:b(A)=m,\ b(X)\ge g(X)
\quad\forall\varnothing\ne X\subsetneq A\}.
\]

其boundedness实际上由singleton lower bounds和total equality自动得到。则：

1. 每个vertex integer；
2. 每条polytope edge平行于某个`chi_u-chi_v`；
3. 全部integer points在feasible unit transfers `b -> b-chi_u+chi_v`下相连。

**Active-row proof of1–2.** 对任何face的relative interior point，crossing tight sets `X,Y`满足

\[
b(X)+b(Y)=b(X\cap Y)+b(X\cup Y),
\]

故`g` supermodularity与feasibility使intersection/union同样tight。Section3的generic-cone/minimum-potential uncrossing在quotient by total row中适用，给cross-free family，span全部active proper-row normals。Complementary rows在quotient中互为负，可删去linear redundancy。以一个root vertex作complement，使proper rows成为laminar family，并加入total row`A`。

从这个laminar family提取independent proper rows，始终保留`A`。对每个laminar tree node`X`，其residual region是`X`去掉所有selected maximal proper children。所有regions分割`A`；row indicators与region indicators通过integer triangular row operations互相生成。因此row rank恰为nonempty regions数。

在vertex处，含total row的active rank为`n`，所以有`n`个nonempty regions；它们全部singleton。每个singleton degree是integer tight RHS的整数线性组合，因此vertex integer。

在edge处，含total row的active rank为`n-1`。所选laminar rows有`n-1`个nonempty regions；恰好一个region有两个vertices`u,v`，其余singleton。所有row-preserving motions仅在该pair内转移相反的degree，故edge direction为`chi_u-chi_v`。证明无需orientation adjacency的physical-path assertion。

**Integer unit-connectivity proof of3.** 取一个generic linear objective`c`，使它在所有vertices取不同值，并且`c_u!=c_v`全部pairs。给定任意integer point`b`，若非全局minimum，存在locally feasible improving unit-transfer direction：若其minimum face有positive dimension，选该face一条edge的improving direction；若`b`是vertex，选一个improving incident edge。前者因`b`在face relative interior而locally feasible，后者是polytope linear optimization的基本edge property。

将方向scale为`z=chi_u-chi_v`。每个proper subset row上的`z(X)`都在`{-1,0,1}`；locally feasible保证active rows不受损，inactive rows在integer point有integer slack至少1。因此完整的unit step`b+z`仍feasible。每步strictly降低`c`，bounded polytope内integer points有限，终止于同一个unique minimizing vertex。反向拼接把任意两个integer points连接。证毕。

### 14.2 Strict degree vectors 的exact realization

在initial system令

\[
f(X)=p(X)+1\ge1,\qquad
g(X)=i_H(X)+f(X),\qquad m=|E(H)|,
\]

其中`i_H(X)`为两端均在`X`的physical edge copies数。`i_H` supermodular、`f` crossing-supermodular，所以`g` crossing-supermodular。

每个orientation的vertex outdegree vector`b`满足

\[
d_H^+(X)=b(X)-i_H(X).
\]

因而strict orientation degree vectors正是`B_g`的integer points。Necessity直接。Sufficiency由physical edge-to-tail assignment给出：每条physical edge选择一个endpoint作tail，vertex`v`需要恰`b_v`条assigned edges。Total capacities为`m`，且每个`X`的capacity至少`i_H(X)`，正是该bipartite capacitated matching的Hall cut conditions。Integer matching/flow因此实现orientation；其cut values自动至少`f(X)`。这里physical parallel copies各有自己的edge-side node，身份不丢失。

### 14.3 一次strict degree transfer 可由合法path macro实现

设`D,E` strict，degree vectors分别为`b,b'=b-chi_s+chi_t`。把它们different physical copies按`D`方向组成`K`。则

\[
d_K^+(v)-d_K^-(v)=b_v-b'_v
=1[v=s]-1[v=t].
\]

所以`K`分解成一条directed simple `s->t` path和edge-disjoint directed circuits。逐边按forward order翻这条path；每prefix净cut变化为`chi_frontier-chi_s`，最多损1。`D`所有residual slacks至少1，故每个physical flip原始`p`-legal。

Path翻完整后degree vector恰为`b'`。Cut值只取决于degree vector，因此新state与`E`具有完全相同cut值，重新strict。若还需达到`E`本身，剩余difference Eulerian，按13.2逐圈serialize。

### Theorem 14 (unique strict component)

\[
\boxed{\text{若initial fiber含strict orientations，则全部strict orientations}\
\text{处于同一个original physical single-flip component。}}
\]

证明：14.1–14.2给strict degree vectors之间的feasible integer unit-transfer chain；14.3把每步转成original legal physical word，并在每个macro终点恢复strict。最后same-degree Eulerian routing达到指定target。

**剩余动态量词。** Strict augmentation existence加本定理，把`mu>=2`情形的connectivity进一步缩为：每个original component是否至少含一个strict state。本文尚未证明这一句。没有把degree-polytope unit connectivity当作non-strict physical-word connectivity：从non-strict state起，degree-transfer endpoint合法并不保证path prefixes合法。

## 15. NEW: Original initial fiber 在single path/circuit宏反转下连通

### Theorem 15 (macro connectivity, nonnegative demand scope)

令`p` integer crossing-supermodular且每个proper row `p(X)>=0`。假设feasible orientation fiber非空。定义一个macro move为：取当前定向中的一条directed simple physical path或一条directed physical circuit，一次反转其所有copies，要求macro终态合法；不要求其逐边prefix合法。则全部feasible orientations在这些macro moves下connected。

**Proof.** 取`g(X)=i_H(X)+p(X)`。Section14.1的degree-polytope proof完全不需要strictness，所以feasible integer degree vectors在unit transfers下connected。`p>=0`保证`b(X)>=g(X)>=i_H(X)`，故每个integer degree point有physical orientation realization。

一次feasible transfer`b'=b-chi_s+chi_t`，从任意current realization`D`选任意target realization`E`。其difference support按`D`方向具有imbalance`chi_s-chi_t`，因而含一条directed simple physical `s->t` path。整条path反转后degree vector恰为`b'`，cut值只由degree vector决定，故macro终态合法。继续沿degree chain；到目标degree后，Eulerian difference分解成directed circuits，逐个完整反转，每个macro保持全部cut值，最终达到目标orientation。证毕。

**Scope.** Initial true-critical `p=k-q>=0`符合；本定理不向arbitrary signed descendant `p_J`扩展。要使signed system具有orientation-realization characterization，需额外`b(X)>=i_H(X)`，相当于使用`max(p_J(X),0)`；该maximum一般不保留crossing-supermodularity，不能沿用本proof。

### 15.1 General connectivity剩余量词可只谈single path/circuit

Theorem15把main theorem降到下列充分statement：

\[
\text{每个legal-endpoint current directed physical path/circuit反转，}
\quad\text{其两端属于同一个single-flip component。}
\]

这允许physical single-flip word使用任意internal ancestral copies并反复恢复，不要求沿macro support monotone，也不要求constant width。无需先处理vertex-disjoint多路径collection；degree macro decomposition已将它们分成single path/circuit的合法终态序列。

### 15.2 Minimum跨component macro的精确first-progress限制

若original single-flip graph不连通，Theorem15给至少一个跨component macro。选physical length最小的一个，support记`K`，其起终态为`R,Q`，共同copies为`J`。

- 若`K`是directed circuit，任意`e in K`从`R`合法翻转都会得到`R'`；`R'`与`Q`只差`K-e`，而`K-e`在`R'`中是single directed path。它的两端已合法，length少1，仍跨components，矛盾。由对称性，`R,Q`的所有`K` edges都不可单翻。
- 若`K`是directed simple path，则该argument直接适用于**第一条和最后一条edge**：去掉endpoint edge仍是single directed path，故两端states这两条edge都不可单翻。`K`的interior edge若被单翻，剩余difference是两条disjoint paths，不能自动用minimum-macro length排除。

Circuit情形的任何同步legal `J` word保持两端cut值相同、`K` current方向完整、macro长度不变，因此其全部paired reachable states仍禁止每条`K` first flip。Path情形则没有全sheet同步性，且本节没有把interior K flips排除成一个未经证明的minimum-pair结论。

## 16. Component degree image：精确接口、gradient trap与extreme-point障碍

令`B_p`为15的initial feasible degree polytope。对original physical-flip component `C`定义

\[
S_C=\{b_D:D\in C\}\subseteq B_p\cap\mathbb Z^A.
\]

它在unit-transfer graph中connected，因为每个physical flip使degree变化`-chi_tail+chi_head`。本文**不**据此声称`S_C` convex、M-convex、face-saturated，或等于其convex hull中的全部integer points。

### 16.1 Node-potential local optimum也可需要暂时后退（initial minmu=1）

使用`research_terminal_debt.md` Section8的optimized `k=2,L=2` cycle control。`A={w,w1,y,y1,c}`，root boundary为`c->r`两条、`r->w`两条、`r->y`一条。Internal edges为

- `K`: `w->y,y->w`各一条；
- tip links：`w->w1,w1->w,y->y1,y1->y`各一条；
- non-tip links：`w1->c,y1->c`各一条，`c->w1,c->y1`各两条。

这是genuine initial true-critical `lambda=5` orientation。完整raw cut audit已保存为`data/node_potential_local_trap.json`（root independently audited）及`data/terminal_unbounded_debt_certificate.json`。

`{w},{w1},{y},{y1}`全部actual-tight，故除`c->w1,c->y1`之外，每条current internal arc都被一个singleton tight row阻止。所有含`c`的proper rows皆非tight，所以四条physical copies `c->w1`两条与`c->y1`两条全部legal，恰为全部legal internal flips。

取vertex potentials

\[
\omega_c=1,\quad\omega_{w1}=\omega_{y1}=0,
\quad\omega_w=2,\quad\omega_y=3,
\qquad F(D)=\sum_v\omega_v d_H^+(v).
\]

每条legal first flip使`F`减少1；当前`F=14`是strict local maximum。然而选一条physical `c->w1` copy，按顺序翻它、再翻`w1->w`，是已证明的safe opening path，其cut net变化依次`chi_w1-chi_c`、`chi_w-chi_c`。两个states均legal，`F`沿word为`14,13,15`。所以该local maximum并非其original component中的global maximum。

**Scope不能扩大。** 该control的`min mu=1`，不是`mu>=2`反例；它只否定generic initial node-gradient greedy progress。`mu>=2`专门的history/closure lemma仍可能成立。此例也未证明component degree image本身不M-convex：用history逃出单state local trap与set-level exchange closure是不同statement。

### 16.2 即使mu>=2，linear objective maximum也不会是strict state

若`D` strict，则`d_H^+(X)>=p(X)+1>=1`全部proper `X`，所以`D[H]` strongly connected，且每条current internal edge均可legal单翻。

给任何nonconstant node potential `omega`，取minimum-potential vertices集合`L`。Strong connectivity使有一条current arc从`L`到`A-L`，它的翻转strictly增加`F=omega dot b`，且原始`p`-legal。因此strict `D`不可能是其component中`F`的maximum，甚至不是local maximum；对minimum使用maximum-potential集合得到对称结论。

因此用component linear extreme orientation作为起点是合理的，但不能把“取objective最大state”直接当作“找到strict state”的潜在函数。Strict degree vectors位于`B_p`的relative interior；linear extrema自然在boundary。这个障碍不依赖16.1的`min mu=1`。

### 16.3 一个明确但仍未证的set-level unit-lift目标

下列property若在`mu>=2`的initial components成立，便足以完成该情形：

\[
b\in S_C,\quad b'=b-\chi_s+\chi_t\in B_p\cap\mathbb Z^A
\quad\Longrightarrow\quad b'\in S_C.
\tag{UNIT-IMAGE-CLOSURE}
\]

它要求component能到达某个`b'` realizer，不要求从指定`D`直接翻一条arc、不要求单调node objective，也不要求stay在`b,b'`两个degree vectors中。Theorem15中的integer degree graph connected立即给`S_C=B_p cap Z^A`。若strict augmentation存在，则每个`C`因此含strict degree vector；同一degree vector的任何realizer具有相同cut slacks，所以该realizer确为strict。Theorem14再将全部components合并。

当前没有UNIT-IMAGE-CLOSURE proof。Degree-polytope root directions只给legal-endpoint path macro，physical-prefix lifting恰是缺失动态桥。把该macro存在性改写成set closure并不会自动证明它；不过本property比“每个当前state有improving legal edge”允许更多history，且不会被16.1反驳。

## 17. Targeted degree routing与µ≥2当前更新

### 17.1 Degree unit transfers可以严格缩短目标L1距离（已证明）

对14.1中的integerdegreepolytopeB_g，任意两个integerpointsb,b′，有unittransferchain长度**恰** `||b−b′||₁/2`，每步都从当前surplusvertex转向deficitvertex。

Proof先给一个localcone接口。在integerb处，令R_b为全部locallyfeasibleunitrootdirections `−χ_u+χ_v`。任何feasibledifference d=b′−b都属于cone(R_b)。若不然，用finitepolyhedralcone separation取c，使c·r≥0对所有r∈R_b，而c·d<0。于是b不是linearobjective c的minimum，但不存在improvinglocallyfeasibleroot，矛盾如下：令F为包含b的smallestface，b∈relintF；若c在F上nonconstant，F的一条edge有improvingrootdirection，at b locallyfeasible；若c在F上constant，任一F-vertex非optimal，取其improvingincidentedge，它是rootdirection，而且所有b-activeconstraints在该vertex也active，所以该directionat b仍locallyfeasible。

把d的cone representation视为nonnegativeflows，每个root `−χ_u+χ_v`是一条u→vflowarc。Net inflow−outflow为d。去掉cycles、按sources/sinks分解，至少有一条从P={u:b_u>b′_u}到N={v:b_v<b′_v}的path。

Locallyfeasiblerootrelation具有transitivity：`u→v`允许 iff每个b-active lower-row X都满足 `u∈X⇒v∈X`。因此沿flowpath的membershipimplications合成，得到directroot `u∈P→v∈N` locallyfeasible。Inactive rows有integer slack≥1，root对任意row的变化至多1，所以完整unitstep也feasible。它把目标L1距离降2。重复至b′，每步必需至少降2，因此length恰L1/2。∎

这不是componentdegreeimage S_C 的unitclosure：本文处理整个B_g，physical-prefixlifting仍另行检查。

### 17.2 Unique strict component的显式word长度

Strict orientation的degrees nonnegative、sum m=|E(H)|，故两degreevectors的L1/2≤m。用17.1degreechain，每个unittransfer在strict起点按14.3用simplepath≤n−1copies实现、macro终点恢复strict。最后same-degreeEulerian difference总共至多m copies，逐圈serialize。

因此任意两个strict orientations间有original-legalword，length≤

    (n−1)||b−b′||₁/2 + m ≤ nm。

不要求每个intermediatephysicalstate自身strict，只要求原需求p合法。

### 17.3 µ≥2 reachability不再OPEN

`research_relative_reachability_audit.md`已完成fixedodd-boundarysafeendpoint、HEAVYexception与ancestor-labelphaseproof，任意initialD可合法augment至strict，length≤n²(n−1)²。因此14末尾和16.3中“每个component是否含strict”的旧OPEN在**all-proper-µ≥2 initial scope**已被该proofsupersede；本文自身的degreeproof不单独承担augmentation。

组合得到该fiber的diameter upper bound

    2n²(n−1)² + nm。

Generalµ1、arbitrarysigneddescendant、UNIT-IMAGE-CLOSURE的independentgeneralproof仍不由此关闭。
