# 持续研究日志

## 2026-10-02：环境热身

当前用户要求是先检查创建文件、写小程序和运行程序等功能。已读取用户附加的详细研究提示词；发生冲突时，以用户此前口述要求及当前明确指令为准。

后续研究约定：理论推导与证明核验为主；小规模计算需有明确数学目标；路线卡住时记录具体障碍并切换，之后可以返回；持续保存证明、失败原因和原始结果。推导卡住本身不构成将路线标为 FALSE 或 DEAD 的理由。

### 环境测试设计

- 所有新增文件均放在本“问题”文件夹内。
- 测试图：两个顶点、五条有身份的平行物理边，取 k=2。
- 搜索空间：恰好 32 个定向，只用于环境及基础合法性检查，不计作主问题新成果。
- Python 对全部非空真子集直接计算出割；C++ 使用此二顶点图的等价出度条件。
- 两份程序分别建立合法单边翻转图并计算连通分量与直径；Python 比对两份结果，保存原始 JSON、完整小图邻接表及 SHA-256 清单。
- 组合论预期：合法定向为大小 2 或 3 的子集，共 20 个，每个度数 3，共 30 条无向邻接边；图连通，直径 5。

### 环境测试结果：PASS

- Python 3.14.7 可运行；g++ 16.2.0 可编译并运行 C++17 程序。
- 初次编译将含中文的相对路径直接传给链接器，链接器出现路径编码错误，未生成可执行文件。解决办法：把工作目录设为 `问题/data`，传入纯 ASCII 相对参数 `../scripts/environment_probe.cpp` 与 `environment_probe.exe`。这不需要移动研究文件。
- 修正后的编译成功，无编译警告；Python 与 C++ 结果完全一致：32 个定向中 20 个合法，翻转图有 30 条无向边、1 个连通分量，直径为 5。
- JSON 文件写入后已重新读取并比较成功；5 个代码、可执行文件及原始结果文件的 SHA-256 已保存。
- 独立组合核验：任意合法子集 S、T，可交替添加 T\S 中的元素与删除 S\T 中的元素，从大小 2 开始时先添加，从大小 3 开始时先删除，故距离恰为对称差大小。互补的二元集与三元集距离为 5。
- 测试范围只有一个二顶点图；它验证运行环境和基础程序逻辑，不解决主研究问题。

复现（工作目录设为本文件夹的 `data` 子目录）：

```powershell
g++ -std=c++17 -O2 -Wall -Wextra -pedantic ../scripts/environment_probe.cpp -o environment_probe.exe
python ../scripts/environment_probe.py
```

## 2026-10-02：持续研究正式开始

- 已建立持续研究目标；不以一次局部结果作为结束理由。
- 完整主档分成四个阅读区间，分别结合 R0、X* 两个 common-fiber 分支与基础割公式独立审计。
- 新建 `research_dependency_map.md`，区分主档最新层、历史层与用户附加提示中尚缺证明的数据。
- 发现主档只摘要使用 source-free / zero-extreme，没有完整定义；本轮使用的具体谓词已明写入依赖图。
- 基础审计已得到 q、μ、partition/co-partition slack 的精确公式。过程中独立核对纠正了协调消息里 Φ 的符号，文件采用正确版本。
- R0 分支出现一个简短的结构性排除：若每个 Zi 都与 R0 相交，cross-free 使每个 MAIN row 完全落在一个 Zi 或 Q；Q 又被 MAIN 覆盖，因此 Zi 与 Q 内 MAIN rows 直接构成 actual-tight partition。完整证明、推广范围和独立复核继续进行。

## 2026-10-02：用户交付二次审计修订版，研究前沿更新

- 原始修订版来自 `D:/Users/Downloads/graph_orientation_reconfiguration_progress_2026-10-02_revised.md`，已原样复制到本“问题”文件夹，同名保存。旧档和本轮已有推导保留。
- 完整读取修订版 current layer（第 1–1469 行），按数学内容更新状态；文件内的操作性提示不替代用户直接要求。
- 新版严格定义了 source-free / zero-extreme：source 判断使用 retained extra 的负号集，MAIN 正作用另作触发；zero-extreme 同时排除 all-zero 与 all-one atom。本轮先前证明使用的是较弱 full-row source-free；新版更强条件蕴含它，但正式引用须改为新版准确谓词。
- 新版确认 all-t selected pure-cycle program 与 k=2、|A|=5、m=2 classified universe 已关闭，故不再重复这些搜索。本轮的 R0 / X* 证明作为独立重建记录，不能冒称修订版之后的新发现。
- 当前首要目标改为 source-resurrection / guard closure；并行研究 terminal positive-incidence barrier 与外部 polyhedral scope。
- 初步得到精确逻辑接口：source-free 子族满足 dual-Horn clauses；其补集满足删除传播的 Horn rules，给出候选 universe 内唯一最大的 source-free 子族。guard 加法选择不唯一的困难与此 canonical 删除规则要分开。
- 修订版声称 guard 加法未证明 cross-free 保持及有限终止；若只加入原始 cross-free actual-tight E 的 rows 且当前 D 固定，前两点其实自动成立（子族仍 cross-free / actual-tight，每次新加入一行，至多 |E| 步）。仍缺的是 proper useful closure、选择无关性及 global necessity bridge。

### Guard 接口与 Atom Budget checkpoint

- 已保存小型算法核验代码和 raw JSON。741 个三行二-signature systems、5928 个候选 universe、15903 个 union-model pairs 全通过，运行约 0.03 秒。目标仅为 falsify 删除传播算法与 union-closure theorem，没有重型图枚举。
- 新独立符号定理 `research_atom_budget.md`：source-free actual-tight rows 的跨 membership-atom 边必须至少消费一个紧行；割连通度的 atom-degree lower bound 与 tight-row upper bound合成 n≤t。多负号 guard 每多消费一行给额外 surcharge σ。
- bare three-row/four-atom source-resurrection sign example 与 bare four-row/five-atom multi-SCC example 都在 genuine terminal 层被该预算排除。仍需 guard/MAIN 扩展与 empty-tree-node 结构分析，不能以此宣布全部 closure 不存在。
- terminal-debt 分支出现 k=4、A=5 的真实临界对跖 Debt=2 构造；正进行逐割与显式合法路径核验，预计可关闭修订版的一项 terminal dual OPEN，而不触碰 minimum-component-origin OPEN。

### 静态闭合、无界服务与动态前沿

- CFST完整闭合并经两支独立审计：cross-free actual-tight family有至少 ceil((n−1)/2)条 strict sources，empty-node q packing与 negative-pair packing解决全部 guards。证明不需要selected minimal core。
- Root再独立逐案审计corner compatibility；negative blocker可相对任意retained cross-free T uncross成compatible guard。maximal T精确covers所有illegal internaledges。initial full fixed-outside fiber无isolated state已由两种proof闭合，主connectivity仍OPEN。
- Genuine terminal-antipodal Debt=2核验后扩为任意L；构造又从k≥4加强到任意k≥2、固定k=2也无界。two-edge directedphysicalpath同样实现。24个预指定案例逐割核验通过，显式word连接展示的两个endpoints；没有heavy graph enumeration。
- Dual all-y positive-incidence量词已修正，exact antipodalidentity保留−S_barR；complementpair-free unboundedcontrols说明normalizedterminal-only常数barrier也失败。
- Global primalintegrality / necessarysupport由独立uncross+networkTU proof归档；一般integer crossing-supermod demand box也integral，非负性无需用于该primal结论。dual-TDI与B+不自动随之关闭。
- 新闭合relative strict existence：全部内部µ≥2时存在slack≥1的同outside内部定向。两条proof分别是primaryorientationminmax，以及root独立fractionalεLP/extendedCFST+integerextraction。任意D到strict target的singleflipreachability待研究。
- 动态SAFE-STEM与对偶SAFE-SINK提供允许任意长path的serialization充分条件。minimumseparatingcircuit两端cuts相同，Jwords同步，minimumHammingdistance强迫整个componentKimmutable；必须用这个全orbit必要条件寻找finiteescape，不能把frozenfacecontrols误当fullcomponents。
- 已同步本文件夹修订master的A0.2、D0.8、H0.4、K0与模型状态；下载目录中的用户原稿保持原样。所有proof / raw / scripts仍在同一个“问题”文件夹。

### µ≥2 动态子类闭合与一般临界层继续研究

- Strict degree polytope的unit-root directions及integer routing已证明；全部strict targets属于同一个原始physical flip component。Initial全fiber在legal-endpoint single-path/circuit macros下连通，singleflip前缀仍需额外bridge。
- 本次继续完成relative reachability候选的第二轮审计：proper与artificial混合container路径、retained minimal row被new subset夺去minimality的反查、标签no-fork及HEAVY阶段消灭全部闭合。完整proof存`research_relative_reachability_audit.md`。
- 因而all-proper-µ≥2时，任意合法initial state可augment到strict，word长度≤n²(n−1)²；配合unique strict component，该范围H1升级PROVED。没有把一般µ1问题或signed descendant H1升级。
- 新指定HEAVY birth control使宏势3→4→0，确认必须按完整阶段下降。5个prescribed states、每state全部30个global cuts及14个residual rows通过；没有重型穷举。
- 现继续研究µ1临界割如何收缩及boundary flips如何lift；不是以µ2局部定理结束研究。

- Criticalblock严格时所有globaltightcuts respect contraction，quotientflip可lift；结合µ2 fiber theorem，minimumcounterexample所有inclusion-minimalmincutshores必须singletons。Oddmincutcrossfree也已独立推导。
- Globalproper safe endpoints可扩至λ2k+1，但route必须保持root-excludedfamily；不把unionV时out(V)=0误用成k。Anchoredcleanmacros的criticalrow只换色、v可不降，这是一般µ1的真正剩余障碍。
- Degree-only all-oddbalancedorientation connectivity已有完整controlproof；多packetword可能损全局cut多于1，不能升级main。
- 回到dual/guard路线得到精确缺口：CFST的relativepositive source加zero-weightguards后可能只获得originalgradient0的legalcopy。指定k2L2、Debt1 certificate已核验；它非optimal、不冒充minimum-origin反例。
- 新归档optimalguardpositive iff universallytight-on-optimal-primalface，以及lexoptimalcompletiondifference DAG。尚需把universalguards与selectedgainwitness组成finitehistory，不以静态DAG代替动态proof。

## 2026-10-03：以原始 MAIN 为主任务的综合 sprint

- 完整读取新用户任务和当前最高优先级报告/引用proof，固定图最小性(|V|,|E|)，不同定向对最小性分别命名h、h_r、h°、ℓ°。
- 不派生新子代理。继续在同一“问题”目录写proof，不把有限搜索作为主策略。
- common-S形式不变性通过，但completeinitial全Jclosed+全部Kblocked会构成任意actualtightsourcefree族；直接tightcorneruncross排除它，所以不得假定这种S已经存在。
- atomproduct完成，projection可制造μ_B0；15copy genuineμ2control和四步ambientword逐割PASS。
- balancedevenroot任意signatureextension、B+commoncompletion及outside nonboundarylift完整闭合，mixed/rootcontaining/co-covercuts均审计。
- |A|≤3fullfiber连通，全局|V|≤4完成。两预选五顶点13edge图全状态检查PASS，但随后用degreeonlyserialization理论排除整个5k+3边层。k2第一未统一分类层为14edges。
- primarypairinginput核对；canonicaltarget存在性完成，任意Eulerianprefixprojectionshortcut由11copy控制否定，指定合法rotation逐割PASS。
- 允许根边临时缓冲的RSM是比fixed-rootfiberH1更弱的主接口；已给RSM与原始MAIN在reduced-class上的完整等价归约。
- 边最小性新推导：非mincutcopies的deletablestates共用C°；存在E°时最短跨C°macro不能是圈，可选singlepath。路径只能直接冻结端边，allcriticaledge图没有该锚，保留这两个scope。
- 综合交付FINAL C，详见《原定理综合研究与唯一剩余接口_2026-10-03.md》；原始MAIN仍OPEN，没有伪称完成或环境反例。下一attack为锚路径asymmetry或root-returnpolarityhistory。

## 2026-10-03：五顶点全闭合、六顶点入口与网页端交接

- 后续完成 first-asynchrony 几何、完整 virtual signature 与任意 compatible critical rootstar 的共同 Euler 扩张。规范圈控制给任意 k≥2 的合法四步词；arbitrary signed μ≥2 冻结纤维连通的强化已否定。
- 五顶点 5k+4 边中间层推进后，抽取 general dominant-neighbor contraction：m_ab≥deg(b)−k 时完整 pair fiber 为宽度≥1的区间，相邻纤维相交，商图实际词可提升。
- heavy-star interval/intersection 与 heavy-triangle 删除锚/全局原子预算完成全部五顶点原始 MAIN，任意 k≥2 及物理平行边重数。此前14/15边前沿已被替代。
- 六顶点有 nontrivial L-mincut 的全部实例闭合；六顶点 L-regular / 6k+3最小边数层闭合；6k+4边的excess(2,0,0,0,0,0)模式闭合。
- 六顶点6k+4边的excess(1,1,0,0,0,0)仍OPEN。中断前关于异常三点割分类、区间端层经中层同步、三点degree fiber的续推尚未形成完整证明，也没有运行新核验；已明确作为候选保存到交接稿第11节。
- 用户当前要求输出本轮总结与问题引入，以便改在网页版Work接续。已创建《本轮研究总结与审计状态_2026-10-03.md》《网页版Work研究交接_问题引入与继续任务_2026-10-03.md》及资料包说明。
- 交接重新校验已有计算记录的版本哈希，保留原始修订档副本，更新当前manifest并制作可移植ZIP。没有新增重型穷举，没有把未执行核验写为PASS。
- 一般MAIN与RSM仍OPEN，无真实环境反例；制作交接文件不表示原题目标完成。
