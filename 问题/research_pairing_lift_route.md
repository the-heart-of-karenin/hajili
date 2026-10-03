# 替代综合路线：odd pairing、Eulerian lift 与 canonical targets

2026-10-03。这里的目标仍是原始physicalsingleflipconnectivity。本文保存一条与历史guard路线不同的尝试，区分已证明targetexistence和未完成的projectedserialization。

## 1. 已核对的primary input

Király–Szigeti, *Simultaneous well-balanced orientations of graphs*，作者托管 [原始论文](https://pagesperso.g-scop.grenoble-inp.fr/~szigetiz/articles/kisz19.pdf)。其Theorem5给每个图的feasible odd-vertex pairing；Claim4给global版本：2k-edge-connected G存在oddvertices的perfectmatching M，使δ_M(X)≤δ_G(X)−2k。局部feasible版本把2k替换为2floor(R_G(X)/2)，其中R_G(X)是cut两侧vertexpairs的最大local edge-connectivity。

以下公式和fixed-roottarget结论是本次独立推导，不把该论文的orientationexistence当作physicalreconfiguration结论。

## 2. Global admissible pairing给even增强图

在λ(G)≥2k+1时选上述M。M只有virtualcopies，不是用户允许翻的originalphysicaledges。

每个vertex满足deg_M(v)≡deg_G(v) mod2，所以δ_M(X)≡δ_G(X) mod2。由admissibility，δ_G−δ_M≥2k且为even。若δ_G(X)=2k+1，则δ_M(X)≤1且为odd，故δ_M(X)=1。

G+M每个degreeeven；每个cutδ_G+δ_M是even且≥2k+1，因此≥2k+2。

任意EulerianorientationF of G+M，投影D=F−M。写

    h(X)=(δ_G(X)−δ_M(X))/2−k≥0，

则exactcutvalues为

    out_D(X)=k+h(X)+in_M(X)，
    in_D(X)=k+h(X)+out_M(X)。

所以D globallyk-strong。D的OUT-tightcut恰h=0且全部跨cutvirtualarcs向外；IN-tight为对偶。criticalmincut必被恰一条M-copy穿过，tightpolarity由其方向决定。

## 3. 新的fixed-critical-rootcanonicaltargetexistence

设deg_G(r)=2k+1，固定任意originalrootstar directionsσ，只要rootout/in是k/k+1。M在r恰有一个virtualcopy；选择其方向使F中rootout/in均k+1。

**Lemma3.1.** 在even graph E=G+M中，这个指定balancedrootstar可扩成Eulerianorientation。

Proof：记A=V−r、H=E[A]，要求内部vertexoutdegrees

    b_v=deg_E(v)/2−R_σ(v)，

其中R_σ(v)为v→r的fixedcopies数，包含virtualrootcopy。Total b(A)=|E(H)|，因为rootdegree2k+2、fixedA→r总k+1。

对任何nonempty X⊆A，integer Hall orientation条件b(X)≥|E_H[X]|化为

    δ_E(X)/2≥R_σ(X)。

左侧≥k+1，右侧≤R_σ(A)=k+1，因此成立。把每条physical/virtualcopy分配给一个endpoint作tail的integerbipartitematching，得到所需Eulerianorientation。∎

由§2投影，该F给originalG的globallylegalD compatiblewith任意balancedσ。它同时smooth：even-degreeverticesout=in，oddvertices差1。这比仅给某个可行rootsignature明确。

### 3.2 Mincut atoms的同时strict target

若选局部feasibleM，对任何separates两个localλ≥2k+2 vertices的cutX，都有

    δ_G(X)−δ_M(X)≥2k+2，h(X)≥1。

故canonicalD在这种cut上双向≥k+1。将localλ≥2k+2的equivalenceclasses称globalmincutatoms，得到：每个balancedfixedrootσ都有一个canonicaltarget，对所有splits某mincutatom的globalcuts同时strict。

这个existence只使用Hall和已核对pairinginput。尚未证明任意当前D可以在保持σ的originalsingleflips下到达该target，也未证明全部canonicaltargets处于同一fixed-rootcomponent。

## 4. 精确projectedprefix账本

在currentEulerianF的一条directedcycle上，从s开始flip一个directedprefix到frontierf，包含originalGcopies与virtualMcopies。Projection在virtualmoves时不改变G，只在originalmoves时翻对应copy。

    Δout_D(X)=χ_X(f)−χ_X(s)−Δout_M(prefix,X)。

对initialD-OUTtightX，所有M-crossarcs原来outward，所以

    Δout_D(X)=χ_X(f)−χ_X(s)
              + #(已经反转的virtualout-crossings of X)。

因此若prefix先由originaledge离开一个含s的tightX，还未翻到virtualout-crossing，该projection会失1并非法。Eulerianendpoint、G+M的2k+2connectivity、或Fprefix的k-strongness，都不能单独保护projection。

这给真实的serialization义务：选择rotation/stems/history，让每个旧tightcut的危险physicalexit得到virtual计数或其它physicalbuffer保护。Virtual翻转本身不是用户允许的progress，不能隐式算成originallegalmove。

## 5. 一个canonicalEulerian控制：任意cycleprefix不安全

k=2，V={w,y,c,r}。OriginalGcopies为：w→c两条；y→c、c→y各一条；w→y、y→w各一条；c→r两条、r→w两条、r→y一条。

Degrees(w,y,c,r)=(6,5,6,5)，λ=5；Doutdegrees=(3,2,3,3)，D globallylegal。M={y→r}使G+M Eulerian；δ_M≤1≤δ_G−4。

Directedphysicalcycle y→w→c→r→y完整reversalcutneutral，但第一步翻y→w使singletonyout2→1非法。因此任意Euleriancycleprefix的projection合法这一shortcut为FALSE。

在本控制中可rotation从r开始合法翻整圈；它不反驳存在某种rotation/stem/history，亦非原定理反例。其作用仅是固定§4不能省去的prefixaudit。

指定控制已独立核验：scripts/verify_synthesis_controls.py逐一检查全部14globalcuts，virtual增强各vertexout/in=3/3；坏首步singletonyout1；rotation r→y、y→w、w→c、c→r 的每个prefix全局合法，终态全部割值恢复。Raw与SHA见data/synthesis_controls_*。未进行orientationcensus。

## 6. 对主定理当前能提供什么

已提供每个fixedcriticalrootstar的canonicaltargetexistence，以及mincutatoms同时strict的target。但reachability和canonicalcomponentconnection仍需一般μ1历史服务。没有由Eulerianlift消去它。

可以继续尝试：沿mincuttree追踪唯一virtualcrossing的polarity，允许长physicalstems；若能证明任意blockedpath/circuit的finiteprojectedserialization，就回到已完成的globalmacro/induction。当前没有不循环的generalmeasure。
