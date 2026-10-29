# grok-secintel-daily

在 GitHub Actions 中定时生成网络安全情报 Markdown 报告，并自动提交到仓库。

约束（重要）：

- 真实 Prompt **不入库**：CI 通过 Secret 生成 `prompt_template.txt`
- 报告日期与路径按北京时间（`Asia/Shanghai`）计算：`outputs/YYYY/MM/YYYY-MM-DD.md`
- 仓库根目录会保留 `LATEST.md`（最新一份日报，便于直接查看）

## 每日邮件通知（GitHub 原生）

最省事的方式：在仓库右上角 **Watch → Custom**，勾选 **Issues**。之后无需每月手动切换订阅，Actions 每天更新都会触发 GitHub 邮件通知。

前提：
- 仓库已启用 Issues
- 你的 GitHub 通知设置开启邮件（Settings → Notifications）

## 文件说明

- `grok.py`：主脚本（支持 `DRY_RUN=1`）
- `prompt_template.example.txt`：可公开的 Prompt 结构示例
- `prompt_template.txt`：真实 Prompt（**不提交**；本地自备 / CI 由 Secret 生成）
- `.github/workflows/daily-report.yml`：定时任务与手动触发工作流
- `outputs/`：日报输出目录（会被工作流提交）
- `LATEST.md`：最近一次运行生成的报告
- `tests/`：配置、请求参数及响应解析等单元测试

## 模型与联网搜索

当前默认模型为 `grok-4.7`（`FAST_MODEL = "grok-4.7"`，`THINKING_MODEL = FAST_MODEL`），草稿生成和最终汇总均使用该模型。脚本先按温度 `0.5`、`0.7`、`0.9` 串行生成 3 份草稿，再以温度 `0.7` 汇总成功的草稿。后续更换模型时，在 `grok.py` 中修改相应常量即可。

草稿生成请求通过 OpenAI Python SDK 的 `extra_body` 在 JSON 请求体顶层加入：

```json
{
  "tools": [{"type": "web_search"}]
}
```

该参数用于启用模型的内置联网搜索能力。最终汇总只依据已生成的草稿，不携带搜索工具，避免汇总阶段另行检索或引入输入草稿之外的信息。所有请求使用流式响应，以便在长响应生成期间持续接收数据，降低代理读超时风险。实际是否执行搜索取决于模型及所配置 API 服务的行为；携带参数本身不能证明已经检索网页。

草稿请求最多尝试 3 次，汇总请求最多尝试 4 次；服务端提供 `Retry-After` 时遵守其等待时间。账户无模型权限或其他不可重试错误会直接结束该次调用。部分草稿失败时，仍会汇总成功的草稿；全部草稿失败或汇总失败时，脚本中止，不写入本次报告。

## 本地使用

建议使用 Python 3.11，与 GitHub Actions 保持一致。

### 1) 准备真实 Prompt

从示例复制一份，再替换内容为你的真实 Prompt：

```bash
cp prompt_template.example.txt prompt_template.txt
```

`prompt_template.txt` 已在 `.gitignore` 中忽略，避免误提交。

### 2) 环境变量

```bash
export XAI_API_KEY="your-key"
export XAI_BASE_URL="https://api.x.ai/v1"
```

### 3) 干跑（不调用 API）

```bash
DRY_RUN=1 python3 grok.py
```

干跑仍需设置上述两个环境变量，并准备 `prompt_template.txt`；不会请求 API，但会将模拟报告写入当天的 `outputs/` 文件和 `LATEST.md`，覆盖已有同名文件。本地脚本不会自动加载 `.env`。

### 4) 正常运行（调用 API）

```bash
pip install -r requirements.txt
python3 grok.py
```

按北京时间查看当天输出文件：

```bash
head -20 "outputs/$(TZ=Asia/Shanghai date +%Y/%m/%Y-%m-%d).md"
```

### 5) 运行测试

```bash
python3 -m unittest discover -s tests -v
```

单元测试不调用真实 API，不能用于确认远端模型或网关支持联网搜索。

## GitHub Actions 使用（私有 Prompt 下发）

### 1) 配置 Secrets

在仓库设置中添加以下 Secrets：

- `XAI_API_KEY`
- `XAI_BASE_URL`
- `PROMPT_TEMPLATE_B64`：真实 `prompt_template.txt` 的 Base64（单行）

生成 `PROMPT_TEMPLATE_B64`（本地一次性操作）：

```bash
base64 < prompt_template.txt | tr -d '\n'
```

将输出粘贴到 GitHub：Settings → Secrets and variables → Actions → New repository secret。

安全提醒：不要在 issue/PR/日志中粘贴 `PROMPT_TEMPLATE_B64`，它等价于明文 Prompt。

### 2) 触发方式

- 定时触发：按 `.github/workflows/daily-report.yml` 的 cron 运行并自动提交 `outputs/` 和 `LATEST.md` 变更
- 手动触发：Actions → Run workflow，可选择 `dry_run=1`（不提交，但会发送 `[DRY_RUN]` 标记的 issue 通知，用于快速验证通知链路）

工作流会用 `printf '%s' "$PROMPT_TEMPLATE_B64" | base64 -d > prompt_template.txt` 生成真实 Prompt。

### 3) 调度注意事项

- 当前 cron 配置为每天 UTC 01:07（北京时间 09:07）；实际启动时间由 GitHub Actions 调度决定。
- 建议保留 `workflow_dispatch` 兜底，必要时手动触发或配合 `dry_run=1` 快速验证依赖。
- 如需更精确的触发，可额外使用外部调度（例如 IFTTT、云端 cron 或自建脚本）调用 `workflow_dispatch`，由外部系统控制时间，Actions 只负责执行。

## 常见排查

- `❌ Missing secret: PROMPT_TEMPLATE_B64`：Actions 未配置 Secret
- `❌ prompt 模板文件不存在`：本地缺少 `prompt_template.txt`（从示例复制并替换即可）
- 模型或网关拒绝 `tools` / `web_search`：确认所配置的模型和 API 服务支持该工具；脚本会保留搜索参数按原有策略重试，不会自动切换成无搜索请求
- 本地检查输出文件找不到：请用北京时间计算路径（`TZ=Asia/Shanghai ...`）
- `.gitignore` 不生效：若文件曾被 git 跟踪过，需要先 `git rm --cached prompt_template.txt`

base64 备注：Actions（Ubuntu）用 `base64 -d`；macOS 常见是 `base64 -D`。
