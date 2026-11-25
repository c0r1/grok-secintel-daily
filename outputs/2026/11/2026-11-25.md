**【CyberSec 情报速报 | 云安全 & AI 重点强化】**

> 生成时间: 2026-11-25 17:46:08 UTC+08:00

**统计范围**: 2026-11-22 - 2026-11-25（包含起止日，共约 3-4 天数据）
**本期热度峰值**: 最高 👍 308 | 最高 👀 未披露
**今日情报眼**: 云控制面满分漏洞披露

---

**📋 生成说明**
本报告汇总公开社交媒体与公开安全通报，技术细节未经人工验证，仅供参考。互动数只采用来源明确显示的数值，缺失标「未披露」，不推算；已收录来源均未直接显示浏览量。不收录利用步骤、PoC、payload 或可复现参数。窗口外材料仅作 [历史参考]，不计入本期热度峰值。

---

**💰 本期最高赏金 / 最炸裂 payout**
- 金额未披露 | @YXN0cm8 | YesWeHack | Critical Path Traversal（CWE-22）
  - 💡 一句话总结: 窗口内赏金相关帖里互动最高；金额与项目名未写明。来源为回复线程，父帖为原奖励帖。原帖利用片段不转载。 | 👍 183 | 🔄 4 | 👀 未披露
  - 🔗 来源: https://x.com/mdp_sec/status/2125099776782012737 | 📅 2026-11-23

窗口外的赏金上调与累计支付不收录，亦不计入峰值。

**☁️ 云安全重点(特别加强板块)**
- Azure Event Grid 认证缺陷（CVE-2026-62841，CVSS 10.0）
  - 🌟 亮点总结: 网络可达的 Improper Authentication / 提权。NVD 于 11 月 23 日公开，向量为 AV:N/AC:L/PR:N/UI:N/S:C，机密性、完整性、可用性均为高。微软说明这是托管服务漏洞，服务侧已缓解，客户无需自行打补丁；发布时评估为未遭利用、未公开披露。本期最高互动来自 CVE 汇总账号，而非云安全研究员原帖。同批汇总还列出 M365 Copilot 授权缺陷（CVE-2026-50691，9.9）、SharePoint 路径遍历致代码执行（CVE-2026-70193，9.9），以及 Azure Profile Data Roaming 与 Azure Machine Learning 的 SSRF（均记为 9.6）等。客户侧动作以 MSRC 单条公告为准，不从分数推断可利用性。不收录利用材料。 | 👍 308 | 🔄 67 | 👀 未披露
  - 🔗 来源: https://x.com/cvedotnow/status/2124994517715575110 | 📅 2026-11-23
  - 厂商说明: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62841
  - 同批汇总: https://threataft.com/articles/microsoft-azure-m365-november-2026-mass-disclosure-cve-cluster | 📅 2026-11-24

- Azure API Management Classic：管理面密钥可能已被未授权读取
  - 🌟 亮点总结: 微软称 11 月 18 日发现、19 日关闭未授权管理面路径（Service Health MZK9-GH0）。影响未按建议加固的 Classic Developer/Basic/Standard/Premium，不含 Consumption 与全部 v2。修复前未授权方可能读取 Named Values、IdP/OIDC client secret、subscription key 与 direct management API token，并执行管理操作。关闭路径不会使已取出的凭据失效，须在签发端轮换；密钥直接写在 APIM 而非 Key Vault 引用时优先级更高，被遗忘的 dev/test 实例同样要清点。挪威 NSM 11 月 20 日通告、23 日更新，将此事与 Equinor、Skagerak Energi 等关联，并称影响超出挪威和能源行业；Equinor 称生产正常、未见数据被窃或篡改迹象。尚无 CVE。NSM 给出的已修补运行时下限为 0.52.x build 31936、0.53.x build 31938。 | 👍 67 | 🔄 22 | 👀 未披露
  - 🔗 来源: https://x.com/TheRegister/status/2124848587947598217 | 📅 2026-11-23
  - 事实页: https://www.csoonline.com/article/4252513/attackers-exploited-an-azure-api-management-flaw-to-steal-secrets-microsoft-warns.html

- Radware Cloud WAF 管理 API 暴露客户云日志导出凭据
  - 🌟 亮点总结: 据公开根因说明，11 月 19 日有人访问了公网可达、无需认证的内部 Cloud WAF 管理 API。可能涉及客户联系信息，以及部分客户用于日志导出的 AWS S3、Azure Blob 或 SFTP 凭据。WAF 流量、证书和终端用户数据据称未暴露。受影响客户应轮换日志导出密钥，并复查 11 月 19 日以来的存储访问日志。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/ | 📅 2026-11-24

- Kyverno 命名空间隔离失效（GHSA-pcx2-xcq4-65vf，CVSS 10.0）
  - 🌟 亮点总结: Akamai 11 月 24 日分析：拥有创建命名空间级 Policy 权限的租户，可借助校验层与执行层的 URL 解析差异，绕过命名空间隔离，使高权限 admission controller 访问其他命名空间或集群级资源，属于 confused deputy。修复版本 1.19.2；遥测称约 4% 企业网络仍有受影响实例。应核对在跑版本。不复述绕过构造。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.akamai.com/blog/security-research/url-parser-differential-broke-kyvernos-namespace-isolation | 📅 2026-11-24

- LiteLLM 与 LM Studio：AI 网关 / 本地 MCP 同窗口公开高危
  - 🌟 亮点总结: ZDI 于 11 月 24 日公开一批 LiteLLM 问题。主项 CVE-2026-136539（CVSS 7.2）为代码注入，可在服务账户上下文执行命令；六项中五项已修，厂商争议 MCP stdio 注入项 CVE-2026-136535，且无单独补丁。同日 LM Studio CVE-2026-133995：无登录条件下将 MCP tool schema 当作可执行内容，修复版本 0.4.16。同窗口另有认证后的路由/回调类问题，影响面包括 provider 凭证与跨租户数据；触发方式不描述。网关持有模型供应商密钥，失陷会把云与模型凭据绑在同一条暴露链上。更早进入 KEV 的 guardrail 沙箱逃逸 CVE-2026-40217（11 月 18 日）为 [历史参考]，不计入峰值。防御是升级到厂商标注的修复版、轮换供应商 key，并把管理面移出公网。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://theinjection.dev/items/zdi-litellm-six-cve-wave/ | 📅 2026-11-24
  - 关联: https://theinjection.dev/items/zdi-lm-studio-mcp-schema-code-injection/

- Wiz：Agent 进攻框架相关的云入侵报告
  - 🌟 亮点总结: 11 月 23 日报告称，自更早的「Black October」以来约三周又有约 20 起厂商披露，Wiz CIRT 接案约 3 倍。文中案例活动本身在 10 月，标 [历史参考]：约 4 日内涉及 2 个 AWS 账号、7 个 EKS 集群，失窃 CI/云身份被扩大到集群高权限。报告强调此类活动吵、快、日志特征明显，出口分散，封 IP 效果有限。防御看异常云 API、长期凭证，以及特权工作负载与云身份的组合告警，而不是单点 IOC。不提供框架用法或入侵步骤。报告页互动未披露。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.wiz.io/blog/agentic-attacks-artex-offensive-ai-frameworks | 📅 2026-11-23

- Microsoft Entra Connect Health：租户联系人元数据被只读访问
  - 🌟 亮点总结: 缺陷约于 2026-07-23 引入，11 月 9 日发现，11 月 19 日服务侧修复，11 月 20 日通知客户（略早于窗口）。窗口内报道重点是后续钓鱼。读到的是管理员与技术联系人邮箱、tenant ID、显示名、初始域名、许可层级和同步状态，不是口令或 token。无本地补丁。受影响租户数量未披露。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.it-connect.tech/entra-connect-health-flaw-exposed-microsoft-tenant-admin-emails/ | 📅 2026-11-24

**📚 最值得读的 Writeup / 公开报告**
- CISA KEV：N-able MailAssure 与 MONAI Label
  - 📝 技术摘要: 窗口内传播帖同时覆盖两条已利用项。MailAssure（CVE-2026-134624）为已认证 API 用户可打到内网的 SSRF，托管控制台曾中断，厂商称已修复。MONAI Label（CVE-2026-133968）为未认证路径穿越写文件，影响可到 RCE，属 AI 标注组件；0.8.6 于 11 月 22 日修复。原始发现条目标注 11 月 20 日，略早于窗口；窗口帖称 agent 在操作者只要求 shell 后自主发现该问题，用时约 11 分钟。美国联邦机构补丁期限约 11 月 26 日。不复述利用链。 | 👍 43 | 🔄 16 | 👀 未披露
  - 🔗 链接: https://x.com/TheHackersNews/status/2125107955951669688 | 📅 2026-11-24
  - 相关报道: https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html | 📅 2026-11-23

- @bountywriteups 11 月 22 日公开分析汇总
  - 📝 技术摘要: 情报聚合帖。标题涉及 Next.js CDN 代理导致的账号接管、JWT、AI 应用中的 SSRF 等。只确认帖文本身；利用链路与 PoC 不展开。底层文章发表日未逐条核实，不作为本期新漏洞计数。 | 👍 36 | 🔄 5 | 👀 未披露
  - 🔗 链接: https://x.com/bountywriteups/status/2124421939137749203 | 📅 2026-11-22

- @bountywriteups 11 月 23 日公开分析汇总
  - 📝 技术摘要: 同账号另一条聚合帖，转发高于点赞。标题涉及通配参数、竞态、OAuth、邮件伪造等。同样只记聚合帖本身，不展开利用步骤。 | 👍 29 | 🔄 10 | 👀 未披露
  - 🔗 链接: https://x.com/bountywriteups/status/2124798913739886784 | 📅 2026-11-23

- Cisco Expressway 集群根命令执行（CVE-2026-76466）仍在被利用
  - 📝 技术摘要: 集群化 Expressway-C/E 上，未认证远程攻击者可获得 root 级操作系统命令执行，并被用于进入内网。CISA 已列入 KEV。动作是安装厂商 10 月更新并排查集群节点。不描述触发条件。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://www.dailyciso.com/briefing/2026-11-24 | 📅 2026-11-24

- Unit 42：Agentic AI 实战战役战术
  - 📝 技术摘要: 报告日期在窗口内；跟踪样本为 2026 年 7–9 月，战役期作背景。行业覆盖政府、物流、酒店、制造、农业与教育。可比样本里，人操作时命令间隔中位数 23.9 秒，agent 接手后降到 1.4 秒。初始入口观察为易受攻击 Web 应用上的 webshell；未见传统编译后门，更多是一次性脚本。价值在速度与取证特征，不在复现。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/ | 📅 2026-11-24

**🔥 社区热议的技术话题或新手法**
- AI 推高赏金报告量，社区在对账猎人是否更赚
  - 💬 讨论核心: 近 90 天公开项目发放快照：HackerOne $12.8M、Bugcrowd $7.2M、Intigriti 约 $1M + €191k，合计约 $21M、1,406 个开放项目。非平台官方口径。官方分拣与身份验证动作见平台动态。 | 👍 89 | 🔄 3 | 👀 未披露
  - 🔗 代表性推文: https://x.com/mdp_sec/status/2125049262052651252 | 📅 2026-11-24

- 代理型攻击框架的窗口内社交热度有限
  - 💬 讨论核心: 能核到的转述帖互动很低。讨论焦点是多操作者、机器速度下的身份与云 API 滥用，而不是单一 CVE。检测应转向行为与身份异常。框架用法不提供。报告详见云安全板块。 | 👍 4 | 🔄 0 | 👀 未披露
  - 🔗 代表性推文: https://x.com/DFIR_Radar/status/2124941962968985813 | 📅 2026-11-23

- MiniMax 推理供应链的 prompt 可见性
  - 💬 讨论核心: Atlas Cloud 与 Novita 称发往 MiniMax 的客户 prompt 到达官方 API，测试链接在 40–130 小时后被打开。OpenRouter 侧窗口帖称已撤下相关 Zero Data Retention 标签。代表帖互动为 0，高互动原帖未核到。ZDR 在此被当作承诺而非控制。 | 👍 0 | 🔄 0 | 👀 未披露
  - 🔗 代表性推文: https://x.com/Z3nlyte/status/2124296992234819916 | 📅 2026-11-22
  - 汇总: https://theinjection.dev/items/minimax-api-reseller-prompt-access/

- 伪造 AI 爬虫扫 .env 与云凭据
  - 💬 讨论核心: 11 月 25 日安全媒体称，有人冒充 OpenAI、Anthropic、DeepSeek 等爬虫，扫描暴露的 .env 和云凭据。细节未在监控源原帖中核实，仅作凭据卫生预警。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://gbhackers.com/category/cloud/ | 📅 2026-11-25

- Agentic 入侵把操作间隔压到秒级
  - 💬 讨论核心: Unit 42 可比样本中，人操作命令间隔中位数 23.9 秒，agent 接手后约 1.4 秒。同周转述称 offensive framework 主机从 11 月 6 日约 3,200 增至 11 月 24 日 8,105，并提到生产环境 agent 批准恶意工具的金融案例。11 月 6 日基数早于窗口，只作背景。代表帖互动未披露。不提供框架或工具用法。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性推文: https://x.com/godvinayak/status/2125419686280192371 | 📅 2026-11-25

**🆕 新上线 / 更新中的 Bug Bounty 或 VDP 项目**
- Aspira VDP | Intigriti
  - 📝 更新点: 11 月 25 日新公开 VDP。窗口最后一天上线，无社区互动数据。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?dir=new&since=1 | 📅 2026-11-25

- METASCAN | Standoff 365
  - 📝 更新点: 11 月 24 日新公开项目。索引页出现的金额标注未经项目页二次核对，不写成已证实赏金。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?dir=new&since=1 | 📅 2026-11-24

- Morpho Midnight Adapter | Cantina
  - 📝 更新点: 11 月 23 日新公开项目。页面未给出本期赏金上限与范围细节。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?dir=new&since=1 | 📅 2026-11-23

- GCash Vulnerability Disclosure | HackerOne
  - 📝 更新点: 11 月 23 日上线的公开 VDP，非现金赏金项目。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?dir=new&since=1 | 📅 2026-11-23

- Beanstalk | Sherlock
  - 📝 更新点: 11 月 22 日新上线。索引页未披露具体范围与最高赏金，需进项目页核对。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?dir=new&since=1 | 📅 2026-11-22

**📢 平台动态 & 政策变化**
- Immunefi Studio 仍为邀请制；官方用 Signals 选项目、Review 降重复来解释提交量上升。帖中 $50,000 案例最早见于 11 月 5 日，属 [历史参考]，不作为本期新发放，亦不计入热度峰值。公告内背景数：DefiLlama 2026 年前九个月黑客事件 290 起，对比一年前 111 起。 | Immunefi | 👍 47 | 🔄 5 | 👀 未披露
- 🔗 来源: https://x.com/immunefi/status/2124865060258672914 | 📅 2026-11-23

- AWS WAF 对 LLM、MCP、A2A 端点的自动发现与 Bedrock Guardrails 防护进入 GA。信号是云厂商把 AI 入口纳入与传统 Web 同类的边缘防护，而不是只靠应用内过滤。 | AWS | 👍 32 | 🔄 0 | 👀 未披露
- 🔗 来源: https://x.com/awswhatsnew/status/2125003619590422828 | 📅 2026-11-23

- HackerOne 称 Q3 2026 报告量创纪录，同比约 +130%，较 Q2 约 +22%；10 月分拣吞吐约去年同期 2.4 倍；10 月 92% 新 Critical 在 24 小时内完成验证。手段包括强制身份验证，以及用 agent 关掉明显不合格报告。官方推文互动未披露。 | HackerOne | 👍 未披露 | 🔄 未披露 | 👀 未披露
- 🔗 来源: https://www.hackerone.com/blog/ai-driven-report-volume-insights-and-actions | 📅 2026-11-24

**🏆 猎人里程碑 / 大额奖励**
- @YXN0cm8 / YesWeHack Critical Path Traversal
- 🌟 中文概述: 与「本期最高赏金」为同一窗口帖，不重复展开，不另计热度。金额与项目名未写明。原帖利用片段不转载。 | 👍 183 | 🔄 4 | 👀 未披露
- 🔗 链接: https://x.com/mdp_sec/status/2125099776782012737 | 📅 2026-11-23

- @Horvix_ / Immunefi $50,000 [历史参考]
- 🌟 中文概述: 同一笔五位数最早见于 11 月 5 日官方帖。11 月 23 日帖是窗口内再传播，不能证实为本期新发放。不计入本期热度峰值。 | 👍 47 | 🔄 5 | 👀 未披露
- 🔗 链接: https://x.com/immunefi/status/2124865060258672914 | 📅 2026-11-23

**☕ 其他有趣八卦 / 吐槽 / 预警**
- 挪威能源公司被点名后，更值得担心的是被遗忘的 Classic 层 dev/test：生产若已改 Key Vault 引用，测试实例仍可能把 secret 写在 Named Values。口径是先假定泄露再轮换，而不是等取证结束。技术细节见云安全板块，不另计热度峰值。 | 👍 67 | 🔄 22 | 👀 未披露
- 🔗 来源: https://x.com/TheRegister/status/2124848587947598217 | 📅 2026-11-23

- Chainflip 被报道确认约 1200 万美元被盗，并向未识别攻击者提出返还要约（报道称留 10%、退 90%，期限压在 11 月 23 日）。这是被盗后的公开谈判，不是赏金计划付款，也不构成任何协助。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
- 🔗 来源: https://fxnx.com/en/analysis/chainflip-acknowledges-12m-exploit-and-puts-a-bounty-offer-to-the-unidentified-attacker-322c5415 | 📅 2026-11-23

- 长生命周期 AI 密钥仍是底色。[历史参考] Datadog 云安全研究原报告或早于窗口（一说约 11 月 10 日），11 月 23 日仍有解读：高危/严重漏洞中位数从 2 月的 4 升至 11 月的 16，云上推理仍大量使用长期 key。不计入本期热度峰值。本期更反复的主题是：网关、策略引擎和 Agent 把一份云身份放大成整片环境；平台修好入口，也不等于已经读走的密钥仍然安全。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
- 🔗 来源: https://www.datadoghq.com/blog/cloud-security-study-learnings-2026/ | 📅 2026-11-23
