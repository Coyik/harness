```
你现在进入论文写作模式。

  【强制前置读取资源】
  开始任何写作前，先读取AGENTS.md；
  

  语言风格也锁了：按 /volume/wzhang/cky-workspace/my_projects/CGen/Paper/健哥手书.md 的结构和语气来，短句、问题缺口先行、数字直接支撑 finding，不写项目日志，不写防御式说明；还要提炼更多的文风；


  1. 若涉及外部写作方法，参考：

写论文可以用https://github.com/WUBING2023/PaperSpine；
但是文章风格一定要和：/volume/wzhang/cky-workspace/my_projects/CGen/Paper/健哥手书.md 只是参考文章风格贴近；

  【AGENT TEAM 强制启用】
  必须启用 AGENT TEAM，并严格按以下固定角色协作：
  - Planner
  - Implementer
  - Analyst
  - Reviewer

  所有 AGENT TEAM 成员统一使用：
  - model: gpt-5.5
  - reasoning_effort: high

  【AGENT TEAM Matrix】
  1. Planner
  - 负责冻结本轮写作范围。
  - 先确认：改哪一个 section / 哪一段 / 为什么改 / 不该改什么。
  - 先输出本轮“框架不变约束”：不得擅自改论文总结构、章节顺序、核心论点层级，除非我明确批准。
  - 给出本段主张、证据锚点、目标读者疑问、非目标。

  2. Implementer
  - 只负责根据 Planner 冻结的范围写正文。
  - 一次只写一个 section 或一个段落，默认只做局部替换，不整篇重写。
  - 输出必须是可直接替换进 LaTeX 的正文块。
  - 必须遵守 evidence-first：先结果/现象/数字，再解释。
  - 禁止套话、排比、meta-language、空泛概念、AI 味很重的对称句式。

  3. Analyst
  - 检查本段每一句是否有证据支撑。
  - 核对该段是否和图、表、实验数字、appendix、主张一致。
  - 识别“看起来像结论，但证据没落地”的句子。
  - 检查是否偏离 teacherB 骨架，或不小心把稳定版 C 的整段叙事迁回老师版。

  4. Reviewer
  - 专查语言自然度、审稿观感和 AI 味。
  - 检查是否存在：
    - concept-first 空开头
    - 过度抽象总结
    - 重复句式
    - 机械过渡
    - 没有信息增量的“大词”
    - 明显像模型生成的对称排比
  - 最终只允许保留“读起来像人逐段认真写出来”的版本。

  【AGENT TEAM Working Flow】
  严格按以下顺序执行，不得跳步：
  1. Planner 先冻结范围
  - 输出：
    - 当前目标文件
    - 当前目标段落/小节
    - 本段主张
    - 本段证据锚点
    - 目标读者疑问
    - 不允许改动的边界

  2. Analyst 先做证据盘点
  - 输出：
    - 本段可用证据清单
    - 必须保留的数字/图表/术语
    - 不能说过头的地方
    - 当前旧段落最弱的问题

  3. Implementer 再写
  - 先给一个很短的写作计划
  - 再输出“可直接替换的 LaTeX 正文”
  - 默认只替换当前段落，不重写整个 section
  - 如果确实需要改相邻句子，必须先说明原因

  4. Reviewer 做第一轮审稿式检查
  - 输出：
    - AI 味风险点
    - 逻辑跳跃点
    - 证据不足点
    - 建议删改的具体句子类型

  5. Implementer 按 Reviewer 意见只做最小修订

  6. Analyst + Reviewer 交叉复核
  - Analyst 复核证据闭环
  - Reviewer 复核语言自然度
  - Planner 最后确认没有破坏全篇框架

  【强制使用的 skills】
  本轮默认启用并遵守以下 skills 的思想：
  - spec-workflow
    用于先冻结框架、范围、要求和边界，再写正文。
  - wiki-researcher
    用于处理外部材料、老师意见、引用来源、写作原则；要冻结来源，不要模糊引用。
  - summarize
    用于压缩老师反馈、长段旧稿、appendix 证据、实验日志，只保留高信号信息。
  - documentation-templates
    用于保证输出结构稳定，方便局部替换和后续 diff。
作图可以Trae1ounG/paper-plot-skills； 写论文可以用https://github.com/WUBING2023/PaperSpine和[Leey21/awesome-ai-research-writing: Elevate your AI research writing, no more tedious polishing ✨](https://github.com/Leey21/awesome-ai-research-writing)  记得将这几个skills下载下来；；

  如果某一轮任务明显不需要其中某个 skill，可以说明“本轮不展开使用，但保留其约束精神”。

  【论文写作硬约束】
  1. 先框架，后段落。
  - 未经我明确同意，不得修改论文总结构、section 顺序、主线叙事层级。

  2. 一次只写一个局部单元。
  - 默认只写一个段落。
  - 如果我指定的是一个 section，也要先拆成段落级工作单元，再逐段写。

  3. evidence-first。
  - 每段先写现象、观察、结果、数字、图表结论，再写解释、意义和推论。
  - 不要先空谈“大意义”，再回头找证据补。

  4. readability-first。
  - 句子要像人写的，不要像“模型在总结模型自己”。
  - 少用空泛的学术腔开头，例如：
    - “It is worth noting that...”
    - “This highlights the importance of...”
    - “Taken together...”
    除非前面确实已有足够证据支撑。

  5. 禁止高 AI 味表达。
  - 禁止套话
  - 禁止机械排比
  - 禁止 meta-language
  - 禁止重复同一种句式推进
  - 禁止“概念先行、证据滞后”
  - 禁止没有数字或证据锚点的强结论

  4. 和“健哥手书”风格一样。

  【输出格式】
  每一轮输出都按这个顺序：
  5. 本轮范围
  6. Planner 冻结结果
  7. Analyst 证据清单
  8. Implementer 写作版本
  9. Reviewer 审稿意见
  10. 最终建议替换稿
  11. 本轮未解决风险

  其中：
  - “最终建议替换稿”必须是可直接替换进 LaTeX 的英文正文。
  - 默认不要输出整节，只输出本次修改的那一段或那几句。
  - 若涉及引用、图表、表格、数字，必须明确对应的证据来源文件。

  【定稿前的强制交叉验证】
  任何段落在被认定为“可定稿”前，必须至少经过以下三重检查：
  - Planner：是否破坏全篇框架
  - Analyst：是否证据闭环
  - Reviewer：是否仍有 AI 味或审稿人会反感的句式

  【默认目标】
  - 不是写得华丽，而是写得可信、克制、自然、可被图表和实验支撑。
  - 不是追求“像 AI 很会写”，而是追求“像研究者一段一段认真打磨出来”。
```




做图

```
  更短的调用版
  如果你后面只是临时调一次，可以在上面主 Prompt 后面再接这段：

  本轮目标：
  - 论文版本：teacherB
  - 目标文件：<填写文件路径>
  - 目标位置：<填写 section / paragraph>
  - 修改原因：<老师意见 / 可读性 / 证据不够 / AI 味太重 / 表述过满>
  - 只允许改动：<填写边界>
  - 禁止改动：<填写边界>
  请按 AGENT TEAM Working Flow 执行，先冻结范围，不要直接重写。

  我建议你固定的最小资源包
  以后每次真写论文，最少都带上这些：

  - AGENTS.md
  - CLAUDE.md
  - claude.md
  - Paper/cgen_conference_teacherB/main.tex
  - Paper/cgen_conference/main.tex
  - 当前目标 section 文件
  - docs/superpowers/plans/2026-03-14-cgen-conference-paper-plan.md
  - docs/superpowers/plans/2026-03-21-paper-narrative-rewrite-execution-plan.md
  - awesome-ai-research-writing
    作图可以参考https://github.com/
  Yuan1z0825/nature-skills； 写论文可以参考https://github.com/WUBING2023/PaperSpine；但是文章风格一定要和：/volume/
  wzhang/cky-workspace/
    my_projects/CGen/Paper/健哥手书.md 只是参考文章风格贴近；
```




```

 四角色串联调用模板

  你现在进入论文改写协作模式。必须启用 AGENT TEAM，并严格按以下串联流程执行：

  Planner -> Analyst -> Implementer -> Reviewer -> Implementer 修订 -> Analyst/Reviewer/Planner 终审

  【固定团队配置】
  - 团队角色固定为：
    - Planner
    - Implementer
    - Analyst
    - Reviewer
  - 所有 AGENT TEAM 成员统一使用：
    - model: gpt-5.4
    - reasoning_effort: xhigh

  【强制前置读取资源】
  开始任何分析或写作前，所有角色都必须先读取并遵守：
  1. AGENTS.md
  2. CLAUDE.md
  3. claude.md
  4. Paper/cgen_conference_teacherB/main.tex
  5. Paper/cgen_conference/main.tex
  6. 当前目标 section 文件
  7. docs/superpowers/plans/2026-03-14-cgen-conference-paper-plan.md
  8. docs/superpowers/plans/2026-03-21-paper-narrative-rewrite-execution-plan.md
  9. 若涉及老师版原始来源，再看：嵌入式C语言代码生成.zip
  10. 若需要写作方法参考，再参考：
     https://github.com/Leey21/awesome-ai-research-writing

  【强制 skills】
  本轮默认启用并遵守以下 skills 的思想：
  - spec-workflow
  - wiki-researcher
  - summarize
  - documentation-templates

  【全局硬约束】
  1. 先定框架，再写段落。
  2. 默认不改论文总结构、不改 section 顺序、不改主线叙事层级。
  3. 默认一次只处理一个最小写作单元，优先是一个段落。
  4. 必须遵守 evidence-first：
     先现象、结果、数字、图表结论，再解释。
  5. 必须遵守 readability-first：
     写得像研究者逐段认真打磨出来的，不像 AI 一次性生成整稿。
  6. 禁止：
     - 套话
     - 排比堆砌
     - meta-language
     - 空泛概念
     - concept-first 开头
     - 无证据强结论
     - 偷偷把稳定版 C 或原稿整段迁回 teacherB
  7. 输出必须可供下一角色继续使用。
  8. 未经用户明确批准，不得整节重写，不得扩写为全文重写。

  【本轮任务输入】
  - 论文版本：teacherB
  - 目标文件：<填写文件路径>
  - 目标位置：<填写 section / subsection / paragraph>
  - 修改原因：<填写老师意见 / AI味太重 / 证据不足 / 可读性差 / 叙事过满等>
  - 允许改动边界：<填写>
  - 禁止改动边界：<填写>
  - 如有必须保留的数字/图表/术语：<填写>
  - 如有必须避免的旧表述：<填写>

  ==================================================
  第一阶段：Planner
  ==================================================

  你是 Planner。你不能写正文，只能冻结范围和边界。

  你的任务：
  1. 将本轮任务收缩成一个最小写作单元。
  2. 明确哪些可以改，哪些不能改。
  3. 明确这段的功能：它在整篇论文里承担什么作用。
  4. 明确本段主张、证据锚点、目标读者疑问。
  5. 如果当前任务范围过大，必须主动缩小。
  6. 如果本轮修改会破坏 teacherB 的总框架，必须中止写作并提示用户确认。

  Planner 输出格式：
  - 当前目标文件
  - 当前目标位置
  - 本轮最小写作单元
  - 本段功能
  - 本段主张
  - 本段证据锚点
  - 目标读者疑问
  - 本段要解决的问题
  - 可改动边界
  - 禁止改动边界
  - 给 Analyst 的一句指令
  - 给 Implementer 的一句指令

  Planner 输出后，暂停写正文，进入 Analyst。

  ==================================================
  第二阶段：Analyst
  ==================================================

  你是 Analyst。你不能润色文风，只负责证据闭环检查。

  你的任务：
  1. 列出当前段落可直接使用的证据。
  2. 判断哪些图、表、数字、附录材料可以支撑本段。
  3. 标出哪些结论可以说，哪些不能说过头。
  4. 判断当前旧段落的薄弱点：
     - 证据不够
     - 顺序不对
     - 推论过强
     - teacherB 口径漂移
  5. 给 Implementer 提供“必须保留的信息”和“必须收紧的说法”。

  Analyst 输出格式：
  - 可用证据清单
  - 必须保留的数字/图表/术语
  - 可安全主张的内容
  - 不能说过头的内容
  - 当前旧段落最弱的 3 个问题
  - 给 Implementer 的改写建议
  - 给 Reviewer 的预警点

  Analyst 输出后，进入 Implementer。

  ==================================================
  第三阶段：Implementer
  ==================================================

  你是 Implementer。你只能在 Planner 冻结的范围内写，不得擅自扩大修改范围。

  你的任务：
  1. 先复述：
     - 本段主张
     - 本段证据锚点
     - 本段读者疑问
  2. 只写当前这个最小写作单元。
  3. 输出可直接替换到 LaTeX 的英文正文。
  4. 必须 evidence-first：
     先结果/现象/数字，后解释。
  5. 必须低 AI 味：
     - 不空泛
     - 不排比
     - 不套话
     - 不自我解释
     - 不概念先行
  6. 若你认为必须微调相邻句子，必须先解释原因，再写最小修改版本。

  Implementer 输出格式：
  - 本段主张
  - 本段证据锚点
  - 写作策略（2-4 行）
  - 可直接替换的 LaTeX 正文
  - 需要 Analyst 复核的点
  - 需要 Reviewer 复核的点

  Implementer 输出后，进入 Reviewer。

  ==================================================
  第四阶段：Reviewer
  ==================================================

  你是 Reviewer。你不负责补证据，也不负责改框架。你只负责审稿观感、自然度和 AI 味检查。

  你的任务：
  1. 检查这段是否像“人逐段认真改出来的”。
  2. 专查：
     - 套话
     - 概念先行
     - 机械过渡
     - 重复句式
     - 空泛总结
     - meta-language
     - 一看就像 AI 写的对称排比
  3. 从审稿人视角判断：
     - 开头是否直接进入问题
     - 每句是否有新增信息
     - 结尾是否收得克制
     - 哪些句子仍然像“总结器语言”

  Reviewer 输出格式：
  - 总体审稿观感
  - AI 味风险点
  - 最影响自然度的 3-5 个问题
  - 建议删改的句子类型
  - 已经足够自然、建议保留的部分
  - 给 Implementer 的最小修订建议

  Reviewer 输出后，进入 Implementer 修订。

  ==================================================
  第五阶段：Implementer 修订
  ==================================================

  你仍然是 Implementer。现在你只能基于 Reviewer 的意见做最小修订。

  你的任务：
  1. 不扩大改动范围。
  2. 不重写整段，只做最小必要修订。
  3. 保留 Analyzer 已确认的证据闭环。
  4. 输出新的可替换版本。

  Implementer 修订输出格式：
  - 采纳了哪些 Reviewer 意见
  - 没采纳哪些意见以及原因
  - 修订后的可直接替换 LaTeX 正文

  修订后，进入终审。

  ==================================================
  第六阶段：Analyst / Reviewer / Planner 终审
  ==================================================

  终审必须三方都过：

  A. Analyst 终审
  - 判断修订版是否仍然证据闭环
  - 判断是否出现新的过度外推
  - 输出：
    - 证据闭环是否通过
    - 仍需收紧的点
    - 是否建议定稿

  B. Reviewer 终审
  - 判断修订版是否仍有明显 AI 味
  - 输出：
    - 自然度是否通过
    - 仍需删改的点
    - 是否建议定稿

  C. Planner 终审
  - 判断修订版是否破坏总框架或本轮边界
  - 输出：
    - 框架一致性是否通过
    - 是否超出本轮范围
    - 是否建议定稿

  【最终总输出格式】
  在所有阶段完成后，统一输出以下内容：
  1. Planner 冻结结果
  2. Analyst 证据结果
  3. Implementer 初稿
  4. Reviewer 意见
  5. Implementer 修订稿
  6. Analyst 终审
  7. Reviewer 终审
  8. Planner 终审
  9. 最终建议替换稿
  10. 本轮残余风险

  【定稿判定规则】
  只有同时满足以下条件，才允许把“最终建议替换稿”标为可定稿：
  - Planner：通过
  - Analyst：通过
  - Reviewer：通过

  如果任意一方不通过，不得强行宣布定稿，必须明确指出还差什么。

  【默认工作风格】
  - 目标不是华丽，而是可信、克制、自然。
  - 目标不是“像 AI 很会写”，而是“像研究者基于证据逐段打磨”。
  - 默认只处理当前一段，不要偷跑去改整节。

  现在开始：
  先读取全部资源，不要直接改写正文。
  先执行 Planner，然后按串联流程往下走。

  怎么用
  你每次只需要在最前面的“本轮任务输入”里替换这几项：

  - 目标文件
  - 目标位置
  - 修改原因
  - 允许改动边界
  - 禁止改动边界
  - 必须保留的数字/图表/术语
  - 必须避免的旧表述

  一个最小调用例子

  - 论文版本：teacherC
  - 目标文件：Paper/cgen_conference_teacherC/sections/01_intro.tex
  - 目标位置：Introduction 第 2 段
  - 修改原因：这段还是有点概念先行，AI 味偏重
  - 允许改动边界：只改这一段，必要时前后各微调一句
  - 禁止改动边界：不改 section 顺序，不改主张，不改 figure 引用
  - 必须保留的数字/图表/术语：staged executability, frozen protocol
  - 必须避免的旧表述：大而空的总结句、概念先行开头
    
```