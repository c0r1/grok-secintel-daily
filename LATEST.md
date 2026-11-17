**【CyberSec 情报速报 | 云安全 & AI 重点强化】**

> 生成时间: 2026-11-17 17:07:53 UTC+08:00

**统计范围**: 2026-11-14 - 2026-11-17（包含起止日，共约 3-4 天数据）
**本期热度峰值**: 最高 👍 359 | 最高 👀 未披露
**今日情报眼**: AI代理已能自动武器化补丁

---

**📋 生成说明**
本报告由 AI 自动汇总公开社交媒体与新闻情报，技术细节未经人工验证，仅供参考。互动数仅采用原帖直接显示的数值，缺失标「未披露」，不推算；浏览量在已核来源中均未披露。窗口外材料标[历史参考]，不计入本期热度峰值。以下只保留影响与防御含义，不包含利用步骤、PoC 或 Payload。

---

**💰 本期最高赏金 / 最炸裂 payout**
本期无高互动/突破性情报

窗口内未核到金额与猎人可追溯的单笔新增大额 payout。Immunefi 公布的是 Solana 生态累计数据，不是单笔赏金；项目奖池上限不等于本期 payout。

---

**☁️ 云安全重点(特别加强板块)**

- GTIG：云上 LLM 凭据转售（LLMjacking）与长效令牌
  - 🌟 亮点总结: 11 月 16 日 GTIG AI Threat Tracker 指出，攻击者从企业环境窃取 LLM 与云资源凭据，再经地下渠道转售算力与 API 访问；同一观察还涉及云配额滥用、配置被植入后门，以及长期有效的 CI/CD API token。多代理框架可在无人逐步确认下对公开补丁做差分并尝试利用。防御重点是短时身份、密钥轮换、异常推理流量与账单监控，并把控制面和流水线令牌加上网络与权限约束，而不是只看传统主机告警。 | 👍 359 | 🔄 108 | 👀 未披露
  - 🔗 来源: https://x.com/TheHackersNews/status/2122330337334464721 | 📅 2026-11-16

- AWS Labs MCP：InfluxDB 令牌外带，兼定价报告路径穿越
  - 🌟 亮点总结: 11 月 16 日两则 AI Agent 工具面公告。GHSA-2f9r-g4f3-wc2j / CVE-2026-126681：awslabs.timestream-for-influxdb-mcp-server 0.0.12 至 0.0.19 之前，连接端点未限制，Prompt Injection 可把伪造 InfluxDB URL 送入客户端上下文，使已配置 API token 发往非预期地址；修复 0.0.19，并需轮换 token。GHSA-mqm3-w68j-75mw / CVE-2026-126816：aws-pricing-mcp-server 1.0.31 之前，成本报告输出路径可写出预定目录之外，且工具被错误标成 readOnlyHint（CVSS 3.1 为 5.5）；修复 1.0.31。MCP 工具应视为带凭证的云控制面。 | 👍 4 | 🔄 0 | 👀 未披露
  - 🔗 来源: https://github.com/awslabs/mcp/security/advisories/GHSA-2f9r-g4f3-wc2j | 📅 2026-11-16

- Wiz AI Security Agent 公开预览
  - 🌟 亮点总结: Wiz 11 月 16 日称 AI Security Agent 进入 Public Preview：在自托管（VM/容器/Serverless/存储桶代码）、受支持 PaaS 与代码仓库发现 AI 应用，对照声称用途与实际能力，并把提示词、配置风险挂到云暴露、权限与数据上。厂商称部分客户环境中发现的 AI Agent 数量可达传统发现引擎的约 5 倍。这是图谱向 Agent 身份与工具权限扩展，不是漏洞通告。 | 👍 1 | 🔄 0 | 👀 未披露
  - 🔗 来源: https://www.wiz.io/blog/introducing-wiz-ai-security-agent | 📅 2026-11-16

- Barracuda / ARTEX：未轮换第三方云密钥链式扩张
  - 🌟 亮点总结: 11 月 16 日前后窗口内报道：攻击者使用已泄露、未轮换的第三方云访问密钥，约 44 小时内触及约 10 个云账户，并沿密钥与源码令牌进入 Kubernetes；资源命名与钱包/凭据搜寻被比对为开源 AI 渗透框架 ARTEX。入侵活动在 11 月 1–2 日，早于本期，本期计入的是窗口内报道。11 月 14 日起另有分析称，Amazon MadPot 见到同类代理请求，目标集中在汇聚 AI 供应商密钥的网关与构建平台，并出现走向云元数据的 SSRF 意图；相关 Cloudflare 案例指向无过期、无 IP 限制的账户级 CI/CD API token。共性是静态云身份。优先轮换第三方长期密钥，排查 IaC state 与 CI 日志，并为令牌加 IP 与权限边界。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.securityweek.com/barracuda-hacked-amid-surge-in-artex-powered-cyberattacks/ | 📅 2026-11-16

- AWS：DJL 模型归档任意本地文件读取（CVE-2026-129266）
  - 🌟 亮点总结: AWS 11 月 16 日发布 2026-183-AWS。Deep Java Library 未校验模型归档元数据中的资源位置，远程未认证方可借助恶意模型归档读取进程可读文件。影响 ≥0.7.0 且 ≤0.38.0，修复版本 0.39.0。官方建议只加载可信归档，并收紧 djl-serving 管理/推理接口与 model_url_pattern。云上推理与模型分发须把模型包视为不可信输入。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://aws.amazon.com/security/security-bulletins/2026-183-aws/ | 📅 2026-11-16

- [历史参考] Datadog《State of Cloud Security 2026》（11 月 10 日发布，不计入本期峰值）
  - 🌟 亮点总结: 云工作负载高危/严重漏洞中位数约从 4 升至 16；使用 Gemini 的组织中近半数仍用长期 API Key，使用 Bedrock 的约 17% 同样如此；部分 AWS IAM / GCP 服务账号密钥超过三年。与本期密钥被收割、补丁窗口被压缩同向，但是背景而非本窗口新披露。 | 👍 未计入 | 🔄 未计入 | 👀 未计入
  - 🔗 来源: https://www.datadoghq.com/state-of-cloud-security/ | 📅 2026-11-10

---

**📚 最值得读的 Writeup / 公开报告**

- GTIG：Agentic Threat Activity Crosses a Significant Threshold
  - 📝 技术摘要: Google 11 月 16 日称，攻击方已用多代理框架加快入侵，并对热门 Web 应用做补丁前后差分、起草并执行利用，以压缩 n-day 窗口。在一台暴露的暂存服务器上看到名为 exploit_agent 的配置：接入多种前沿与本地 LLM，配置注释为俄文；同机还有受害方遥测与入侵后脚本。遥测指向法国媒体、娱乐与教育站点。报告未证明该框架本身造成那些入侵，也未给出具体 CVE、受害规模或实测时延。同期记录 LLMjacking、钓鱼即服务用 LLM 改诱饵，以及大量看似可用、实际无效的 LLM 生成利用代码。另述零日披露节奏上升（2025 年月均约 8 起，2026 年月均约 11 起，8 月约 22 起）。失陷后常见云配额占用与配置后门。这是威胁情报观察，不是复现材料。防御含义：补丁日即暴露窗口，优先修面向互联网的应用，并轮换可能已泄露的模型与云 API 密钥。 | 👍 359 | 🔄 108 | 👀 未披露
  - 🔗 链接: https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold | 📅 2026-11-16

- DeepAudit 未认证配置接口泄露 LLM 与 Git 令牌（CVE-2026-129877）
  - 📝 技术摘要: VulnCheck 于 11 月 16 日发布。DeepAudit 2.0.0-beta.1 至 3.8.0 的配置默认值接口缺少关键功能认证，未认证请求即可取回运营方的 LLM 供应商 API key 以及 GitHub/GitLab token，随后可滥用对应仓库与模型账户。CVSS 4.0 为 8.7。公开建议是升级、立刻轮换已暴露密钥，并限制该接口。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://www.vulncheck.com/advisories/deepaudit-2.0.0-beta.1-through-3.8.0-information-disclosure-via-api-v1-config-defaults | 📅 2026-11-16

- RedAmon 沙箱终端通道缺失认证（CVE-2026-129855）
  - 📝 技术摘要: 11 月 16 日收录、产品侧称 11 月 14 日披露。RedAmon 7.8.0 之前，kali-sandbox 终端服务缺少认证，能到达该监听端口的同主机或相邻容器调用方可在容器内获得 root 级交互壳。影响限于可达该服务的相邻环境，不是直接的互联网 RCE。修复版本 7.8.0。适合作为「AI 渗透框架自身变成攻击面」的案例，而非操作手册。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://app.opencve.io/cve/CVE-2026-129855 | 📅 2026-11-16

---

**🔥 社区热议的技术话题或新手法**

- exploit_agent / 补丁差分自动化
  - 💬 讨论核心: @TheHackersNews 11 月 16 日帖是本期已核实最高赞。焦点从「人用 LLM 写 PoC」转到「代理自己对比补丁并往下打」。Google 称这是其首次看到 LLM 框架在无人介入下做漏洞发现与利用尝试，但证据停留在暴露服务器上的框架与配置，归因与实战成功率仍未公开。无效 LLM 利用代码变多，会抬高分诊噪音。讨论应落在把面向互联网的补丁收到当日、限制预发布源码扩散，而不是复现该流水线。 | 👍 359 | 🔄 108 | 👀 未披露
  - 🔗 代表性推文: https://x.com/TheHackersNews/status/2122330337334464721 | 📅 2026-11-16

- 2026 年 CVE 越过 10 万，可利用子集仍很小
  - 💬 讨论核心: International Cyber Digest 引 VulnCheck：截至 11 月 13 日已有 100,222 条 CVE，约为 2025 全年两倍；在野目录约 1.4%（1,363）。另有评论称，公布到被利用的中位时间从约 120 天降到约 80 天，且大量利用紧跟公开 PoC。数量本身不是风险，可到达、可利用的那一小部分才是，优先级不能再按 CVE 数量排。 | 👍 128 | 🔄 21 | 👀 未披露
  - 🔗 代表性推文: https://x.com/IntCyberDigest/status/2121456841494614053 | 📅 2026-11-14

- [历史参考] DeepMind：Agent Swarm 与 Prompt Injection（论文 11 月 9 日，不计入本期峰值）
  - 💬 讨论核心: 论文《Scaling Adaptive Prompt Injection Attacks with Agent Swarms》提交于 11 月 9 日；原帖在窗口外。11 月 15 日二次报道继续传播同一结论：协作式代理在完整预算下把多款模型的抗注入成功率压到约 10% 或更低；Gemini 4 Argon 约 66%，Kimi K3、GLM-5.3、DeepSeek-V4.1-Flash 约 1%。社区共识是不能只靠模型对齐，必须做权限、工具与数据面的纵深限制。 | 👍 未计入 | 🔄 未计入 | 👀 未计入
  - 🔗 代表性推文: https://arxiv.org/abs/2611.11861 | 📅 2026-11-09

---

**🆕 新上线 / 更新中的 Bug Bounty 或 VDP 项目**
本期无高互动/突破性情报

窗口内可见的新项目或赏金上调，要么互动未达收录阈值，要么无法核实上线日落在本窗口。Deriv 双倍与 Firedancer 加码的主公告早于 11 月 14 日，不计入本期。

---

**📢 平台动态 & 政策变化**

- Immunefi 称研究者在 Solana 生态项目上累计获得 1180 万美元赏金，其中约 990 万美元对应可直接盗取或永久冻结资金的 Critical；并在 Breakpoint 招揽尚未开赏金的协议。此为累计口径，不是窗口内单笔 payout。 | Immunefi | 👍 42 | 🔄 3 | 👀 未披露
- 🔗 来源: https://x.com/immunefi/status/2122298690757136619 | 📅 2026-11-16

---

**🏆 猎人里程碑 / 大额奖励**
本期无高互动/突破性情报

---

**☕ 其他有趣八卦 / 吐槽 / 预警**

- Wiz 用一串二进制发预热：解码后是 “24 DAYS TILL ZERO DAY CLOUD READY TO HACK?”，指向其云安全活动倒计时，不是漏洞披露。 | 👍 156 | 🔄 14 | 👀 未披露
- 🔗 来源: https://x.com/wiz_io/status/2121998646119899577 | 📅 2026-11-15

- 预警：把 AI 网关、MCP Server 和 CI/CD 令牌当成云控制面同等资产。窗口内已同时出现未认证读密钥、Prompt Injection 外带云数据面 token，以及用永不过期 API token 进入多云账户的案例。优先动作是轮换、改短时身份、给令牌加 IP 与权限边界，并把互联网资产的补丁 SLA 收到公布当日。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
- 🔗 来源: https://github.com/awslabs/mcp/security/advisories/GHSA-2f9r-g4f3-wc2j | 📅 2026-11-16
