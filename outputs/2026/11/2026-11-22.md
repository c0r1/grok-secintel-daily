**【CyberSec 情报速报 | 云安全 & AI 重点强化】**

> 生成时间: 2026-11-22 15:57:00 UTC+08:00

**统计范围**: 2026-11-19 - 2026-11-22（包含起止日，共约 3-4 天数据）
**本期热度峰值**: 最高 👍 424 | 最高 👀 未披露
**今日情报眼**: nginx疑在野，补丁须重启

---

**📋 生成说明**
本报告由多份公开源汇总稿合并去重而成，技术细节未经人工复核，仅供参考。互动数只保留原稿明确给出的数值，缺失标「未披露」，不推算。2026-11-18 及更早仅标注为历史参考，不计入本期热度峰值。以下为影响与修复要点，不含利用步骤或 PoC。

---

**💰 本期最高赏金 / 最炸裂 payout**
本期无高互动/突破性情报
窗口内未见可追溯的猎人到账帖。赏金表上调与新项目见文末对应板块，不计入 payout。

**☁️ 云安全重点(特别加强板块)**
- nginx2root：HTTP/2 内存安全问题可致未认证代码执行，西澳 SOC 称已见在野
  - 🌟 亮点总结: [历史参考] F5 于 11-18 修补五条可独立触发的 nginx 内存破坏问题（含 CVE-2026-123007、CVE-2026-123633，CVSS 4.0 9.2）。本期要点：HTTP/2 开启即可打到只提供静态文件的实例；worker 权限代码执行不等于直接 root。修复版为开源 1.30.7 / 1.31.9 与对应 NGINX Plus，必须重启进程，reload 不够。Cloudflare 称其边缘已修，且对走其 HTTP 代理的源站，客户端 HTTP/2/3 帧不会直达 nginx；源站若可直连则仍暴露。WASOC 通报 20261119001（11-19）称已获知其中至少一条在野利用，但未点名具体 CVE，也未称西澳政务网已中招。GCP-2026-087/089 将相关问题标为 Critical/High，并给出含修复的 GKE 补丁版本；影响面是边缘与入口，不是新的云控制面接管。 | 👍 424 | 🔄 67 | 👀 未披露
  - 🔗 来源: https://x.com/Cloudflare/status/2123659503123980374 | 📅 2026-11-20
  - 补充: https://blog.cloudflare.com/nginx2root/ ；在野更新 https://x.com/DailyDarkWeb/status/2123668428661678116 （👍 30 | 🔄 5 | 👀 未披露）；GCP 跟进 https://echelongraph.io/pulse/health/gcp
  - [历史参考] Wiz 首发帖为 11-18，👍 717，不计入本期峰值: https://x.com/wiz_io/status/2123072696544002464

- VMware vCenter CVE-2026-123890：未认证拿到管理员会话，零日已利用约两个月
  - 🌟 亮点总结: Broadcom 于 11-19 发布 VMSA-2026-0009。VMware Directory Service 认证绕过，CVSS 9.8，无官方绕过，并按紧急变更处理。网络可达即可获得管理员会话，进而控制其下虚拟化资产。Mandiant/GTIG 称疑似中国关联组织 Armory Castle（原 UNC5221）至少自 2026 年 9 月初利用（利用起点为历史背景）。修复版本：9.1.1.0200、9.0.2.0200、8.0 U3m；VCF 5.x 需异步补丁并配合 SDDC Manager 5.2.5；VCF/vSphere Foundation 9.x 有对应构建。vCenter 7.0 无公开补丁，需联系支持。CISA 于 11-20 列入 KEV，联邦修复期限 11-23。补丁不能替代入侵排查。 | 👍 0 | 🔄 0 | 👀 未披露
  - 🔗 来源: https://x.com/Sujeet/status/2123943324126216283 | 📅 2026-11-21
  - 厂商与研究: https://www.securityweek.com/newly-patched-vmware-vcenter-flaw-exploited-as-zero-day-by-chinese-apt/ ；https://censys.com/advisory/cve-2026-123890/

- Microsoft `agent-framework` PyPI 1.26.1 / 1.26.2 投毒
  - 🌟 亮点总结: 11-19 公开报道称，官方包的这两个版本会在安装环境中收集 Azure、AWS、GitHub 与 CI 相关凭据；Wiz 将发布权限关联到微软发布流水线证书。PyPI 已隔离这两个版本，最后干净版本为 1.26.0。若安装过这两个版本，应视为主机与云身份已暴露：重装环境，轮换云密钥、CI/OIDC 凭据和相关 token，并查发布日志。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.helpnetsecurity.com/2026/11/19/microsoft-agent-framework-package-pypi-compromised/ | 📅 2026-11-19
  - 补充: https://siliconangle.com/2026/11/19/wiz-ties-microsoft-agent-framework-package-compromise-to-release-pipeline-certificate/

- Rackspace Spot：泄露凭据可读客户 Kubernetes Secret
  - 🌟 亮点总结: 公开通报称 11-17 约 00:20–22:00 UTC（侵入时段早于本统计窗），未授权方用泄露凭据进入托管 Kubernetes 平台 Spot，可在部分客户组织中创建 Pod、读取集群 Secret，并接触 Spot API / refresh token。11-18 经客户报告发现，11-21 宣布服务恢复。根因被描述为观测系统凭据被盗，凭据来源未说明。受影响客户应重签 API token、更换自动化 refresh token、更新 kubeconfig，并轮换 Secret 中的云与数据库凭据，回看 11-17 以来审计日志。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.bleepingcomputer.com/news/security/rackspace-spot-breach-let-hackers-access-customer-kubernetes-secrets/ | 📅 2026-11-21

- phpAfterShell CVE-2026-126714 打进 GCP PHP 运行时
  - 🌟 亮点总结: PHP 默认文件型 session 非原子覆写，写入中断后新旧序列化数据可能拼接；在应用存在可用反序列化链时可能导致 RCE。CVSS 4.0 为 9.2。Depthfirst 用 AI 研究平台发现。GCP-2026-090（11-20）点名 App Engine Standard/Flexible、Cloud Run、Cloud Functions 等，需升级运行时或重建镜像后重新部署。官方版本线：8.2.36 / 8.3.37 / 8.4.28 / 8.5.13。缓解方向是升级，并在 Web 运行配置中关闭 session.upload_progress、限制写入 session 的不可信数据。同一次 PHP 发布还包含其他问题，应按运行时而不是只按发行版公告排查。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.wiz.io/blog | 📅 2026-11-19

- Linux KVM CVE-2026-99312：AMD 宿主上客户机可读约 127GB 宿主内存
  - 🌟 亮点总结: Terra Security 经云厂商漏洞赏金报告。仅影响开启嵌套虚拟化的 AMD 宿主；共享宿主机上其他租户内存可能落入可读范围。上游内核已修，DigitalOcean 称已对自身集群热补丁、客户无需操作；自建 KVM 需升级宿主内核或关闭嵌套虚拟化。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://thehackernews.com/search/label/Cloud%20security | 📅 2026-11-20

- GCP 跨租户文件读写 CVE-2026-126054（Dataform / BigQuery Studio / Colab Enterprise）
  - 🌟 亮点总结: 公告 GCP-2026-084 于 11-19 发布，NVD 11-20 入库。已认证攻击者可借助工作区路径与 Git 集成，跨租户读私有文件并写入任意文件。CVSS 4.0 9.3。[历史参考] Google 称 2026-10-10 已修补，客户无需操作。这是云上数据与笔记本平面的租户隔离失败，不是新的未修补 0day。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://docs.cloud.google.com/bigquery/docs/security-bulletins | 📅 2026-11-19
  - 补充: https://nvd.nist.gov/vuln/detail/CVE-2026-126054

- N-able Mail Assure / SpamExperts 托管云服务器遭未授权访问
  - 🌟 亮点总结: 中断始于 11-16（窗口前），11-19 披露。厂商称未知攻击者进入托管云中的一台服务器，并导致管理接口与 API 被禁用。美洲、亚太、欧洲的 Mail Assure 与 SpamExperts 受影响。截至披露，厂商称尚无客户数据或租户邮箱被访问的证据，调查仍在进行。属于云邮件安全控制面可用性事件，不是已证实的邮箱数据泄露。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://thehackernews.com/search/label/Cloud%20security | 📅 2026-11-19

**📚 最值得读的 Writeup / 公开报告**
- Cloudflare：nginx2root 五缺陷与代理边界
  - 📝 技术摘要: 把五条独立内存破坏问题按配置前提拆开：仅开 HTTP/2、HTTP/2 反代、HTTP/3 反代、resolver 变量反代、邮件代理。说明边缘代理解析 HTTP/2/3 能挡住对应帧到达源站，以及直连、非代理主机名、邮件与部分解析器路径仍然暴露。适合做暴露面分级，而不是当成通用 WAF 规则可替代补丁。博客页本身互动未披露；关联推文为下方热度。 | 👍 424 | 🔄 67 | 👀 未披露
  - 🔗 链接: https://blog.cloudflare.com/nginx2root/ | 📅 2026-11-20
  - 关联推文: https://x.com/Cloudflare/status/2123659503123980374

- Censys：实验室复现边界与暴露面看板
  - 📝 技术摘要: 窗口内帖称已在自有实验环境验证上述 nginx 代码执行问题，并公开受影响实例追踪看板。价值在于区分「版本字符串落在影响区间」和「真实可利用配置」，避免把版本统计直接当成失陷数。 | 👍 3 | 🔄 3 | 👀 未披露
  - 🔗 链接: https://x.com/censysio/status/2123221739362529382 | 📅 2026-11-19

- Amazon：Cairn Agent 自主发现并利用 MONAI Label 0day（CVE-2026-133968）
  - 📝 技术摘要: 2026-11-20 Amazon Threat Intelligence 公开。中等置信度中国关联行动方把开源渗透框架 Cairn 暴露在公网且无认证，行动记录因此可见。Agent 被赋予拿到 shell 一类目标，并在修复发布前利用 MONAI Label（≤0.8.5，CVSS 9.8，默认无认证）造成任意文件写入并取得 root。截至约 11-22，修复主要在源码（PR 1915），PyPI 仍见 0.8.5；另有周报称已有修复代码但窗口内尚无已发布修复版本，并称自 9 月起被利用。维护方提示该服务不应暴露到公网。影响使用该组件做 AI 标注的研究环境。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/ | 📅 2026-11-20
  - 补充: https://theinjection.dev/items/amazon-cairn-monai-label-zero-day/ ；https://whatgotpwned.com/weekly/2026-W47

- Dragos 金丝雀 + OpenRouter 下游推理商处理事件
  - 📝 技术摘要: Dragos 报告日为 11-19：约 2026-07 至 11 月投放约 200 万条带唯一链接与假凭证的 prompt，结论是至少三家托管商发生数据被盗，转售方会读客户 prompt，Zero Data Retention 往往管不住后续跳。OpenRouter 11-22 称自身无未授权访问，但已下架三家提供商、取消 125 个端点的 ZDR 资格并通知可能受影响的客户。公开点名包括 Novita、Phala、Together 的相关公告。测试 URL 有在推理后约 40–130 小时被访问的情况。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/ | 📅 2026-11-22

- PromptArmor FrontierBreach 企业 Agent 提示注入评测
  - 📝 技术摘要: 报道日 11-19，基准发布为 11-18 [历史参考，原帖 👍 1,688、浏览约 1.21M，不计入本期峰值]。报道称原始 21 个模型隐藏指令平均成功率 34.9%；第三方 skills 约 45.5%，高于连接器、文档系统和本地文件。Gemini 4 Argon 约 4.3%，Grok 4.5 约 91.4%。计分方式是同案例多次尝试中有一次成功即计入，不能当成自然流量被劫持的概率。企业侧应限制 Agent 工具权限与技能来源，而不是只看模型榜单。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://i10x.ai/news/frontierbreach-promptarmor-prompt-injection-benchmark-enterprise-agents | 📅 2026-11-19

**🔥 社区热议的技术话题或新手法**
- nginx 补丁窗口与「代理是否等于已防护」
  - 💬 讨论核心: 社区把焦点从「有没有 PoC」转到暴露条件：HTTP/2 是否对公网开放、源站能否绕过 CDN 直连、worker 是否以 root 运行。西澳 SOC 的在野通报把优先级从「等待确认」推到「先升级再验证」。禁用 HTTP/2 盖不住邮件代理、HTTP/3 和 resolver 路径。 | 👍 424 | 🔄 67 | 👀 未披露
  - 🔗 代表性推文: https://x.com/Cloudflare/status/2123659503123980374 | 📅 2026-11-20

- 侦察输出解读，而不是再堆扫描器
  - 💬 讨论核心: 窗口内一条实操向讨论把 401/403、CNAME 接管面、url/user_id 参数分开看，强调验证到可复现证据再停。原稿称互动未达非名单源强制收录线，仅作方法话题保留。 | 👍 156 | 🔄 22 | 👀 未披露
  - 🔗 代表性推文: https://x.com/NullSecurityX/status/2123698164154994734 | 📅 2026-11-20

- 控制面零日：补丁日不是入侵起点
  - 💬 讨论核心: vCenter 案例被用来强调目录服务认证绕过会直接变成 SSO 管理员。公开讨论集中在 7.0 无公开补丁、Quick Patch 不能交付此次更新，以及补完后仍需查管理员账号与目录库是否被拷走。 | 👍 0 | 🔄 0 | 👀 未披露
  - 🔗 代表性推文: https://x.com/Sujeet/status/2123943324126216283 | 📅 2026-11-21

- Agentic offense 已越过「人在环里点下一步」
  - 💬 讨论核心: 11-20 的 Cairn/MONAI 案例把「Agent 自己找 0day 并打到 root」从预期变成已观测事件。微软 11-19 另称 Storm-0940 用 AI 框架打过大量组织，部分在三小时内拿到云上特权。防御讨论集中在最小权限、短时凭证和可见性，而不是再找一个模型层银弹。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性来源: https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/ | 📅 2026-11-20
  - 补充: https://blogs.microsoft.com/on-the-issues/2026/11/19/security-fundamentals-to-enable-the-frontier/

- 推理供应链：ZDR 只约束第一跳
  - 💬 讨论核心: 路由商的隐私标签不能证明下游托管商、转售商或被入侵的推理节点没有留下 prompt 与凭证。实用动作是轮换出现在 prompt、工具参数和 trace 里的密钥，并重新审查哪些端点还标着 ZDR。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性来源: https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/ | 📅 2026-11-22

**🆕 新上线 / 更新中的 Bug Bounty 或 VDP 项目**
- Ticko 新增 Critical 档，上限 $200,000
  - 📝 更新点: bugbounty.fyi 记录 11-19 23:22 自托管项目新增档位：Critical 至 $200,000，High 至 $25,000，Medium 至 $3,000。未见官方范围说明的二次核验，也不是已支付案件。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?show=rewards&dir=up&since=7 | 📅 2026-11-19

- DFX.swiss Critical 上限由 CHF 10,000 调至 CHF 50,000
  - 📝 更新点: 11-20 14:11，平台为 Compass Security。窗口内涨幅最大的已核实赏金调整之一。无对应漏洞细节。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?show=rewards&dir=up&since=7 | 📅 2026-11-20

- Bucket Protocol 补齐档位，High 至 $50,000
  - 📝 更新点: 11-19 01:32 自托管项目新增 Low $50、Medium $2,000、High $50,000。同批还有 Minati 顶格展示为 $50,000，需以项目页为准。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?show=rewards&dir=up&since=7 | 📅 2026-11-19

- Immunefi：Audit Comp | Base Everest 新公开项目
  - 📝 更新点: 11-19 上线记录。Web3 审计竞赛入口，具体范围与赏金以项目页为准，本窗口未见猎人到账帖。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?dir=new&since=7 | 📅 2026-11-19

- Inspectiv 同日批量 VDP
  - 📝 更新点: 11-19 记为新公开 VDP，名单合并为 Shipt、Razer、Root、ShipHero、Sisense、LemFi、Upside、Zayo、Inunity、Backlight。偏披露而非高额赏金，页面未给出各项目赏金上限。适合当作资产监控，不宜当成 payout 信号。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?dir=new&since=7 | 📅 2026-11-19

**📢 平台动态 & 政策变化**
- CISA 将 CVE-2026-123890 列入 KEV（11-20），联邦修复期限压到 11-23。私有云控制面补丁被抬到与边界设备同级。 | CISA / Broadcom | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://blog.ostorlab.co/vmware-vcenter-auth-bypass-cve-2026-123890.html | 📅 2026-11-20

- Cisco Expressway CVE-2026-76466 列入 CISA KEV。漏洞公告为 2026-10-21 [历史参考]。本期新事实是 11-20 列入 KEV，联邦缓解期限 11-23。影响集群部署中的 Expressway-C/E，未授权远程访问可导致设备 root。无临时绕过。X14 及更早需迁移，X15.5.3 及更早的首个修复版本为 X15.5.20。 | CISA / Cisco | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://nvd.nist.gov/vuln/detail/CVE-2026-76466 | 📅 2026-11-20
  - [历史参考] 厂商公告: https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-vcs-static-cred-hr7EWZ8t.html | 📅 2026-10-21

- 欧委会 DIGIT 在 HackerOne 给多个开源组件补档：11-20 21:46，PuTTY、FileZilla、Apache Kafka 的 Critical 档至 €7,500，VLC Critical 至 €5,000。属于政府托管开源赏金补档，金额仍远低于商业 Critical。 | HackerOne | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?show=rewards&dir=up&since=7 | 📅 2026-11-20

- 美国 OPM VDP（Bugcrowd）扩大范围：11-22 增加 applicationmanager.gov 等至少 19–20 个资产。政府 VDP，默认无赏金预期，攻击面清单变长不代表赏金提高。 | Bugcrowd | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes | 📅 2026-11-22

- Automattic（HackerOne）提高最低赏金：11-20 00:51，Critical 最低 $500→$1,000，High $300→$600，Medium $200→$300。变的是保底，不是顶格。 | HackerOne | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?show=rewards&dir=up&since=7 | 📅 2026-11-20

**🏆 猎人里程碑 / 大额奖励**
本期无高互动/突破性情报

**☕ 其他有趣八卦 / 吐槽 / 预警**
- Chainflip 金库被转走 122.86 BTC、520.22 ETH、约 325 万 USDC 与 75.8 万 USDT。公开分析认为是聚合签名密钥暴露，而不是合约逻辑漏洞；以太坊侧资金很快进入 Tornado Cash。项目方给出 11-23 18:38 UTC 前退回 90%、自留 10% 的追回要约，并称已能关联 11-11 的资金准备与 11-20 注册的验证者。FLIP 盘中大跌。这不是白帽赏金披露。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.theblock.co/news/defi/2026-11-21-chainflips-flip-drops-34-after-attacker-drains-4-86-million-from-vault-with-suspected-key-compromise-444804 | 📅 2026-11-21
  - 补充: https://chainflip.io/return

- 攻击方自己的 Cairn 控制台没做认证，Amazon 是读操作员留下的 prompt 与 Agent 日志还原战役的。进攻自动化的审计缺口先打在使用者自己身上。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.theregister.com/security/2026/11/20/china-attackers-deployed-ai-agents-that-autonomously-found-and-exploited-a-0-day-to-take-over-a-university-server/5311382 | 📅 2026-11-20

- 欧盟委员会 11-19 确认，其内部系统在 10-22 发现遭受一场「AI 生成」的网络活动，部分应用被下线；未点名工具或攻击步骤。发现日早于本统计窗，确认披露落在窗口内。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://theinjection.dev/items/european-commission-ai-cyber-campaign/ | 📅 2026-11-19

- Signal 称已在检测到操作系统级 AI 代理读屏时打开截图阻断，覆盖其声明的 iOS 27、Android 与 Windows 11；并称 macOS 27 无法阻断。这是产品防护，不是漏洞利用。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://theinjection.dev/items/signal-os-ai-agent-screen-capture/ | 📅 2026-11-20

- [历史参考] Fireworks AI 的客户通知在窗口内仍在发酵，但入侵窗口是 2026-08-03 至 10-07 与 10-23 至 10-30，不是本周新入侵，不计入本期热度峰值。Uber 向俄勒冈报备通知约 149,346 人；Cursor 称其发给 Fireworks 的密钥泄露后，只读 trace 桶里的未脱敏凭证被用来碰 SaaS，并曾在扩展市场缓存中出现篡改版 Claude Code 扩展。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.neoteo.com/en/fireworks-ai-breach-two-incidents-and-the-cursor-link | 📅 2026-11-20
