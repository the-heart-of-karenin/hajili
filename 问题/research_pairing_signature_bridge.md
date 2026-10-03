# 配对路线继续：完整虚拟signature、任意临界根星、平滑定向的逆向表示

2026-10-03。主目标为原始MAIN；本文件的existence与certificate重写均不冒充physicalsingleflip连接词。

## 1. 记号与已有输入

G为finite loopless labelled multigraph，λ(G)≥2k+1。M为奇度vertices上的perfectmatching，copies为virtual，并满足

    δ_M(X)≤δ_G(X)−2k    (全部nonemptyproper X)。

这是global k-feasible pairing，不要求M的pairs是G的physicaledges。存在性已在research_pairing_lift_route.md核对。

为M的全部copies固定一个orientation τ。每vertex的canonical G-outdegree设为

    b_τ(v)=(deg_G(v)+deg_M(v))/2−out_τ(v)。

偶度vertex恰balanced；每条M-pair的两个奇度endpoints一个取floor(deg/2)，一个取ceil(deg/2)。Virtualsignature改变一条copy就使b在它的两个endpoints间转移一个unit。

## 2. 完整虚拟signature扩张定理

**Theorem 2.1.** 任意τ都能扩成G+M的Eulerianorientation；G部分D为k-strong。所有具有degreevector b_τ的physicalorientations自动k-strong。

Proof：对任何proper X，令i_G(X)数两端在X的physicalcopies，定义

    c_τ(X)=b_τ(X)−i_G(X)
           =(δ_G(X)−δ_M(X))/2+in_τ(X)≥k。

总量b_τ(V)=|E(G)|。所以每个X的tailcapacity b_τ(X)至少i_G(X)，integer edge-to-tail Hall assignment实现b_τ；每条physicalcopy独立赋给一个endpoint作tail。Cutout正是c_τ，因此D globallylegal；D+τ每vertex balanced。任何其它同b_τ realizer的cutvalues完全相同，结论也成立。∎

因此不是仅“某个Eulerianorientation投影合法”：固定M后，全部2^{|M|}个virtualsignatures都有非空canonicalfibers。它们的degreevectors构成一个由matching-endpoint unit transfers组成的hypercube。

这只是degree/certificatecube。Physicalsingleflip graph不能直接等同于它：翻virtualcopy本身没有改变G。

## 3. 新加强：完整τ可以与任意临界根星同时固定

设deg_G(r)=L=2k+1，A=V−r，M在r的唯一copy为ra。给任意balanced physicalrootstar σ，即out_σ(r)为k或k+1。固定任意完整τ，仅要求

    out_τ(r)=k+1−out_σ(r)。

**Theorem 3.1.** 存在canonicalphysicalorientation D，同时具有degreevector b_τ和完整labelledrootstar σ。因而G+M有同时扩张σ与τ的Eulerianorientation。

Proof：对v∈A记R_σ(v)为v→r的fixedphysicalcopies数。在H=G[A]要求internaloutdegree

    β(v)=b_τ(v)−R_σ(v)。

β(A)=|E(H)|。Hall条件β(X)≥i_H(X)等价于

    c_τ(X)≥R_σ(X)，    X⊆A。

若out_σ(r)=k+1，则R_σ(A)=k，Theorem2.1的c_τ(X)≥k立即覆盖所有X。

若out_σ(r)=k，则R_σ(A)=k+1且τ的rootcopy为r→a。若a∈X，in_τ(X)≥1，故c_τ(X)≥k+1，仍覆盖R_σ(X)。

剩余a∉X的nonemptyproper X⊊A。令Y=A−X，m_r(X)为root与X之间全部physicalcopies数；rootmate a在Y，所以

    δ_G(Y)=δ_G(X)+L−2m_r(X)，
    δ_M(Y)=δ_M(X)+1。

对Y使用M的admissibility，得到

    δ_G(X)−δ_M(X)≥2m_r(X)。

因此c_τ(X)≥m_r(X)≥R_σ(X)。X=A时total equality直接给Hall equality；X=∅平凡。所有Hall inequalities闭合，integerassignment实现β，所得D保留σ、实现b_τ，并由Theorem2.1合法。∎

相较research_pairing_lift_route.md §3，本节不再允许interior virtualdirections自由选择；全部τ已经固定。关键新步是对同一criticalroot的另一岸Y=A−X再次使用admissibility。

**Corollary 3.2.** 固定τ。凡与τ根copy方向相容的balancedrootstars（也就是同一个weight k或k+1 layer中的全部labelledsignatures），都有canonicalrealizers，且所有这些realizers的globalcutvalues相同。

此结论给RSM的一个统一目标族；仍未证明任意当前fixedstarstate能到达其canonicalrealizer，或同cutvalues的不同realizers已经相连。不能把existence/Hall当reachability。

## 4. 匹配head→tail的path：所有终态都合法

设D+τ Eulerian，τ中g=u→v。D globallystrong，故有physicaldirected simplepath P:v→u。

**Lemma 4.1.** 任意这样的P反转后D^P仍k-strong，且与τ^g组成Eulerianorientation。

Proof：g+P为G+M的directedphysical/virtualcircle，整圈反向后仍Eulerian；Theorem2.1的投影公式给D^P合法。亦可直接看cut：若v∈X、u∉X，则g进入X，in_τ(X)≥1，使c_τ(X)≥k+1；P的unittransfer至多减1。其它cut不减。∎

这给配对cube的每条edge一个legal-endpoint singlepathmacro，而且不需要寻找某条特殊P。仍未给prefixes合法：中间frontier可能离开另一个包含u、v的tightcut。前一文件的prefix账本继续适用。

## 5. 可强制一个physical odd–odd pair进入M

取physicaledge e=uv，u、v在G均奇度。因为λ(G−e)≥2k，G−e有k-feasible oddpairing M′；它不包含u、v。令

    M=M′+(virtual uv)。

逐割δ_M=δ_M′+δ_e≤δ_G−2k，所以M对G admissible。

若canonicalD中physical e与virtual uv方向相反，二者在G+M构成directed2cycle；翻整圈只在G中翻e，且投影仍合法。因此这一canonicalrealizer中e确实globallydeletable。

没有推论说任意当前D都能进入这个particularcanonicalfiber；也没有把M′的virtualedge当physicaledge。

## 6. 新核对的primary input：全体smooth states的逆向表示

Bernáth–Iwata–Király–Király–Szigeti，*Recent results on well-balanced orientations*，Discrete Optimization 5 (2008)，[作者托管原始论文](https://pagesperso.g-scop.grenoble-inp.fr/~szigetiz/articles/RRWBO_BIKKSz.pdf)，Theorem8.2：任意smooth k-strong D都存在上述global k-feasible M及τ，使D+τ Eulerian。这是既有文献输入，不是本次新证明；局部well-balanced版本不具有同样逆向性质，不能换用更强local pairing。

因此全部smoothlegalstates恰是“某个globaladmissibleM的某个canonicalsignaturefiber”的union。这是覆盖全部smoothstates的精确结论，而非只覆盖选定target。

还未证明每个Ωcomponent都包含smoothstate；legal-endpointdegreechain允许到达smoothdegree，但physical-word义务仍在。也未证明不同M的canonicalfibers在Ω中合并。

## 7. 在odd L-regular图中的精确certificate重编码

若每vertexdegree=L，则每个legalD自动smooth。对physicale=u→v：

    e合法flip ⇔ D−e k-strong
               ⇔ 存在D-compatible admissible pairing包含virtual uv，
                   该virtualcopy方向v→u。

Forward：合法flip要求uout=k+1、vout=k；D−e两endpoint均balanced，其它vertices仍smooth。对D−e用Theorem8.2得M′，再加入virtualv→u；admissibility按§5，D+τ Eulerian。

Backward：physicale与virtualcopy组成directed2cycle，§5直接给合法singleflip。

这没有把“含physicalpairs的perfectmatching”假定为总存在：M的其它pairs可以不是Gedges。也没有证明固定D下compatiblepairings的2-switchgraph连通。证书可以重选，但实际改变D只能计physicalflips。

## 8. 下一步实际缺口

配对signatures的存在性、临界rootstar兼容性、smoothstate逆向覆盖已经明确；剩余是originalphysicalhistory如何实现匹配head→tail路径，并允许改变配对证书避免guard循环。

Criticalcut只被一条M-copy穿过，故其polarity由这一virtualbit决定。非criticalh=0tightcuts可有多条M-crossings，已有unboundeddebt控制禁止把这一路线简化为常数buffer。

可以研究shortestcycle的dynamic witness，而不固定某个guard闭包；尚无证明每次可执行service使该cycle缩短。因此MAIN保持OPEN，RSM也未关闭。
