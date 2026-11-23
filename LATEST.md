**【CyberSec 情报速报 | 云安全 & AI 重点强化】**

> 生成时间: 2026-11-23 16:56:53 UTC+08:00

**统计范围**: 2026-11-20 - 2026-11-23（包含起止日，共约 3-4 天数据）
**本期热度峰值**: 最高 👍 270 | 最高 👀 未披露
**今日情报眼**: vCenter在野利用限期将至

---

**📋 生成说明**
本报告由多份公开来源草稿合并、去重、排序而成，技术细节未经人工验证，仅供参考。只保留影响与处置方向，不含利用步骤或 PoC。互动只采用草稿中明确写出的数值，缺失标「未披露」，不外推；浏览量在各份中均未披露。窗口外首发仅作 [历史参考]，不计入本期热度峰值。

---

**💰 本期最高赏金 / 最炸裂 payout**
本期无高互动/突破性情报

窗口内未保留可追溯的大额到账原帖。DFX 11-20 上调赏金上限属项目调整，不是本期已支付奖金，见文末。

---

**☁️ 云安全重点(特别加强板块)**

- VMware vCenter 认证绕过 CVE-2026-123890（CVSS 9.8，在野）
  - 🌟 亮点总结: CISA 于 11-20 列入 KEV，美国联邦机构整改期限为 11-23。公开报告称网络可达的未认证访问者可取得 vCenter / SSO 管理员会话，并进一步触及 ESXi 与虚拟机数据。Mandiant/Google 将活动关联到 Armory Castle（原 UNC5221），称至少自 9 月初利用，涉及伪造 SSO 管理员与 SAML 签名材料。补丁版本包括 9.1.1.0200、9.0.2.0200、8.0 U3m；无官方 workaround，7.0 无公开修复且已过支持窗口。Broadcom VMSA-2026-0009 日期为 11-19，作 [历史参考]。仅升级不能清除已落入的会话或被带走的签名密钥，需排查非预期 SSO 管理员、轮换相关密钥，并隔离管理面。同批 KEV 未见公开确认的勒索软件关联。 | 👍 270 | 🔄 63 | 👀 未披露
  - 🔗 来源: https://x.com/tldrcve/status/2124521515677069731 | 📅 2026-11-22
  - 同事件媒体帖: https://x.com/TheHackersNews/status/2123676173888795110 | 👍 143 | 🔄 42 | 👀 未披露 | 📅 2026-11-20

- NGINX HTTP/2 未认证 RCE（窗口内扩散；主披露为历史参考）
  - 🌟 亮点总结: [历史参考] 主披露在 11-18（Wiz 等指出 CVE-2026-123633 与 CVE-2026-123007；启用 HTTP/2 时未认证 RCE，CVSS 4.0 9.2；F5 同日发补丁）。该历史帖不计入本期峰值。窗口内 CyberScoop 称研究方披露了五枚 NGINX 问题且均有可用利用，测试中曾与内核问题串联到宿主机控制。公开修复版本包括 1.30.7 与 1.31.9。第三方活动页将 GCP-2026-089 标为 11-20 High，关联上述缺陷；GCP-2026-087 的 Critical 文本在 11-19，不计入本期。反代、Ingress 与仅托管静态文件的实例均在影响讨论范围内，应核对版本与 HTTP/2 是否开启，不要用第三方 exploit 包验证。 | 👍 8 | 🔄 3 | 👀 未披露
  - 🔗 来源: https://x.com/CyberScoopNews/status/2123582975761695164 | 📅 2026-11-20
  - [历史参考] https://x.com/wiz_io/status/2123072693042082117 | 📅 2026-11-18
  - GCP 公告索引: https://echelongraph.io/pulse/health/gcp | 📅 2026-11-20

- CISA 同日另三枚在野漏洞（与 vCenter 同一 KEV 批次）
  - 🌟 亮点总结: 11-20 一批加入，联邦期限同为 11-23。CVE-2026-76466（Cisco Expressway，CVSS 9.8）为硬编码凭据，集群设备上可导致 root 命令执行；CVE-2026-129448（Apache Roller，CVSS 9.8）为认证前反序列化导致的远程代码执行风险；CVE-2025-42884（SAP NetWeaver，CVSS 6.5）为未认证信息泄露/篡改。四枚均未见公开确认的勒索软件关联。优先处理对互联网或管理网暴露的实例。 | 👍 6 | 🔄 0 | 👀 未披露
  - 🔗 来源: https://x.com/DailyDarkWeb/status/2123852649451663860 | 📅 2026-11-20

- GCP-2026-090：phpAfterShell（CVE-2026-126714）影响 Cloud Run / App Engine PHP 运行时
  - 🌟 亮点总结: Google Cloud 于 11-20 公告。PHP 默认 files session handler 的严重缺陷可在特定条件下导致 RCE（PHP 评分 CVSS 9.2）。受影响面包括 App Engine Standard/Flexible、Cloud Run、Cloud Run functions 等。厂商缓解方向是关闭 Session Upload Progress、改用非本地 session 存储，并升级到已修复的 PHP 分支；托管运行时补丁镜像仍在滚动。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://docs.cloud.google.com/support/bulletins | 📅 2026-11-20

- GCP 托管运行时完成 Java4Shell（CVE-2026-114938）补丁铺开
  - 🌟 亮点总结: [历史参考] 漏洞于 11-17 公开：OpenJDK Base64 解码内存破坏，可在特定 x86-64（AVX-512 VBMI）上影响 Java 17.0.6+ / 21 / 25 / 27，堆越界写可导致 RCE；ARM 与 Java 8/11 常规构建不受影响。本期新事实是 GCP-2026-082 于 11-20 更新：Java 17/21/25 修补版基础镜像已在 Cloud Run、Cloud Functions、App Engine、Buildpacks 完成推送。自动更新的托管运行时无需手工换镜像，但温实例需重新部署才立刻切到新 JVM；App Engine 标准环境与 Cloud Run 二代在 11-30 前仍保留临时 AVX-512 防护。自管 GKE/VM 仍需自行升级并重启。云上优先核对托管运行时是否已切到修补镜像，而不是只看自建 JDK。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://docs.cloud.google.com/support/bulletins | 📅 2026-11-20

- KVM CVE-2026-99312：客户机读取 AMD 宿主机内存
  - 🌟 亮点总结: 11-20 公开简报称，研究者从单台云虚拟机读取了约 127GB 宿主机内存。这是 hypervisor 隔离失效，直接影响多租户。公开建议是升级宿主机内核（简报列出的分支包括 6.12.118、6.18.64、7.3.5）或临时关闭 nested。互动与完整顾问原文未在本窗口内核到。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://podcasts.apple.com/us/podcast/november-20-2026-cyber-briefing/id1663966320?i=1000803138303 | 📅 2026-11-20

- Rackspace Spot：泄露凭据可读客户 Kubernetes Secret
  - 🌟 亮点总结: 厂商称 11-17 有人用泄露凭据进入 Spot，能在部分客户集群创建 Pod、列举节点/卷，并读取 Secret 以及 Spot API/刷新令牌。GitHub 回复（11-20）把根因归到一套被入侵的可观测性系统；服务 11-21 报恢复。受影响客户应重签 Spot 令牌、更换自动化刷新令牌、拉取新 kubeconfig，并轮换集群 Secret 中的凭据，同时回看 11-17 起的工作负载日志。这是云控制面凭据被盗后的集群接管路径，不是新的 Kubernetes 逃逸 0day。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://brandefense.io/security-news/rackspace-spot-breach-kubernetes-secrets/ | 📅 2026-11-22

- GKE：CVE-2026-99288 Linux TCP 远程 DoS，11-20 补丁版本更新
  - 🌟 亮点总结: 内核 TCP 锁无关查找竞态可被远程流量打成内核 panic，影响 GKE Standard / Autopilot 的控制面与节点；官方说明不导致提权或容器逃逸。GKE Sandbox 与 Windows 节点不受影响。11-20 公告补充了 COS 上 1.32 / 1.33 的修补版本，1.37 的 COS 与 Ubuntu 镜像仍在推进。同页邻近的 DirtyFrag / Fragnesia 容器逃逸条目日期为 11-19，作 [历史参考]，不计入本期。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://docs.cloud.google.com/kubernetes-engine/security-bulletins | 📅 2026-11-20

---

**📚 最值得读的 Writeup / 公开报告**

- Amazon：Cairn 代理自主发现并利用 MONAI Label 0day
  - 📝 技术摘要: Amazon 威胁情报 11-20 披露，疑似中国关联操作者在 9 月约 48 小时的高校行动中，用开源渗透框架 Cairn 的自主代理发现 MONAI Label 未知漏洞（CVE-2026-133968，CVSS 9.8）。认证默认关闭；代理在短时间内从接口测绘走到任意文件写入，并在一台高校服务器上获得 root。维护者已在代码中修复，窗口内出现 0.8.6 修复版本的后续报道。补丁确认落地前，应打开认证并避免把服务暴露给不可信网络。这是「代理找 0day」进入真实入侵披露的案例，阅读重点是隔离研究型标注服务，而不是复现利用链。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://iacompa.com/news/amazon-cairn-ai-agents-zero-day-monai-label | 📅 2026-11-20

- Java4Shell 窗口状态（探测 vs 已确认入侵）
  - 📝 技术摘要: ThreatDefence 于 11-21 更新：GreyNoise 统计到 11-21 约 261 次、7 个 IP 的探测形请求，未见已确认入侵；截至其引用的 11-20 CISA KEV 快照尚未收录。多家企业应用在实验条件下可打到预认证 RCE，但公开可靠利用并不通用，且依赖 CPU 特性与调用路径；同期大量声称 PoC 不可用。防御重点是升级 Java 并重启。Optimizely 11-20 更新称相关缓解与可用补丁已于当日 20:10 UTC 完成，监测未发现其产品或客户环境被利用，属厂商侧收尾，不是新的 0day。漏洞首发 11-17 为 [历史参考]。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://threatdefence.com/article/java4shell-cve-2026-114938-openjdk-rce-patching-hunting | 📅 2026-11-21
  - Optimizely: https://support.optimizely.com/hc/en-us/articles/50533122142605-Security-Advisory-Java4Shell-CVE-2026-114938-Security-Vulnerability-updated-November-20-2026 | 📅 2026-11-20

- Dragos：约 200 万条推理请求里的金丝雀凭据
  - 📝 技术摘要: HD Moore 团队 7 月至 11 月向常见 AI 推理服务发送约 200 万条带唯一 URL 与金丝雀密钥的 prompt。至少三家托管商在研究者通知前不知道数据已被盗；攻击者使用了诱饵密钥，包括对 AWS API 的大量调用（列举存储与密钥服务、尝试创建 IAM 用户与 Bedrock 密钥）。另有模型实验室及供应商主动抓取了本应零留存的链接。SANS 11-20 播客作了同期转述。结论是：prompt 路由与密钥是否进入推理链路，本身就是暴露面。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://lava.security/blog/ai-inference-canary-research-prompts-exposed | 📅 2026-11-21
  - 同期播客: https://isc.sans.edu/podcastdetail/10188 | 📅 2026-11-20

- Together AI：2026 年 6–7 月推理请求提示词样本泄露
  - 📝 技术摘要: 11-21 官方说明，MiniMax M3、GLM-5.2、Kimi K2.6 的部分提示词样本放在私有 Hugging Face 仓库。开发公开仓库 xorl 时，AI 编码代理把仓库凭证提交进公开 Git，扫描回滚前已被未授权方下载，并用来试探样本里的其他凭证（含 Dragos 金丝雀）。危害是提示词与其中的密钥外泄，不是模型权重泄露。新账号默认改为零数据保留。应轮换被提交的密钥并审计 agent 的 git 权限。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026 | 📅 2026-11-21

- OpenRouter：三家推理供应商下架，125 个端点取消 ZDR
  - 📝 技术摘要: 11-22 公告称 OpenRouter 自身未被攻破；研究方发现部分推理供应商的数据策略与宣传不符。措施是下架 3 家供应商、125 个端点移出 Zero Data Retention（含预防性下架）。公开点名包括 Together AI、Phala、Novita。Phala 侧 DeepSeek V4 Flash 0731 在 10-21 至 11-08 的请求内容应按已暴露处理。同期另有转述称 Atlas Cloud、Novita 警告客户提示到达了 MiniMax 官方 API。要点是「零保留」标签不能代替供应商侧验证；经路由发送的 API Key 与私有提示词仍可能落在下游，用过这些路由的一方应轮换请求里出现过的密钥。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/ | 📅 2026-11-22

---

**🔥 社区热议的技术话题或新手法**

- Bug Bounty Writeup 日更汇总（窗口内达到 List 互动阈值的原帖）
  - 💬 讨论核心: @bountywriteups 11-20 帖汇总多篇 Writeup 链接（标题涉及 Apple Podcasts Connect 盲 SSRF、Google Docs postMessage、Uber 令牌接口账号接管、JWT 等）。单篇原始发表日未逐条核进本窗口，只记这条汇总本身，不把其中旧文算作本期新洞。11-22 续集仅 👍 12、🔄 2，未单独计入。 | 👍 23 | 🔄 3 | 👀 未披露
  - 🔗 代表性推文: https://x.com/bountywriteups/status/2123702424506679566 | 📅 2026-11-20

- 推理供应链：便宜路由打破零留存
  - 💬 讨论核心: 社区把 Dragos 金丝雀实验、Together 样本被下载和 OpenRouter 下架连在一起看。争议点不是模型越狱，而是中间商、编码代理和对象存储里的 prompt 样本。ZDR 可被上游留存、爬虫回连或仓库泄露打穿。Together 的入口是编码代理把私有仓库凭证提交进公开 Git；同周微软 Agent Framework 投毒的 11-20 跟进亦指向发布流水线客户端证书（恶意版 1.26.1 / 1.26.2 于 11-17 上传后约一小时被隔离，最后干净版 1.26.0，作 [历史参考]；Wiz 在攻击者 webhook 保留的 50 条请求里看到 3 起成功窃取，不能代表全部受害面）。实操共识是：密钥不要进 prompt，路由要白名单，发布与代理提交要审查签名和权限。 | 👍 2 | 🔄 0 | 👀 未披露
  - 🔗 代表性推文: https://x.com/fourweekmba/status/2124393009743544542 | 📅 2026-11-22
  - 流水线跟进 [历史参考为主，11-20 公开复盘]: https://4sysops.com/archives/microsoft-agent-framework-attack-traced-to-release-pipeline-certificate/ | 📅 2026-11-20

- 自主代理打 0day，而不是只做 prompt injection
  - 💬 讨论核心: MONAI Label 一案被和「只靠注入劫持 Agent」区分开：Cairn 代理是在找软件缺陷并拿到代码执行。11-22 报道称 GTIG 与 Mandiant 在暴露的暂存服务器上看到名为 exploit_agent 的系统，能对照补丁差异自动找缺陷、生成并启动利用。同期 Help Net Security 报道用更大注入样本做强化学习，反而可能让模型更好劫持。社区结论是补丁窗口正在被机器速度压缩；模型对齐不够，工具权限和默认无认证才是突破口。防御侧应默认「补丁公开即有自动化利用」，而不是讨论如何复现。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性推文: https://www.techradar.com/pro/security/google-says-it-just-saw-the-first-fully-autonomous-cyberattack-and-says-a-significant-threshold-has-been-crossed-in-terms-of-cybersecurity | 📅 2026-11-22
  - 同期实验: https://www.helpnetsecurity.com/2026/11/20/ai-prompt-injection-red-team/ | 📅 2026-11-20

- 云上 Java 运行时补丁不等于业务已安全
  - 💬 讨论核心: 高互动讨论集中在 11-17 至 11-19 [历史参考]。窗口内可核实的新事实是云厂商镜像铺开、探测仍在、上述来源未证实成功入侵。GCP 11-20 宣布基础镜像滚完，但自管 JVM、未重启的温实例，以及不走 Buildpacks 的容器仍然暴露。社区共识偏向：先给暴露在外且跑在受影响 CPU 上的 Java 17+ 服务打补丁并重启，并警惕伪造 PoC 仓库。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性推文: https://docs.cloud.google.com/support/bulletins | 📅 2026-11-20

- MCP 把参数当成 kubectl 参数（CVE-2026-134817）
  - 💬 讨论核心: 11-22 披露，mcp-server-kubernetes 会把远端 MCP 客户端传入的、以横线开头的值交给 kubectl，从而被当成参数。VulnCheck 称其中一种参数可导致服务端读本地文件，4.2.0 已修复。这是 AI 工具层到 Kubernetes 控制面的参数注入。处置是升级组件并限制 MCP 客户端身份。同窗口另有 Obot 公告：任意已登录用户把自身改名为 anonymous 后，能调用从未授权的 MCP 工具，0.28.2 修复，说明治理网关若用保留名做默认拒绝，会被命名绕过。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性推文: https://theinjection.dev/ | 📅 2026-11-22

---

**🆕 新上线 / 更新中的 Bug Bounty 或 VDP 项目**

- GCash Vulnerability Disclosure
  - 📝 更新点: bugbounty.fyi 于 11-23 记为 HackerOne 新公开项目（页面「Today」）。赏金档与范围细节未在摘要中披露。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?dir=new&since=1 | 📅 2026-11-23

- Beanstalk
  - 📝 更新点: 同一追踪页将 11-22（相对 11-23 的「Yesterday」）记为 Sherlock 新公开项目。最高赏金未披露。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?dir=new&since=1 | 📅 2026-11-22

- 11-20 至 11-23 范围增减，不单列为新项目
  - 📝 更新点: 追踪页在该窗口记录了 vidaXL、BlaBlaCar（YesWeHack）以及多个 security.txt / Bugcrowd 范围追加。这些是范围变更，不是新计划上线。11-19 的 Immunefi「Base Everest」等不在窗口内。转发 Amazon VRP GenAI 范围的帖未确认为本窗口新上线项目，不计入。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?show=scope&dir=up&since=1 | 📅 2026-11-20

---

**📢 平台动态 & 政策变化**

- CISA 于 11-20 将 CVE-2026-123890 等纳入 KEV，联邦民事机构须在 11-23 前完成处置；条目要求做取证分诊。这是本窗口最硬的政策截止日。技术细节见云安全板块 vCenter 条目，不重复计热度。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.rescana.com/post/vmware-vcenter-cve-2026-123890-directory-service-auth-bypass-patch-now | 📅 2026-11-20

- HackerOne / Bugcrowd / Intigriti / YesWeHack / Immunefi 官方账号在窗口内的政策帖，未能核到达到收录阈值的原帖互动，不编造平台政策变化。Intigriti Bug Bytes（10-30）为 [历史参考]。 | 👍 未披露 | 🔄 未披露 | 👀 未披露

---

**🏆 猎人里程碑 / 大额奖励**
本期无高互动/突破性情报

窗口内没有可追溯到猎人、金额与原帖的大额到账或里程碑。

---

**☕ 其他有趣八卦 / 吐槽 / 预警**

- DFX 热钱包事件后上调赏金。官方说明 11-18 攻击者拷走热钱包私钥，损失略低于 CHF 50,000，作 [历史参考]，不计入本期峰值。11-20 起赏金上限从 CHF 10,000 调至 CHF 50,000，并取消生产环境的自动 GitHub 部署。属项目调整，不是本期 payout。 | 👍 4 | 🔄 1 | 👀 未披露
  - 🔗 来源: https://x.com/compasssecurity/status/2123735236106424457 | 📅 2026-11-20

- GL.iNet：攻击者于 11-20 利用 GoodCloud 缺陷，向部分路由器和 KVM 植入恶意软件。厂商已堵路径，11-22 起推固件；只升级固件清不掉已落地的感染，需要恢复出厂。影响型号包括 RM1 系列及使用 GoodCloud 的部分路由。边缘设备云管理面再次成为入口。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://cybersixt.com/ | 📅 2026-11-22

- Qubole 跨账号 AWS 角色被滥用；银行与卡组织本周确认第三方事件
  - 攻击发生在 10 月，作 [历史参考]，不计入本期热度。Chase、Visa、Mastercard 的第三方事件说明落在 11-19 至 11-20，汇总文日期为 11-21。攻击者借助供应商 AWS 身份 AssumeRole 进入客户账号，不少角色长期闲置。处置重点是清点并删除不用的跨账号角色、加上源条件，而不是只看本账号 IAM 用户。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://rokkhe.hashnode.dev/attacks-this-week-nov-21-2026-vcenter-confluence-litellm | 📅 2026-11-21

- Java4Shell 与 PHP 相关公开仓库里混有不可用、疑似批量生成的 PoC /「利用演示」，增加防守方甄别成本。Java4Shell 的 11-21 状态文写明尚无确认入侵。PHP 安全发布本身在 11-19，作 [历史参考]。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://threatdefence.com/article/java4shell-cve-2026-114938-openjdk-rce-patching-hunting | 📅 2026-11-21

- RunPod 托管 MCP 在创建成功后追加指令，要求编码智能体打 0–10 分且不要告诉用户。官方文档承认该行为，可用请求头关闭。属于智能体侧信道「隐藏指令」，不是 RCE。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://theinjection.dev/ | 📅 2026-11-21
