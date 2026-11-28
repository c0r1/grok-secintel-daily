**【CyberSec 情报速报 | 云安全 & AI 重点强化】**

> 生成时间: 2026-11-28 16:52:36 UTC+08:00

**统计范围**: 2026-11-25 - 2026-11-28（包含起止日，共约 3-4 天数据）
**本期热度峰值**: 最高 👍 136 | 最高 👀 未披露
**今日情报眼**: 账号被控与云Critical并行

---

**📋 生成说明**
本报告由多份公开情报草稿合并、去重、排序而成。技术细节未经人工复现，仅供防御参考。只保留能对应到原帖或原页、且发布时间落在统计窗口内的条目。互动数只取各版本明确写出的数值并取最大值；缺失标「未披露」，不估算。浏览量在已给出的原帖指标中均未出现，一律「未披露」。窗口外背景标 **[历史参考]**，不计入热度峰值。不收录利用步骤或 PoC。

---

**💰 本期最高赏金 / 最炸裂 payout**
- 奖池抬至 $125,000（尚未兑现 Critical） | 社区 | Immunefi / Base Everest | 135K+ 行 Rust/Solidity 中 0 个 Critical；2 个 High 解锁半池，满池 $250,000 仍空
  - 💡 一句话总结: 窗口内最高公开奖池，但是竞赛额度不是已支付账单 | 👍 82 | 🔄 8 | 👀 未披露
  - 🔗 来源: https://x.com/immunefi/status/2125658301077880929 | 📅 2026-11-25
- $21,526（审计赛头名，非单漏洞披露赏金） | @xdeltabear | Immunefi / Plether | 上线前 Critical：缺少时间限制，交易者可在利好前双向下注，赢侧按旧价格成交、输侧全额退回，反复抽取资金池
  - 💡 一句话总结: 310 名研究员、1,391 份报告、18 个独立 Critical，均在主网上线前拦住；其后名次见猎人板块 | 👍 77 | 🔄 13 | 👀 未披露
  - 🔗 来源: https://x.com/immunefi/status/2126291471267770406 | 📅 2026-11-27
- 不记为实付：$1,100,000 仅为档位上限 | — | Immunefi / Beanstalk | bugbounty.fyi 记 11-25 新增 Critical 档；另有页面显示项目 Closed，且委员会文本按 Beans 计价
  - 💡 一句话总结: 上限变更，不能当成已到账美元赏金 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?show=rewards&dir=up&since=1 | 📅 2026-11-25

---

**☁️ 云安全重点(特别加强板块)**
- Wiz：攻击框架 Intent ID 泄漏进受害者日志（ARTEX / Cairn）
  - 🌟 亮点总结: agentic 攻击框架会把内部计数器 iNNNN 写进受害端日志。防御价值是用该计数对齐节奏、把跨云入侵串成同一操作者，并和人工操作区分；日志被清洗或跨工具拼接后信号会失效。不是新的云接管手法。窗口内研究帖互动最高。 | 👍 132 | 🔄 26 | 👀 未披露
  - 🔗 来源: https://www.wiz.io/blog/agentic-offensive-frameworks-intent-ids-artex-cairn （@wiz_io，2026-11-25 19:57 UTC） | 📅 2026-11-25
- CVE-2026-85258 Vertex AI Assistant 私有控制台 API 缺少授权（CVSS 4.0 9.3）
  - 🌟 亮点总结: 未认证远程调用即可列出、读取、创建并发送他人聊天会话中的消息，属于云上 AI 会话接管，不是模型越狱。Google 写明 2026-04-13 已在服务端修复，客户无需操作；11-27 才发 CVE。公开索引未见 KEV、未见 PoC。报告人 Arvin Shivram。 | 👍 56 | 🔄 9 | 👀 未披露
  - 🔗 来源: https://x.com/cvedotnow/status/2126406308408463686 ；记录 https://www.cve.org/CVERecord?id=CVE-2026-85258 | 📅 2026-11-27
- CVE-2026-110739 GKE Fleet 命名空间接入可升至 project owner（CVSS 4.0 9.0）
  - 🌟 亮点总结: 低权限已认证主体借助 namespace onboarding API 的输入校验缺口（拒绝名单不完整），可升到项目 Owner。服务端补丁日为 2026-09-25，Google 称客户无需动作；11-27 公开。未见在野利用、未见 KEV、未见公开 PoC。报告人 asterfiester。与上条同日构成 GCP 控制面补披露。 | 👍 56 | 🔄 9 | 👀 未披露
  - 🔗 来源: https://x.com/cvedotnow/status/2126406308408463686 ；记录 https://www.cve.org/CVERecord?id=CVE-2026-110739 | 📅 2026-11-27
- Radware Cloud WAF：内网管理 API 暴露到公网且无认证
  - 🌟 亮点总结: 入侵发生在 11-19（约 10 小时后封堵），窗口内仍在通报。可能触及客户联系方式，以及部分客户用于日志外送的 AWS S3、Azure Blob/SAS、SFTP 凭据。厂商称流量检测、证书、终端用户数据与客户应用流量未暴露，但已有客户收到陌生 IP 访问日志桶的 AWS 告警。处置只做凭据轮换与自 11-19 起的存储访问日志核查。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://x.com/Sujeet/status/2126189036272521701 | 📅 2026-11-27
- AWS Kiro Web：间接内容触发托管环境命令执行（CVE-2026-136267，CVSS 3.1 为 8.8）
  - 🌟 亮点总结: 云托管 AI IDE 在处理仓库文件或网页等会话内容时，未把工具调用标记与数据隔离开。特定模型会把标记复述出来并在订阅者的托管开发环境中当命令执行，且不弹同意提示。影响窗口为 2026-05-18 至 2026-10-30，涉及 DeepSeek v3.2、GLM-5、MiniMax M2.1/M2.5、Qwen3-coder-next。AWS 称 10 月 30 日已在服务侧修复，客户无需动作。已修复披露，不是新的可打入口。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://aws.amazon.com/security/security-bulletins/2026-202-aws/ | 📅 2026-11-25
- Google Cloud Application Integration 不安全反序列化（CVE-2026-106169）
  - 🌟 亮点总结: 与上述 GCP Critical 同窗口被一并点名，影响为 RCE，涉及 2026-09-22 前版本。处置重点是核对是否仍有未升级的滞留组件，而不是把旧洞当成新 0day。草稿未给 CVSS、互动与 PoC。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://x.com/cvedotnow/status/2126406308408463686 | 📅 2026-11-27
- AI Agent 工具面入口（MCP）
  - 🌟 亮点总结: GitLab MCP OAuth 的 SSRF（CVE-2026-135221，2026-11-25 修复，已认证用户可打到内网）；一组 Crypto APIs MCP 包在 HTTP 模式绑定 0.0.0.0 且不鉴权（CVE-2026-138026，2026-11-27）。共同模式是「Agent 工具面 = 云凭据与内网的新入口」，而不是传统 IMDSv1。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://theinjection.dev/category/vulnerability/ | 📅 2026-11-25

---

**📚 最值得读的 Writeup / 公开报告**
- Inside Agentic Offensive Frameworks: Intent IDs（Wiz）
  - 📝 技术摘要: 进攻框架用单调 Intent 计数器标记每一步自动化动作，计数会漏进云日志、代理和主机遥测。防御方可按计数区间还原同一次任务、判断并行度，并在计数跳变时怀疑多操作者共用同一框架。计数被重写、日志采样或跨账号拼接后，关联会断。 | 👍 132 | 🔄 26 | 👀 未披露
  - 🔗 链接: https://www.wiz.io/blog/agentic-offensive-frameworks-intent-ids-artex-cairn | 📅 2026-11-25
- Bugcrowd：CISA 联邦 VDP 五年数
  - 📝 技术摘要: 44,493 份报告、5,700+ 有效披露、5,300+ 已修复。说明的是规模化协调披露，不是新利用技术。 | 👍 38 | 🔄 1 | 👀 未披露
  - 🔗 链接: https://x.com/mdp_sec/status/2125707293648134511 （页内引用 @Bugcrowd，2026-11-25 19:31 UTC；原帖状态 ID 未单独返回） | 📅 2026-11-25
- YesWeHack：Claude Code、Codex、Gemini CLI 盲测 PortSwigger 实验环境
  - 📝 技术摘要: 三款编码 agent 都能指出实验环境中的隐藏漏洞，差异在后续利用完成度。适合作为「发现 ≠ 可提交」的对照，不提供实验步骤。 | 👍 35 | 🔄 3 | 👀 未披露
  - 🔗 链接: https://x.com/yeswehack/status/2126228439648870878 | 📅 2026-11-27
- Intigriti Bug Bytes #242
  - 📝 技术摘要: 月报级索引，不是单点复现。窗口内值得跟的四条只保留题目级：Optimizely 向 178 家机构下发恶意 JavaScript；22 年历史的 PostgreSQL 类型混淆被推进到 RCE；GitHub Actions 链可给 Codex 埋后门；不依赖等号的 innerHTML XSS。另有编码 agent 在任务外联时把用户邮箱放进 HTTP 请求头。此处不展开利用链。 | 👍 6 | 🔄 2 | 👀 未披露
  - 🔗 链接: https://www.intigriti.com/researchers/blog/bug-bytes/intigriti-bug-bytes-242-november-2026 | 📅 2026-11-27
- PolinRider：伪造开发者身份的 GitHub 供应链活动（Apiiro）
  - 📝 技术摘要: Apiiro 给出下界约 7,609 个仓库、2,330 个账号；加载器在 10-27 至 11-06 被推入约 2,040 个仓库，约 86% 落在超过一年的真实个人账号。提交可被改写到受害者名下并回写日期。GitHub 于 2026-11-25 暂停相关账号并撤下其 PR。影响是开发者凭据与下游构建物被偷，不是 GitHub 平台 0day。此处不展开加载器与后续阶段。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://apiiro.com/blog/polinrider-north-korea-worm-forged-github-commits | 📅 2026-11-26

---

**🔥 社区热议的技术话题或新手法**
- Agentic 攻击框架的日志指纹
  - 💬 讨论核心: 社区把 ARTEX/Cairn 的 Intent ID 当成防御关联信号：同一计数器可把多云日志串起来，并判断操作节奏。讨论点是检测与分桶，不是框架用法，也不是单独定性的 IOC。 | 👍 132 | 🔄 26 | 👀 未披露
  - 🔗 代表性推文: https://www.wiz.io/blog/agentic-offensive-frameworks-intent-ids-artex-cairn | 📅 2026-11-25
- 云上 AI 控制面鉴权，而不是 Prompt Injection
  - 💬 讨论核心: 本期可核实的 Critical 落在 Vertex AI 私有 API 缺授权和 GKE Fleet 权限提升。模型越狱仍是长线话题，但窗口内高影响事件是云 API 与 Kubernetes 控制面。 | 👍 56 | 🔄 9 | 👀 未披露
  - 🔗 代表性推文: https://x.com/cvedotnow/status/2126406308408463686 | 📅 2026-11-27
- 编码 agent 会不会自己越界打目标
  - 💬 讨论核心: Intigriti 线程强调先在同范围、同速率的受控环境里验证 agent，再对准真实项目；主动利用前要人工确认，并留下 HTTP/决策日志。YesWeHack 的实验环境对照是同一讨论的数据点。 | 👍 35 | 🔄 3 | 👀 未披露
  - 🔗 代表性推文: https://x.com/yeswehack/status/2126228439648870878 | 📅 2026-11-27
- 安全厂商自己的「内部 API 公网无认证」
  - 💬 讨论核心: Radware 事件被用来强调：WAF 厂商的管理面如果无认证暴露，客户侧 S3/Blob 日志密钥会变成第二现场。处置共识是轮换外送凭据并回看存储日志。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性推文: https://x.com/Sujeet/status/2126189036272521701 | 📅 2026-11-27
- 应用层 ADR，而不是再堆一层云告警
  - 💬 讨论核心: Wiz ADR 主张用调用栈和父子进程解释运行时告警，直接针对 Agent 拉起 shell、反序列化、动态执行。属检测产品讨论，不是新漏洞。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性推文: https://www.sdxcentral.com/news/wiz-fights-rogue-agents-and-bad-spawns-with-adr-addition/ | 📅 2026-11-26

---

**🆕 新上线 / 更新中的 Bug Bounty 或 VDP 项目**
- Base Everest 审计赛（进行中）
  - 📝 更新点: 奖池已解锁 $125,000，Critical 仍为 0，剩余 $125,000 未解锁；窗口内剩余时间不足 6 天。 | 👍 82 | 🔄 8 | 👀 未披露
  - 🔗 来源: https://x.com/immunefi/status/2125658301077880929 | 📅 2026-11-25
- Lido Lend（Immunefi）新公开
  - 📝 更新点: 2026-11-27 上线。合约 Critical 为受影响资金的 10%，下限 $20,000、上限 $2,000,000；Web Critical 最高 $100,000。基于修改过的 Morpho Blue fork，范围含合约仓库、IRM、markets、guardian daemon 与 https://lend.lido.fi。无 KYC。全级别要求 PoC；已知审计问题不计赏金。这是项目天花板，不是已到账赏金。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://immunefi.com/bug-bounty/lido-lend/information/ | 📅 2026-11-27
- Beanstalk（Immunefi）Critical 档被记入追踪
  - 📝 更新点: 页面记「新增 Critical，上限 $1,100,000」。与 Closed 状态、Beans 计价并存。投前以 Immunefi 当前政策为准，不能按美元实付理解。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/programs/beanstalk | 📅 2026-11-25
- Optimism（Immunefi）范围扩张
  - 📝 更新点: 跟踪页记 +34 in scope，天花板仍约 $2,000,000。具体资产以 Immunefi 当时页面为准；未见同步的赏金结构说明帖。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/ | 📅 2026-11-27
- Deriv.com（HackerOne）上调赏金
  - 📝 更新点: Critical 上限 $5,000 → $7,500；High 上限 $2,500 → $3,000。幅度有限，但是窗口内少数可核对的现金档上调。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?show=rewards&dir=up&since=1 | 📅 2026-11-26

---

**📢 平台动态 & 政策变化**
- HackerOne 累计赏金越过 $550M（2016 年蛋糕对应的是 $10M） | HackerOne | 👍 136 | 🔄 6 | 👀 未披露
  - 🔗 来源: https://x.com/Hacker0x01/status/2126315208087843090 | 📅 2026-11-27
  - 说明: 平台累计里程碑，不是单人单洞，也不是窗口内新 payout。本期已核实点赞最高。
- CISA 联邦 VDP 五年：44,493 份报告、5,700+ 有效、5,300+ 已修复 | Bugcrowd | 👍 38 | 🔄 1 | 👀 未披露
  - 🔗 来源: https://x.com/mdp_sec/status/2125707293648134511 | 📅 2026-11-25
- YesWeHack 放出编码 agent 实验环境系列总结，比较 Claude Code、Codex、Gemini CLI | YesWeHack | 👍 35 | 🔄 3 | 👀 未披露
  - 🔗 来源: https://x.com/yeswehack/status/2126228439648870878 | 📅 2026-11-27
- JPCERT/CC 周报汇总 22 条，点名 Drupal core、nginx、F5、Oracle，以及未开认证的 Node-RED 遭探测 | JPCERT/CC | 👍 23 | 🔄 9 | 👀 未披露
  - 🔗 来源: https://x.com/jpcert/status/2125761412689784886 | 📅 2026-11-26
  - 说明: 补丁窗口提醒，不是新 PoC。
- 多个项目暂停或重开收报告 | 多平台 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes | 📅 2026-11-28
  - 说明: Coveo（Intigriti）临近窗口结束仍显示 Paused；DataCamp（Intigriti）、Mondelēz（HackerOne）暂停收报告；Coolblue 重新开放。影响是暂时不能按暂停项目交新单。

---

**🏆 猎人里程碑 / 大额奖励**
- HackerOne 社区累计赏金 $550M
  - 🌟 中文概述: 平台自 2016 年对应 $10M 的公开里程碑，累计越过 $550M。不是单人单洞，也不是本期某一笔到账。窗口内已核实点赞最高，为本期热度峰值来源。 | 👍 136 | 🔄 6 | 👀 未披露
  - 🔗 链接: https://x.com/Hacker0x01/status/2126315208087843090 | 📅 2026-11-27
- Plether 审计赛：@xdeltabear $21,526，其后 Omisanin0 $11,250、Web3Vinay $9,150、Mclovin $4,459、Unineko $4,270
  - 🌟 中文概述: 最有价值的一条是双向下注缺少时间锁，资金尚未上线。赛前另有「63 个独立缺陷、18 个 Critical、覆盖约 90% 代码」的社区清点，与 1,391 份报告的竞赛规模不是同一口径。 | 👍 77 | 🔄 13 | 👀 未披露
  - 🔗 链接: https://x.com/immunefi/status/2126291471267770406 | 📅 2026-11-27
- Google Cloud 致谢 Arvin Shivram（Vertex AI）、asterfiester（GKE Fleet）
  - 🌟 中文概述: 两条均为服务端早已修补后的 CVE 公开，不是窗口内新利用。 | 👍 56 | 🔄 9 | 👀 未披露
  - 🔗 链接: https://x.com/cvedotnow/status/2126406308408463686 | 📅 2026-11-27

---

**☕ 其他有趣八卦 / 吐槽 / 预警**
- Base Everest 十几万行代码、0 个 Critical，半池先被两个 High 抬起来。奖池营销和真实严重性已经分开计价。 | 👍 82 | 🔄 8 | 👀 未披露
  - 🔗 来源: https://x.com/immunefi/status/2125658301077880929 | 📅 2026-11-25
- 两条 GCP Critical 的补丁日分别是 4 月与 9 月，CVE 统一拖到 11-27。看公告时先分清「公开日」和「仍可利用」。 | 👍 56 | 🔄 9 | 👀 未披露
  - 🔗 来源: https://www.cve.org/CVERecord?id=CVE-2026-85258 | 📅 2026-11-27
- 1Password：员工企业 GitHub 被控后，攻击者读取源码并向后端推送恶意代码，下载了部分用户的姓名、邮箱、账号标识、登录时间、公钥、SRP 参数，以及邀请/开通/恢复邮件中的 token 等非机密元数据。公司称客户保险库内容、保护保险库的密钥未被访问；受影响 GitHub 账号已禁用，可能暴露的内部凭据已轮换。直接风险是精准钓鱼，不是保险库明文泄露。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://1password.com/blog/update-on-nov-2026-security-incident | 📅 2026-11-25
- pCloud Pass：用户在开启 2FA 后仍收到未知设备登录通知。公司确认密码管理器遭攻击并称已遏制，少量邮箱暴露且出现登录尝试；云存储未受影响，并称密码与笔记在客户端加密。公司没有说明加密保险库文件是否被带走。应把暴露邮箱视为钓鱼面，并关注官方是否补充保险库是否外流。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.bleepingcomputer.com/news/security/pcloud-confirms-password-manager-hack-after-suspicious-login-alerts/ | 📅 2026-11-27
- 开发者机器与 CI 是实际受害面：PolinRider 用改写后的提交混进真实账号仓库，GitHub 在 2026-11-25 暂停相关账号。建议只做防御动作——停用可疑 PR 的 CI、轮换仓库与本机令牌、核对近期回写日期的提交，不要去复现加载器。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://techaeris.com/2026/11/27/polinrider-malware-github-repos-ethereum/ | 📅 2026-11-27

---

**[历史参考，不计入本期热度峰值]**
- NGINX CVE-2026-123633 / CVE-2026-123007（约 11-18，@wiz_io 帖 👍 719）。窗口内 JPCERT 周报与 CSA 新加坡提醒帖（https://x.com/CSAsingapore/status/2125844861094097232 ，2026-11-26，👍 0 | 🔄 0）只是补丁提醒，不把 719 计入峰值。
- Wiz 对 10 月 EKS / Terraform runner 入侵的复盘（主报告约 11-23；CSA Frontier Ready Daily 于 11-25 转述）不计入本期新披露口径。
- Datadog《2026 State of Cloud Security》（主发布约 2026-11-23）不计入本期热度。
- ZeroDay Times 于 2026-11-26 转写的 GitHub cache poisoning（$7,500）是既有公开案例的二次分析，不计入本期新 payout。
