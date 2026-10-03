# Weighted dual source 与 unweighted guard closure 的另一个精确缺口

2026-10-02。**PROVED CONNECTED CONTROL**；不声称optimal-dual / minimum-component-origin反例。

## 1. 静态CFST不能单独保证原weighted support的legal positive-gradientedge

CFST给cross-free actualtight F 的**relative** strict sources。Compatible-blocker closure把F扩成maximalcrossfree T后，T的strictsourcesglobally legal。但一个T-source可能只对新guards positive、对原F全部neutral，所以原cutweights的nodepotentialgradient仍0。

因此下列unqualifiedstatement为FALSE：

    nonzero nonnegative crossfree actualtight dualsupport F
    ⇒ 某条globally legal physicaledge的原Δ_y严格positive。

即便weightedrows在两个antipodes都tight、指定K是directed2circuit、Debt_y>0，statement仍可失败。

## 2. 固定k=2、L=2 arm control

直接使用已完整逐割核验的terminal construction：`A={w,w1,y,y1,c}`，boundary为 `c→r`两条、`r→w`两条、`r→y`一条。K为`w→y,y→w`各一条。J为

    w→w1,w1→w,y→y1,y1→y：各一条；
    w1→c,y1→c：各一条；
    c→w1,c→y1：各两条。

这是globally2-arc-strong、λ=5、minµ1的genuineinitial system。四个singleton `{w},{w1},{y},{y1}`actualtight。所有legalinternalcopies恰为`c→w1,c→y1`各两条；其他currentarcs都被tail-side的一条singletontightrow阻止。

令y只在`{w},{y}`各取weight1，其余0。两个weightedrows在R与完整K-reversed antipode都tight，因为K是circuit、cutvalues不变。其vertexpotential为

    φ(w)=φ(y)=1，φ(w1)=φ(y1)=φ(c)=0。

故四条globallylegalcopies全部Δ_y=0。RelativeF-sources `w1→w,y1→y`梯度1，但分别被omittedtightguards `{w1},{y1}`阻止；没有globallylegalpositive-gradientcopy。

指定e=`w→y`。K另一copy两端φ相同，gradient0；weighted slack S_R=0；每条J的positivegradient至多1，所以L_J=Σ[Δ−1]_+=0；P_e=1。因此

    Debt_e,R(y)=1>0。

实际optimaldeletioncost是L=2，本y不是optimal。故这个control只关闭positive-Debt arbitrary-certificate版本，不能当作“某optimaldual也无legalpositiveedge”或minimum-origincounterexample。

## 3. 加guard后legal source出现，原gradient仍0

加两条guard `{w1},{y1}`，得到T四条singletontightrows。T的legalstrictsources就是c→w1/c→y1 copies；它们对新增guardpositive，而对原Fneutral，完全符合CFST与compatibleblocker theorem。

保持原weights不变意味着guardweights为0，originalgradient仍0。若另给两guard weightε∈(0,1)，legalcopies梯度ε>0；在本control里这个perturbation不改变Debt=1，但“任意guard都可这样加且保住某optimalobjective”尚无一般theorem，不能从这一个例子推出。

## 4. 对minimum-reference路线的限制

`research_terminal_debt.md` §10已区分Δ>1与Δ=1的complementarity；这里进一步区分relativepositive source与globallylegalpositive originalgradient。两道接口都不能省：

1. 若仅知道dualpositive-supportcrossfree，CFST不保证originalweightedgradient在某legalcopypositive；
2. 即便另有lemma给legalpositivegradient，Δ∈(0,1]仍不能强迫该copy进入optimalcompletion。

可继续研究的精确targets：optimaldual选择是否能让blocker guards获得positiveweights而保住objective；或从optimalprimalcompletion抽取有ancestor-safehistory的firstprogress，不用weightedsource作shortcut。两者目前OPEN。

证据来源：`data/terminal_unbounded_debt_certificate.json`的optimizedk2,L2cycle记录，以及独立legalityaudit`data/node_potential_local_trap.json`。本文件不增加graphsearch，也不把已知connectedarmcontrol重称maincounterexample。

独立focusedcertificate已补存：`scripts/verify_dual_guard_gap.py`用同一解析constructor，只核验12条internalcopies各自的singleflip及两antipodes的全部62个globalcuts；4条legalcopy均Δ=0，2条relativeF-sources均illegal，Debt=1，PASS。raw及SHA在`data/dual_guard_gap_*`。

## 5. 一条guard可以在optimaldual中positive的充要条件（已证明）

考虑bounded feasible primal orientation/deletion LP，cutrow U 写为 `a_U·z≥b_U`。则

    存在optimaldual使y_U>0
    iff 每个optimalprimal completion都使U-row tight。 (5.1)

Necessity：任意optimalprimal与任意optimaldual之间dual-gap为一组nonnegativecomplementarityterms之和。若某optimalprimal在U有positive slack，则所有optimalduals的y_U都必须0。

Sufficiency可直接从normalcone证明，不需混用integerdual与strictdual。令F为primaloptimalface，取z*∈relint F；U是universallytightrow，故其normal是F normalcone的一个generator。Objective c在该normalcone的relativeinterior，因为F是它的完整minimizingface。可以取ε>0，使c−εa_U仍在normalcone中；将剩余normal写成active-row/box-normal的nonnegativecombination，再加回εa_U，得到optimaldual且y_U≥ε。同样对任意有限collection的universallytightrows，用 `c−εΣ a_U`，得到它们simultaneouslypositive的optimaldual。Equalitynormal的lineality与boxconstraints按usualnormalcone计入即可。

Primalbox integral时，“所有optimalprimal”可等价检查“所有integeroptimalcompletions”：optimalface的vertices仍integer，任一点是这些vertexcombination。该equivalence不意味着所选simultaneouslypositive dual本身integral。

**Guard接口。** Reference-tight guard U 若在某个optimalcompletion中已经strict，则它不可能被赋positiveweight而保持dualoptimality。所以“用ε给所有blockers加权”不是无条件操作。真正的optimum-preserving weightedclosure只能加入universallytightguards；并且还需证明其positive支持能选成所需cross-freegeometry，不能从5.1单独推出。

第2节的tip-onlycertificate非optimal，因此没有触犯5.1。真正optimalarmcertificate需要把深层prefix/guards一起计量；这个例子不提供universallytightblockerclosure的一般proof。
