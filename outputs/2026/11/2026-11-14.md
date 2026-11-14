**【CyberSec 情报速报 | 云安全 & AI 重点强化】**

> 生成时间: 2026-11-14 15:33:10 UTC+08:00

**统计范围**: 2026-11-11 - 2026-11-14（包含起止日，共约 3-4 天数据）
**本期热度峰值**: 最高 👍 249 | 最高 👀 未披露
**今日情报眼**: GitHub供应链大规模盗云密钥

已核实最高点赞为 Perplexity SPACE 红队帖（👍 249，正文有详条）；浏览量均未披露。多热点并存时，情报眼按大规模密钥泄露/供应链优先，锚定 wfx-loot。历史参考不计入峰值。

---

**📋 生成说明**
本报告由多份 AI 汇总稿合并、去重、排序而成，技术细节未经人工验证，仅供参考。互动只保留来源明确给出的数值，缺失标「未披露」，不推算。窗口外背景标「历史参考」，不计入本期热度峰值。

---

**💰 本期最高赏金 / 最炸裂 payout**
本期无高互动/突破性情报

---

**☁️ 云安全重点(特别加强板块)**
- Perplexity SPACE：Agent 沙箱红队，安全专用模型并不必然更强
  - 🌟 亮点总结: 本期已核实最高赞。对 Computer Agent 的 Firecracker microVM 沙箱做红队：12 个模型执行「逃出 VM、取走仅存在于宿主机的凭据」和「绕过出网策略访问被禁 URL」。标准 CTF 提示会把算力带离真正要测的隔离边界；改写任务后，花在 VM–宿主机边界上的努力平均上升约 60 个百分点。非安全专用模型有时比安全向模型更会找隔离与网络绕过（含 DNS 欺骗一类）。网络策略缺陷已修，复测未再绕过。对云上 Agent 运行时：隔离、凭据放置和出网策略比模型榜单更关键。 | 👍 249 | 🔄 31 | 👀 未披露
  - 🔗 来源: https://x.com/perplexity_ai/status/2120582674549203004 | 📅 2026-11-11

- wfx-loot：被劫持 GitHub 账号向大量仓库投放 CI 密钥窃取器，直指云与 AI 凭据
  - 🌟 亮点总结: 约 11 月 10 日起，攻击者以被盗写权限推送自称 wfx 的 GitHub Actions 载荷。Aikido 统计约 4,837 个账号对约 61,764 个仓库发起探测 PR（常见标题 “docs: dependency audit notes”），至少约 1,835 个仓库实际执行并外传；GitGuardian 自有样本约 28,500 个补丁、2,367 个账号、17,715 个仓库，计数口径不同，规模结论一致。窃取面覆盖 Actions secrets、OIDC/runtime token、AWS/GCP/Azure 会话，以及 OpenAI、Anthropic、Gemini、Cursor 等 AI 令牌。云侧可创建长期 AKIA、把角色信任改成 `"Principal": {"AWS": "*"}` 一类持久化，并给 Azure 应用添加联邦凭据；单纯轮换密钥不够。提交常在约一分钟内回滚并删除运行日志。npm postinstall 使风险延伸到开发者本机。属供应链 + Cloud Takeover 前置条件，优先排查可写仓库、信任策略与联邦凭据残留。 | 👍 196 | 🔄 36 | 👀 未披露
  - 🔗 来源: https://x.com/IntCyberDigest/status/2120951007878238368 | 📅 2026-11-12
  - 分析: https://www.aikido.dev/blog/compromised-github-accounts-push-ci-secret-stealer-to-tens-of-thousands-of-repositories

- AntiFox（基于 ARTEX）关联入侵触及 AWS 生产密钥
  - 🌟 亮点总结: Arctic Wolf 披露，Alibaba Cloud 上托管的 AntiFox 界面与针对公网 IIS 及关联 AWS 环境的活动有关。攻击者使用有效 IAM/EC2 角色做跨服务枚举（含 Secrets Manager、S3、Bedrock 等），部分 GetSecretValue 与 S3 操作成功。AWS 称服务本身未被攻破，问题出在客户侧被盗凭证。属本期云与 AI 进攻框架交叉的实战入侵，而非云控制面 0day。 | 👍 149 | 🔄 54 | 👀 未披露
  - 🔗 来源: https://x.com/TheHackersNews/status/2120540829488197766 | 📅 2026-11-11
  - 背景报道: https://thehackernews.com/2026/11/antifox-ai-pentesting-platform-linked.html

- Mior 与 Skyfall：恶意云主机可破坏 AMD SEV-SNP 机密虚拟机
  - 🌟 亮点总结: 11 月 13 日公开的两起主机侧攻击，直接打在「不信任 Hypervisor」的机密计算模型上。Mior（CVE-2026-0462，CVSS 4.0 约 5.9）在 SEV-SNP 启动阶段干扰 PSP 对 RMP 的写入，可改访客内存、打开本应关闭的调试，并伪造证明报告中的软件度量；需要 Hypervisor + BIOS/UEFI 控制及可控 PCIe 设备。Skyfall（CVE-2026-40671，约 4.9）利用 VM 启动失败路径上未清理的缓存，经 Transient Scheduler 侧信道读出寄存器（实验中含磁盘加密密钥一类数据），只需恶意 Hypervisor。影响多代 EPYC（约 7003/8004/8005/9004/9005）。修复在主机固件/微码，租户无法自行打补丁，只能等云厂商更新，并用 SNP attestation 的 TCB 核对。未见在野利用表述。 | 👍 71 | 🔄 15 | 👀 未披露
  - 🔗 来源: https://x.com/TheHackersNews/status/2121264146390122799 | 📅 2026-11-13

- AWS mcp-gateway-registry：SSRF 可达内网/IMDS，另有管理 API 提权
  - 🌟 亮点总结: 2026-11-11 AWS 公告。CVE-2026-125926（2026-180-AWS）影响 v1.0.3–1.34.0：具备注册或修改服务器权限的认证用户，可让网关向部署内网甚至实例元数据端点发请求并回读响应。1.35.0 修复，但升级前已保存的上游地址不会自动清理，需人工复查并视情况轮换所附角色凭证。临时缓解包括限制注册权限、收紧出站、EC2 强制 IMDSv2。同产品 CVE-2026-100307（2026-179-AWS）为外部管理 API 缺少授权，低权限用户可把自己提升为 registry 管理员，修复在 1.25.0；因此停在 1.25–1.34 仍暴露于 SSRF。研究员署名为 novice-22。 | 👍 0（抽样原帖） | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://aws.amazon.com/security/security-bulletins/2026-180-aws/ | 📅 2026-11-11

- Datadog《State of Cloud Security 2026》：云工作负载高危漏洞中位数约增至 4 倍
  - 🌟 亮点总结: 正式发布在窗口边缘（11 月 10 日），11-11 起持续被转述，计入本期讨论。所分析云服务的高危/严重漏洞中位数由 2026 年 2 月约 4 个升至 11 月约 16 个，并与前沿模型加速挖洞（所谓 Vulnpocalypse）同期。使用 Gemini 的组织中近半数仍用长期 API key，使用 Bedrock 的约 17% 同样如此；另有表述称 Azure 侧默认长期密钥且绝大多数组织未改。约 60% 的组织在跑发布不足 24 小时的包版本。AWS 数据边界采用率由 2025 年的 40% 升至约 55%。建议用工作负载短时身份访问推理服务，而不是单独的长期 key。 | 👍 0（窗口内转述帖） | 🔄 0 | 👀 未披露
  - 🔗 来源: https://www.datadoghq.com/state-of-cloud-security/ | 📅 2026-11-11（覆盖）

- CVE-2026-127119：aws-sdk-pandas 默认 EMR 日志桶所有权未校验
  - 🌟 亮点总结: AWS 于 2026-11-12 公告（2026-181-AWS）。awswrangler / aws-sdk-pandas 在 ≥1.1.0 且 <3.18.0 时，EMR 模块把可预测的默认日志位置（`aws-logs-{account}-{region}`）交给 RunJobFlow，且不核验桶归属。攻击者若预先占住该桶名，可能读到其他租户的 EMR 集群日志（含作业步骤输出）。3.18.0 已修复。不能立刻升级时，应显式指定日志位置，或在本账号各区域先建好默认日志桶。同系列更早的 SageMaker / Athena 可预测桶问题为 [历史参考]（原文早于本窗口），不计入本期热度。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://aws.amazon.com/security/security-bulletins/2026-181-aws/ | 📅 2026-11-12

- CVE-2026-126793：AWS Advanced Go Wrapper Aurora 方言检测提权
  - 🌟 亮点总结: 2026-11-12 公告 2026-182-AWS。已认证数据库用户可在他人 search_path 上创建函数；当目标用户经受影响的 wrapper 连接 Amazon Aurora PostgreSQL 时，可能提升至该用户权限，包括 rds_superuser 成员。影响 awssql/v2 2.0.0–2.0.2，修复为 2.0.3。属云数据库客户端库的权限边界问题，应核对依赖版本，而不是只看数据库引擎补丁。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://aws.amazon.com/security/security-bulletins/2026-182-aws/ | 📅 2026-11-12

**📚 最值得读的 Writeup / 公开报告**
- Google DeepMind：Agent Swarm 自适应 Prompt Injection
  - 📝 技术摘要: 论文约 11 月 10 日，窗口内解读计入本期。公开红队基准接近饱和后，16 智能体协作的 Agentic Optimizer 仍能稳定打出间接注入。最强攻击预算下，Gemini 4 Argon 作为防御方抵抗率约 66%，若干开源权重模型（Kimi K3、GLM-5.3、DeepSeek 等）抵抗率可低至约 1%。结论是 Prompt Injection 远未解决，更强模型也会变成更强攻击者。评估关闭了部分模型外缓解，数字不能直接当成生产默认配置。 | 👍 46（相关讨论帖） | 🔄 8 | 👀 未披露
  - 🔗 链接: https://arxiv.org/html/2611.11861v1 | 📅 2026-11-12

- Cursor 安全事件更新：Fireworks 密钥泄露链到恶意扩展
  - 📝 技术摘要: 11 月 13 日更新。攻击者取得 Cursor 发给 Fireworks、且被对方暴露的访问密钥，复制只读共享桶中的 coding agent traces（多为非 Privacy Mode、2025 年数据）。极少数 traces 含未脱敏凭证（称不足 0.01% 客户 API 凭证暴露），进而触及部分 SaaS，并在 10 月 29 日向 Cursor VS Code 扩展市场缓存投放恶意 Claude Code 扩展副本（约 11 小时，最多约 5,000 用户可能命中）。官方称 11 月 1 日后活动被阻断，Privacy Mode 用户的提示与代码未受影响。属 AI 编码工具供应链/凭证残留事件。 | 👍 未披露（相关转推 🔄 77） | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://cursor.com/blog/security-incident-update | 📅 2026-11-13

- Aikido / GitGuardian / Semgrep：wfx-loot 的规模、回滚与云后门
  - 📝 技术摘要: 长文补足推文未展开的检测点。链路是先确认写权限，再把 shell 载荷塞进已有 workflow、npm install 钩子或一次性分支；执行后回滚并删日志，只看最终 commit 会漏掉。GitGuardian 将活动分为 10 月小规模前奏与 11 月 10–12 日主波，外传地址随版本从 HTTP 切到 Telegram；GitHub 拦截 workflow 形态时，npm 钩子仍可能在安装阶段执行。Semgrep 强调检测 wfx-docs 分支、指定 PR/commit 标题，以及 AWS 信任策略被改成通配主体、Azure 联邦凭据名含 wfx-ci-；与 10 月 GhostAction 受害账号有重叠，但研判更像不同行动者。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://www.aikido.dev/blog/compromised-github-accounts-push-ci-secret-stealer-to-tens-of-thousands-of-repositories | 📅 2026-11-12
  - 互补: https://blog.gitguardian.com/wfx-loot-a-ci-secret-stealer-pushed-with-stolen-github-credentials/ | https://semgrep.dev/blog/2026/seconds-from-disaster-wfx-phantom-and-the-ci-pipeline-nobody-was-watching/

- Amazon Threat Intelligence：ARTEX 智能体犯罪活动观察
  - 📝 技术摘要: 2026-10-03 至 11-05，MadPot 诱饵以热门 LLM 推理 API 形态捕获 ARTEX 智能体请求，请求中带有战役自身记录。最突出战役是大规模窃取 AI 模型凭证，并以被盗 key 支付后续推理，形成自我维持循环；记录还涉及侦察、漏洞测试、云权限扩展与加密货币欺诈尝试。Amazon 对使用 ARTEX 的评估为中等置信，并已向可能受影响的 AWS 客户通报。与本期 AntiFox 滥用同属智能体进攻框架实战化。Datadog 追踪文正式日期为 11 月 9 日，标 [历史参考]，仅作互补背景。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/ | 📅 2026-11-13

- NEAR AI：SGLang RCE 打进推理环境（窗口内为事件跟进）
  - 📝 技术摘要: 入侵约发生在 2026-11-08，公司通报略早于本窗口；11-11 与 11-13 的公开复盘计入本期。攻击者利用 SGLang 推理引擎的远程代码执行进入一台位于可信执行环境中的推理服务器，触及约 100 名 Private Chat 用户的账户信息，以及旧部署上 18 个 Agent 的历史、设置与日志；日志中还有 2 个客户的 Cloud API key（已吊销）。公司称未见已存储的 Private Chat 对话或上传文件被访问，但 11-08 当天经该服务器的请求（含机密模式）可能被观察到。具体 SGLang 缺陷编号公开材料未给出。教训是模型服务软件要按互联网暴露面补丁，而不能只防 prompt injection。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://dailysecurityreview.com/resources/sglang-rce-flaw-exploited-to-breach-near-ai-18-agents-exposed/ | 📅 2026-11-11

**🔥 社区热议的技术话题或新手法**
- Agent 沙箱逃逸：安全模型未必更会打隔离
  - 💬 讨论核心: Perplexity 公开 SPACE 红队后，焦点从「哪个模型更会做 CTF」转到提示是否把 agent 带到真实信任边界。DNS 欺骗绕过出网策略被点名为比部分内核逃逸更现实的发现。对云上 Computer-use / 代码 Agent：凭据必须放在 VM 外，出网默认拒绝。 | 👍 249 | 🔄 31 | 👀 未披露
  - 🔗 代表性推文: https://x.com/perplexity_ai/status/2120582674549203004 | 📅 2026-11-11

- 轮换密钥挡不住 CI 植入的云后门
  - 💬 讨论核心: wfx 讨论的反复点是：AWS 信任策略被改成任意主体、新建长期访问密钥、Azure 以仓库 OIDC 添加联邦凭据。只轮换 Actions secret 会留下第二条入口。检测要看 CloudTrail 中的 CreateAccessKey、UpdateAssumeRolePolicy 和异常联邦凭据名。 | 👍 196 | 🔄 36 | 👀 未披露
  - 🔗 代表性推文: https://x.com/IntCyberDigest/status/2120951007878238368 | 📅 2026-11-12

- 智能体渗透框架（ARTEX / AntiFox）被用于真实云入侵
  - 💬 讨论核心: 规划–执行多智能体把已知手法（Web shell、凭证校验、Secrets Manager/S3 枚举）做成可并行、低人工的流水线。速度与覆盖面上升，但初始访问仍常来自被盗应用凭证或公网应用，而非云控制面 0day。防御重心是短生命周期身份、IMDSv2、最小权限，以及密钥暴露即吊销。 | 👍 149 | 🔄 54 | 👀 未披露
  - 🔗 代表性推文: https://x.com/TheHackersNews/status/2120540829488197766 | 📅 2026-11-11

- Prompt Injection 基准饱和 ≠ 问题消失
  - 💬 讨论核心: 有讨论称人类攻击对部分 Gemini/Claude 迁移成功率已低于 1%，但 DeepMind 的 agent swarm 仍能自适应打穿。共识转向：防御要按工具输出、记忆写入和多步 agent 来测，而不是只看单轮 jailbreak 榜。 | 👍 46 | 🔄 8 | 👀 未披露
  - 🔗 代表性推文: https://x.com/alexbieyx/status/2121295605284905143 | 📅 2026-11-13

- 2026 年 CVE 突破 10 万，主要归因是 AI 辅助挖洞
  - 💬 讨论核心: VulnCheck 在 11 月 13 日计数约 100,222，超过 2025 年全年一倍以上。Microsoft 11 月单月约 1,094（10 月约 1,474）。观点是行业从「漏洞不够」变成「披露数据消化不了」。实操建议是优先处理在野和可达漏洞，而不是追全量 CVE。 | 👍 1 | 🔄 0 | 👀 未披露
  - 🔗 代表性推文: https://x.com/VulnCheckAI/status/2121362842364645683 | 📅 2026-11-13

**🆕 新上线 / 更新中的 Bug Bounty 或 VDP 项目**
本期无高互动/突破性情报

**📢 平台动态 & 政策变化**
- CISA 在窗口前后把多枚在野漏洞列入 KEV，包括 Check Point 网关链、Outlook 欺骗 CVE-2026-124194（经 Office 更新修复，泄露 NTLM）、Chrome CVE-2026-125350 等。11 月 10 日补丁日本身在窗口边缘，窗口内仍是补丁优先级话题。 | CISA / Microsoft | 👍 1 | 🔄 1 | 👀 未披露
  - 🔗 来源: https://x.com/socradar/status/2120467196304646450 | 📅 2026-11-11

- 微软称 11 月 12–13 日全球 Microsoft 365 中断来自既有网络扩容遗留问题叠加近期网络变更，并非网络攻击或 AI Agent；Outlook、Teams、Copilot 等受影响，Downdetector 侧报告量为近 12 个月最大。保险估算损失量级数亿美元，但多数网络险不覆盖非恶意中断。 | Microsoft | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.geekwire.com/2026/a-huge-pain-in-the-ass-microsoft-365-starts-to-recover-after-a-daylong-global-email-blackout/ | 📅 2026-11-13

**🏆 猎人里程碑 / 大额奖励**
- @Parth0x108 称在 CertiK Hunt 打到一枚在野 Critical
  - 🌟 中文概述: 11 月 13 日公布，未披露金额与漏洞细节；CertiK 官号转发祝贺。互动高于多数赏金炫耀帖，但信息量不足以判断云或合约层影响。 | 👍 73 | 🔄 0 | 👀 未披露
  - 🔗 链接: https://x.com/Parth0x108/status/2121301540000000000 | 📅 2026-11-13

**☕ 其他有趣八卦 / 吐槽 / 预警**
- Check Point 网关遭 PHP2Shell（CVE-2026-109618/109619）加 Gaia 本地提权 CVE-2026-123039 串联，获取 root 后部署后门，部分事件横向到 ESXi 并投放 wiper；厂商称大约数十客户受影响，活动可追溯到 10 月底，CISA 于 11 月 13 日列入 KEV。防火墙本身成为跳板。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.csoonline.com/article/4248693/the-firewall-becomes-the-foothold-attackers-turn-check-point-gateways-against-customers.html | 📅 2026-11-13

- ScreenConnect 第三方插件/被控面板被用来向至少 288 台主机、约 48 个组织投递；同期 N-able N-central 在 PoC 公开后出现在野利用（厂商紧急修补）。远程管理软件仍是本周边缘入口。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://cvetodo.com/threat-report/2026-11-13 | 📅 2026-11-14

- 马士基确认收购遗留系统遭入侵，WhiteArmor 索要约 500 万美元比特币、声称约 100GB 数据；公司称现有证据未显示其他系统或客户 API/EDI 受影响。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://cybersecurityjournal.ca/news/85292-cybersecurity-daily-brief-2026-11-11/ | 📅 2026-11-11

- FBI 称过去约 18 个月，朝鲜相关行动者以深度伪造视频会议（FaceStealer）盗取超过 4 亿美元加密资产。社会工程仍比多数 0day 的现金产量更高。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://infosecindustry.com/news/the-hacker-news/ | 📅 2026-11-13

- [历史参考] Qubole 跨账号信任被滥用：多家客户遗留的、信任 Qubole AWS 账号的 IAM role，在 10-14 至 10-26 被用来读密钥和 S3；11-11 仍有复核。Sentra 称十余至数十家。AWS 表示自身服务未被攻破、行为符合设计。不计入本期热度。窗口内动作应是清点并删除不再使用的第三方信任角色。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.rescana.com/post/qubole-aws-cross-account-trust-abuse-prepare-now | 📅 2026-11-11
