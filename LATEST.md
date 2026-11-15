**【CyberSec 情报速报 | 云安全 & AI 重点强化】**

> 生成时间: 2026-11-15 15:47:14 UTC+08:00

**统计范围**: 2026-11-12 - 2026-11-15（包含起止日，共约 3-4 天数据）
**本期热度峰值**: 最高 👍 99 | 最高 👀 未披露
**今日情报眼**: CI供应链大规模窃取云密钥

已核实最高赞来自 The Hacker News 关于 Mior/Skyfall 的帖（2026-11-13，👍 99 / 🔄 23），正文有详细条目。浏览量在可追溯来源中均未直接显示，标「未披露」。窗口外及历史参考不计入峰值。

---

**📋 生成说明**
本报告由多份公开情报草稿合并、去重、排序而成，技术细节未经人工验证，仅供参考。互动只保留来源明确显示的数值，缺失标「未披露」，不推算。只保留事件影响与防御要点，不含利用步骤、载荷或复现细节。

---

**💰 本期最高赏金 / 最炸裂 payout**

- **$25,000 | @ixNyf | Immunefi | 智能合约 High**
  - 💡 一句话总结: 其首笔 High，冲上 90 日榜第 30；平台并给出 2026 年迄今 393 笔 High、260 名研究者的累计口径 | 👍 97 | 🔄 4 | 👀 未披露
  - 🔗 来源: https://x.com/immunefi/status/2120834502297841910 | 📅 2026-11-12

- **$11,000 | jojobizzare0102 | Immunefi | 智能合约 Medium**
  - 💡 一句话总结: 中危仍稳定出金，2026 年已付 189 笔 Medium | 👍 82 | 🔄 8 | 👀 未披露
  - 🔗 来源: https://x.com/immunefi/status/2121166232586256483 | 📅 2026-11-13

**[历史参考，不计入本期峰值]** OpenAI 将核心产品 Critical 上限提至约 $30,000、叠加奖金后最高约 $172,000 的公告在 2026-11-02/03，不在本统计窗。

---

**☁️ 云安全重点(特别加强板块)**

- **AMD SEV-SNP：Mior / Skyfall 打破机密 VM 主机隔离假设**
  - 🌟 亮点总结: ETH Zurich（Skyfall 含 Google）于 2026-11-13 公开两类需恶意 hypervisor 的攻击。Mior（CVE-2026-0462，CVSS 4.0 约 5.9）还可改内存并伪造 attestation；Skyfall（CVE-2026-40671，约 4.9）为信息泄露。修复在主机 SEV 固件/微码与平台 BIOS，租用机密 VM 的客户无法自行打补丁，须向云厂商确认 TCB/固件版本。未见在野利用声明。互动对应下述推文，不是网页另计。 | 👍 99 | 🔄 23 | 👀 未披露
  - 🔗 来源: https://x.com/TheHackersNews/status/2121266182242324769 | 📅 2026-11-13
  - 延伸阅读: https://thehackernews.com/2026/11/new-mior-and-skyfall-attacks-let-rogue.html

- **Chainguard Athena：9 个 Java 库 12 个静默漏洞，含 2 个 Critical 认证绕过**
  - 🌟 亮点总结: 11 月 12 日第二批披露，涉及 Apache Kerby、MockServer 等。每条有公开 VEX、GitHub 补丁与 Chainguard 仓库回移植，并与 Akamai、Cloudflare、Cloudsmith、Palo Alto、Zafran 做缓解协同。这是窗口内最具体的「AI 辅助挖洞 → 供应链静默漏洞」云原生制品案例，优先核对 Maven 依赖是否命中公告版本。 | 👍 21 | 🔄 6 | 👀 未披露
  - 🔗 来源: https://x.com/cloudsmith/status/2120987153215914277 | 📅 2026-11-12

- **wfx-loot：盗用 GitHub 令牌窃取 CI/云/AI 密钥，并留下抗轮换持久化**
  - 🌟 亮点总结: Aikido 于 11 月 12 日公开，窗口内持续被报道。约 4,837 个被盗 GitHub 账号对约 61,764 个仓库做写入探测，载荷在至少约 1,800 个仓库中实际运行。攻击不依赖 GitHub Actions 0day，而是有效写权限。探针 PR 标题类似 “docs: dependency audit notes”，分支常见 `wfx-docs`；向已有 workflow、脚本或 npm 生命周期钩子植入窃密逻辑后，短时间内回滚并删除运行记录，run 编号空洞是痕迹。目标含 Actions 密钥、`GITHUB_TOKEN`、OIDC，以及 AWS/Azure/GCP 与多家 AI 服务密钥。持久化可在单纯轮换后仍存活：AWS 角色信任被放宽，Azure 应用上出现以 `wfx-ci-` 为名的异常联合身份凭据。约 50 个账号具备包发布权限，公开报道点名部分大型机构与政府相关仓库。处置是按痕迹排查、轮换工作流能触达的全部密钥，并清理云侧后门，而不是只改 GitHub token。 | 👍 11 | 🔄 2 | 👀 未披露
  - 🔗 来源: https://x.com/AikidoSecurity/status/2121215028346900914 | 📅 2026-11-13

- **Amazon MadPot：ARTEX 代理被用于 AI 密钥窃取与交易所 KYC 深伪**
  - 🌟 亮点总结: AWS 安全博客（CJ Moses，2026-11-13）称，2026-10-03 至 11-05，伪装成 LLM API 的 MadPot 收到开源代理框架 ARTEX 回传的战役记忆。主线是窃取模型访问密钥并回填自身推理账单，形成自维持窃密；另一线对两家加密交易所做实时深伪过 KYC，记录中的尝试均被服务端拒绝。Amazon 对「使用 ARTEX」与「中国关联、多团伙」为中等置信，且不能核实代理自报战果；已通报可能受影响的 AWS 客户并发布 IOC。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/ | 📅 2026-11-13

- **Cursor 事后说明：Fireworks 侧密钥泄露牵出恶意 Claude Code 扩展**
  - 🌟 亮点总结: Cursor 于 2026-11-13 发布事件更新。攻击者使用 Cursor 发给 Fireworks 的访问密钥，拷走只读训练用存储桶中的历史 coding-agent trace（多为 2025、非 Privacy Mode）；不到 0.01% 客户的 API 凭证出现在其中。10-29 攻击者把非 Anthropic 发布的 `Anthropic.claude-code` 2.1.312/2.1.313 放到 Cursor 扩展市场缓存，约 11 小时，最多约 5,000 名请求特定缓存版本的用户可能拿到恶意构建。官方称最后可见攻击活动在 11-01 且已被阻断，Anthropic 官方通道与 Open VSX 源未受此影响。已安装对应版本者应按官方通知检查主机并轮换凭证，仅卸载扩展可能不够。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://cursor.com/blog/security-incident-update | 📅 2026-11-13

- **CVE-2026-125926：mcp-gateway-registry 注册 API SSRF，可打到内网与实例元数据**
  - 🌟 亮点总结: 厂商公告 AWS-2026-180 发布于 2026-11-11（窗口前一日），11-12 至 11-13 窗口内持续报道，本条按窗口内报道收录，不计入峰值。已认证且具备注册/修改服务器权限的用户，可让网关向部署内网及云实例元数据端点发请求并回读响应。影响 v1.0.3–1.34.0，修复版本 1.35.0。管理 API 越权（CVE-2026-100307）已在 1.25.0 修复，但该版本仍受本 SSRF 影响。未见公开在野利用证据。临时缓解是收紧注册权限、限制组件出站、强制 IMDSv2 并收缩实例角色。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://aws.amazon.com/security/security-bulletins/2026-180-aws/ | 📅 2026-11-12（公告 2026-11-11）

- **AWS 11 月 12 日另两则公告：Aurora Go Wrapper 提权、pandas EMR 日志位置所有权**
  - 🌟 亮点总结: 2026-182 / CVE-2026-126793：AWS Advanced Go Wrapper 在 Aurora PostgreSQL 方言检测路径存在不可信搜索路径，已认证用户在特定配置下可能提权至数据库高权限角色；公开转述指向修复版本 awssql/v2 2.0.3。2026-181 / CVE-2026-127119：AWS SDK for pandas 对默认 EMR 集群日志位置所有权校验不足，影响 awswrangler 1.1.0 至 3.18.0 之前。二者均为云数据面/SDK 信任边界问题，需按公告升级，而非仅靠网络层隔离。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://aws.amazon.com/security/security-bulletins/ | 📅 2026-11-12

**[历史参考，不计入本期峰值]**
- Datadog《State of Cloud Security 2026》原文约 2026-11-10。抽样中云服务高危/严重漏洞中位数由 2026 年 2 月约 4 个升至 11 月约 16 个；使用 Gemini 的组织中近半数依赖长寿命 API Key，Bedrock 侧约 17%；约 60% 组织在跑发布不足 24 小时的包版本；AWS data perimeter 采用率约 55%。窗口内 11-12 起仍有转述。官方帖互动属于窗口外，不计入峰值。https://www.datadoghq.com/state-of-cloud-security/
- CVE-2026-119990（Azure OpenAI 关键功能缺失认证，CVSS 9.8）于 11 月 10 日由微软发布。微软称服务端已缓解，客户无需操作，且未见已知在野利用。
- Google Cloud 2027 安全展望原文约 11-09，11-12 有媒体转述。核心判断是攻击窗口将短于人工响应，风险从直接盗数转向诱导自治 agent 做出有害业务决策；建议把每个 agent 当作一等身份并保留人工升级。

---

**📚 最值得读的 Writeup / 公开报告**

- **The Hacker News：Mior 与 Skyfall（SEV-SNP）**
  - 📝 技术摘要: 威胁模型是「不信任云主机」。Mior 破坏启动期内存权限表并影响 attestation；Skyfall 在故意失败的 VMRUN 后，通过已公开的瞬时调度侧信道读到寄存器状态。论文与厂商说明均指出利用条件苛刻（恶意 hypervisor，Mior 还需 BIOS/固件配合）。客户侧动作是核对云厂商固件与 SNP attestation TCB，而不是自行补丁。 | 👍 99 | 🔄 23 | 👀 未披露
  - 🔗 链接: https://x.com/TheHackersNews/status/2121266182242324769 | 📅 2026-11-13
  - 报告: https://thehackernews.com/2026/11/new-mior-and-skyfall-attacks-let-rogue.html

- **Aikido：wfx-loot CI 窃密活动**
  - 📝 技术摘要: 先用被盗账号开探测 PR 确认写权限，再向 workflow 注入窃密逻辑，跑完回滚并删运行记录。收集面覆盖 CI 密钥、云厂商凭证与 AI 供应商密钥；随后用 OIDC 换云会话，并尝试留下 AWS 信任策略或 Entra 联合凭据。排查信号是 `wfx-docs`、指定 PR 文案，以及 Actions 运行编号空缺。阅读价值在于「轮换不够」的云取证清单。 | 👍 11 | 🔄 2 | 👀 未披露
  - 🔗 链接: https://x.com/AikidoSecurity/status/2121215028346900914 | 📅 2026-11-13

- **Amazon：ARTEX 代理战役复盘（AWS Security Blog）**
  - 📝 技术摘要: 诱饵 LLM API 因 agent 会回传任务上下文，单次请求即带出系统提示、工具历史与知识图。报告描述的是窃取 AI 网关凭据的自筹资循环，以及对交易所活体检测的深伪尝试及失败；强调结果未经独立证实。适合做检测与密钥卫生，而不是复现攻击。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/ | 📅 2026-11-13

- **Check Point Research：PHP2Shell + CVE-2026-123039**
  - 📝 技术摘要: 公开链是「Mobile Access Portal 初始访问 → Gaia Dynamic CLI 提权到 root → 持久化」。厂商给出受影响 Gaia 版本、在野时间窗与客户侧调查指引。优先安装已包含 PHP2Shell 与该 LPE 的 Jumbo/热修，并按公告做入侵排查。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/ | 📅 2026-11-12

- **Cursor 安全事件更新**
  - 📝 技术摘要: 把扩展投毒追溯到供应商访问密钥与历史 agent trace 中的未脱敏凭证，划清 Anthropic 官方通道未受影响、Open VSX 源未带毒。适合作为 AI 编码工具供应链复盘：已安装指定恶意构建的主机，卸载扩展不足以结案。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://cursor.com/blog/security-incident-update | 📅 2026-11-13

---

**🔥 社区热议的技术话题或新手法**

- **机密计算的信任根仍在云主机固件**
  - 💬 讨论核心: Mior/Skyfall 再次说明 SEV-SNP 防的是恶意运营商，而补丁在 host BIOS/SEV 固件。租户无法自己修，只能用 attestation 核对 TCB。该帖是本期已核实赞数最高的讨论。 | 👍 99 | 🔄 23 | 👀 未披露
  - 🔗 代表性推文: https://x.com/TheHackersNews/status/2121266182242324769 | 📅 2026-11-13

- **CI OIDC → 云角色信任改写（抗轮换后门）**
  - 💬 讨论核心: 焦点不是脚本本身，而是「密钥轮换后仍能登录」：AWS AssumeRole 信任被放宽，Azure/Entra 联合凭据以 `wfx-ci-` 开头。讨论从秘密扫描转到信任策略与联合身份的变更检测。 | 👍 6 | 🔄 0 | 👀 未披露
  - 🔗 代表性推文: https://x.com/MalwareBibleJP/status/2121605074552311971 | 📅 2026-11-14

- **Agentic offense / 自维持 AI 密钥狩猎**
  - 💬 讨论核心: 社区焦点从「模型会不会写 exploit」转到「开源 agent 框架已被用于持续作战」。ARTEX 案例的新点是：偷来的模型 key 直接支付下一轮推理，且 agent 会把完整记忆打到它以为的推理端点。防御含义落在 LLM 网关默认口令、长生命周期 key，以及不要把未知推理端点当可信后端。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性推文: https://x.com/DFIR_Radar/status/2121423825963225579 | 📅 2026-11-14

- **长寿命云托管模型 API Key**
  - 💬 讨论核心: 底层报告为 2026-11-10 **[历史参考]**，窗口内仍被转述。论点是：与其再堆一层 prompt 过滤，不如取消 Gemini/Bedrock/Foundry 的长期密钥，改走工作负载短时身份。静态 AI key 被放在与 CI 窃密同一风险链上。本条不计入峰值。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性链接: https://www.voicendata.com/cloud/datadog-flags-fourfold-rise-in-cloud-vulnerabilities-amid-ai-adoption-12804278 | 📅 2026-11-12

- **MCP Gateway 成为云元数据新入口**
  - 💬 讨论核心: MCP 注册中心把「AI 工具发现」和「服务端代发请求」绑在一起后，SSRF 的爆炸半径落到 IMDS 与内网控制面。共识是：能改上游 URL 的身份应视为高权限，出站默认拒绝 IMDS 与内网段。公告日本身为 11-11，本条取窗口内讨论。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性链接: https://cyberpress.org/aws-mcp-gateway-ssrf-flaw/ | 📅 2026-11-13

**[历史参考，不计入本期峰值]** 11 月上旬的 DeepMind 多智能体注入与 Amazon 任务篡改研究（链接日期约 11-10）本周仍被引用。结论停留在：注入远未解决，权限和人工确认要放在模型之外。

---

**🆕 新上线 / 更新中的 Bug Bounty 或 VDP 项目**
本期无高互动/突破性情报

窗口内未核到新项目上线。Google Cloud「Root-in-Cloud」与 Phala Cloud TEE/机密 AI 赏金（Critical 最高约 $7,500，帖时 2026-11-11）均不在本统计窗，标 **[历史参考]**，不计入本期峰值。

---

**📢 平台动态 & 政策变化**

- **Deriv 在 HackerOne 对 Medium/High/Critical 提供 2 倍赏金，活动窗口 2026-11-10 至 11-24（官推在窗口内）** | HackerOne | 👍 26 | 🔄 7 | 👀 未披露
  - 🔗 来源: https://x.com/Hacker0x01/status/2120823422783512608 | 📅 2026-11-12

- **CISA KEV 新增 Check Point CVE-2026-123039，联邦机构修补期限 2026-11-16** | CISA（经由公开汇总） | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://blog.checkpoint.com/security/security-advisory-active-exploitation-of-php2shell-and-local-privilege-escalation/ | 📅 2026-11-13

---

**🏆 猎人里程碑 / 大额奖励**

- **@ixNyf 拿到 Immunefi 个人首笔 High（$25,000），90 日榜第 30**
  - 🌟 中文概述: 平台用该单说明 High 仍分散在大量「只有一笔」的研究者中（260 人里 172 人仅一笔） | 👍 97 | 🔄 4 | 👀 未披露
  - 🔗 链接: https://x.com/immunefi/status/2120834502297841910 | 📅 2026-11-12

- **jojobizzare0102 获得 $11,000 Medium**
  - 🌟 中文概述: 官方强调中危不吸睛但持续出金，2026 年已支付 189 笔 Medium | 👍 82 | 🔄 8 | 👀 未披露
  - 🔗 链接: https://x.com/immunefi/status/2121166232586256483 | 📅 2026-11-13

- **@mdp_sec 周结：$3.6k XSS、$3k P1 等**
  - 🌟 中文概述: 汇总帖于 11-13 发布。其中 Skyscanner/@Bugcrowd 的 $3,000 P1 原帖在 11-10，标 **[历史参考]**，不单独计入本期峰值；本条互动只计 11-13 帖 | 👍 65 | 🔄 1 | 👀 未披露
  - 🔗 链接: https://x.com/mdp_sec/status/2121173729879482711 | 📅 2026-11-13

---

**☕ 其他有趣八卦 / 吐槽 / 预警**

- **Check Point 网关遭在野利用：PHP2Shell 串联 CVE-2026-123039，已入 CISA KEV**
  - 💬 预警: Check Point Research 于 2026-11-12 确认，面向 Mobile Access Portal 的 PHP2Shell 被用于初始访问，再经 Gaia Dynamic CLI 本地提权 CVE-2026-123039（CVSS 7.8）拿到 root 并做持久化。活动约从 2026-10-30 持续至 11-04；PHP2Shell 热修 10-23 已有。CISA 于 11-13 将其列入 KEV，联邦期限 2026-11-16。公开报道称部分客户在 10-30 与 11-02 遭波及，个别案例涉及 ESXi 擦除。优先给暴露网关打已包含两处修复的 Jumbo/热修，而不是等待完整利用细节。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://blog.checkpoint.com/security/security-advisory-active-exploitation-of-php2shell-and-local-privilege-escalation/ | 📅 2026-11-12

- **Uber 确认经 Fireworks AI 泄露美国司机驾照等个人信息**
  - 💬 预警: 供应商 2026-10-09 通知凭据被盗用；州申报可见量级包括南卡约 3,430、马萨诸塞约 2,567、罗得岛约 1,873。Notion 亦受同一供应商事件影响。攻击者动机被描述为盗卖 LLM token，而非直接打进 Uber 生产网。与 Cursor 事件同属 Fireworks 密钥链，但是不同受害者。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://techcrunch.com/2026/11/13/uber-confirms-hackers-stole-thousands-of-drivers-license-information-in-data-breach/ | 📅 2026-11-13

- **npm 包 @claudecode/cli 被标为恶意软件**
  - 💬 预警: GHSA-vp2q-gp5r-xh5j（2026-11-13），全版本受影响且无补丁版。任何安装或运行过的机器应视为完全失陷：从另一台干净设备轮换全部密钥并重装主机，不要只删包。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://github.com/advisories/GHSA-vp2q-gp5r-xh5j | 📅 2026-11-13

- **只轮换密钥会漏掉 wfx 留下的云后门**
  - 💬 预警: 若仓库在 11 月 10 日之后出现可疑 CI 改动或 workflow run 编号空洞，应同时查 AWS 信任策略是否对异常主体放开，以及 Azure 应用是否新增 `wfx-ci-` 一类联合身份凭据；有包发布权限的账号还要核对已发布制品。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://x.com/AikidoSecurity/status/2121215028346900914 | 📅 2026-11-13

- **自建 MCP registry 不要停在 1.25.0**
  - 💬 预警: 该版本修的是另一条管理面越权，SSRF（CVE-2026-125926）仍在，直到 1.35.0。Fork 同样需要合入上游地址校验。公告日为 11-11，窗口内仍是有效修补提醒。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://aws.amazon.com/security/security-bulletins/2026-180-aws/ | 📅 2026-11-11
