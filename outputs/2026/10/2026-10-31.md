**【CyberSec 情报速报 | 云安全 & AI 重点强化】**

> 生成时间: 2026-10-31 14:55:58 UTC+08:00

**统计范围**: 2026-10-28 - 2026-10-31（包含起止日，共约 3-4 天数据）
**本期热度峰值**: 最高 👍 11515 | 最高 👀 6.0k（YouTube，非推文）
**今日情报眼**: 币安热钱包遭盗约63亿美元

---

**📋 生成说明**
本报告由多份公开来源汇总稿合并、去重后整理，技术细节未经人工验证，仅供参考。互动只采用来源明确显示的数值，未核实的标「未披露」，不估算。窗口外首次披露与更早奖金标「[历史参考]」，不计入本期热度峰值。利用步骤、PoC 与 payload 均不展开。

---

**💰 本期最高赏金 / 最炸裂 payout**
- $15,000 | 帖文未点名 | Immunefi | 区块链/DLT 基础设施 Critical
  - 💡 一句话总结: 窗口内唯一核实到账；该研究员累计 $133,126，平台累计近 $1.45 亿。 | 👍 82 | 🔄 5 | 👀 未披露
  - 🔗 来源: https://x.com/immunefi/status/2115775164323594623 | 📅 2026-10-29

Intigriti Bug Bytes #241 复盘的 $250K Chrome 全链、约 $175K Edge、$90K Google RCE 等，奖金均早于本窗口，标 **[历史参考]**，不计入本期峰值。

**☁️ 云安全重点(特别加强板块)**
- Wiz：AI 开发平台「Black October」，下游 LLMJacking
  - 🌟 亮点总结: 2026-10-30 长文串联本月至少 9 家 AI 开发/托管平台失陷。窗口内新披露为 CommandCode（10-28）与 Northflank（10-30）；Fireworks、OpenCode、Warp 称见到 “agent swarm”，其余多为 10 月上中旬事件。公开根因不一：凭证、供应链、构建基础设施提权、第三方依赖、遗留系统；共同点是专打环境变量里的 AI 访问密钥。Wiz 观察到企业云密钥在供应商侧凭证暴露后约 30 分钟内被住宅 IP 探测，随后可以小流量保活；一例在约 30 小时内产生约 80 万次 Bedrock 调用、约 90% 成功，因策略允许 `global.*` 跨区推理，限流仅约 6%。另一把受限密钥被疑似转售池调用后大量失败。Zeabur 已宣布因事件关停。防御重点是轮换供应商下发的模型密钥、收紧过宽的跨区推理 profile，并对短时跨组织模型探测告警。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.wiz.io/blog/black-october-for-ai-developer-platforms | 📅 2026-10-30
- 公开可列举云存储桶约 48.4 万个、文件约 180.5 亿
  - 🌟 亮点总结: SC Media / Security Affairs（10-29/30）转述 Ransomnews Cloud Exposure Index。快照约在 10-07，只看桶名与元数据、未打开文件内容。Amazon S3 约 34.8 万（约 71.9%–72%），Azure Blob 约 6.9 万，GCS 约 5.3 万。凭证/密钥相关文件约 32.1 万；暴露的 `.env` 中约 67% 最后修改于 2026。Azure 在备份、导出、薪酬类命名上占比偏高。部分桶是有意公开，但备份、证书和 `.env` 不应可列举。指数页日期为 10-27，贴边窗口，按 10-29/30 媒体跟进收录。建议核对匿名列举与 Block Public Access，并按备份、密钥类文件名做周期扫描。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.scworld.com/brief/ransomnews-identifies-18-billion-files-in-publicly-listable-cloud-buckets | 📅 2026-10-30
- Google Cloud Application Integration 反序列化（CVE-2026-93327）公告落入窗口
  - 🌟 亮点总结: GCP-2026-074 于 2026-10-28 发布，NVD 于 2026-10-30 入库。2026-09-11 之前的 SubWorkflow 任务中，已认证用户可借助恶意序列化对象执行任意代码（CWE-502）。Google 标为 Critical，并写明 9 月 11 日已修补、客户无需操作。这是补丁后公告，不是新的在野 0day。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://docs.cloud.google.com/support/bulletins | 📅 2026-10-28
- Wiz：2026 AI 威胁准备度调查（n=100）
  - 🌟 亮点总结: 52% 的受访组织在过去一年发现边界内有未经批准的 AI 应用；35% 正式允许团队自行部署 AI 工具；9% 承认完全无法发现未授权 AI 工作负载。建议把模型端点、镜像仓库和流水线按生产系统做配置、补丁和准入控制，并限制 Agent 凭证范围。样本只有 100 名安全决策者，不宜外推成全行业比例。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.wiz.io/blog/ai-threat-readiness-survey-report-2026 | 📅 2026-10-30
- Intruder《2026 Cloud Security Index》页面更新 **[历史参考]**
  - 🌟 亮点总结: 正文首次发布为 2026-08-11，10-30 仅见页面更新，不计入本期热度。其 12 个月至 2026-07 的客户样本仍显示：弱 IAM 在 AWS/Azure/GCP 分别约 97%/90%/87%；公网暴露服务约 76%/64%/8%。多云策略不能按同一张清单套用。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.intruder.io/blog/cloud-security-index | 📅 2026-08-11（页面更新 2026-10-30）

**📚 最值得读的 Writeup / 公开报告**
- Orange Tsai：纯逻辑缺陷的 Microsoft Edge 全链（已修补）
  - 📝 技术摘要: 2026-10-28 公开，Intigriti 10-30 将其列为本期首条。作者称该链在 Pwn2Own Berlin 2026 获得 $175,000（奖金在 5 月，属 **[历史参考]**），微软于赛后次日修补，登记 CVE-2026-45492 / 45494 / 45495。公开信息只确认：全程逻辑缺陷、无内存破坏、可从恶意页面走到 Windows 上的代码执行，且作者强调手工完成、未用 AI。具体导航、协议与文件写入步骤不转述。已更新的 Edge 不在受影响范围。 | 👍 115（YouTube，非推文） | 🔄 未披露 | 👀 6.0k（YouTube，非推文）
  - 🔗 链接: https://blog.orange.tw/posts/2026-10-the-last-proof-of-human-craft-browser-full-chain/ | 📅 2026-10-28
- CrowdStrike：Prompt Injection 分类扩至 222 项，新增 Agent 规划面
  - 📝 技术摘要: 2026-10-29 博客。新增手法指向 Agent 如何拆目标、选工具、决定哪条规则生效，而不是只改聊天回复。官方点名 Goal Decomposition Exploitation：诱导规划阶段把受限动作（例如外传文件）当成完成任务所必需。防御结论是把计划、工具权限和出站目的地放到模型之外强制执行，而不是只过滤最终回复。官方推文未过高热阈值。 | 👍 19 | 🔄 1 | 👀 未披露
  - 🔗 链接: https://www.crowdstrike.com/en-us/blog/new-prompt-injection-techniques-cover-agent-planning-attacks/ | 📅 2026-10-29

**🔥 社区热议的技术话题或新手法**
- 人工研究 vs AI 挖洞
  - 💬 讨论核心: Edge 全链公开与 Intigriti 10-30 的 Bug Bytes 把「纯逻辑、手工链」和更早的 AI 辅助 Chrome 全链放在同一讨论里。社区焦点是：AI 抬高了发现下限，浏览器全链仍依赖对产品逻辑的细读。$250K Chrome 条目本身不在本窗口。 | 👍 35 | 🔄 2 | 👀 未披露
  - 🔗 代表性推文: https://x.com/intigriti/status/2116275961972850884 | 📅 2026-10-30
- PHP2Shell 等仍出现在窗口内的在野清单 **[历史参考]**
  - 💬 讨论核心: 原始补丁日为 2026-10-21，早于本窗口。10-28 至 10-30 的日/周报及 Sysdig 仍把 PHP 核心未授权 RCE（CVE-2026-109618、CVE-2026-109619）列为活跃利用，并提及可与权限提升缺陷串联；Sysdig 同帖还称 Node.js Brotli 问题同样在被利用。本条只记录「补丁窗口短于新闻周期」。行动项限于核对版本与暴露面，不提供利用链或检测特征。 | 👍 4 | 🔄 1 | 👀 未披露
  - 🔗 代表性推文: https://x.com/sysdig/status/2115524308986695979 | 📅 2026-10-28
- Langflow OSS 未授权代码执行进入补丁窗口
  - 💬 讨论核心: IBM 10-28 公告、CVE 于 10-29 公开。CVE-2026-110186 影响 1.0.0–1.12.8，CVSS 9.8，无需账号即可因代码生成控制不当执行任意代码；同批还有认证绕过 CVE-2026-93680（同样 9.8）。修复版本为 1.13.0。截至 10-29 未见 KEV 或公开 PoC 索引。自建 LLM 工作流应升级，不要只停在 1.12.x。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性推文: https://www.ibm.com/support/pages/node/7294467 | 📅 2026-10-28
- Gemini 4 Carbon 先向防御方灰度
  - 💬 讨论核心: Google 于 2026-10-28 宣布该模型先给一小部分受信任的网络安全防御方，再视反馈扩大。厂商自述其在漏洞发现、验证与补丁类基准上领先，并称美国政府正在测试。这是准入与护栏策略，不是已验证的独立评测。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 代表性推文: https://cio.eletsonline.com/artificial-intelligence/google-gemini-4-carbon-frontier-ai-model-cybersecurity-staged-rollout-india/76533/ | 📅 2026-10-30

**🆕 新上线 / 更新中的 Bug Bounty 或 VDP 项目**
本期无高互动/突破性情报

**📢 平台动态 & 政策变化**
- @zseano 称 Expedia Group 项目约两个月内已支付奖金从 $21k 升到 $250k，近 30 天声誉领先为 @m0chan98。回复指出重复率可能很高。这是存量项目热度，不是新上线。 | HackerOne | 👍 233 | 🔄 4 | 👀 未披露
  - 🔗 来源: https://x.com/zseano/status/2115577340273066390 | 📅 2026-10-28
- HackerOne 改版 Hacker Success Program：五档 Ascendant → Established → Vanguard → Paragon → Apex，按近六个月有效影响评定，重复与 Informative 不扣分。档位预计 11-30 分配，在此之前支持政策不变。 | HackerOne | 👍 79 | 🔄 4 | 👀 未披露
  - 🔗 来源: https://x.com/Hacker0x01/status/2116254364746588426 | 📅 2026-10-30
- Intigriti 发布 Bug Bytes #241，汇总 Edge 逻辑全链及 Discord、Cloudflare 等更早披露的复盘；大额奖金不在本窗口。同刊讨论把身份核验前移到付费项目的提交阶段，并写明负责任披露在未核验时仍应被接受。1026 挑战截止 2026-11-02 23:59 UTC。 | Intigriti | 👍 35 | 🔄 2 | 👀 未披露
  - 🔗 来源: https://www.intigriti.com/researchers/blog/bug-bytes/intigriti-bug-bytes-241-october-2026 | 📅 2026-10-30

**🏆 猎人里程碑 / 大额奖励**
本期无高互动/突破性情报

**☕ 其他有趣八卦 / 吐槽 / 预警**
- 币安热钱包被盗，为已知最大加密货币盗窃。公开估计约 55–64 亿美元：Binance/TRM 约 63–63.6 亿，Chainalysis 曾报约 59.1 亿；vx-underground 账本写为约 55 亿被盗、约 28.3 亿冻结、仍流失约 26.7 亿。TRM 称约 63.6 亿美元于 10-29 约 20:05 UTC 起、约 20 分钟内从至少 10 条链转出。Tether CEO 确认已冻结超过 15.67 亿 USDT，该帖为点赞峰值；稳定币与部分链上资产合计冻结约 27–30 亿美元。公司称已预留约 63.4 亿美元覆盖损失，目标周日恢复提现，并称未见私钥泄露。公开初步调查指向运维终端进入服务侧并提交未经审批的提现，后续说明称还有更多入口；EIP-7702 委托只作为公开归因中的绕过名称，构造不展开。BTC 等不可冻结资产仍在攻击者地址。多家链上机构评估指向与朝鲜相关的 TraderTraitor，此为归因判断而非法庭结论。同晚另有 Polymarket 数百万美元级失窃的说法，细节当时仍模糊。 | 👍 11515 | 🔄 1140 | 👀 未披露
  - 🔗 来源: https://x.com/paoloardoino/status/2115918000373346709 | 📅 2026-10-29
- 猎人 @thedawgyg 批评 Apple 赏金计划，并称将公开四个月研究中的材料，包括未达奖金线、因而未报送的问题。后续帖澄清：未修复的更严重问题会先扣下，先放出的多与 DoS 档有关。本期只记录程序信任与披露争议，不转载任何材料、也不讨论升级路径。 | 👍 7625 | 🔄 350 | 👀 未披露
  - 🔗 来源: https://x.com/thedawgyg/status/2115418343138107448 | 📅 2026-10-28
- @vxunderground 10-28 记录一份伪装成马来西亚公司发票的 ISO，内含伪造的 Chromium 组件，VirusTotal 检出低。独立 status 未固化，指标来自账号时间线。样本只记到诱饵类型，取出与执行方法不转述。 | 👍 1812 | 🔄 144 | 👀 未披露
  - 🔗 来源: https://x.com/vxunderground | 📅 2026-10-28
- Cursor 市场中的 Anthropic Claude Code 扩展出现恶意版本 2.1.312 / 2.1.313，约 10-29 02:27–13:35 PT 在架（约 11 小时），Cursor 称最多影响约 5,000 名用户。恶意包会收集主机与用户信息，并尝试建立持久远程访问；官方称关键步骤在多数机器上会因缺少管理员权限而失败。市场曾短暂关闭后重建。入侵官方账号的路径仍未公开。请只从已确认干净的版本重装，不要执行来路不明的「清理脚本」。如何写入后门不转述。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://cursor.com/blog/claude-code-extension-security-notice | 📅 2026-10-29
- Cisco 确认 ASA/FTD 远程接入 SSL VPN 漏洞 CVE-2026-76418（报道称 CVSS 8.6）遭在野利用，未认证攻击者可使设备重载。这是自 8 月以来第二起同类防火墙在野问题。建议核对隧道组配置并按厂商公告升级，此处不提供利用条件。 | 👍 未披露 | 🔄 未披露 | 👀 未披露
  - 🔗 来源: https://www.itsecuritynews.info/it-security-news-roundup-2026-10-29-morning/ | 📅 2026-10-29
