# 最小环境分离对的 first-asynchrony：精确局部多面体

2026-10-03，接续删除分量锚。主目标仍为原始MAIN，不把下面的局部结构当作连通性完成。研究继续，主目标保持active。

## 1. 最小对象与适用范围

固定同一原图G的一个环境分量C。在所有R∈C、Q∉C的合法对中取Hammingdistance h最小者；K为差异physicalcopies，J为共同copies，h≥2。这里可以取C=C°，但本节不要求这个删除锚存在。

二元环境标签给fixed-J cube恰两个端点R,Q；其coordinateface integral且为segment。必要supportclassification给K是directedphysicalcircuit或vertex-disjointdirectedpaths。以下始终按R定向K。

取共同copy g=a→b∈J，假设R^g合法，而Q^g非法。R^g当然仍在C。

本节也适用于原始全环境最小h。若使用same-root-star最小h_r，则只有g不incidentroot时可直接使用；rootflip后的R^g与旧Q根星不同，不能用h_r的距离下界。这个例外不是小措辞，应保留给root-return策略。

## 2. h+1坐标face的全部可能顶点

只放开K∪{g}，其它共同directions冻结；K以R为0、Q为1，g以共同初始方向为0。写

    O=(0_K,0)=R，A=(1_K,0)=Q，B=(0_K,1)=R^g。

g=0slice恰O,A；A^g=(1_K,1)不可行。

任何g=1合法stateT都在C：否则它与B的距离≤h，等号只能T_K=1_K，已被Q^g不可行排除。因此T与A跨环境labels，hminimality要求

    dist(T,A)=1+#{K-coordinates where T agrees with R}≥h。

所以T_K至多一条copy取Q的方向。令

    L={e∈K：R^{g,e}合法}，C_e=(unit_e,1)。

完整cube的合法vertices精确为

    {O,A,B}∪{C_e:e∈L}。

这是实际原始componentlabels推导，不是把frozenrestriction的components当原图components。Fullglobalprimalintegrality使整个coordinateface恰这些vertices的convexhull，没有额外fractionalvertices。

## 3. 两类真正polytopeedges

### 3.1 若L⊊K，则A—B是一条全局polytopeedge

直接给exposingobjective。令q=|K−L|≥1，给missingcoords系数1/q、L中coords系数−ε，g系数1−|L|ε；取ε>0且|L|ε<1（L为空也可）。

A和B的objective都为1−|L|ε>0；O为0；每个C_e比B少ε。故exposedface恰conv{A,B}。

### 3.2 对每个e∈L，A—C_e都是全局polytopeedge

给e系数1，其余Kcoords系数ε∈(0,1)，g系数(h−1)ε。A与C_e均为1+(h−1)ε；B为(h−1)ε，O为0，其它C_f为hε，严格较小。故exposedface恰conv{A,C_e}。

这些都是coordinateface的edges，也就是fullglobalpolytope的edges。两类必要supportclassification可以正式使用；没有把support形状当作adjacency的充分条件。

## 4. 新定理：one-sided共同launch的端点约束

**定理4.1。** 若R^g合法、Q^g非法，则

    indeg_K(a)=0，outdeg_K(b)=0。

换句话说，反向g=b→a加入K时不能在任何physicalvertex造成第二条入边或第二条出边。对于pathcollection，原g的tail只能是某条pathstart或support之外的vertex；head只能是某条pathend或support之外的vertex。

Proof：假设a有K-incomingcopye₀。A—B的difference按B定向为K加反向g；它在a有至少两incomingcopies，违反polytopeedge必要support的in/outdegree≤1。所以3.1迫使L=K。

选e∈K−{e₀}，h≥2保证可选。由3.2，A—C_e是edge；difference按C_e定向为K−e加反向g。e₀仍在，a仍有两incomingcopies，矛盾。故indeg_K(a)=0。

若b有K-outgoingcopy，完全同样选择另一条e，得到两outgoingcopies的矛盾。∎

对偶：若共同g仅在Q可翻，则按Q的反向K应用，原R方向下必须

    outdeg_K(a)=0，indeg_K(b)=0。

即Q-only的共同launch从R-pathend/outside指向R-pathstart/outside。

注意这不禁止synchronous共同moves触碰internalKvertices；两个端点都合法时上述h+1face顶点约束不成立。Circlecase其实所有共同moves都同步，因为两端所有割值相同。

## 5. 使用删除锚时再排除一种局部闭圈

取C=C°，h=h°，已知minimumh°差异support不能是circle。

**推论5.1。** 若K有至少两条pathcomponents，R-only共同g不能恰从某一个component的start指向同一component的end。

否则K加反向g含一个physicalcircle及至少一个其它path，所以不可能是edge support；3.1迫使L=K。

若那个circle之外有至少两条Kcopies，删任一外部e仍留下circle加非空pathsupport，违反A—C_e的edgeclassification。若circle之外只有唯一copye，则A—C_e的support恰该circle；它的Hammingdistance为h，且两端分别在C°内外，成为一个minimumh°circuitpair，与删除锚的circle排除矛盾。∎

所以R-onlyg若连接两个既有pathendpoints，必须join两个不同pathcomponents，除非K本来就是单path。也可能接入一个outsidevertex或形成outside的新path；这些分支不能省略。

## 6. ℓ°最短singlepathmacro的严格prefix禁令

另取ℓ°的最短跨C°singlepathmacroP=s=v₀→…→v_ℓ=t，起态R∈C°、终态Q∉C°。本节不把该pair同时当h°最小。

**定理6.1。** 任意propernonemptyprefix或suffix的整体反转，在R或Q对应方向下都不可行。

例如R反转prefixs→v_i若合法，得到F。Prefixmacro长度i<ℓ°，不能跨C°，所以F仍在C°；F与Q恰差remainingdirectedsuffixv_i→t，长度ℓ°−i<ℓ°，又是跨C°合法终态macro，矛盾。Suffix及Q端同理。∎

于是每个internalvertexv_i都有两条actualcommon-tightrows：

- X_i包含s,t而不包含v_i，阻挡prefixunittransfer；
- Y_i包含v_i而不包含s,t，阻挡suffixunittransfer。

证明：prefixreversal的cutout净变化χ_{v_i}−χ_s；非法必有R-OUTtightX_i含s不含v_i。完整P终态Q合法又迫使t∈X_i。Suffix同理，R-OUTtightY_i含v_i不含t，完整P终态迫使s∉Y_i。两row的endpointmembership相同，故R,Q上同样tight。

此结论强于“首尾Kcopy非法”，但仍不冻结任意interiorKcopy：翻一条interiorcopy只切成两个pathsegments，不是properprefix/suffixmacro。不能借定理6.1偷偷加强ℓ°的minimality。

## 7. 原始first-asynchrony的cut账本

对于任意合法终态singlepathP=s→t，不要求minimumh：

    out_Q(X)=out_R(X)+χ_X(t)−χ_X(s)。

若共同g=a→b在R合法Q非法，则存在globalproperX满足

    s,a∈X，t,b∉X；
    out_R(X)=k+1，out_Q(X)=k。

这是R-near、Q-tight的endpoint-separatingguard；反向one-sidedcase交换s,t。Common-tightfamily只包含endpointmembership相同的rows，所以这条新guard不能直接加入而仍称“common同态closed族”。

在minimumh pathcollection中净变化是所有endpoints之和，可能超过1；不能把本singlepath的near= k+1账本原封不动套到多path。

## 8. 主目标推进与仍需完成的工作

定理4.1把最小ambientseparation的one-sided共同moves限制为endpoint-compatiblelaunches；推论5.1排除properpathcomponent上的局部闭圈。定理6.1把最短singlepathmacro的每个internalvertex压到一对common-tightguards，而非只知道两个端边非法。

这给actualhistory的结构，但还未给termination：一次one-sidedlaunch可能使distance从h增到h+1，face中的L也可能为空，此时不能立刻flip任何Kcopy。外部新path、不同pathcomponent的连接、以及singlepath上的endpointrotation仍要处理。

下一步：分析这些endpoint-compatiblelaunches能否用可执行completion/history产生新的minimumpair，使端点或pathcomponent严格改善；rootflip在h_r的例外必须单独利用，不能把它消掉。新结果不复活constantbuffer，也不把source数当well-foundedmeasure。

## 9. Critical endpoint 在同步 paired orbit 内锁住根星

设K的某个pathstart s在原图degree=2k+1。因为K在s恰有一条出copy且无入copy，Q的singletonout比R少1；两端合法迫使

    out_R(s)=k+1，out_Q(s)=k。

任何共同outgoingcopy s→v若在R可翻，在Q就使singletonout k→k−1；任何共同incomingcopy v→s若在Q可翻，在R就使singletonin k→k−1。因此没有incident s的同步共同singleflip。Pathend t对偶：out_R(t)=k、out_Q(t)=k+1，也无incident t的同步共同singleflip。

这是真实paired orbit中的局部star锁，不声称整个环境分量锁住该star；第一次只在一端合法的rootflip正是逃出同步orbit的一种方式。若最小对象为h_r，还必须保留§1的rootflip例外，不能在锁的基础上错误地继续使用同根星距离下界。

Endpoint potential给出的信息也仅是局部信息：在各start赋1、end赋−1、其它vertex赋0，R-only的endpoint-compatible共同move对该nodepotential的outdegree目标增量≤0，Q-only增量≥0。已存在的14→13→15真实legalhistory否定“一步无正梯度就全局最优”；故不把这个符号表当作终止证明。

## 10. 指定控制：L可以为空，而另一个同步服务边解锁路径

这不是minimum ambient separated pair。取k=2、V={s,v,t,z}，初态R的11条labelledcopies为

    e:s→v，f:v→t，g:s→t；
    ts1,ts2:t→s；sz:s→z；
    h,zt2:z→t；vz:v→z；zv1,zv2:z→v。

原图degrees为(5,5,6,6)，λ=5。令Q=R^{e,f}，差异K是s→v→t。所有cuts已检查，R、Q、R^g合法，Q^g非法。

只释放e,f,g的8个states中，恰三个合法，按(e,f,g)bits是

    000，110，001。

Common tight rows X={s,t}、Y={v}阻挡所有mixed e/f方向；所以R^g后e、f仍都非法，§2中的L=∅。这排除不带minimum-origin额外证明的“one-sided launch必立即unlock K”。

但是h这条另一共同copy可在R、Q同步翻转；在R侧实际合法word

    h，e，f，h

把R连到Q。沿word outdegrees(s,v,t,z)依次为

    (3,2,2,4)→(3,2,3,3)→(2,3,3,3)
    →(2,2,4,3)→(2,2,3,4)。

每一步全部14个globalcuts双向≥2。这也准确说明minimum-origin假设能排除该控制中的同步解锁，但尚未证明它会排除所有L=∅的first-asynchronyfaces。

指定核验：scripts/verify_first_asynchrony_triangle.py，仅检查上述8个coordinate assignments及5个指定history states，不枚举原图全部orientations。完整cut表存data/first_asynchrony_triangle_raw.json，code/raw hashes存data/first_asynchrony_triangle_sha256.json。

## 11. 两个进一步的冻结范围

**Parallel-class corollary。** 对§1的minimum ambient pair，若某parallelclass含K-copy，则该class的所有copies在两端都不可flip；这也适用于整个同步paired orbit。

Proof：K-copy e=u→v在R不可flip，Q中的v→u也不可flip。任何同classcopy的合法性只取决于当前direction与全部cutvalues，不取决于copyidentity。同向e的共同copy在R非法；若在Q合法，就成为Q-only u→v，与§4的outdeg_K(u)=0要求矛盾。反向e的共同copy在Q非法；若在R合法，就成为R-only v→u，与indeg_K(v)=0要求矛盾。其它K-copies本就被minimum distance冻结。∎

若该class只有一条K-copy，其totalmultiplicity m_uv≤2k−1：设R中u→v有α条，v→u有β条。R中e非法的tightblocker要求α≤k；Q中反向e非法要求β+1≤k，所以m_uv=α+β≤2k−1。排除circle后每class至多一K-copy，故h°的pathsupport满足此bound。

**Critical separating shore lock。** 对任意singlepath legalendpointpairR,Q及δ_G(X)=2k+1，若X包含s不包含t，则Rout(X)=k+1、Qout(X)=k。因此任何crossing-X共同copy都不能同步flip，整个同步orbit保留其direction。对偶shore同理。

这扩展§9的criticalsingletonstar锁到所有分离pathendpoints的globalmincuts；没有说这些copies在整个ambientcomponent冻结。也没有把one-sidedlaunch排除掉。多path时只有净endpointimbalance为±1的criticalcut可用同一结论，不能遗漏该条件。
