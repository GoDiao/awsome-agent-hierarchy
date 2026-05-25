"""
Generate the GitHub Pages site from README.md and README-zh.md.

Run:
    python generate.py
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path


REPO_URL = "https://github.com/GoDiao/awsome-agent-hierarchy"
SITE_TITLE = "Awesome Agent Hierarchy"
SITE_DESCRIPTION = "A browsable, tagged ecosystem map of AI agent tooling across the full agent stack."
FRAMEWORK_IMAGE = "awesome-agent-hierarchy.png"

TAGS = ["Official", "Framework", "Example", "Research", "Infra", "Archived Classic"]
TAG_RE = re.compile(r"`(" + "|".join(re.escape(t) for t in TAGS) + r")`")
TAG_SLUGS = {tag: tag.lower().replace(" ", "-") for tag in TAGS}

LAYER_META = [
    {
        "idx": "01",
        "en": "Foundation Layer",
        "zh": "基础层",
        "desc_en": "LLMs, Prompt Engineering, Context",
        "desc_zh": "大语言模型、提示工程、上下文",
        "chips_en": ["LLMs", "Prompts", "Context"],
        "chips_zh": ["大模型", "提示", "上下文"],
        "icon": "chip",
        "color": "#2563eb",
        "support": False,
    },
    {
        "idx": "02",
        "en": "Agent Brain",
        "zh": "代理大脑",
        "desc_en": "Planning, Reasoning, Decision Engine",
        "desc_zh": "规划、推理、决策引擎",
        "chips_en": ["Planning", "Reasoning", "Decision"],
        "chips_zh": ["规划", "推理", "决策"],
        "icon": "brain",
        "color": "#0f8a50",
        "support": False,
    },
    {
        "idx": "03",
        "en": "Tool Layer",
        "zh": "工具层",
        "desc_en": "Search, Browser, Code, API, DB, Files",
        "desc_zh": "搜索、浏览器、代码、API、数据库、文件",
        "chips_en": ["Search", "Browser", "Code", "API"],
        "chips_zh": ["搜索", "浏览器", "代码", "API"],
        "icon": "tools",
        "color": "#6d3bbd",
        "support": False,
    },
    {
        "idx": "04",
        "en": "Agent Workflows",
        "zh": "代理工作流",
        "desc_en": "Research, Coding, Sales, Support, Content",
        "desc_zh": "研究、编码、销售、客服、内容",
        "chips_en": ["Research", "Coding", "Sales", "Support"],
        "chips_zh": ["研究", "编码", "销售", "客服"],
        "icon": "workflow",
        "color": "#c98a00",
        "support": False,
    },
    {
        "idx": "05",
        "en": "Multi-Agent Systems",
        "zh": "多代理系统",
        "desc_en": "Manager, Worker, Reviewer, Specialist, Memory",
        "desc_zh": "管理、工作者、审查、专家、记忆",
        "chips_en": ["Manager", "Worker", "Reviewer", "Memory"],
        "chips_zh": ["管理", "工作者", "审查", "记忆"],
        "icon": "agents",
        "color": "#de5b16",
        "support": False,
    },
    {
        "idx": "06",
        "en": "Infrastructure",
        "zh": "基础设施",
        "desc_en": "LangGraph, CrewAI, OpenAI SDK, MCP, Docker, K8s",
        "desc_zh": "LangGraph、CrewAI、OpenAI SDK、MCP、Docker、K8s",
        "chips_en": ["Frameworks", "MCP", "Docker", "K8s"],
        "chips_zh": ["框架", "MCP", "Docker", "K8s"],
        "icon": "cloud",
        "color": "#1f5f9f",
        "support": True,
    },
    {
        "idx": "07",
        "en": "Observability",
        "zh": "可观测性",
        "desc_en": "Logging, Tracing, Eval, Hallucination, Cost",
        "desc_zh": "日志、追踪、评估、幻觉、成本",
        "chips_en": ["Logging", "Tracing", "Eval", "Cost"],
        "chips_zh": ["日志", "追踪", "评估", "成本"],
        "icon": "chart",
        "color": "#0f7c7a",
        "support": True,
    },
    {
        "idx": "08",
        "en": "Security",
        "zh": "安全层",
        "desc_en": "Sandbox, Permission, Keys, Guardrails, HITL",
        "desc_zh": "沙箱、权限、密钥、护栏、人工审批",
        "chips_en": ["Sandbox", "Keys", "Guardrails", "HITL"],
        "chips_zh": ["沙箱", "密钥", "护栏", "审批"],
        "icon": "shield",
        "color": "#c7333b",
        "support": True,
    },
]


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def inline_md(text: str) -> str:
    text = esc(text)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1" loading="lazy">', text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def icon(name: str) -> str:
    icons = {
        "chip": '<svg viewBox="0 0 24 24"><rect x="7" y="7" width="10" height="10" rx="2"/><path d="M4 9h3M4 15h3M17 9h3M17 15h3M9 4v3M15 4v3M9 17v3M15 17v3"/></svg>',
        "brain": '<svg viewBox="0 0 24 24"><path d="M9 4a4 4 0 0 0-4 4v1a4 4 0 0 0 0 8v1a3 3 0 0 0 6 0V4z"/><path d="M15 4a4 4 0 0 1 4 4v1a4 4 0 0 1 0 8v1a3 3 0 0 1-6 0V4z"/><path d="M9 9H6M18 9h-3M9 14H6M18 14h-3"/></svg>',
        "tools": '<svg viewBox="0 0 24 24"><path d="M14 6l4 4-8 8H6v-4z"/><path d="M5 5l4 4M7 3l4 4M3 7l4 4"/></svg>',
        "workflow": '<svg viewBox="0 0 24 24"><rect x="3" y="4" width="5" height="5" rx="1"/><rect x="16" y="4" width="5" height="5" rx="1"/><rect x="9.5" y="15" width="5" height="5" rx="1"/><path d="M8 6.5h8M12 9v6"/></svg>',
        "agents": '<svg viewBox="0 0 24 24"><circle cx="12" cy="7" r="3"/><circle cx="5" cy="17" r="3"/><circle cx="19" cy="17" r="3"/><path d="M10 9l-3 5M14 9l3 5M8 17h8"/></svg>',
        "cloud": '<svg viewBox="0 0 24 24"><path d="M7 18h10a4 4 0 0 0 0-8 6 6 0 0 0-11-2 5 5 0 0 0 1 10z"/><path d="M8 14h8"/></svg>',
        "chart": '<svg viewBox="0 0 24 24"><path d="M4 19V5"/><path d="M4 19h16"/><path d="M7 15l3-4 3 2 4-6"/><circle cx="7" cy="15" r="1"/><circle cx="10" cy="11" r="1"/><circle cx="13" cy="13" r="1"/><circle cx="17" cy="7" r="1"/></svg>',
        "shield": '<svg viewBox="0 0 24 24"><path d="M12 3l7 3v5c0 5-3 8-7 10-4-2-7-5-7-10V6z"/><path d="M9 12l2 2 4-5"/></svg>',
        "search": '<svg viewBox="0 0 24 24"><circle cx="10" cy="10" r="5"/><path d="M14 14l5 5"/></svg>',
        "repo": '<svg viewBox="0 0 24 24"><path d="M6 4h10a2 2 0 0 1 2 2v14H8a2 2 0 0 1-2-2z"/><path d="M8 18h10M9 8h5"/></svg>',
        "chevron": '<svg viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"/></svg>',
    }
    return icons.get(name, icons["repo"])


def parse_readme(text: str) -> list[dict]:
    sections: list[dict] = []
    h2: dict | None = None
    h3: str | None = None
    buf: list[str] = []
    in_details = False
    det_buf: list[str] = []
    det_title = ""

    def flush_text() -> None:
        nonlocal buf
        if h2 and h3 and buf:
            content = "\n".join(buf).strip()
            if content and content != "---":
                h2["items"].append({"title": h3, "content": content, "type": "text"})
        buf = []

    for line in text.splitlines():
        if re.match(r"^## (Contents|目录|Contributing|贡献|License|许可)", line):
            flush_text()
            h2 = None
            h3 = None
            continue
        if line.startswith("## "):
            flush_text()
            h3 = None
            h2 = {"title": line[3:].strip(), "items": []}
            sections.append(h2)
            continue
        if line.startswith("### "):
            flush_text()
            h3 = line[4:].strip()
            continue
        if line.strip().lower() == "<details>":
            in_details = True
            det_buf = []
            continue
        if in_details and line.strip().lower().startswith("<summary>"):
            det_title = re.sub(r"<[^>]+>", "", line).strip()
            continue
        if line.strip().lower() == "</details>":
            in_details = False
            content = "\n".join(det_buf).strip()
            if h2 and content:
                h2["items"].append({"title": det_title, "content": content, "type": "details"})
            continue
        if in_details:
            det_buf.append(line)
        else:
            buf.append(line)

    flush_text()
    return sections


def get_layer_sections(sections: list[dict]) -> list[dict]:
    skip = ["contributing", "贡献", "license", "许可", "contents", "目录"]
    return [s for s in sections if not any(k in s["title"].lower() for k in skip)]


def split_repo_tags(markdown: str) -> tuple[str, list[str]]:
    tags = TAG_RE.findall(markdown)
    without = TAG_RE.sub("", markdown)
    without = re.sub(r"\s{2,}", " ", without).strip()
    return without, tags


def parse_repo(markdown: str) -> dict | None:
    content, tags = split_repo_tags(markdown)
    match = re.match(
        r"^\[([^\]]+)\]\((https://github\.com/[^)]+)\)\s*(?:!\[Stars\]\(([^)]+)\))?\s*-\s*(.*)$",
        content,
    )
    if not match:
        return None
    name, url, stars, desc = match.groups()
    return {"name": name, "url": url, "stars": stars or "", "desc": desc, "tags": tags}


def repo_card(markdown: str) -> str:
    repo = parse_repo(markdown)
    if not repo:
        return f'<li class="repo-card fallback" data-tags="">{inline_md(markdown)}</li>'
    tag_slugs = " ".join(TAG_SLUGS[t] for t in repo["tags"])
    tag_html = "".join(f'<span class="tag tag-{TAG_SLUGS[t]}">{esc(t)}</span>' for t in repo["tags"])
    stars = f'<img src="{esc(repo["stars"])}" alt="Stars" loading="lazy">' if repo["stars"] else ""
    return f"""
<li class="repo-card" data-tags="{esc(tag_slugs)}">
  <div class="repo-top">
    <a class="repo-name" href="{esc(repo["url"])}" target="_blank" rel="noopener">{esc(repo["name"])}</a>
    {stars}
  </div>
  <p>{inline_md(repo["desc"])}</p>
  <div class="tags">{tag_html}</div>
</li>"""


def count_repo_items(content: str) -> int:
    return len(re.findall(r"^- \[[^\]]+\]\(https://github\.com/", content, re.M))


def parse_provider_content(text: str) -> tuple[list[str], list[dict]]:
    notes: list[str] = []
    groups: list[dict] = []
    current_group: dict | None = None
    current_provider: dict | None = None

    for raw in text.splitlines():
        stripped = raw.strip()
        if not stripped:
            continue
        if stripped.startswith(">"):
            notes.append(stripped[1:].strip())
            continue
        if stripped.startswith("#### "):
            current_group = {"title": stripped[5:].strip(), "providers": []}
            groups.append(current_group)
            current_provider = None
            continue
        match_provider = re.match(r"^- \*\*([^*]+)\*\*(?:\s*-\s*(.*))?$", stripped)
        if match_provider:
            if current_group is None:
                current_group = {"title": "Providers", "providers": []}
                groups.append(current_group)
            current_provider = {"name": match_provider.group(1), "desc": match_provider.group(2) or "", "models": []}
            if current_provider["desc"]:
                current_provider["models"].append({"name": current_provider["name"], "url": "", "desc": current_provider["desc"]})
            current_group["providers"].append(current_provider)
            continue
        if raw.startswith("  - ") and current_provider is not None:
            model = raw[4:].strip()
            match_model = re.match(r"^\[([^\]]+)\]\(([^)]+)\)\s*-\s*(.*)$", model)
            if match_model:
                current_provider["models"].append(
                    {"name": match_model.group(1), "url": match_model.group(2), "desc": match_model.group(3)}
                )
            else:
                current_provider["models"].append({"name": model, "url": "", "desc": ""})
            continue
        match_platform = re.match(r"^- \[([^\]]+)\]\(([^)]+)\)\s*-\s*(.*)$", stripped)
        if match_platform:
            if current_group is None:
                current_group = {"title": "Providers", "providers": []}
                groups.append(current_group)
            current_group["providers"].append(
                {
                    "name": match_platform.group(1),
                    "desc": "",
                    "models": [
                        {"name": match_platform.group(1), "url": match_platform.group(2), "desc": match_platform.group(3)}
                    ],
                }
            )
            current_provider = None
            continue
    return notes, groups


def render_provider_accordions(text_en: str, text_zh: str, open_first: bool) -> str:
    notes_en, groups_en = parse_provider_content(text_en)
    notes_zh, groups_zh = parse_provider_content(text_zh)
    html_parts: list[str] = []
    if notes_en or notes_zh:
        html_parts.append('<div class="provider-notes">')
        if notes_en:
            html_parts.append(f'<blockquote class="lang-en">{inline_md(notes_en[0])}</blockquote>')
        if notes_zh:
            html_parts.append(f'<blockquote class="lang-zh">{inline_md(notes_zh[0])}</blockquote>')
        html_parts.append("</div>")

    html_parts.append(
        '<div class="provider-actions">'
        '<button onclick="setProviders(this, true)">Expand all providers</button>'
        '<button onclick="setProviders(this, false)">Collapse all providers</button>'
        "</div>"
    )
    for group_i, group_en in enumerate(groups_en):
        group_zh = groups_zh[group_i] if group_i < len(groups_zh) else {"title": group_en["title"], "providers": []}
        html_parts.append(
            '<section class="provider-group">'
            f'<div class="provider-group-title"><span class="lang-en">{inline_md(group_en["title"])}</span>'
            f'<span class="lang-zh">{inline_md(group_zh["title"])}</span></div>'
        )
        for prov_i, prov_en in enumerate(group_en["providers"]):
            prov_zh = group_zh["providers"][prov_i] if prov_i < len(group_zh.get("providers", [])) else prov_en
            is_open = open_first and prov_i == 0
            state_class = " open" if is_open else ""
            model_count = max(len(prov_en["models"]), len(prov_zh.get("models", [])))
            html_parts.append(
                f'<div class="provider{state_class}">'
                f'<button class="provider-head" type="button" onclick="toggleProvider(this)">'
                f'<span class="provider-name"><span class="lang-en">{esc(prov_en["name"])}</span>'
                f'<span class="lang-zh">{esc(prov_zh["name"])}</span></span>'
                f'<span class="provider-count">{model_count} models</span><span class="provider-arr">{icon("chevron")}</span></button>'
                f'<div class="provider-body{state_class}">'
            )
            html_parts.append('<div class="lang-en"><div class="model-grid">')
            for model in prov_en["models"]:
                href = f' href="{esc(model["url"])}" target="_blank" rel="noopener"' if model["url"] else ""
                html_parts.append(
                    f'<a class="model-card"{href}><strong>{esc(model["name"])}</strong><span>{inline_md(model["desc"])}</span></a>'
                )
            html_parts.append("</div></div>")
            html_parts.append('<div class="lang-zh"><div class="model-grid">')
            for model in prov_zh.get("models", []):
                href = f' href="{esc(model["url"])}" target="_blank" rel="noopener"' if model["url"] else ""
                html_parts.append(
                    f'<a class="model-card"{href}><strong>{esc(model["name"])}</strong><span>{inline_md(model["desc"])}</span></a>'
                )
            html_parts.append("</div></div></div></div>")
        html_parts.append("</section>")
    return "".join(html_parts)


def render_markdown_list(text: str) -> str:
    html_parts: list[str] = []
    in_ul = False
    for raw in text.splitlines():
        t = raw.strip()
        if not t:
            if in_ul:
                html_parts.append("</ul>")
                in_ul = False
            continue
        if t == "---":
            if in_ul:
                html_parts.append("</ul>")
                in_ul = False
            html_parts.append('<hr class="md-hr">')
            continue
        if t.startswith(">"):
            if in_ul:
                html_parts.append("</ul>")
                in_ul = False
            html_parts.append(f"<blockquote>{inline_md(t[1:].strip())}</blockquote>")
            continue
        if t.startswith("- "):
            if not in_ul:
                html_parts.append('<ul class="repo-list">')
                in_ul = True
            html_parts.append(repo_card(t[2:]))
            continue
        if not t.startswith("#### ") and not t.startswith("**"):
            if in_ul:
                html_parts.append("</ul>")
                in_ul = False
            html_parts.append(f'<p class="md-p">{inline_md(t)}</p>')
    if in_ul:
        html_parts.append("</ul>")
    return "".join(html_parts)


def render_topic_body(item_en: dict, item_zh: dict | None, open_first: bool) -> str:
    content_en = item_en.get("content", "")
    content_zh = item_zh.get("content", "") if item_zh else ""
    if item_en.get("type") == "text" and "Large Language Models" in item_en.get("title", ""):
        return render_provider_accordions(content_en, content_zh, open_first=True)
    return f'<div class="lang-en">{render_markdown_list(content_en)}</div><div class="lang-zh">{render_markdown_list(content_zh)}</div>'


def render_layer_content(sec_en: dict, sec_zh: dict | None) -> str:
    parts: list[str] = []
    zh_items = sec_zh.get("items", []) if sec_zh else []
    for i, item_en in enumerate(sec_en.get("items", [])):
        item_zh = zh_items[i] if i < len(zh_items) else None
        title_en = item_en["title"]
        title_zh = item_zh["title"] if item_zh else title_en
        count = count_repo_items(item_en.get("content", ""))
        if item_en.get("type") == "text" and "Large Language Models" in title_en:
            _, groups = parse_provider_content(item_en.get("content", ""))
            count_label = f"{sum(len(g['providers']) for g in groups)} providers"
        else:
            count_label = f"{count} repos"
        open_class = " open" if i == 0 else ""
        parts.append(
            f'<section class="sub{open_class}">'
            f'<button class="sub-head{open_class}" type="button" onclick="toggleSub(this)">'
            f'<span class="sub-icon">{icon("repo")}</span>'
            f'<span class="sub-name"><span class="lang-en">{inline_md(title_en)}</span>'
            f'<span class="lang-zh">{inline_md(title_zh)}</span></span>'
            f'<span class="sub-cnt">{esc(count_label)}</span><span class="sub-arr">{icon("chevron")}</span></button>'
            f'<div class="sub-body{open_class}">{render_topic_body(item_en, item_zh, i == 0)}</div>'
            "</section>"
        )
    return "".join(parts)


def layer_stats(sec: dict | None) -> dict:
    if not sec:
        return {"topics": 0, "repos": 0}
    topics = sum(1 for item in sec.get("items", []) if item.get("type") == "details")
    repos = sum(count_repo_items(item.get("content", "")) for item in sec.get("items", []) if item.get("type") == "details")
    return {"topics": topics, "repos": repos}


def build_repo_index(layers_en: list[dict], layers_zh: list[dict]) -> list[dict]:
    index: list[dict] = []
    for layer_i, sec_en in enumerate(layers_en):
        sec_zh = layers_zh[layer_i] if layer_i < len(layers_zh) else None
        zh_items = sec_zh.get("items", []) if sec_zh else []
        for item_i, item_en in enumerate(sec_en.get("items", [])):
            if item_en.get("type") != "details":
                continue
            item_zh = zh_items[item_i] if item_i < len(zh_items) else None
            zh_lines = item_zh.get("content", "").splitlines() if item_zh else []
            en_repo_lines = [line[2:] for line in item_en.get("content", "").splitlines() if line.startswith("- ")]
            zh_repo_lines = [line[2:] for line in zh_lines if line.startswith("- ")]
            for repo_i, line in enumerate(en_repo_lines):
                repo = parse_repo(line)
                if not repo:
                    continue
                zh_repo = parse_repo(zh_repo_lines[repo_i]) if repo_i < len(zh_repo_lines) else None
                index.append(
                    {
                        "name": repo["name"],
                        "url": repo["url"],
                        "desc": repo["desc"],
                        "descZh": zh_repo["desc"] if zh_repo else repo["desc"],
                        "tags": [TAG_SLUGS[t] for t in repo["tags"]],
                        "tagLabels": repo["tags"],
                        "layer": LAYER_META[layer_i]["en"],
                        "layerZh": LAYER_META[layer_i]["zh"],
                        "topic": item_en["title"],
                        "topicZh": item_zh["title"] if item_zh else item_en["title"],
                        "href": f"layer-{layer_i + 1:02d}.html",
                    }
                )
    return index


def nav() -> str:
    return f"""
<nav class="nav">
  <div class="nav-inner">
    <a href="index.html" class="nav-brand">Awesome Agent <i>Hierarchy</i></a>
    <div class="nav-actions">
      <a href="{REPO_URL}/blob/main/CONTRIBUTING.md" class="nav-link" target="_blank" rel="noopener">Submit a Repo</a>
      <div class="lang-group">
        <button class="active" onclick="setLang('en')">EN</button>
        <button onclick="setLang('zh')">中文</button>
      </div>
      <a href="{REPO_URL}" class="nav-gh" target="_blank" rel="noopener">GitHub ^</a>
    </div>
  </div>
</nav>"""


def page_shell(title: str, body: str, description: str = SITE_DESCRIPTION) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="{esc(FRAMEWORK_IMAGE)}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="style.css">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Serif+Display:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
</head>
<body>
{body}
</body>
</html>"""


def tag_filter_html(onclick: str = "setTag") -> str:
    buttons = [f'<button class="active" data-tag="all" onclick="{onclick}(\'all\')">All</button>']
    for tag in TAGS:
        slug = TAG_SLUGS[tag]
        buttons.append(f'<button data-tag="{esc(slug)}" onclick="{onclick}(\'{esc(slug)}\')">{esc(tag)}</button>')
    return f'<div class="tag-filter">{"".join(buttons)}</div>'


def common_script(repo_index: list[dict] | None = None) -> str:
    index_json = json.dumps(repo_index or [], ensure_ascii=False)
    tag_slugs_json = json.dumps(["all", *[TAG_SLUGS[t] for t in TAGS]])
    return f"""
<script>
const REPO_INDEX = {index_json};
const KNOWN_TAGS = {tag_slugs_json};
let activeTag = 'all';
let homeTag = 'all';

function setLang(l) {{
  const btns = document.querySelectorAll('.lang-group button');
  btns.forEach(b => b.classList.remove('active'));
  btns[l === 'en' ? 0 : 1].classList.add('active');
  document.body.classList.toggle('lang-zh-active', l === 'zh');
  document.documentElement.lang = l === 'zh' ? 'zh' : 'en';
  const input = document.getElementById('search') || document.getElementById('home-search');
  if (input) input.placeholder = l === 'zh' ? '搜索仓库、主题或标签...' : 'Search repositories, topics, or tags...';
  localStorage.setItem('lang', l);
  renderHomeSearch();
}}
function toggleSub(el) {{
  el.classList.toggle('open');
  el.nextElementSibling.classList.toggle('open');
}}
function expandAllTopics() {{
  document.querySelectorAll('.sub-head,.sub-body,.sub').forEach(el => el.classList.add('open'));
}}
function collapseAllTopics() {{
  document.querySelectorAll('.sub-head,.sub-body,.sub').forEach(el => el.classList.remove('open'));
}}
function toggleProvider(el) {{
  const provider = el.closest('.provider');
  provider.classList.toggle('open');
  el.nextElementSibling.classList.toggle('open');
}}
function setProviders(el, open) {{
  const root = el.closest('.sub-body') || document;
  root.querySelectorAll('.provider').forEach(p => p.classList.toggle('open', open));
  root.querySelectorAll('.provider-body').forEach(p => p.classList.toggle('open', open));
}}
function setTag(tag) {{
  activeTag = KNOWN_TAGS.includes(tag) ? tag : 'all';
  document.querySelectorAll('.search-area .tag-filter button').forEach(btn => {{
    btn.classList.toggle('active', btn.dataset.tag === activeTag);
  }});
  applyFilters();
}}
function applyFilters() {{
  const input = document.getElementById('search');
  const q = input ? input.value.toLowerCase().trim() : '';
  document.querySelectorAll('.repo-card').forEach(li => {{
    const textMatch = !q || li.textContent.toLowerCase().includes(q);
    const tags = (li.dataset.tags || '').split(' ').filter(Boolean);
    const tagMatch = activeTag === 'all' || tags.includes(activeTag);
    li.hidden = !(textMatch && tagMatch);
  }});
  document.querySelectorAll('.sub').forEach(sub => {{
    const repos = Array.from(sub.querySelectorAll('.repo-card'));
    sub.hidden = repos.length > 0 && repos.every(li => li.hidden);
  }});
}}
function handleSearch() {{
  applyFilters();
}}
function setHomeTag(tag) {{
  homeTag = KNOWN_TAGS.includes(tag) ? tag : 'all';
  document.querySelectorAll('.global-search .tag-filter button').forEach(btn => {{
    btn.classList.toggle('active', btn.dataset.tag === homeTag);
  }});
  renderHomeSearch();
}}
function renderHomeSearch() {{
  const box = document.getElementById('home-search');
  const target = document.getElementById('home-results');
  if (!box || !target || !REPO_INDEX.length) return;
  const q = box.value.toLowerCase().trim();
  const isZh = document.body.classList.contains('lang-zh-active');
  const matches = REPO_INDEX.filter(repo => {{
    const tagMatch = homeTag === 'all' || repo.tags.includes(homeTag);
    const hay = [repo.name, repo.desc, repo.descZh, repo.layer, repo.layerZh, repo.topic, repo.topicZh, repo.tagLabels.join(' ')].join(' ').toLowerCase();
    return tagMatch && (!q || hay.includes(q));
  }}).slice(0, 24);
  if (!q && homeTag === 'all') {{
    target.innerHTML = '<p class="empty-results">Type a query or choose a tag to search across all repositories.</p>';
    return;
  }}
  if (!matches.length) {{
    target.innerHTML = '<p class="empty-results">No matching repositories found.</p>';
    return;
  }}
  target.innerHTML = matches.map(repo => `
    <a class="result-card" href="${{repo.href}}">
      <span class="result-layer">${{isZh ? repo.layerZh : repo.layer}}</span>
      <strong>${{repo.name}}</strong>
      <p>${{isZh ? repo.descZh : repo.desc}}</p>
      <span class="result-tags">${{repo.tagLabels.map(t => `<em>${{t}}</em>`).join('')}}</span>
    </a>
  `).join('');
}}
const saved = localStorage.getItem('lang');
if (saved === 'zh') setLang('zh');
renderHomeSearch();
window.addEventListener('scroll', () => {{
  const btt = document.getElementById('btt');
  if (btt) btt.classList.toggle('show', window.scrollY > 300);
}});
</script>"""


def gen_index(layers_en: list[dict], layers_zh: list[dict], repo_index: list[dict]) -> str:
    total_topics = sum(layer_stats(sec)["topics"] for sec in layers_en)
    total_repos = sum(layer_stats(sec)["repos"] for sec in layers_en)
    cards: list[str] = []
    for i, meta in enumerate(LAYER_META):
        stats = layer_stats(layers_en[i] if i < len(layers_en) else None)
        chip_en = "".join(f"<span>{esc(chip)}</span>" for chip in meta["chips_en"])
        chip_zh = "".join(f"<span>{esc(chip)}</span>" for chip in meta["chips_zh"])
        support = " support-layer" if meta["support"] else ""
        cards.append(
            f"""
    <a class="layer-card rich-card{support}" style="--layer-color:{meta['color']}" href="layer-{meta['idx']}.html">
      <div class="layer-card-top">
        <span class="layer-icon">{icon(meta['icon'])}</span>
        <span class="layer-card-idx">{meta['idx']}</span>
      </div>
      <div class="layer-card-title"><span class="lang-en">{esc(meta['en'])}</span><span class="lang-zh">{esc(meta['zh'])}</span></div>
      <div class="layer-card-desc"><span class="lang-en">{esc(meta['desc_en'])}</span><span class="lang-zh">{esc(meta['desc_zh'])}</span></div>
      <div class="chip-row"><span class="lang-en">{chip_en}</span><span class="lang-zh">{chip_zh}</span></div>
      <div class="card-stats">{stats['topics']} topics · {stats['repos']} repos</div>
    </a>"""
        )
    body = nav() + f"""
<section class="hero home-hero">
  <div class="hero-copy">
    <p class="eyebrow">Curated AI agent ecosystem</p>
    <h1><span class="lang-en">Awesome Agent Hierarchy</span><span class="lang-zh">Awesome Agent Hierarchy</span></h1>
    <p><span class="lang-en">A tagged architecture map for exploring agent frameworks, tools, workflows, infrastructure, observability, and security.</span><span class="lang-zh">一张带标签的 AI Agent 架构地图，用于探索框架、工具、工作流、基础设施、可观测性和安全能力。</span></p>
  </div>
  <img class="framework-hero" src="{FRAMEWORK_IMAGE}" alt="Awesome Agent Hierarchy ecosystem framework" loading="eager">
</section>
<section class="stats-row" aria-label="Site statistics">
  <div><strong>8</strong><span>Layers</span></div>
  <div><strong>{total_topics}</strong><span>Topics</span></div>
  <div><strong>{total_repos}</strong><span>Repos</span></div>
  <div><strong>{len(TAGS)}</strong><span>Tags</span></div>
</section>
<section class="global-search">
  <div class="section-head">
    <h2>Explore the map</h2>
    <a href="{REPO_URL}/blob/main/CONTRIBUTING.md" target="_blank" rel="noopener">Submit a Repo</a>
  </div>
  <input id="home-search" type="text" placeholder="Search repositories, topics, or tags..." oninput="renderHomeSearch()">
  {tag_filter_html("setHomeTag")}
  <div id="home-results" class="home-results"></div>
</section>
<section class="layer-grid">
{''.join(cards)}
</section>
<button class="btt" id="btt" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">^</button>
<footer class="foot"><span class="lang-en">Content from </span><span class="lang-zh">内容来自 </span>README.md / README-zh.md</footer>
{common_script(repo_index)}
"""
    return page_shell("Awesome Agent Hierarchy", body)


def gen_layer(idx: int, sec_en: dict, sec_zh: dict | None, repo_index: list[dict]) -> str:
    meta = LAYER_META[idx - 1]
    stats = layer_stats(sec_en)
    nav_en = []
    nav_zh = []
    for layer_meta in LAYER_META:
        active = ' class="active"' if layer_meta["idx"] == meta["idx"] else ""
        nav_en.append(f'<a href="layer-{layer_meta["idx"]}.html"{active}>{esc(layer_meta["en"])}</a>')
        nav_zh.append(f'<a href="layer-{layer_meta["idx"]}.html"{active}>{esc(layer_meta["zh"])}</a>')
    body = nav() + f"""
<div class="breadcrumb">
  <a href="index.html"><span class="lang-en">All Layers</span><span class="lang-zh">所有层级</span></a>
  <span>/</span>
  <span class="lang-en">{esc(meta['en'])}</span><span class="lang-zh">{esc(meta['zh'])}</span>
</div>
<section class="layer-hero" style="--layer-color:{meta['color']}">
  <span class="layer-hero-icon">{icon(meta['icon'])}</span>
  <div>
    <p class="eyebrow">{meta['idx']} Layer</p>
    <h1><span class="lang-en">{esc(meta['en'])}</span><span class="lang-zh">{esc(meta['zh'])}</span></h1>
    <p><span class="lang-en">{esc(meta['desc_en'])}</span><span class="lang-zh">{esc(meta['desc_zh'])}</span></p>
  </div>
  <div class="layer-hero-stats">
    <span><strong>{stats['topics']}</strong> topics</span>
    <span><strong>{stats['repos']}</strong> repos</span>
  </div>
</section>
<div class="search-area">
  <input id="search" type="text" placeholder="Search repositories, topics, or tags..." oninput="handleSearch()">
  {tag_filter_html("setTag")}
  <div class="topic-actions">
    <button onclick="expandAllTopics()">Expand all</button>
    <button onclick="collapseAllTopics()">Collapse all</button>
  </div>
</div>
<main class="main-area">
{render_layer_content(sec_en, sec_zh)}
</main>
<div class="layer-nav">
  <div class="lang-en">{' <span>|</span> '.join(nav_en)}</div>
  <div class="lang-zh">{' <span>|</span> '.join(nav_zh)}</div>
</div>
<button class="btt" id="btt" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">^</button>
<footer class="foot"><span class="lang-en">Content from </span><span class="lang-zh">内容来自 </span>README.md / README-zh.md</footer>
{common_script(repo_index)}
"""
    return page_shell(f"{meta['idx']}. {meta['en']} - {SITE_TITLE}", body, f"{meta['en']}: {meta['desc_en']}")


def main() -> None:
    base = Path(__file__).resolve().parent
    docs_dir = base / "docs"
    docs_dir.mkdir(exist_ok=True)

    sections_en = parse_readme((base / "README.md").read_text(encoding="utf-8"))
    sections_zh = parse_readme((base / "README-zh.md").read_text(encoding="utf-8"))
    layers_en = get_layer_sections(sections_en)
    layers_zh = get_layer_sections(sections_zh)
    repo_index = build_repo_index(layers_en, layers_zh)

    (docs_dir / "index.html").write_text(gen_index(layers_en, layers_zh, repo_index), encoding="utf-8")
    for i in range(1, 9):
        sec_en = layers_en[i - 1]
        sec_zh = layers_zh[i - 1] if i - 1 < len(layers_zh) else None
        (docs_dir / f"layer-{i:02d}.html").write_text(gen_layer(i, sec_en, sec_zh, repo_index), encoding="utf-8")
    print(f"Generated {1 + 8} files in {docs_dir}")


if __name__ == "__main__":
    main()
