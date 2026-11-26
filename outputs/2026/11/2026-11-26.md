**【CyberSec 情报速报 | 云安全 & AI 重点强化】**

> 生成时间: 2026-11-26 17:27:07 UTC+08:00

**统计范围**: 2026-11-23 - 2026-11-26（包含起止日，共约 3-4 天数据）
**本期热度峰值**: 最高 👍 311 | 最高 👀 未披露
**今日情报眼**: 云托管密钥被盗，能源企业中招

说明：互动只采用草稿中明确核实的数值。已核实最高赞为 PortSwigger Web Security Academy（2026-11-24，MCP 实验）👍 311、🔄 45；次高为 Immunefi 支付帖 👍 53、GMI Cloud 说明帖 👍 49。浏览量均未披露。未核实互动一律标「未披露」，不推算、不计入峰值。初始通告早于窗口的事项仅作背景，并标注「历史参考」。技术细节未经人工复现。

---

**📋 生成说明**
本报告由多份公开报道草稿合并、去重、排序而成，技术细节未经人工验证，仅供参考。不收录利用步骤、PoC 或 payload。

---

**💰 本期最高赏金 / 最炸裂 payout**
- $12,500 | @gzeon | Immunefi | 区块链本体漏洞获赏
  - 💡 一句话总结: 链本身漏洞获赏；Immunefi 称 2026 年至今已支付 330 份高危区块链报告，来自 150 名研究者，gzeon 个人有 7 份。未核到窗口内更高金额的已支付赏金帖。 | 👍 53 | 🔄 4 | 👀 未披露
  - 🔗 来源: https://x.com/immunefi/status/2125530943352193378 | 📅 2026-11-25

**☁️ 云安全重点(特别加强板块)**
- GMI Cloud 推理日志被未授权访问（含 OpenRouter 端点）
  - 🌟 亮点总结: GMI 称日志系统被未授权方进入。2026-10-18 至 11-18 经其推理端点（含 OpenRouter）的 prompt 与响应可能泄露；GPU 算力未受影响。第一条路径 10 月 22 日关闭后，对方用失陷凭据走第二条路径，直到 11 月 18 日切断。现已停记 prompt/响应正文。prompt 中的 API key 应立即轮换并核对调用记录。官方帖约数未核实，不计入；后续说明帖核实赞数为 49。 | 👍 49 | 🔄 7 | 👀 未披露
  - 🔗 来源: https://x.com/gmi_cloud/status/2125479299792928856 | 📅 2026-11-24

- Azure API Management Classic：存储密钥被未授权读取，挪威能源企业中招
  - 🌟 亮点总结: 微软 11 月 18 日发现、19 日关闭访问路径；修复不会自动作废可能已被读取的凭据。受影响为 APIM Classic 的 Developer/Basic/Standard/Premium；Consumption 与全部 v2 不受影响。未做网络加固、或把 secret 放在 APIM 而非 Key Vault 的实例，Named Values、IdP/OIDC client secret、subscription key、直连管理 API token 可能已被读取。挪威 NSM（通报 11 月 20 日发布、23 日更新）点名 Equinor、Skagerak Energi，要求按已泄露处理、全量轮换，并核对下游 API 是否被滥用。客户侧无法靠补丁包自行关闭该入口。公开材料未给出 CVE。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.helpnetsecurity.com/2026/11/24/azure-apim-vulnerability-credential-theft/ | 📅 2026-11-24

- N-able Mail Assure 托管云 SSRF（CVE-2026-134624）进入 CISA KEV
  - 🌟 亮点总结: CVSS 9.3。已认证 API 用户可借 LDAP 同步连通性检查，把平台服务器指向任意内网主机与端口。N-able 称 Mail Assure / SpamExperts Hosted Cloud 中断约始于 11 月 16 日，利用被限制在单台托管服务器，11 月 21 日恢复控制台与 API。CISA 于 11 月 23 日入库，联邦限期 11 月 26 日。属托管邮件安全云的内网探测面，不是客户 IAM 提权。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html | 📅 2026-11-24

- AWS Kiro Web 命令执行（CVE-2026-136267，AI 云 IDE）
  - 🌟 亮点总结: 部分模型会话中，仓库文件或网页等被读入内容里的 tool-call 标记可能被复述，并在订阅者托管开发环境中执行，且无同意提示。影响时段为 2026-05-18 至 2026-10-30，涉及模型包括 DeepSeek v3.2、GLM-5、MiniMax M2.1/M2.5、Qwen3-coder-next。AWS 称 10 月 30 日已服务端修复，客户无需操作。CVSS 3.1 为 8.8。属间接内容注入打到云端执行环境，不是窗口内新的在野 0day。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://aws.amazon.com/security/security-bulletins/2026-202-aws/ | 📅 2026-11-25

- Amazon ECS MCP Server：排障工具绕过敏感信息打码（CVE-2026-135614）
  - 🌟 亮点总结: `awslabs.ecs-mcp-server` 0.1.36 之前，默认敏感数据设置下，排障工具仍可能返回 ECS 任务定义中的容器环境变量明文和 secret 引用。能影响 Agent 输入的一方（包括 Prompt Injection）可能借此拿到这些值。应升级到 0.1.36 或更高版本，并轮换以明文放在任务定义环境变量中的凭据。未见在野利用报道。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://aws.amazon.com/security/security-bulletins/2026-200-aws/ | 📅 2026-11-24

- Microsoft Entra Connect Health：只读租户元数据与管理员邮箱
  - 🌟 亮点总结: 缺陷约 2026-07-23 引入，11 月 9 日发现，11 月 19 日服务端修复，20 日起通知客户；窗口内为 11 月 23 日公开报道。攻击者读到技术联系人/管理员邮箱、tenant ID、显示名、初始域名、区域、许可层级、目录同步状态等。微软称未见配置被改；密码、token、有效密钥、订阅数据与本地 AD 拓扑据称为未暴露。主要风险是定向钓鱼与租户侦察，不是直接接管。客户无需装补丁。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.helpnetsecurity.com/2026/11/23/microsoft-entra-connect-health-vulnerability-tenant-data/ | 📅 2026-11-23

- Amazon OpenSearch Service：快照仓库注册 SSRF（CVE-2026-135414）
  - 🌟 亮点总结: 具备域上快照管理权限的用户，可通过仓库端点设置，让服务侧节点向其指定的网络地址发请求。CVSS 中等，需高权限。修复版本为服务软件 R20260720。暂时不能升级时，应收紧 `manage_snapshots` 以及相关 `es:ESHttpPut`、`iam:PassRole`。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://aws.amazon.com/security/security-bulletins/2026-201-aws/ | 📅 2026-11-24

- Datadog《State of Cloud Security 2026》：云工作负载高危漏洞中位数约 4 倍
  - 🌟 亮点总结: 11 月 23 日学习帖重申：抽样云服务的 High/Critical 漏洞中位数从 2026 年 2 月的 4 升至 11 月约 16（所称 Vulnpocalypse）。近半数 Gemini 用户仍用长期 API key，Bedrock 约 17%；Azure 上 97% 组织保留 Foundry 默认长期密钥。60% 组织在跑发布不足 24 小时的依赖，工作负载平均约 149 个依赖。报告同时提到 Shai-Hulud 2.0 会搜云凭据。结论是 AI 加快漏洞、错误配置和弱身份的暴露，而不是发明新的云攻击原语。底层报告发布于 11 月 10 日，属[历史参考]；本条取窗口内解读。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.datadoghq.com/blog/cloud-security-study-learnings-2026/ | 📅 2026-11-23

**📚 最值得读的 Writeup / 公开报告**
- AI Agent 约 11 分钟打穿 MONAI Label（CVE-2026-133968）
  - 📝 技术摘要: CISA 11 月 23 日将 MONAI Label 路径穿越写入 KEV（CVSS 9.8，未认证可在数据目录外写文件并导向 RCE）。Amazon 称疑似中国关联操作者使用 CAIRN 一类 AI 解题引擎，只给目标 IP 和「拿到 shell」目标，由 Agent 自行规划。活动约自 2026-09-08 起持续约 48 小时，指向东亚（非中国大陆）高校；对一台主机，Agent 识别该问题后约 11 分钟完成任意文件写入，并进一步获得 root 级访问。联邦修补限期 11 月 26 日。窗口内价值是 Agent 自主找问题并落地，不是新的手写 PoC。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html | 📅 2026-11-24

- 1Password 后端事件：员工 GitHub 被控，保险库未触及
  - 📝 技术摘要: 11 月 19 日发现员工企业 GitHub 被用于读取私有源码，并向后端推入恶意代码，下载部分客户的姓名、邮箱、账号标识、创建与最后登录时间、公钥、不能单独登录的 SRP 参数，以及部分邀请/开通/恢复邮件中的 token；同时进入 CI/CD。公司称可能暴露的基础设施凭据已轮换。保管库内容、保护密钥、账户密码、Secret Key、客户端与扩展未被访问。残留风险是用真实姓名和恢复类 token 钓鱼，而不是解开保险库。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://1password.com/blog/update-on-nov-2026-security-incident | 📅 2026-11-25

- OpenRouter：三家推理供应商数据策略失守
  - 📝 技术摘要: 厂商公告日本身为 11 月 22 日，属窗口前一日；本条取 11 月 23 日窗口内报道。Dragos 自 7 月至 11 月投递约 200 万条带金丝雀的 prompt（含测试用 AWS key），发现至少三家供应商数据外泄，并有人拿种子凭据去碰测试系统和金丝雀 AWS 账户。OpenRouter 称自身未被入侵，已下架三家供应商，并将 125 个端点移出 Zero Data Retention。公开拆解包括：Together AI 由编码 Agent 把仓库凭据提交到公开 GitHub；Phala 推理服务器被控；另有请求被错误转发。结论是「零留存」只约束第一跳。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://www.bleepingcomputer.com/news/security/openrouter-drops-ai-providers-over-leaked-prompts-and-secrets/ | 📅 2026-11-23

- Drupal SA-CORE-2026-019 / CVE-2026-136716
  - 📝 技术摘要: 11 月 25 日发布，风险 21/25（Highly critical）。11 月 18 日针对安装器的修复（SA-CORE-2026-017 / CVE-2026-132165）没有覆盖处于异常或未完成安装状态的站点，这些站点仍可能被未认证接管。官方称已有在野利用，且界面上看不出是否处于该状态。已锁好安装器的站点不受影响。修复版本为 10.6.23、11.3.23、11.4.14，生产站点升级后还需跑 update hook。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://www.drupal.org/sa-core-2026-019 | 📅 2026-11-25

- Datadog Security Labs：Mitigeddon（披露到在野利用）
  - 📝 技术摘要: 2026 年迄今公开 CVE 已超 10 万，高于 2025 年约 5 万、2024 年约 4 万。在野利用样本中，17% 在披露当天被利用，另有 20% 在一周内；披露到利用的中位数 33 天（2025 年为 60 天，2024 年为 163 天，不含先利用后披露的 0day）。工具聚合 OSV、CISA KEV、VulnCheck 与 Datadog 遥测，用来判断云环境是否真有人在打，而不是只看分数。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://securitylabs.datadoghq.com/articles/introducing-mitigeddon/ | 📅 2026-11-23

**🔥 社区热议的技术话题或新手法**
- MCP 服务器测试进入常规 Web 训练
  - 💬 讨论核心: PortSwigger 于 11 月 24 日上线 MCP 实验专题，覆盖有缺陷的访问控制与认证、SQL 注入，以及 OAuth 账号接管。讨论中有人强调把 MCP server/skill 钉到具体 commit，并先读文件再运行，避免后续 push 改变已审查内容。这是窗口内唯一核到具体互动数、且赞数最高的公开帖，为本期热度峰值。Agent 工具面正在被当成普通 Web/API 攻击面。 | 👍 311 | 🔄 45 | 👀 未披露
  - 🔗 代表性推文: https://x.com/WebSecAcademy/status/2125819201818591489 | 📅 2026-11-24

- Cisco Expressway CVE-2026-76466 在野 root RCE，联邦限期落在窗口内
  - 💬 讨论核心: CVSS 9.8。集群化 Expressway-C/E 上，未认证远程命令执行到 root。初始通告早于本窗口，属[历史参考]；本条只收窗口内报道：CISA 联邦限期为 11 月 23 日，已有暴露在公网的设备被打穿后横向到集群其他节点，并出现疑似 AI 辅助的内网搜寻。无官方绕过，需升级到修复版本（报道给出的版本为 X15.5.20）。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性推文: https://www.dailyciso.com/briefing/2026-11-24 | 📅 2026-11-24

- Agentic offensive frameworks（CAIRN / ARTEX / CyberStrikeAI）
  - 💬 讨论核心: 公开报道把多起活动串到 AI 原生渗透框架。CAIRN 一类案例是人只定 IP 和「拿到 shell」，Agent 自行改打法。ARTEX 被描述为用窃得的模型 API key 支付下一轮窃密，并在 AWS 日志中检索基金、发票类关键词；入口还包括 Cognito User Pool 与长期访问密钥。防御含义是云审计要识别机器速度的并行侦察和凭据链式利用，而不只是单条漏洞告警。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性推文: https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html | 📅 2026-11-24

**🆕 新上线 / 更新中的 Bug Bounty 或 VDP 项目**
- Base Everest 审计赛（Immunefi）仍在收报告
  - 📝 更新点: 11 月 23 日官号再次宣传，截止 12 月 1 日。奖池由最高有效严重性决定：Critical $250k、High $125k、Medium $70k、Low $30k。范围是 Beryl/Cobalt/Denim/Everest 相关 Rust 与 Solidity，要求在本地 devnet 提供可运行 PoC，禁止打公共 sequencer。赞数未在抓取结果中披露。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://x.com/immunefi/status/2124934011487412327 | 📅 2026-11-23

- bugbounty.fyi 聚合页上的范围/上线变化（非平台官方帖）
  - 📝 更新点: 2026-11-26 页面将若干项目标为近 24 小时内变化（聚合站相对时间）。「Fresh to hunt」包括 Osero SDK / Swap API（Sherlock，上限 $15k）、Nubank Brasil（Bugcrowd，$4,000）、Instadapp 扩大范围（Immunefi，上限 $500k）、DANA（YesWeHack）、KHealth（HackerOne）、Intuition（Immunefi，上限 $100k）。另将 1Password（Intigriti，上限 $30,000）与 BoursoBank（YesWeHack）标为 New。这些是计划上限或范围变化，不是已支付赏金。1Password 的「New」在另一页按近 30 天理解，不能确认就是本 4 天窗口内上线，且与同周后端事件无公开因果关系。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/ | 📅 2026-11-26

**📢 平台动态 & 政策变化**
- CrowdStrike 以全股票方式收购 Zscaler，作价约 439 亿美元。路透称超过 Google 收购 Wiz 的 320 亿美元，为网络安全并购纪录。换股比例 1.135 股 CRWD，相对 11 月 20 日收盘溢价约 34%；合并后 ARR 预计超过 100 亿美元，由 Kurtz 执掌，Chaudhry 留任并入董事会。预计于 CrowdStrike FY2028 下半年交割，交割前两家仍独立运营。属产业整合，不是漏洞披露。 | CrowdStrike / Zscaler | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.reuters.com/legal/transactional/crowdstrike-buy-zscaler-439-billion-2026-11-23/ | 📅 2026-11-23

- CISA KEV：11 月 23 日将 N-able Mail Assure SSRF（CVE-2026-134624）与 MONAI Label 路径穿越（CVE-2026-133968）入库，联邦限期 11 月 26 日。11 月 25 日再加入 10 条，其中多条涉及 Mitel MiCollab，另有 Juniper Session Smart 与 Vates Xen Orchestra。联邦机构被要求按 BOD 26-04 优先处理暴露资产。细节以目录原文为准。 | CISA | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.dailyciso.com/briefing/2026-11-26 | 📅 2026-11-26

**🏆 猎人里程碑 / 大额奖励**
- @gzeon 获得 $12,500，并被标为 Immunefi All Star（90 天榜第 6、2026 年第 20）；其 2026 年已有 7 份高危区块链报告获支付
  - 🌟 中文概述: 窗口内唯一核实到具体金额与原帖互动的支付。金额不高，但指向区块链本体，而不是普通合约漏洞。同期平台计数为 330 份高危报告、150 名研究者。 | 👍 53 | 🔄 4 | 👀 未披露
  - 🔗 链接: https://x.com/immunefi/status/2125530943352193378 | 📅 2026-11-25

**☕ 其他有趣八卦 / 吐槽 / 预警**
- 1Password：保险库没破，但子集中的姓名、邮箱和部分邮件 token 已出。接下来更可能是仿冒支持、邀请或恢复邮件。只在官方客户端或站点输入凭据。公司称已把相关邮件验证码从 6 位数字加长。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://1password.com/blog/update-on-nov-2026-security-incident | 📅 2026-11-25

- GL.iNet GoodCloud：云管通道被用来给部分路由器和 KVM 植入恶意软件。厂商称云侧路径已堵，但已感染设备不会自动清除，需刷最新稳定固件，并检查挂在 KVM 上的主机。发现约在 11 月 20 日，窗口内仍在传播处置建议。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://cyberrecaps.com/news/cybersecurity-news-november-23-2026 | 📅 2026-11-23

- 英国零售商 Next 称第三方供应商遭攻击，已访问数据「有限且良性」，目前无证据表明客户个人数据被波及；自身系统据称为未失陷。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.theguardian.com/business/2026/nov/23/next-issues-cyber-attack-warning-after-benign-data-accessed-by-hackers | 📅 2026-11-23
