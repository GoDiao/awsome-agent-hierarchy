"""
Generate static HTML pages from README.md and README-zh.md.

Run:
    python generate.py
"""
from __future__ import annotations

import html
import os
import re
from pathlib import Path


SECTIONS_EN = [
    ("01", "Foundation Layer", "LLMs, Prompt Engineering, Context"),
    ("02", "Agent Brain", "Planning, Reasoning, Decision Engine"),
    ("03", "Tool Layer", "Search, Browser, Code, API, DB, Files"),
    ("04", "Agent Workflows", "Research, Coding, Sales, Support, Content"),
    ("05", "Multi-Agent Systems", "Manager, Worker, Reviewer, Specialist, Memory"),
    ("06", "Infrastructure", "LangGraph, CrewAI, OpenAI SDK, MCP, Docker, K8s"),
    ("07", "Observability", "Logging, Tracing, Eval, Hallucination, Cost"),
    ("08", "Security", "Sandbox, Permission, Keys, Guardrails, HITL"),
]

SECTIONS_ZH = [
    ("01", "\u57fa\u7840\u5c42", "\u5927\u8bed\u8a00\u6a21\u578b\u3001\u63d0\u793a\u5de5\u7a0b\u3001\u4e0a\u4e0b\u6587"),
    ("02", "\u4ee3\u7406\u5927\u8111", "\u89c4\u5212\u3001\u63a8\u7406\u3001\u51b3\u7b56\u5f15\u64ce"),
    ("03", "\u5de5\u5177\u5c42", "\u641c\u7d22\u3001\u6d4f\u89c8\u5668\u3001\u4ee3\u7801\u3001API\u3001\u6570\u636e\u5e93\u3001\u6587\u4ef6"),
    ("04", "\u4ee3\u7406\u5de5\u4f5c\u6d41", "\u7814\u7a76\u3001\u7f16\u7801\u3001\u9500\u552e\u3001\u5ba2\u670d\u3001\u5185\u5bb9"),
    ("05", "\u591a\u4ee3\u7406\u7cfb\u7edf", "\u7ba1\u7406\u3001\u5de5\u4f5c\u8005\u3001\u5ba1\u67e5\u3001\u4e13\u5bb6\u3001\u8bb0\u5fc6"),
    ("06", "\u57fa\u7840\u8bbe\u65bd", "LangGraph\u3001CrewAI\u3001OpenAI SDK\u3001MCP\u3001Docker\u3001K8s"),
    ("07", "\u53ef\u89c2\u6d4b\u6027", "\u65e5\u5fd7\u3001\u8ffd\u8e2a\u3001\u8bc4\u4f30\u3001\u5e7b\u89c9\u3001\u6210\u672c"),
    ("08", "\u5b89\u5168\u5c42", "\u6c99\u7bb1\u3001\u6743\u9650\u3001\u5bc6\u94a5\u3001\u62a4\u680f\u3001\u4eba\u5de5\u5ba1\u6279"),
]

TAGS = ["Official", "Framework", "Example", "Research", "Infra", "Archived Classic"]
TAG_RE = re.compile(r"`(" + "|".join(re.escape(t) for t in TAGS) + r")`")
TAG_SLUGS = {tag: tag.lower().replace(" ", "-") for tag in TAGS}


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
            if content:
                h2["items"].append({"title": h3, "content": content, "type": "text"})
        buf = []

    for line in text.splitlines():
        if re.match(r"^## (Contents|\u76ee\u5f55|Contributing|\u8d21\u732e|License|\u8bb8\u53ef)", line):
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


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def inline_md(text: str) -> str:
    text = esc(text)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1" loading="lazy">', text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def split_repo_tags(markdown: str) -> tuple[str, list[str]]:
    tags = TAG_RE.findall(markdown)
    without = TAG_RE.sub("", markdown)
    without = re.sub(r"\s{2,}", " ", without).strip()
    return without, tags


def render_tags(tags: list[str]) -> str:
    if not tags:
        return ""
    spans = []
    for tag in tags:
        cls = TAG_SLUGS[tag]
        spans.append(f'<span class="tag tag-{cls}">{esc(tag)}</span>')
    return f'<span class="tags">{"".join(spans)}</span>'


def render_li(markdown: str) -> str:
    content, tags = split_repo_tags(markdown)
    tag_attr = esc(" ".join(TAG_SLUGS[tag] for tag in tags))
    tag_html = render_tags(tags)
    body = inline_md(content)
    if tag_html and " - " in body:
        head, tail = body.split(" - ", 1)
        body = f"{head} {tag_html} - {tail}"
    elif tag_html:
        body = f"{body} {tag_html}"
    return f'<li data-tags="{tag_attr}">{body}</li>'


def render_list(text: str) -> str:
    lines = text.splitlines()
    html_parts: list[str] = []
    in_ul = False
    in_prov = False
    prov_parts: list[str] = []

    def close_ul() -> None:
        nonlocal in_ul
        if in_ul:
            html_parts.append("</ul>")
            in_ul = False

    def close_provider() -> None:
        nonlocal in_prov, prov_parts
        if in_prov:
            prov_parts.append("</ul></div>")
            html_parts.append("".join(prov_parts))
            prov_parts = []
            in_prov = False

    for raw in lines:
        t = raw.strip()
        if not t:
            close_ul()
            close_provider()
            continue
        if t == "---":
            close_ul()
            close_provider()
            html_parts.append('<hr class="md-hr">')
            continue
        if t.startswith(">"):
            close_ul()
            close_provider()
            html_parts.append(f"<blockquote>{inline_md(t[1:].strip())}</blockquote>")
            continue
        if t.startswith("#### "):
            close_ul()
            close_provider()
            name = inline_md(t[5:])
            prov_parts = [f'<div class="prov"><div class="prov-name">{name}</div><ul>']
            in_prov = True
            continue
        if re.match(r"^\*\*[^*]+\*\*$", t) and not t.startswith("-"):
            close_ul()
            close_provider()
            name = inline_md(t.replace("**", ""))
            prov_parts = [f'<div class="prov"><div class="prov-name">{name}</div><ul>']
            in_prov = True
            continue
        if in_prov and t.startswith("- "):
            prov_parts.append(f"<li>{inline_md(t[2:])}</li>")
            continue
        if t.startswith("- "):
            close_provider()
            if not in_ul:
                html_parts.append('<ul class="rl">')
                in_ul = True
            html_parts.append(render_li(t[2:]))
            continue
        close_ul()
        close_provider()
        if not t.startswith("**"):
            html_parts.append(f'<p class="md-p">{inline_md(t)}</p>')

    close_ul()
    close_provider()
    return "".join(html_parts)


def count_repo_items(content: str) -> int:
    return len(re.findall(r"^- \[[^\]]+\]\(https://github\.com/", content, re.M))


def render_section_bilingual(sec_en: dict | None, sec_zh: dict | None) -> str:
    zh_items = sec_zh.get("items", []) if sec_zh else []
    en_items = sec_en.get("items", []) if sec_en else []
    html_parts: list[str] = []

    for i in range(max(len(en_items), len(zh_items))):
        item_en = en_items[i] if i < len(en_items) else None
        item_zh = zh_items[i] if i < len(zh_items) else None
        item = item_en or item_zh
        if not item:
            continue
        if item.get("type") == "details":
            title_en = item_en["title"] if item_en else item_zh["title"]
            title_zh = item_zh["title"] if item_zh else item_en["title"]
            content_en = item_en["content"] if item_en else ""
            content_zh = item_zh["content"] if item_zh else ""
            cnt = max(count_repo_items(content_en), count_repo_items(content_zh))
            html_parts.append(
                '<div class="sub">'
                '<button class="sub-head" type="button" onclick="toggleSub(this)">'
                f'<span class="sub-name"><span class="lang-en">{inline_md(title_en)}</span>'
                f'<span class="lang-zh">{inline_md(title_zh)}</span></span>'
                f'<span class="sub-cnt">{cnt}</span><span class="sub-arr">></span></button>'
                '<div class="sub-body">'
                f'<div class="lang-en">{render_list(content_en)}</div>'
                f'<div class="lang-zh">{render_list(content_zh)}</div>'
                "</div></div>"
            )
        else:
            content_en = item_en["content"] if item_en else ""
            content_zh = item_zh["content"] if item_zh else ""
            html_parts.append(f'<div class="lang-en">{render_list(content_en)}</div>')
            html_parts.append(f'<div class="lang-zh">{render_list(content_zh)}</div>')
    return "".join(html_parts)


def get_layer_sections(sections: list[dict]) -> list[dict]:
    skip = ["contributing", "\u8d21\u732e", "license", "\u8bb8\u53ef", "contents", "\u76ee\u5f55"]
    return [s for s in sections if not any(k in s["title"].lower() for k in skip)]


def page_shell(title: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<link rel="stylesheet" href="style.css">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Serif+Display:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
</head>
<body>
{body}
</body>
</html>"""


def nav() -> str:
    return """
<nav class="nav">
  <div class="nav-inner">
    <a href="index.html" class="nav-brand">Awesome Agent <i>Hierarchy</i></a>
    <div class="nav-actions">
      <div class="lang-group">
        <button class="active" onclick="setLang('en')">EN</button>
        <button onclick="setLang('zh')">\u4e2d\u6587</button>
      </div>
      <a href="https://github.com/tianX-ai/awsome-agent-hierarchy" class="nav-gh" target="_blank" rel="noopener">GitHub ^</a>
    </div>
  </div>
</nav>"""


def common_script(with_search: bool = False) -> str:
    search_js = ""
    if with_search:
        tag_buttons = ",".join(repr(TAG_SLUGS[t]) for t in TAGS)
        search_js = f"""
let activeTag = 'all';
const knownTags = ['all', {tag_buttons}];
function setTag(tag) {{
  activeTag = knownTags.includes(tag) ? tag : 'all';
  document.querySelectorAll('.tag-filter button').forEach(btn => {{
    btn.classList.toggle('active', btn.dataset.tag === activeTag);
  }});
  applyFilters();
}}
function applyFilters() {{
  const input = document.getElementById('search');
  const q = input ? input.value.toLowerCase().trim() : '';
  document.querySelectorAll('ul.rl li').forEach(li => {{
    const textMatch = !q || li.textContent.toLowerCase().includes(q);
    const tags = (li.dataset.tags || '').split(' ').filter(Boolean);
    const tagMatch = activeTag === 'all' || tags.includes(activeTag);
    li.hidden = !(textMatch && tagMatch);
  }});
  document.querySelectorAll('.sub').forEach(sub => {{
    const items = Array.from(sub.querySelectorAll('ul.rl li'));
    sub.hidden = items.length > 0 && items.every(li => li.hidden);
  }});
}}
function handleSearch() {{
  applyFilters();
}}
"""
    return f"""
<script>
function setLang(l) {{
  const btns = document.querySelectorAll('.lang-group button');
  btns.forEach(b => b.classList.remove('active'));
  btns[l === 'en' ? 0 : 1].classList.add('active');
  document.body.classList.toggle('lang-zh-active', l === 'zh');
  document.documentElement.lang = l === 'zh' ? 'zh' : 'en';
  const input = document.getElementById('search');
  if (input) input.placeholder = l === 'zh' ? '\u641c\u7d22\u4ed3\u5e93...' : 'Search repositories...';
  localStorage.setItem('lang', l);
}}
function toggleSub(el) {{
  el.classList.toggle('open');
  el.nextElementSibling.classList.toggle('open');
}}
{search_js}
const saved = localStorage.getItem('lang');
if (saved === 'zh') setLang('zh');
window.addEventListener('scroll', () => {{
  const btt = document.getElementById('btt');
  if (btt) btt.classList.toggle('show', window.scrollY > 300);
}});
</script>"""


def gen_index() -> str:
    cards = []
    for i, (se, sz) in enumerate(zip(SECTIONS_EN, SECTIONS_ZH), 1):
        idx = f"{i:02d}"
        cards.append(f"""
    <a class="layer-card" href="layer-{idx}.html">
      <div class="layer-card-idx">{idx}</div>
      <div class="layer-card-title"><span class="lang-en">{esc(se[1])}</span><span class="lang-zh">{esc(sz[1])}</span></div>
      <div class="layer-card-desc"><span class="lang-en">{esc(se[2])}</span><span class="lang-zh">{esc(sz[2])}</span></div>
    </a>""")
    body = nav() + f"""
<section class="hero">
  <h1><span class="lang-en">The AI Agent Stack</span><span class="lang-zh">AI \u4ee3\u7406\u6280\u672f\u6808</span></h1>
  <p><span class="lang-en">A curated, tagged map of tools, libraries, and frameworks for building AI agent systems.</span><span class="lang-zh">AI Agent \u7cfb\u7edf\u6784\u5efa\u5de5\u5177\u3001\u5e93\u548c\u6846\u67b6\u7684\u7cbe\u9009\u6807\u7b7e\u5730\u56fe\u3002</span></p>
  <hr class="hero-rule">
</section>
<div class="layer-grid">
{''.join(cards)}
</div>
<button class="btt" id="btt" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">^</button>
<footer class="foot"><span class="lang-en">Content from </span><span class="lang-zh">\u5185\u5bb9\u6765\u81ea </span>README.md / README-zh.md</footer>
{common_script()}
"""
    return page_shell("Awesome AI Agent Hierarchy", body)


def tag_filter_html() -> str:
    buttons = ['<button class="active" data-tag="all" onclick="setTag(\'all\')">All</button>']
    for tag in TAGS:
        slug = TAG_SLUGS[tag]
        buttons.append(f'<button data-tag="{esc(slug)}" onclick="setTag(\'{esc(slug)}\')">{esc(tag)}</button>')
    return f'<div class="tag-filter">{"".join(buttons)}</div>'


def gen_layer(idx: int, sec_en: dict | None, sec_zh: dict | None) -> str:
    se = SECTIONS_EN[idx - 1]
    sz = SECTIONS_ZH[idx - 1]
    idx_str = f"{idx:02d}"
    content = render_section_bilingual(sec_en, sec_zh)
    nav_en = []
    nav_zh = []
    for i, (en, zh) in enumerate(zip(SECTIONS_EN, SECTIONS_ZH), 1):
        active = ' class="active"' if i == idx else ""
        nav_en.append(f'<a href="layer-{i:02d}.html"{active}>{esc(en[1])}</a>')
        nav_zh.append(f'<a href="layer-{i:02d}.html"{active}>{esc(zh[1])}</a>')
    body = nav() + f"""
<div class="breadcrumb">
  <a href="index.html"><span class="lang-en">All Layers</span><span class="lang-zh">\u6240\u6709\u5c42\u7ea7</span></a>
  <span>/</span>
  <span class="lang-en">{esc(se[1])}</span><span class="lang-zh">{esc(sz[1])}</span>
</div>
<section class="hero">
  <h1><span class="lang-en">{esc(se[1])}</span><span class="lang-zh">{esc(sz[1])}</span></h1>
  <p><span class="lang-en">{esc(se[2])}</span><span class="lang-zh">{esc(sz[2])}</span></p>
  <hr class="hero-rule">
</section>
<div class="search-area">
  <input id="search" type="text" placeholder="Search repositories..." oninput="handleSearch()">
  {tag_filter_html()}
</div>
<main class="main-area">
{content}
</main>
<div class="layer-nav">
  <div class="lang-en">{' <span>|</span> '.join(nav_en)}</div>
  <div class="lang-zh">{' <span>|</span> '.join(nav_zh)}</div>
</div>
<button class="btt" id="btt" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">^</button>
<footer class="foot"><span class="lang-en">Content from </span><span class="lang-zh">\u5185\u5bb9\u6765\u81ea </span>README.md / README-zh.md</footer>
{common_script(with_search=True)}
"""
    return page_shell(f"{idx_str}. {se[1]} - Awesome AI Agent Hierarchy", body)


def main() -> None:
    base = Path(__file__).resolve().parent
    docs_dir = base / "docs"
    docs_dir.mkdir(exist_ok=True)

    sections_en = parse_readme((base / "README.md").read_text(encoding="utf-8"))
    sections_zh = parse_readme((base / "README-zh.md").read_text(encoding="utf-8"))
    layers_en = get_layer_sections(sections_en)
    layers_zh = get_layer_sections(sections_zh)

    (docs_dir / "index.html").write_text(gen_index(), encoding="utf-8")
    for i in range(1, 9):
        sec_en = layers_en[i - 1] if i - 1 < len(layers_en) else None
        sec_zh = layers_zh[i - 1] if i - 1 < len(layers_zh) else None
        (docs_dir / f"layer-{i:02d}.html").write_text(gen_layer(i, sec_en, sec_zh), encoding="utf-8")
    print(f"Generated {1 + 8} files in {docs_dir}")


if __name__ == "__main__":
    main()
