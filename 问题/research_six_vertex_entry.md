# 六顶点前沿：nontrivial critical cut、odd-regular最小边数层与下一层

2026-10-03。接续全部五顶点MAIN；一般目标仍OPEN，不把下面的范围扩大。

## 1. 六顶点所有nontrivial L-mincut案已闭合

令L=2k+1。六顶点G若有nontrivialL-mincut，选择大小2或3的一岸A。其genuinecriticalfullfiber由|A|≤3定理connected；quotientG/A有4或5顶点，已全部proved。B+commoncompletion及nonboundarylift给实际originalphysicalword。

所以六顶点反例若存在，λ=L且全部mincutshores仅criticalsingleton及complement。

## 2. 六顶点odd L-regular图全部闭合

**Theorem2.1.** |V|=6、所有vertexdegree=L、λ≥L时，Ω_k(G)connected，任意labelledmultiplicity。

若有nontrivialmincut，用§1。否则每paircut严格大于L且为even，故m_uv≤k。每triplecut严格大于L且为odd，故δ(X)≥L+2=2k+3；其internaledgecount

    i_G(X)=(3L−δ(X))/2≤2k。

任何singletondegree-legalorientation满足pairout/in≥2k−m≥k，tripleout/in≥3k−i≥k。六顶点的全部propercuts为singleton、pair、triple及complements，所以degree-onlyserialization闭合。∎

该范围恰六顶点最小边数层|E|=6k+3：degree≥L与totaldegree=6L使所有degrees=L。因此本层不需multigraphcensus。

## 3. 下一层中的一个完整degreepattern

|E|=6k+4时总degreeexcess为2，patterns恰(2,0,0,0,0,0)或(1,1,0,0,0,0)。

**Pattern(2,0,0,0,0,0) CLOSED。** 若nontrivialmincut，用§1。Heavypair若存在，只可能连接唯一highvertexa与criticalvertexb，m_ab=k+1；dominant-neighborcontraction到五顶点闭合。

若没有heavy pair，pairs全部degree自动合法。任一3/3partition至少一侧是三个criticalvertices；它的cut严格大于L且为odd，internaledges≤2k，双向k由degreebounds保证，故该cut及补岸均合法。全部cutsdegree-only，再闭合该pattern。

## 4. 第一项尚未统一处理的六顶点pattern

Pattern(1,1,0,0,0,0)：两个highverticesdegree2k+2，其它四个criticaldegreeL。若无nontrivialmincut，heavy pair至多为两个highvertices之间multiplicityk+1。

三点cut若含恰一个highvertex，degree总量6k+4，cut为even且≥2k+2。只有δ=2k+2时internalcount=2k+1，cutconstraint才不由singletonbounds自动保证。

对这种shoreX={a,c,d}（a high、c,d critical），令out(a)=k+h_a（h_a∈{0,1,2}），out(c/d)=k+h_{c/d}（h∈{0,1}）。Exactout/inbounds要求

    1≤h_a+h_c+h_d≤3。

所以出现真正的three-vertex degree coupling；五顶点的heavy-pairstar interval证明不能直接移植。若多个这样的rows在fixedoutside下把内部weight压成singleton，也不能宣布环境disconnected，仍需允许criticalrootbuffers。

本段没有构造原始反例，也没有断言这个pattern失败；只明确六顶点新cut义务。一般RSM仍未闭合。
