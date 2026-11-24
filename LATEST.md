**【CyberSec 情报速报 | 云安全 & AI 重点强化】**

> 生成时间: 2026-11-24 18:51:21 UTC+08:00

**统计范围**: 2026-11-21 - 2026-11-24（包含起止日，共约 3-4 天数据）
**本期热度峰值**: 最高 👍 37 | 最高 👀 未披露
**今日情报眼**: 邮件安全关键SSRF列入KEV

说明：只保留统计窗口内公开来源。互动数仅采用原稿明确写出的数值，缺失标「未披露」，不推算。11 月 19 日前的首发研究、补丁与漏洞披露标「历史参考」，不计入本期热度峰值。不展开利用步骤或 PoC。

---

**📋 生成说明**
本报告由多份自动汇总稿去重合并，技术细节未经人工验证，仅供参考。

---

**💰 本期最高赏金 / 最炸裂 payout**
本期无高互动/突破性情报

**☁️ 云安全重点(特别加强板块)**
- N-able Mail Assure / SpamExperts：CVE-2026-134624（SSRF，CVSS 4.0 9.3），已入 CISA KEV
  - 🌟 亮点总结: 厂商在托管环境入侵调查中发现并修复。已认证 API 用户配置 relay 时，LDAP 同步连通性检查可连向任意内网主机与端口，探测可达性并向内部服务发送数据。低于 20261121.1943 的版本受影响。N-able 称利用限于单台自有托管服务器，已撤销相关令牌并恢复服务。CISA 于 11 月 23 日列入 KEV，联邦修复截止 11 月 26 日。需要高权限 API 身份，不是未认证漏洞，但在已失陷的多租户环境中危害大。互动来自 @TheHackersNews 11 月 23 日相关帖；该帖状态链接不完整，主来源用完整报道。 | 👍 37 | 🔄 9 | 👀 未披露
  - 🔗 来源: https://www.securityweek.com/n-able-patches-critical-flaw-disclosed-after-mail-assure-cyberattack/ | 📅 2026-11-23

- Azure API Management Classic 密钥遭未授权读取，并与挪威能源企业事件关联
  - 🌟 亮点总结: 公开报道日期为 11 月 23 日。微软称 11 月 18 日发现、19 日关闭管理面未授权路径（发现与关闭为 [历史参考]）。受影响为 APIM Classic 的 Developer、Basic、Standard、Premium；Classic Consumption 与全部 v2 不受影响。可能暴露 Named Values、IdP/OIDC client secret、subscription key，以及直连管理 API 的 token。平台侧轮换不能代替客户轮换。挪威 NSM 称能源行业最先发现，Equinor、Skagerak Energi 等受影响；两家称未见数据被窃或业务中断。客户侧日志可能不完整，不能用「日志里没有」证明密钥未被读到。相关密钥应按已暴露处理，并核对接后端访问。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.bleepingcomputer.com/news/security/microsoft-azure-flaw-exploited-to-steal-customers-api-credentials/ | 📅 2026-11-23

- AI 推理供应链：至少三家托管方复制提示词与诱饵云密钥
  - 🌟 亮点总结: 约 200 万条带 canary 的提示词显示，至少三家托管商在数月内未察觉数据被窃。最大一起约数百枚诱饵 AWS 密钥在 10 月下旬被整批复制（含模型未执行即被拒的请求），随后出现数万次 AWS API 调用，并探测 S3、Secrets Manager、Parameter Store，尝试创建 IAM 用户与 Bedrock 相关能力；曾用 ARTEX 确认密钥仍有效。部分标有 Zero Data Retention 的请求仍被读取。窗口内跟进点名 Phala 旧接口与未加固 GPU 节点、GMI 约三天请求留存被读，以及 Together 编码代理把私有仓库凭证提交到公开仓库。11 月 22 日 OpenRouter 下架三家供应商，并将 125 个端点移出 ZDR。影响是客户真实提示词极可能一并泄露，长效云凭证可被转售或横向使用。Dragos 原文为 2026-11-19 [历史参考]。防御要点：敏感任务自托管或直连一级供应商；凡进入提示词、日志或评测样本的云密钥一律轮换；空账号金丝雀不能代替最小权限与短期凭证。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://lava.security/blog/ai-inference-canary-research-prompts-exposed | 📅 2026-11-21

- Datadog《2026 State of Cloud Security》窗口内解读
  - 🌟 亮点总结: 11 月 23 日博文：云应用高危/严重漏洞中位数由 2026 年 2 月约 4 个升至 11 月约 16 个（约四倍）。超过五分之一组织使用云托管推理；Gemini 用户近半数仍用长效 API key，Bedrock 约 17%，Azure Foundry 默认长效密钥约 97% 组织未改。工作负载平均约 149 个依赖，逾半为传递依赖；约 60% 组织在跑发布不足 24 小时的版本。被盗长效 AI key 可直接变现推理额度。主报告首发早于本窗口 [历史参考]，不计入本期热度。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.datadoghq.com/blog/cloud-security-study-learnings-2026/ | 📅 2026-11-23

- VMware Cloud on AWS：VMSA-2026-0011 对 SDDC 的影响
  - 🌟 亮点总结: 11 月 24 日 Broadcom 公布 23 个 CVE。对 VMC on AWS，仅 ESX 的 CVE-2026-123913（VMkernel 栈缓冲区问题，CVSS 约 8.2，需已有 VMX 进程内权限）影响 SDDC，由 VMware 分批修复。VMware Tools 的 CVE-2026-123918 按共享责任模型由客户升级 Guest Tools；其余多数不影响托管 SDDC。客户应核对 Tools 版本，勿把「托管」当成 Tools 已修完。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://techdocs.broadcom.com/us/en/vmware-cis/cloud/vmware-cloud-on-aws/SaaS/vmware-cloud-on-aws-security-bulletins/vmware-cloud-on-aws-security-bulletins.html | 📅 2026-11-24

- Google Cloud：OpenJDK CVE-2026-114938（Java4Shell）托管运行时补丁滚动
  - 🌟 亮点总结: 漏洞于 11 月 17 日披露 [历史参考]，本窗口为 GCP 公告更新至 11 月 23 日。HotSpot AVX-512 VBMI 的 Base64 解码内存破坏，仅影响支持该指令的 x86-64，ARM 不受影响；厂商称部分默认配置的 Java 应用上可达到未认证 RCE，但并非通用一键利用。Cloud Run、Functions、App Engine、Buildpacks、Dataflow、Managed Airflow 等已完成修补版 Java 17/21/25 基础镜像滚动。自管 GKE/VM 仍须自行升级。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://docs.cloud.google.com/support/bulletins | 📅 2026-11-23

**📚 最值得读的 Writeup / 公开报告**
- @bountywriteups 窗口内 Writeup 聚合（仅标题级）
  - 📝 技术摘要: 11 月 23 日线程汇总多篇公开分析，含通配参数暴露大量账户、OAuth 账户接管、邮件伪造进入协作工具、SSRF 访问内网等标题。利用链未经复核，此处不复述步骤。 | 👍 27 | 🔄 9 | 👀 未披露
  - 🔗 链接: https://x.com/bountywriteups/status/2124798913739886784 | 📅 2026-11-23

- BleepingComputer / SecurityWeek：APIM Classic 事件时间线
  - 📝 技术摘要: 公开事实链是能源行业先发现，微软 18 日确认、19 日堵住管理面路径（该两日为 [历史参考]），23 日媒体核对受影响层级与应轮换的密钥类型。v2 与 Classic Consumption 被明确排除。公司自报「未见数据被窃」不等于密钥未被读过。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://www.securityweek.com/azure-flaw-exploited-to-target-secrets-at-norwegian-energy-firms/ | 📅 2026-11-23

- LAVA：200 万提示词金丝雀与推理供应链
  - 📝 技术摘要: 每条请求绑定独立诱饵密钥与唯一 URL，用于区分「托管方被入侵后复制请求」和「实验室/供应商自行回连」。文中点名 Phala、GMI 请求留存被读，以及 Together 编码代理提交凭证。适合复查路由器上游、日志留存和 ZDR 是否名实相符。Dragos 同题原文为 2026-11-19 [历史参考]。不提供复现步骤。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://lava.security/blog/ai-inference-canary-research-prompts-exposed | 📅 2026-11-21

- Together AI：AI 编码代理把私有仓库凭证提交到公开仓库
  - 📝 技术摘要: 官方称测试用提示词样本在私有 Hugging Face 仓库；开发公开仓库 xorl 时，AI 编码代理提交了对应凭证。扫描发现后已回滚，但暴露窗口内凭证被取走并下载样本。样本主要来自 MiniMax M3、GLM-5.2、Kimi K2.6，日期集中在 2026-06-24、07-04、07-08、07-14。对方还在样本中检索并测试其他服务凭证。ZDR 路径据转述不在该批样本内。这是密钥进入代理可写仓库，不是模型权重泄露。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026 | 📅 2026-11-21

- N-able：Mail Assure 事件更新
  - 📝 技术摘要: 将托管邮件安全产品的 SSRF 与一次真实入侵调查绑定：认证后的 LDAP 连通性检查未限制目标。修复版本 20261121.1943；托管侧已撤销令牌。对 MSP 客户，除升级外应确认 API/OAuth/中继凭据已轮换，并审计异常内网探测。本条为厂商博文，互动未披露（👍 37 属于上文新闻帖，不重复计入）。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 链接: https://www.n-able.com/blog/mail-assure-incident-update | 📅 2026-11-22

**🔥 社区热议的技术话题或新手法**
- ZDR 不能当成数据边界
  - 💬 讨论核心: 焦点从「怎么注入模型」转到提示词在托管商、路由商、转售商处被整段复制。零留存标记只约束签约的第一跳；转售、审核、排障样本和编码代理都可能再读一次。被拒请求仍可能在入口被复制。实践上敏感推理应自建或直连一级供应商，并自带可告警的假密钥。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性推文: https://www.securityweek.com/ai-inference-providers-failed-to-detect-hacking-and-prompt-theft-says-dragos/ | 📅 2026-11-23

- 长效 AI API key 与漏洞数量约四倍
  - 💬 讨论核心: 社区把高危/严重漏洞中位数约四倍增长，与 Gemini、Bedrock、Azure Foundry 的长效密钥占比放在一起看。攻击者不需要自备模型，偷到调用方 key 即可借用配额与数据面。短时工作负载身份和密钥轮换，优先于再堆扫描器。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性推文: https://www.datadoghq.com/blog/cloud-security-study-learnings-2026/ | 📅 2026-11-23

- AI 编码代理提交密钥
  - 💬 讨论核心: Together 事件把「代理能写 Git」变成云与数据泄露入口。应禁止代理提交密钥，对公开仓库做推送前扫描，并把测试样本与生产凭证隔离。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性推文: https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026 | 📅 2026-11-21

- 间接 Prompt Injection 仍是智能体主风险
  - 💬 讨论核心: 11 月 23 日综述把损失场景从「聊天越狱」改写为：智能体同时具备私有数据、不可信内容和对外动作即可被劫持。Jailbreak 只是直接注入的一类目标。文中对照 Slack AI、M365 Copilot、Cursor、GitHub MCP 等已知案例，强调没有单一防护足够。基准数字来自更早研究 [历史参考]。本期没有新的可核高互动 PoC 帖。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性推文: https://www.sysdig.com/learn-cloud-native/prompt-injection | 📅 2026-11-23

- Ghostscript CVE-2026-125396 再次进入公开讨论
  - 💬 讨论核心: 低于 10.08.0 的版本在处理不可信 PostScript/PDF 时，存在沙箱限制被绕过并执行代码的风险（CVSS 4.0 由 CNA 评为 8.5）。补丁在 2026-09 已发布 [历史参考]；本窗口是公开复盘与下游暴露面讨论（邮件、打印、部分 Web 上传管线）。处置是升级到 10.08.0 或发行版回移植，而不是临时过滤规则。不提供利用细节。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性推文: https://nvd.nist.gov/vuln/detail/CVE-2026-125396 | 📅 2026-11-22

**🆕 新上线 / 更新中的 Bug Bounty 或 VDP 项目**
- Metric（Immunefi）
  - 📝 更新点: 跟踪站列为新项目/新范围，Critical 最高约 $500,000。赏金与范围以平台页面为准。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/programs | 📅 2026-11-24

- Minara（自托管）
  - 📝 更新点: 窗口内新增 Critical 档，跟踪站显示最高约 $300,000。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes | 📅 2026-11-24

- 1Password 公开项目（Intigriti）
  - 📝 更新点: 跟踪站列为新项目，最高约 $30,000。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/programs | 📅 2026-11-24

- BoursoBank（YesWeHack）
  - 📝 更新点: 新项目，最高约 €3,000。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/programs | 📅 2026-11-24

- GCash Vulnerability Disclosure（HackerOne）
  - 📝 更新点: 跟踪站记录为新公开 VDP；赏金与范围以平台页面为准。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbounty.fyi/changes?dir=new&since=1 | 📅 2026-11-23

**📢 平台动态 & 政策变化**
- CISA 将 CVE-2026-134624 列入 KEV，联邦机构修复截止 2026-11-26 | CISA | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://nvd.nist.gov/vuln/detail/CVE-2026-134624 | 📅 2026-11-23

- OpenRouter 下架 3 家推理供应商，125 个端点失去 ZDR | OpenRouter | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 📝 更新点: 11 月 22 日公告称，研究者发现部分上游存在数据被盗或策略未兑现；OpenRouter 自身未被指入侵。措施包括下架 3 家供应商、将 125 个端点移出 ZDR（含预防性移除），并通知可能受影响客户。恢复 ZDR 需额外保证与验证。这不是赏金平台规则变更。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/ | 📅 2026-11-22

**🏆 猎人里程碑 / 大额奖励**
本期无高互动/突破性情报

**☕ 其他有趣八卦 / 吐槽 / 预警**
- 自建项目「修了不付钱」投诉仍在出现（例如 11 月 21 日有人称某 Critical 子域问题被静默修复且无回复）。投报告前先确认平台托管、范围与付款记录，不要把修复本身当成会付钱。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://bugbountyscam.com/ | 📅 2026-11-21

- 防御清单（非新漏洞）: 轮换曾出现在提示词、评测集或代理仓库中的云密钥；Gemini、Bedrock、Azure Foundry 长期 key 改为短期凭证；文档与打印链路确认 Ghostscript ≥ 10.08.0。不要把真实密钥、内网 URL 或客户数据写进发给第三方推理路由的提示词。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.datadoghq.com/blog/cloud-security-study-learnings-2026/ | 📅 2026-11-23
