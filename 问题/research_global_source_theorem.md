# 全局 physical source 定理：无需先固定临界边界

2026-10-03。用于原始MAIN，不是signed localprojection。G为finite loopless physicalmultigraph，λ(G)≥2k+1；D globallyk-strong。

## 1. 定量global CFST

取任意非空cross-free actualout-k-tight familyF，properglobalshores；n为非空Booleanatoms数，n≥2。跨atoms当前物理弧g若不leaves任何F-row而enters至少一row，称relative strictsource。其数Z满足

    Z≥k+ceil(n/2)。

### 完整树预算

互补tightpair不可能，因为两向cut值均k将使无向cut2k<λ。F有trows、split-tree有e=t+1−n个empty nodes。每empty node的incidentbranchespartition整个V。

所有normal或所有complementaryincidentrows均tight的pureempty node不可能：若partition有d≥2块且各out=k（或各in=k），cross-blockphysicaledgesM=d k；但每块无向cut≥2k+1给2M≥d(2k+1)>2dk，矛盾。因此empty nodesmixed。

对每mixedemptyv，normalbranches的unionU_v nonemptyproper，out_D(U_v)≥k。定义ν(g)=F-negativerows数、σ=Σinteratom max(ν−1,0)。沿treepath同样按相邻negative-negativepairs收费，给σ≥e k。

紧行总消耗为

    M−Z+σ=t k，故M≤(t−e)k+Z=(n−1)k+Z。

全局atomquotient每个vertexdegree≥2k+1，没有另删outsidebudget，故M≥ceil(n(2k+1)/2)=nk+ceil(n/2)。合并得Z≥k+ceil(n/2)。∎

## 2. 任意global actual-tight source-free family同样不可能

若非空actualtightF不cross-free，用tightcorneruncrossing保留negativephysicaledgecover。每个newpositivecorner有oldpositiveancestor；零petalphysicaledges使所有oldnegativecoverage保持。source-freeness随替换保持，shorepotentialstrictdescent给nonemptycross-free族，再由§1排除。

因此source-free排除不要求一开始cross-free，也不要求degree2k+1root。这与 research_main_theorem_synthesis.md §2 的initialcriticalfiber版本范围不同：这里允许全部originalglobalcopies，包括root/boundary。

## 3. 全局合法sources与主目标的剩余接口

Compatible negativeguardextension在constantglobaldemandk下同样成立：crossingactualtightcuts的cornersactualtight且petals间无physicalcopies。MaximalcrossfreeactualtightT覆盖全部illegaloriginalarcs，其relative sources全部globallylegal。因此n_T atoms时至少k+ceil(n_T/2)条globallegalphysicalcopies。

这给允许rootbuffers时的静态source供应，但不保证任意指定criticalroot或targetedge可被服务。历史flip可以删除oldtightrows、出生newnear-tightrows，并产生合法undo；source数量不是无循环终止量。

若一个same-state closedserviceSCC的定义真的蕴含“每个positivephysicalservice都有S内negativeguard”，则其rows构成上述source-freeF，任意大小都被排除。不将这个结论套到不同历史时刻rows的SCC，也不把private-witnessSCC closure当all-serviceclosure。

对MAIN的作用：无需再花主要精力证明size≥4的**静态全serviceclosed族**不存在；真正未完成的是ambientminimumcomponent如何强迫一个同态closedcertificate，或怎样在没有该certificate时用root-returnhistory取得targetprogress。
