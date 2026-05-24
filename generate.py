"""
Generate static HTML pages from README.md and README-zh.md.
Run: python generate.py
"""
import re
import os

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
    ("01", "基础层", "大语言模型、提示工程、上下文"),
    ("02", "代理大脑", "规划、推理、决策引擎"),
    ("03", "工具层", "搜索、浏览器、代码、API、数据库、文件"),
    ("04", "代理工作流", "研究、编码、销售、客服、内容"),
    ("05", "多代理系统", "管理、工作者、审查、专家、内存"),
    ("06", "基础设施", "LangGraph、CrewAI、OpenAI SDK、MCP、Docker、K8s"),
    ("07", "可观测性", "日志、追踪、评估、幻觉、成本"),
    ("08", "安全层", "沙箱、权限、密钥、护栏、人工审批"),
]


def parse_readme(text):
    """Parse README into structured sections. Returns list of (h2_title, items)."""
    sections = []
    lines = text.split('\n')
    h2 = None
    h3 = None
    buf = []
    in_details = False
    det_buf = []
    det_title = ''

    def flush():
        nonlocal buf
        if h3 and buf:
            t = '\n'.join(buf).strip()
            if t and h2:
                h2['items'].append({'title': h3, 'content': t, 'type': 'text'})
        buf = []

    for line in lines:
        # Skip TOC and Contributing
        if re.match(r'^## (Contents|目录|Contributing|贡献)', line):
            flush()
            h2 = None
            continue

        if re.match(r'^## ', line):
            flush()
            h3 = None
            h2 = {'title': line.replace('## ', '').strip(), 'items': []}
            sections.append(h2)
            continue

        if re.match(r'^### ', line):
            flush()
            h3 = line.replace('### ', '').strip()
            continue

        if re.match(r'<details>', line, re.I):
            in_details = True
            det_buf = []
            continue

        if in_details and re.match(r'<summary>', line, re.I):
            det_title = re.sub(r'<[^>]+>', '', line).strip()
            continue

        if re.match(r'</details>', line, re.I):
            in_details = False
            t = '\n'.join(det_buf).strip()
            if h2 and t:
                h2['items'].append({'title': det_title, 'content': t, 'type': 'details'})
            continue

        if in_details:
            det_buf.append(line)
        else:
            buf.append(line)

    flush()
    return sections


def inline_md(text):
    """Convert inline markdown to HTML."""
    # Images: ![alt](url)
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1" loading="lazy">', text)
    # Links: [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    # Bold
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    # Code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text


def render_list(text):
    """Render markdown list content to HTML."""
    lines = text.split('\n')
    html = ''
    in_ul = False
    in_prov = False
    prov_html = ''

    for line in lines:
        t = line.strip()

        if not t:
            if in_ul:
                html += '</ul>'
                in_ul = False
            if in_prov:
                prov_html += '</ul></div>'
                html += prov_html
                prov_html = ''
                in_prov = False
            continue

        # Blockquote
        if t.startswith('>'):
            if in_ul:
                html += '</ul>'
                in_ul = False
            html += f'<blockquote>{inline_md(t[1:].strip())}</blockquote>'
            continue

        # H4 provider name
        if t.startswith('#### '):
            if in_ul:
                html += '</ul>'
                in_ul = False
            if in_prov:
                prov_html += '</ul></div>'
                html += prov_html
            name = inline_md(t[5:])
            prov_html = f'<div class="prov"><div class="prov-name">{name}</div><ul>'
            in_prov = True
            continue

        # Inside provider
        if in_prov and t.startswith('-'):
            prov_html += f'<li>{inline_md(t[2:])}</li>'
            continue

        if in_prov and not t.startswith('-'):
            prov_html += '</ul></div>'
            html += prov_html
            prov_html = ''
            in_prov = False

        # Bold standalone line (provider name without ####)
        if re.match(r'^\*\*[^*]+\*\*$', t) and not t.startswith('-'):
            if in_ul:
                html += '</ul>'
                in_ul = False
            name = inline_md(t.replace('**', ''))
            prov_html = f'<div class="prov"><div class="prov-name">{name}</div><ul>'
            in_prov = True
            continue

        # Regular list items
        if t.startswith('- '):
            if not in_ul:
                html += '<ul class="rl">'
                in_ul = True
            html += f'<li>{inline_md(t[2:])}</li>'
            continue

        # Non-bold, non-bold text that looks like a note
        if t.startswith('**') and not t.startswith('- '):
            # Already handled above
            continue

        if in_ul:
            html += '</ul>'
            in_ul = False

        # Regular paragraph
        html += f'<p class="md-p">{inline_md(t)}</p>'

    if in_ul:
        html += '</ul>'
    if in_prov:
        prov_html += '</ul></div>'
        html += prov_html

    return html


def render_section_bilingual(sec_en, sec_zh):
    """Render one section with both EN and ZH content."""
    html = ''

    # Build a map of ZH items by matching order
    zh_items = sec_zh.get('items', []) if sec_zh else []
    en_items = sec_en.get('items', []) if sec_en else []

    # Combine all items
    all_items = []
    for i, item in enumerate(en_items):
        zh_item = zh_items[i] if i < len(zh_items) else None
        all_items.append((item, zh_item))

    # Also add any extra ZH items
    for i in range(len(en_items), len(zh_items)):
        all_items.append((None, zh_items[i]))

    for item_en, item_zh in all_items:
        if not item_en and not item_zh:
            continue

        item = item_en or item_zh

        if item.get('type') == 'details':
            title_en = item_en['title'] if item_en else item_zh['title']
            title_zh = item_zh['title'] if item_zh else item_en['title']
            content_en = item_en['content'] if item_en else ''
            content_zh = item_zh['content'] if item_zh else ''

            cnt = max(
                (len(re.findall(r'^- ', content_en, re.M)) if content_en else 0),
                (len(re.findall(r'^- ', content_zh, re.M)) if content_zh else 0)
            )

            html += '<div class="sub">'
            html += '<div class="sub-head" onclick="toggleSub(this)">'
            html += f'<span class="sub-name"><span class="lang-en">{inline_md(title_en)}</span><span class="lang-zh">{inline_md(title_zh)}</span></span>'
            html += f'<span class="sub-cnt">{cnt}</span>'
            html += '<span class="sub-arr">▶</span></div>'
            html += '<div class="sub-body">'
            html += f'<div class="lang-en">{render_list(content_en)}</div>'
            html += f'<div class="lang-zh">{render_list(content_zh)}</div>'
            html += '</div></div>'
        else:
            content_en = item_en['content'] if item_en else ''
            content_zh = item_zh['content'] if item_zh else ''
            html += f'<div class="lang-en">{render_list(content_en)}</div>'
            html += f'<div class="lang-zh">{render_list(content_zh)}</div>'

    return html


def find_section(sections, idx):
    """Find section by index number (0-based)."""
    count = 0
    for s in sections:
        if s['title'].startswith('##'):
            continue
        if count == idx:
            return s
        count += 1
    # Fallback: return by position
    filtered = [s for s in sections if not s['title'].startswith('贡献') and not s['title'].startswith('Contributing')]
    return filtered[idx] if idx < len(filtered) else None


def get_layer_sections(sections):
    """Get the 8 main layer sections (## headings)."""
    result = []
    for s in sections:
        title = s['title']
        # Skip non-layer sections
        if any(kw in title.lower() for kw in ['contributing', '贡献', '许可', 'license', 'contents', '目录']):
            continue
        result.append(s)
    return result


def gen_index(sections_en, sections_zh):
    """Generate index.html landing page."""
    layers_en = get_layer_sections(sections_en)
    layers_zh = get_layer_sections(sections_zh)

    cards = ''
    for i in range(min(8, len(layers_en))):
        idx_str = f"{i+1:02d}"
        se = SECTIONS_EN[i]
        sz = SECTIONS_ZH[i]
        cards += f'''
    <a class="layer-card" href="layer-{idx_str}.html">
      <div class="layer-card-idx">{idx_str}</div>
      <div class="layer-card-title"><span class="lang-en">{se[1]}</span><span class="lang-zh">{sz[1]}</span></div>
      <div class="layer-card-desc"><span class="lang-en">{se[2]}</span><span class="lang-zh">{sz[2]}</span></div>
    </a>'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Awesome AI Agent Hierarchy</title>
<link rel="stylesheet" href="style.css">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Serif+Display:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
</head>
<body>

<nav class="nav">
  <div class="nav-inner">
    <a href="index.html" class="nav-brand">Awesome Agent <i>Hierarchy</i></a>
    <div class="nav-actions">
      <div class="lang-group">
        <button class="active" onclick="setLang('en')">EN</button>
        <button onclick="setLang('zh')">中文</button>
      </div>
      <a href="https://github.com/tianX-ai/awsome-agent-hierarchy" class="nav-gh" target="_blank">GitHub ↗</a>
    </div>
  </div>
</nav>

<section class="hero">
  <h1><span class="lang-en">The AI Agent Stack</span><span class="lang-zh">AI 代理技术栈</span></h1>
  <p><span class="lang-en">A curated list of tools, libraries, and frameworks for building AI Agent systems, organized by 8 architectural layers.</span><span class="lang-zh">AI Agent 系统构建工具、库和框架的精选列表，按 8 个架构层级分类整理。</span></p>
  <hr class="hero-rule">
</section>

<div class="layer-grid">
{cards}
</div>

<button class="btt" id="btt" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">↑</button>

<footer class="foot">
  <span class="lang-en">Content from </span><span class="lang-zh">内容来自 </span>README.md / README-zh.md
</footer>

<script>
function setLang(l) {{
  const btns = document.querySelectorAll('.lang-group button');
  btns.forEach(b => b.classList.remove('active'));
  btns[l === 'en' ? 0 : 1].classList.add('active');
  document.body.classList.toggle('lang-zh-active', l === 'zh');
  document.documentElement.lang = l === 'zh' ? 'zh' : 'en';
  localStorage.setItem('lang', l);
}}
const saved = localStorage.getItem('lang');
if (saved === 'zh') setLang('zh');
window.addEventListener('scroll', () => {{
  document.getElementById('btt').classList.toggle('show', window.scrollY > 300);
}});
</script>
</body>
</html>'''


def gen_layer(idx, sec_en, sec_zh):
    """Generate a layer page (layer-01.html etc)."""
    idx_str = f"{idx:02d}"
    se = SECTIONS_EN[idx - 1]
    sz = SECTIONS_ZH[idx - 1]

    # Render all content
    content_html = render_section_bilingual(sec_en, sec_zh)

    # Sub-sections for search
    sub_sections = ''
    if sec_en and sec_en.get('items'):
        for item in sec_en['items']:
            if item.get('type') == 'details':
                sub_sections += f'<div class="sub">'
                zh_title = ''
                i_idx = sec_en['items'].index(item)
                if sec_zh and i_idx < len(sec_zh.get('items', [])):
                    zh_title = sec_zh['items'][i_idx].get('title', '')
                sub_sections += f'''<div class="sub-head" onclick="toggleSub(this)">
      <span class="sub-name"><span class="lang-en">{inline_md(item["title"])}</span><span class="lang-zh">{inline_md(zh_title)}</span></span>
      <span class="sub-cnt">{len(re.findall(r"^- ", item["content"], re.M))}</span>
      <span class="sub-arr">▶</span>
    </div>'''

                # Get matching ZH content
                zh_content = ''
                if sec_zh and i_idx < len(sec_zh.get('items', [])):
                    zh_content = sec_zh['items'][i_idx].get('content', '')

                sub_sections += f'''<div class="sub-body">
      <div class="lang-en">{render_list(item["content"])}</div>
      <div class="lang-zh">{render_list(zh_content)}</div>
    </div></div>'''
            else:
                # Non-details text content
                i_idx = sec_en['items'].index(item)
                zh_content = ''
                if sec_zh and i_idx < len(sec_zh.get('items', [])):
                    zh_content = sec_zh['items'][i_idx].get('content', '')
                sub_sections += f'<div class="lang-en">{render_list(item["content"])}</div>'
                sub_sections += f'<div class="lang-zh">{render_list(zh_content)}</div>'

    # Build layer nav (bottom)
    nav_links_en = ''
    nav_links_zh = ''
    for i in range(8):
        s = f"{i+1:02d}"
        cls = ' style="font-weight:700;color:var(--accent)"' if i + 1 == idx else ''
        nav_links_en += f'<a href="layer-{s}.html"{cls}>{SECTIONS_EN[i][1]}</a>'
        if i < 7:
            nav_links_en += ' <span style="color:var(--text-3)">·</span> '
        nav_links_zh += f'<a href="layer-{s}.html"{cls}>{SECTIONS_ZH[i][1]}</a>'
        if i < 7:
            nav_links_zh += ' <span style="color:var(--text-3)">·</span> '

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{idx_str}. {se[1]} — Awesome AI Agent Hierarchy</title>
<link rel="stylesheet" href="style.css">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Serif+Display:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
</head>
<body>

<nav class="nav">
  <div class="nav-inner">
    <a href="index.html" class="nav-brand">Awesome Agent <i>Hierarchy</i></a>
    <div class="nav-actions">
      <div class="lang-group">
        <button class="active" onclick="setLang('en')">EN</button>
        <button onclick="setLang('zh')">中文</button>
      </div>
      <a href="https://github.com/tianX-ai/awsome-agent-hierarchy" class="nav-gh" target="_blank">GitHub ↗</a>
    </div>
  </div>
</nav>

<div class="breadcrumb">
  <a href="index.html"><span class="lang-en">All Layers</span><span class="lang-zh">所有层级</span></a>
  <span>/</span>
  <span class="lang-en">{se[1]}</span><span class="lang-zh">{sz[1]}</span>
</div>

<section class="hero">
  <h1><span class="lang-en">{se[1]}</span><span class="lang-zh">{sz[1]}</span></h1>
  <p><span class="lang-en">{se[2]}</span><span class="lang-zh">{sz[2]}</span></p>
  <hr class="hero-rule">
</section>

<div class="search-area">
  <input id="search" type="text" placeholder="Search repos..." oninput="handleSearch(this.value)">
</div>

<main class="main-area">
{sub_sections}
</main>

<div style="max-width:var(--max-w);margin:0 auto;padding:0 2rem 2rem;font-size:0.82rem;line-height:2.2">
  <div class="lang-en">{nav_links_en}</div>
  <div class="lang-zh">{nav_links_zh}</div>
</div>

<button class="btt" id="btt" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">↑</button>

<footer class="foot">
  <span class="lang-en">Content from </span><span class="lang-zh">内容来自 </span>README.md / README-zh.md
</footer>

<script>
function setLang(l) {{
  const btns = document.querySelectorAll('.lang-group button');
  btns.forEach(b => b.classList.remove('active'));
  btns[l === 'en' ? 0 : 1].classList.add('active');
  document.body.classList.toggle('lang-zh-active', l === 'zh');
  document.documentElement.lang = l === 'zh' ? 'zh' : 'en';
  // Update search placeholder
  document.getElementById('search').placeholder = l === 'zh' ? '搜索仓库...' : 'Search repos...';
  localStorage.setItem('lang', l);
}}
function toggleSub(el) {{
  el.classList.toggle('open');
  el.nextElementSibling.classList.toggle('open');
}}
function handleSearch(q) {{
  q = q.toLowerCase().trim();
  document.querySelectorAll('ul.rl li').forEach(li => {{
    li.style.display = (!q || li.textContent.toLowerCase().includes(q)) ? '' : 'none';
  }});
  document.querySelectorAll('.sub').forEach(sub => {{
    if (!q) {{ sub.style.display = ''; return; }}
    const has = Array.from(sub.querySelectorAll('ul.rl li')).some(li => li.style.display !== 'none');
    sub.style.display = has ? '' : 'none';
  }});
}}
const saved = localStorage.getItem('lang');
if (saved === 'zh') setLang('zh');
window.addEventListener('scroll', () => {{
  document.getElementById('btt').classList.toggle('show', window.scrollY > 300);
}});
</script>
</body>
</html>'''


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    docs_dir = os.path.join(base, 'docs')
    os.makedirs(docs_dir, exist_ok=True)

    # Read READMEs
    with open(os.path.join(base, 'README.md'), encoding='utf-8') as f:
        md_en = f.read()
    with open(os.path.join(base, 'README-zh.md'), encoding='utf-8') as f:
        md_zh = f.read()

    sections_en = parse_readme(md_en)
    sections_zh = parse_readme(md_zh)

    layers_en = get_layer_sections(sections_en)
    layers_zh = get_layer_sections(sections_zh)

    print(f"Found {len(layers_en)} EN sections, {len(layers_zh)} ZH sections")

    # Generate index
    index_html = gen_index(sections_en, sections_zh)
    with open(os.path.join(docs_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_html)
    print("Generated index.html")

    # Generate layer pages
    for i in range(min(8, len(layers_en))):
        sec_en = layers_en[i] if i < len(layers_en) else None
        sec_zh = layers_zh[i] if i < len(layers_zh) else None
        html = gen_layer(i + 1, sec_en, sec_zh)
        path = os.path.join(docs_dir, f'layer-{i+1:02d}.html')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Generated layer-{i+1:02d}.html ({sec_en['title'][:30]}...)")

    print(f"\nDone! Generated {1 + min(8, len(layers_en))} files in {docs_dir}")


if __name__ == '__main__':
    main()
