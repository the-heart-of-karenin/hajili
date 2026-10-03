# Canonical也需要换证书：任意k的odd-regular控制与signed µ2冻结反例

2026-10-03。以下是指定parametriccontrols的理论核验，不是原始MAIN的反例搜索。

## 1. 四顶点odd (2k+1)-regular family

任意k≥2，V={w,y,c,d}，R的labelledphysicalarcs：

    K：e=w→y，f=y→w；
    w→c、y→d、c→y、d→w各k−1条；
    g=c→w、d→y、c→d、d→c各1条。

每vertexdegree L=2k+1，outdegrees(w,y,c,d)=(k,k,k+1,k+1)。Undirectedmultiplicities为

    m_wy=m_cd=2，m_wc=m_yd=k，m_wd=m_yc=k−1。

Singlescut为L；paircutδ=2L−2m≥L+1，所以λ=L，所有mincutshores为singleton或其complement。每physicalcopy都属于某个mincut，故E°为空。这准确覆盖删除锚未处理的allcriticaledge范围。

任何outdegrees全部在{k,k+1}的orientation都k-strong：singleton双向≥k，pairout/in≥2k−m≥k；四顶点全部propercuts已经覆盖。因而下文可用degree区间严格核验所有history states。

e与f最初都illegal：两者tail的singletonout=k。R已经smooth，而非“不平滑起点造成的障碍”。

## 2. 初态已经canonical，但K上没有合法首步

取admissiblepairing M={wc,yd}，τ=w→c、y→d。R+τ Eulerian，每vertexout/in=k+1。

M admissibility逐类：singleton δ_G−δ_M=L−1=2k；pairwc/yd的δ_M=0、δ_G=2k+2；pairwy/cd的δ_M=2、δ_G=4k−2，差4k−4≥2k；pairwd/yc差2k+2。Complementshore相同。

所以“canonical的每个directedphysicalcircle已有一条合法copy”对k≥2为FALSE。不能把k=1的相关circle性质不经证明推广。

这不是minimumambientseparation：explicit word

    g，e，f，g

连接R与R^{e,f}。Degreevectors依次

    (k,k,k+1,k+1)→(k+1,k,k,k+1)
    →(k,k+1,k,k+1)→(k+1,k,k,k+1)
    →(k,k,k+1,k+1)。

每步都globallylegal且smooth。最终只交换e、f两条physicalcopies的方向。

## 3. 同一physicalword的动态pairing证书

初态用M、τ。翻g时，virtualwc同时从w→c换为c→w；这只是记录新的Euleriancertificate，实际G只有g这一singleflip。

在R^g，zero-physical-change地改配对为

    N={wy,cd}，virtual directions y→w、c→d。

N也admissible：singleton gap0；pairwc/yd的δ_G−δ_N=2k；其它pairgap非负。Degreebalance保持，故R^g+N仍Eulerian。

现在e=w→y与virtualy→w构成directed2cycle，其physicalsingleflip合法；换该virtualdirection为w→y。接着f=y→w与它构成directed2cycle，也合法。之后改回M及τ在R^g的方向，最后restore g。

这给一个完整可审阅的certificate history：某次physical服务后，仅重选配对使差异copy可翻。不能把re-pairing计成physicalprogress，也不能据这个控制宣布一般admissiblepairings总有需要的switch。

## 4. Signed µ≥2一般定理确实失败

在上述G再增加两条physicalcopies c→w、d→y，并将它们与所有非Kcopies冻结在给定direction；只允许e、f翻。

新原图每vertexdegree 2k+2；maxmultiplicity为k+1，故singleton与最小paircut均为2k+2，λ(G⁺)=2k+2。R⁺仍legal；完整Kcircle reversal不改变任何cutvalue，也legal。

两个单翻却仍illegal，因w、y的out仍k。所以这个coordinate restriction恰两个isolatedstates：K的两种cycleorientations。

在完整四顶点vertexset上写freegraph F（只有两条Kcopies）及signeddemand

    p_J(X)=k−out_fixed(X)。

全部properX满足恒等式

    δ_F(X)−p_J(X)−p_J(V−X)=δ_{G⁺}(X)−2k≥2。

但fiber不连通；p_J({c})=p_J({d})=−2。故“任意signed crossing-supermodulardemand、全proper µ≥2即可singleflipconnected”的强化明确为FALSE。Initialtruecritical p≥0的已证明µ2定理没有受损；其scope不是装饰条件。

若再删除F中的isolatedvertices c、d并投影到{w,y}，需求变为两个singleton各1，µ恰0。不能把vertexelimination前的µ2读成projectedµ2；这与atomprojection审计一致。

## 5. 小型核验与意义

scripts/verify_pairing_bridge_controls.py对k=2,3,4,5各核验7个指定certificate/history states，全14个globalcuts、全部matchingadmissibility及Eulerianbalance通过。另在k2实例核验40个完整virtualsignature与labelledcriticalrootstarqueries，各保存一个canonicalcompletion；没有枚举图或原图全部orientationgraph。

Signedµ2freezecontrol另外仅检查4个K assignments及全部14个signedmargins。原始cut表、witnesses与hash见data/pairing_bridge_controls_*。

这组结果同时确认canonicalroute的存在性加强有真实witness，并排除两个会让证明跳步的强化。剩余必须证明一般physicalhistory或dynamicre-pairing的有限进展；MAIN保持OPEN。
