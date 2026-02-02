#!/usr/bin/env python3
"""Grok 网络安全情报生成脚本。

- 串行调用 fast 多次生成草稿，再由 thinking 汇总为最终报告
- 输出路径：outputs/YYYY/MM/YYYY-MM-DD.md（按 Asia/Shanghai）
- DRY_RUN=1：不调用 API，仅验证模板填充与写文件
"""

from __future__ import annotations

import os
import re
import sys
import random
import time
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

try:
    from openai import OpenAI
except ModuleNotFoundError:
    OpenAI = None  # type: ignore[assignment]

# --- 常量配置 ---
FAST_MODEL = "grok-4-fast"
THINKING_MODEL = "grok-4.1-thinking"
TEMPERATURES = [0.1, 0.6, 1.0]
THINKING_TEMPERATURE = 0.1
API_TIMEOUT = 300.0  # 秒
MAX_RETRIES = 2  # 最多重试 2 次（总共尝试 3 次）
MAX_CONTENT_LENGTH = 15000  # 每份 fast 输出的最大字符数，避免 thinking 上下文过长
RETRY_MIN_DELAY = 2.0
RETRY_MAX_DELAY = 5.0
PROMPT_TEMPLATE_FILE = "prompt_template.txt"
OUTPUT_DIR = "outputs"
LATEST_REPORT_FILE = "LATEST.md"
TIMEZONE = "Asia/Shanghai"

# --- 汇总 Prompt 模板 ---
SUMMARY_PROMPT_TEMPLATE = """你是一个专业的网络安全情报审查和整合专家。

我提供了 {n} 份由 AI 生成的"网络安全情报速报"（来自同一个 prompt 的多次生成结果）。
由于每次生成存在随机性，各份内容在情报条目、互动数据、链接等方面可能存在差异。

请你按以下规则整合输出最终版：

【整合规则】
1. **按板块逐一处理**: 依次处理每个板块（最高赏金、云安全重点、Writeup、热议话题等）
2. **情报去重与合并**: 
   - 若多份内容提及同一情报（相同漏洞/相同推文），合并为一条
   - 保留信息最完整、描述最准确的版本
   - 互动数据（点赞/转发/浏览）取各份中的最大值
3. **链接校验**: 若同一情报在不同版本中链接不同，优先保留格式完整的推文链接
4. **Top 限制**: 每个板块最终保留 Top 3-5 条最有价值的情报（云安全板块可适当放宽）
5. **优先级排序**: 在每个板块内，按互动数据（点赞优先）降序排列
6. **热度峰值更新**: 统计整合后所有情报中的最高点赞数和最高浏览量，更新开头的"本期热度峰值"
7. **情报眼提炼**: 基于整合后的全部情报，重新提炼一句 20 字以内的趋势概括

【输出要求】
- 严格保持原有的输出格式和板块结构
- 所有中文描述保持专业、干练
- 不要添加原内容中没有的情报
- 不要输出你的分析过程，直接输出最终整合后的完整报告

**整合要求补充（硬约束）**
1. **板块完整性**：无论输入草稿是否为空，最终必须保留全部板块；为空就用统一句式“本期无高互动/突破性情报”。
2. **时间窗口硬约束**：所有收录事件的发布时间必须在报告“统计范围”窗口内；如需引用背景，必须标注“历史参考”，且不得计入本期热度峰值。
3. **热度峰值一致性**：热度峰值必须从最终保留条目中计算（取最大值），且峰值对应事件在正文中必须有详细条目。
4. **情报眼锚定**：今日情报眼默认锚定在“热度峰值”对应事件；若有多个热点，优先级：Critical/大规模安全事件 > 密钥泄露/供应链事件 > 新工具/方法讨论。
5. **去重优先级**：同一事件多版本时，优先保留互动最高且技术细节最完整的版本；链接保留互动最高的那条作为主来源。
6. **你是审稿器而非作者**：不要重新创作或补充不存在的情报，只做合并、去重、排序、标注与纠错。

---

{contents}"""


def get_now() -> datetime:
    return datetime.now(ZoneInfo(TIMEZONE))


def is_dry_run() -> bool:
    return os.environ.get("DRY_RUN", "0") == "1"


def log(message: str) -> None:
    print(message, flush=True)


def load_env_config() -> tuple[str, str]:
    api_key = os.environ.get("XAI_API_KEY")
    base_url = os.environ.get("XAI_BASE_URL")

    if not api_key:
        log("ERROR: 环境变量 XAI_API_KEY 未设置")
        sys.exit(1)
    if not base_url:
        log("ERROR: 环境变量 XAI_BASE_URL 未设置")
        sys.exit(1)

    return api_key, base_url


def load_prompt_template(filepath: str, now: datetime) -> str:
    """加载并填充 prompt 模板（使用统一 now，避免跨天不一致）。"""
    if not os.path.exists(filepath):
        log(f"ERROR: prompt 模板文件不存在: {filepath}")
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8") as f:
        template = f.read()

    log(f"加载 prompt 模板: {filepath} ({len(template)} 字符)")

    # 填充占位符（使用传入的基准时间）
    prompt = template.replace("{{CURRENT_TIME}}", now.strftime("%Y-%m-%d %H:%M:%S"))
    prompt = prompt.replace("{{END_DATE}}", now.strftime("%Y-%m-%d"))
    prompt = prompt.replace(
        "{{START_DATE}}", (now - timedelta(days=3)).strftime("%Y-%m-%d")
    )
    prompt = prompt.replace("{{PREVIOUS_YEAR}}", str(now.year - 1))

    return prompt


def call_with_retry(
    client: OpenAI,
    model: str,
    prompt: str,
    temperature: float,
    label: str,
) -> str | None:
    """带重试的 API 调用；成功返回内容，失败返回 None。"""
    for attempt in range(MAX_RETRIES + 1):
        try:
            if attempt == 0:
                log(f"   {label} ...")
            else:
                delay = random.uniform(RETRY_MIN_DELAY, RETRY_MAX_DELAY)
                log(f"   {label} retry {attempt}/{MAX_RETRIES} (sleep {delay:.1f}s)...")
                time.sleep(delay)

            start_time = time.time()
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
            )
            elapsed = time.time() - start_time

            content = response.choices[0].message.content
            if content:
                content = content.strip()
                log(f"   {label} ok ({elapsed:.1f}s, {len(content)} chars)")
                return content
            else:
                log(f"   {label} empty response")

        except Exception as e:
            if attempt == MAX_RETRIES:
                log(f"   {label} ERROR (final): {e}")
            else:
                log(f"   {label} ERROR: {e}")

    return None


def sequential_call_grok_fast(
    client: OpenAI,
    prompt: str,
    temperatures: list[float],
) -> list[str | None]:
    """串行调用 fast 多次。"""
    log(f"\n调用 {FAST_MODEL} x {len(temperatures)}")
    results = []

    for i, temp in enumerate(temperatures, 1):
        label = f"[{i}/{len(temperatures)}] temp={temp}"
        result = call_with_retry(client, FAST_MODEL, prompt, temp, label)
        results.append(result)

    return results


def call_thinking_model(
    client: OpenAI,
    contents: list[str],
) -> str | None:
    """调用 thinking 模型汇总审查。"""
    log(f"\n调用 {THINKING_MODEL} 汇总")

    # 构建汇总 prompt，对每份内容做长度截断避免上下文过长
    contents_text = ""
    for i, content in enumerate(contents, 1):
        # 截断过长内容
        if len(content) > MAX_CONTENT_LENGTH:
            content = content[:MAX_CONTENT_LENGTH] + "\n\n[内容已截断...]"
            log(f"   WARN: 第 {i} 份内容超过 {MAX_CONTENT_LENGTH} 字符，已截断")
        contents_text += f"【第 {i} 份内容】\n{content}\n\n---\n\n"

    summary_prompt = SUMMARY_PROMPT_TEMPLATE.format(
        n=len(contents),
        contents=contents_text.strip(),
    )

    result = call_with_retry(
        client,
        THINKING_MODEL,
        summary_prompt,
        THINKING_TEMPERATURE,
        "[汇总]",
    )

    return result


def save_to_file(content: str, now: datetime) -> str:
    """保存内容到 outputs/YYYY/MM/YYYY-MM-DD.md（按传入 now）。"""
    year = now.strftime("%Y")
    month = now.strftime("%m")
    date = now.strftime("%Y-%m-%d")

    output_dir = Path(OUTPUT_DIR) / year / month
    output_dir.mkdir(parents=True, exist_ok=True)

    filepath = output_dir / f"{date}.md"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.rstrip() + "\n")

    log(f"\n保存文件: {filepath}")
    return str(filepath)

def save_latest(content: str) -> str:
    """保存最新报告到仓库根目录，便于直接查看。"""
    filepath = Path(LATEST_REPORT_FILE)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.rstrip() + "\n")
    log(f"保存文件: {filepath}")
    return str(filepath)


def inject_generated_time(content: str, now: datetime) -> str:
    """在报告头部注入生成时间（使用 now），避免依赖模型是否复述 {{CURRENT_TIME}}。"""
    generated_line = f"> 生成时间: {now.strftime('%Y-%m-%d %H:%M:%S')} UTC+08:00"

    lines = content.splitlines()
    head = "\n".join(lines[:30])
    if re.search(r"(^|\n)\s*(>|-|\*)?\s*生成时间\s*[:：]", head):
        return content

    if not lines:
        return generated_line + "\n"

    insert_at = 0
    for idx, line in enumerate(lines):
        if line.strip():
            insert_at = idx + 1
            break

    out_lines = lines[:insert_at] + ["", generated_line, ""] + lines[insert_at:]
    return "\n".join(out_lines).lstrip("\n")


def main() -> None:
    start_time = time.time()

    # 在整个流程中统一使用同一个时间点，避免跨天边界不一致
    now = get_now()
    report_date = now.strftime("%Y-%m-%d")
    dry_run = is_dry_run()

    if dry_run:
        log("DRY_RUN=1")
    log(f"开始 [{now.strftime('%Y-%m-%d %H:%M:%S')} UTC+08:00]")

    # 1. 加载配置
    log("\n检查环境变量...")
    api_key, base_url = load_env_config()
    log("   XAI_API_KEY: [REDACTED]")
    log("   XAI_BASE_URL: [REDACTED]")

    if not dry_run:
        if OpenAI is None:
            log("ERROR: 依赖未安装：openai 包缺失（正常运行需要，DRY_RUN 可不安装）")
            sys.exit(1)
        client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            timeout=API_TIMEOUT,  # timeout 设置在 client 级别
        )

    # 2. 加载 prompt 模板（传入统一的时间点）
    log("\n检查 prompt 模板...")
    prompt = load_prompt_template(PROMPT_TEMPLATE_FILE, now)
    log(f"   prompt 长度: {len(prompt)} 字符")
    log(
        f"   窗口: {(now - timedelta(days=3)).strftime('%Y-%m-%d')}~{now.strftime('%Y-%m-%d')}"
    )

    # 3. 干跑模式：跳过 API 调用，生成模拟内容
    if dry_run:
        log("\nDRY_RUN：跳过 API 调用")
        final_content = (
            "# DRY_RUN\n\n"
            f"- time: {now.strftime('%Y-%m-%d %H:%M:%S')} UTC+08:00\n"
            f"- report_date: {report_date}\n"
            f"- window: {(now - timedelta(days=3)).strftime('%Y-%m-%d')}~{now.strftime('%Y-%m-%d')}\n"
            f"- prompt_len: {len(prompt)}\n"
            f"- output: {OUTPUT_DIR}/{now.strftime('%Y/%m/%Y-%m-%d')}.md\n"
        )

    else:
        # 3. 串行调用 grok-4-fast × 3
        results = sequential_call_grok_fast(client, prompt, TEMPERATURES)

        # 4. 检查结果（降级模式）
        valid_results = [r for r in results if r is not None]
        success_count = len(valid_results)
        total_count = len(TEMPERATURES)

        log(f"\n{FAST_MODEL} 结果: {success_count}/{total_count} 成功")

        if success_count == 0:
            log(f"ERROR: {FAST_MODEL} 全部失败，任务中止")
            sys.exit(1)

        # 5. 调用 thinking 模型汇总
        final_content = call_thinking_model(client, valid_results)

        if final_content is None:
            log(f"ERROR: {THINKING_MODEL} 调用失败，任务中止")
            sys.exit(1)

    # 6. 保存到本地文件（传入统一的时间点）
    log("\n写入输出文件...")
    final_content = inject_generated_time(final_content, now)
    output_path = save_to_file(final_content, now)
    log(f"   ok: {output_path}")
    latest_path = save_latest(final_content)
    log(f"   ok: {latest_path}")

    # 7. 输出日期供 workflow 使用（使用同一个 now，确保与文件名一致）
    log(f"\n报告日期: {report_date}")
    log(f"输出路径: {output_path}")

    # 输出 GitHub Actions 可读取的格式
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as f:
            f.write(f"report_date={report_date}\n")
            f.write(f"output_path={output_path}\n")
        log("   已写入 GITHUB_OUTPUT")

    # 8. 完成
    elapsed = time.time() - start_time
    if dry_run:
        log(f"\n完成 (DRY_RUN, {elapsed:.1f}s)")
    else:
        log(f"\n完成 ({elapsed:.1f}s)")


if __name__ == "__main__":
    main()
