# 新的一般归约：至多k条边离开主邻居的vertex可收缩

2026-10-03。由五顶点intervallift继续抽出的一般定理；对原始MAIN的最小反例给新增必要结构。

## 1. 不再需要critical pair boundary的收缩条件

G为loopless labelledmultigraph，k≥1，|V(G)|≥3。取distincta,b，记d=deg_G(b)、m=m_ab。假设

    d≥2k+1，m≥d−k。

也就是b至多有k条physicalcopies连向a以外的vertices。收缩{a,b}并删除内部loops，得Q。

**Theorem1.1.** 每个k-strongorientationF of Q都有一个非空、connected的fullfixed-outside lift fiber；每个legalquotientsingleflip都可通过这些fiberslift。因此若Ω_k(Q)connected，则Ω_k(G)connected。

这里不假设δ_G({a,b})=2k+1，不假设µ2strictification，也不只检查singletoncuts。

## 2. 精确fiber是一个interval

固定F，记R_b为所有b与a以外vertices之间当前b-outgoingcopies数，u为内部a→bcopies数。则

    out_D(b)=m−u+R_b，in_D(b)=d−m+u−R_b。

b的singleton合法性恰

    u∈I(F)=[m+R_b−(d−k), m+R_b−k]∩Z。

因为0≤R_b≤d−m≤k，且m≥d−k，I的lower≥0、upper≤m；它的width恒为d−2k≥1。没有额外截断使它变成singleton。

## 3. 所有mixed cuts自动受保护

设D实现F的outsidecopies且u∈I(F)。于是b双向在[k,d−k]内，特别out_D(b),in_D(b)≤d−k≤m。

Take a globalpropercut X containinga butnotb。若X=V−b，双向cutvalues就是b的in/out，已合法。否则将b加入X，映到Q的propernonemptyshore Y，且有exact identities

    out_D(X)=out_F(Y)+δ_G(b,X)−out_D(b)，
    in_D(X)=in_F(Y)+δ_G(b,X)−in_D(b)。

δ_G(b,X)≥m，因为a∈X。两个extra terms非负，所以X双向≥k。

含b不含a的cut取complement即属于同一审计。含两者或不含两者的cutrespectcontraction，直接由F合法性保证（singletonb已单独处理）。因此全globalmixedcuts闭合；I(F)精确等于整个liftfiber的合法weightinterval。

Conversely，任意globallegalD投影到Q仍legal，且必满足b singletonbounds。因此没有删去原问题的任何liftstate。

## 4. Physicalidentity、相邻fiber和wordlift

I width至少1。内部m个labelledcopies的directions形成subsetweightintervalcube，所有statesconnected：在相邻weightlayers之间交替add/delete实现任意copyidentity交换，其它layers按weight连到这两个layers。

一条Q flip若原copy不incidentb，则R_b不变，新旧I相同；若incidentb，R_b变化±1，I整体平移一个unit。由于width≥1，I(F)∩I(F′)含integer。

给定当前D，可先在其actualfullfiber走到该共同weight的任何physicalassignment，再翻Q指定的outsidecopy；同一internalassignment在新fiber仍合法。逐步lift完整Q-word，最后在终点fiber对齐目标D′。全部计数都按physicalcopies，parallelidentities完整保留。∎

## 5. 对原始最小反例的直接约束

在λ(G)≥L=2k+1、字典序最小反例中，Q有更少vertices且λ(Q)≥L，所以原图不允许上述vertexpair。故对每个vertexb及每个邻居a都必须

    m_ab≤deg_G(b)−k−1。

特别criticalvertexdeg=L时，每个neighbor multiplicity≤k，至少有3个distinctneighbors。

这排除的不只是oddregular图中由paircut已推出的multiplicitybound；它还排除高degreecenter通过k+1或更多copies连接criticalleaf的情况。Boundary可远大于L，仍能用connectedfiber与intersection来归约。

本定理不排除allcriticaledge oddregularcore；也不单独关闭RSM。但这是一般MAIN上的正式归约，独立于五顶点边数层。

## 6. 五顶点还有一个广泛子类

若五顶点G λ≥L，所有pairs除至多一个ab外均m≤k，而该ab有m≥k+1，则Gconnected，不限制edgecount或degreeexcess。

Proof仍收缩ab。FixedoutsideR_a,R_b、T=R_a+R_b，要求u落在

    [0,m] ∩ [k−R_a,deg(a)−k−R_a]
          ∩ [m+R_b−(deg(b)−k),m+R_b−k]。

Q-rootlegal给T∈[k,deg(a)+deg(b)−2m−k]。两个vertexintervals的width分别deg(a)−2k、deg(b)−2k，均≥1；两个crossgaps均≥m−k≥1；outsideprofilebounds使全部lowers≤k≤m−1、uppers≥m−k≥1。故intersectionwidth≥1。

Singleton、abpair由这些bounds与Qroot保证，其它pairs因m≤k自动合法；五顶点全部cut形状已覆盖。一次quotientflip只使R_a或R_b变化±1，相邻intervals有公共weight，wordlift如§4。∎

这是case“一个exceptionalpair”的无边数上限推广，不是对一般多exceptionalpair图的证明。
