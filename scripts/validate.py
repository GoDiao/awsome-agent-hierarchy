"""Validate the Awesome AI Agent Hierarchy repository."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_TAGS = ["Official", "Framework", "Example", "Research", "Infra", "Archived Classic"]
TAG_RE = re.compile(r"`(" + "|".join(re.escape(t) for t in ALLOWED_TAGS) + r")`")
REPO_LINE_RE = re.compile(r"^- \[[^\]]+\]\((https://github\.com/([^/)]+)/([^)\s#?]+)[^)]*)\)")
MOJIBAKE_MARKERS = [
    "\ufffd",
    "\u9239",
    "\u6d93",
    "\u939c",
    "\u7487",
    "\u9369",
    "\u6d60",
    "\u5b80",
    "\u9438",
    "\u95ab",
]
ASCII_PUNCT = "".join(chr(i) for i in range(128) if not chr(i).isalnum() and chr(i) not in [" ", "-"])
ANCHOR_TRANS = str.maketrans("", "", ASCII_PUNCT)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def github_anchor(title: str) -> str:
    anchor = title.strip().lower().translate(ANCHOR_TRANS)
    anchor = re.sub(r"\s+", "-", anchor)
    return re.sub(r"-+", "-", anchor).strip("-")


def check_toc(path: str, toc_title: str, final_titles: set[str]) -> None:
    lines = read(path).splitlines()
    try:
        start = lines.index(f"## {toc_title}")
    except ValueError:
        fail(f"{path} missing {toc_title} section")
    try:
        end = next(i for i in range(start + 1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        fail(f"{path} missing end marker after {toc_title}")

    actual: list[tuple[int, str]] = []
    for line in lines[end + 1 :]:
        if line.startswith("## "):
            title = line[3:].strip()
            if re.match(r"^\d{2}\. ", title) or title in final_titles:
                actual.append((2, title))
        elif line.startswith("### "):
            actual.append((3, line[4:].strip()))

    expected = []
    for level, title in actual:
        indent = "  " if level == 3 else ""
        expected.append(f"{indent}- [{title}](#{github_anchor(title)})")
    toc = [line for line in lines[start + 2 : end] if line.strip()]
    if toc != expected:
        fail(f"{path} Contents/目录 is out of sync with headings")


def parse_blocks(path: str) -> list[dict]:
    lines = read(path).splitlines()
    blocks: list[dict] = []
    h2 = ""
    h3 = ""
    current: dict | None = None
    for line_no, line in enumerate(lines, 1):
        if line.startswith("## "):
            h2 = line[3:].strip()
        elif line.startswith("### "):
            h3 = line[4:].strip()
        elif line.strip().lower() == "<details>":
            current = {"line": line_no, "h2": h2, "h3": h3, "urls": [], "tags": [], "lines": []}
        elif current is not None:
            if line.startswith("- ") and "https://github.com/" in line:
                match = REPO_LINE_RE.search(line)
                if match:
                    url = match.group(1).rstrip("/")
                    tags = TAG_RE.findall(line)
                    current["urls"].append(url)
                    current["tags"].append(tags)
                    current["lines"].append((line_no, line))
            if line.strip().lower() == "</details>":
                blocks.append(current)
                current = None
    return blocks


def check_required_files() -> None:
    for rel in ["CONTRIBUTING.md", "SELECTION_CRITERIA.md", "LICENSE", "generate.py", "docs/index.html"]:
        if not (ROOT / rel).exists():
            fail(f"Missing required file: {rel}")


def check_encoding() -> None:
    paths = ["README.md", "README-zh.md", "generate.py", "CONTRIBUTING.md", "SELECTION_CRITERIA.md"]
    paths.extend(str(p.relative_to(ROOT)) for p in (ROOT / "docs").glob("*.html"))
    for rel in paths:
        text = read(rel)
        for marker in MOJIBAKE_MARKERS:
            if marker in text:
                fail(f"Encoding residue {marker.encode('unicode_escape').decode()} found in {rel}")


def check_readmes() -> None:
    check_toc("README.md", "Contents", {"Contributing", "License"})
    check_toc("README-zh.md", "\u76ee\u5f55", {"\u8d21\u732e\u6307\u5357", "\u8bb8\u53ef\u8bc1"})

    en = parse_blocks("README.md")
    zh = parse_blocks("README-zh.md")
    if len(en) != len(zh):
        fail(f"README block count mismatch: {len(en)} != {len(zh)}")
    if not en:
        fail("No <details> blocks found")

    for lang, blocks in [("README.md", en), ("README-zh.md", zh)]:
        for block in blocks:
            count = len(block["urls"])
            if not 1 <= count <= 10:
                fail(f"{lang}:{block['line']} has {count} GitHub repos; expected 1..10")
            if len(block["urls"]) != len(set(block["urls"])):
                fail(f"{lang}:{block['line']} has duplicate repo URLs")
            for line_no, line in block["lines"]:
                tags = TAG_RE.findall(line)
                if not tags:
                    fail(f"{lang}:{line_no} repo item is missing a required tag")
                unknown = [tag for tag in re.findall(r"`([^`]+)`", line) if tag not in ALLOWED_TAGS]
                if unknown:
                    fail(f"{lang}:{line_no} has unknown tag(s): {', '.join(unknown)}")

    for i, (a, b) in enumerate(zip(en, zh), 1):
        if a["urls"] != b["urls"]:
            fail(f"README URL order mismatch in block {i}: {a['h3']} / {b['h3']}")
        if a["tags"] != b["tags"]:
            fail(f"README tag mismatch in block {i}: {a['h3']} / {b['h3']}")

    if "up to 10" not in read("README.md").lower():
        fail("README.md does not state the up-to-10 curation rule")
    if "\u6700\u591a\u6536\u5f55 10" not in read("README-zh.md"):
        fail("README-zh.md does not state the up-to-10 curation rule")


def check_docs_features() -> None:
    html_files = sorted((ROOT / "docs").glob("layer-*.html"))
    if len(html_files) != 8:
        fail(f"Expected 8 layer pages, found {len(html_files)}")
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        for needle in ["tag-filter", "data-tags=", "setTag(", "handleSearch()"]:
            if needle not in text:
                fail(f"{path.relative_to(ROOT)} missing docs feature marker: {needle}")
    css = read("docs/style.css")
    for needle in [".tag-official", ".tag-framework", ".tag-example", ".tag-research", ".tag-infra", ".tag-archived-classic"]:
        if needle not in css:
            fail(f"docs/style.css missing tag style: {needle}")


def check_docs_fresh() -> None:
    before = snapshot(["docs", "generate.py"])
    subprocess.run([sys.executable, "generate.py"], cwd=ROOT, check=True)
    after = snapshot(["docs", "generate.py"])
    if before != after:
        fail("docs are not fresh; run python generate.py")


def snapshot(paths: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for rel in paths:
        path = ROOT / rel
        if path.is_file():
            result[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
        elif path.is_dir():
            for child in sorted(path.rglob("*")):
                if child.is_file():
                    result[str(child.relative_to(ROOT))] = hashlib.sha256(child.read_bytes()).hexdigest()
    return result


def github_api_check(repo: str, token: str | None) -> tuple[int, dict | None]:
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "awesome-agent-hierarchy-validator",
        },
    )
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        return exc.code, None
    except urllib.error.URLError:
        return 0, None


def check_links() -> None:
    urls = []
    for block in parse_blocks("README.md"):
        urls.extend(block["urls"])
    repos = sorted({"/".join(re.search(r"github\.com/([^/]+/[^/)#?]+)", url).group(1).split("/")[:2]) for url in urls})
    cache_dir = ROOT / ".omc" / "state"
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_path = cache_dir / "github_link_check.json"
    cache = json.loads(cache_path.read_text(encoding="utf-8")) if cache_path.exists() else {}
    audit_path = cache_dir / "github_api_audit.json"
    if audit_path.exists():
        audit = json.loads(audit_path.read_text(encoding="utf-8"))
        for repo, payload in audit.items():
            if isinstance(payload, dict) and payload.get("status") == 200:
                cache[repo] = payload
    token = os.environ.get("GITHUB_TOKEN")
    missing = [repo for repo in repos if not (cache.get(repo) and cache[repo].get("status") == 200)]

    def check_one(repo: str) -> tuple[str, dict]:
        status, payload = github_api_check(repo, token)
        result = {"status": status}
        if payload:
            result.update(
                {
                    "full_name": payload.get("full_name"),
                    "archived": payload.get("archived"),
                    "pushed_at": payload.get("pushed_at"),
                    "stargazers_count": payload.get("stargazers_count"),
                }
            )
        return repo, result

    bad: list[str] = []
    if missing:
        workers = min(16, max(1, len(missing)))
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = [pool.submit(check_one, repo) for repo in missing]
            for future in as_completed(futures):
                repo, result = future.result()
                cache[repo] = result
                if result.get("status") != 200:
                    bad.append(f"{repo} ({result.get('status')})")
    cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    if bad:
        fail("Broken GitHub repo links: " + ", ".join(bad[:20]))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-links", action="store_true", help="Check GitHub repository links through the GitHub API")
    parser.add_argument("--check-docs", action="store_true", help="Verify generated docs are fresh")
    args = parser.parse_args()

    check_required_files()
    check_encoding()
    check_readmes()
    check_docs_features()
    if args.check_docs:
        check_docs_fresh()
    if args.check_links:
        check_links()
    print("Validation passed")


if __name__ == "__main__":
    main()
