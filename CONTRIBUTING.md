# Contributing

Thanks for helping improve Awesome AI Agent Hierarchy. This project is a curated map of AI agent systems, not a complete directory, so every addition should make the hierarchy clearer for builders.

## What Belongs Here

- Open-source GitHub repositories that help people build, operate, evaluate, or secure AI agent systems.
- Official SDKs, frameworks, examples, research implementations, infrastructure, benchmarks, and carefully preserved classic projects.
- Resources that fit an existing third-level topic. If a project spans several topics, place it where readers are most likely to look first.

## Selection Rules

- Each third-level topic should contain **up to 10 curated GitHub repositories**. Fewer than 10 is fine when the category does not have enough strong projects.
- Prefer maintained, widely used, official, or technically distinctive repositories.
- Avoid duplicate links inside the same topic.
- Avoid generic lists, toy demos, or abandoned projects unless they are historically important and tagged as `Archived Classic`.
- Descriptions should be short, factual, and useful for comparison.
- Keep `README.md`, `README-zh.md`, and `docs/` synchronized.

## Required Tags

Every repository item must include at least one of these tags:

- `Official`: maintained by the project, vendor, standards body, or original research team.
- `Framework`: reusable SDK, library, platform, or orchestration framework.
- `Example`: template, demo app, sample implementation, cookbook, or tutorial repository.
- `Research`: paper implementation, benchmark, dataset, survey, or academic resource.
- `Infra`: deployment, database, observability, security, gateway, runtime, or integration infrastructure.
- `Archived Classic`: archived or inactive project that is still useful as historical context.

Multiple tags are allowed when they help readers decide quickly.

## Local Checks

Run these before opening a pull request:

```bash
python scripts/validate.py
python generate.py
python scripts/validate.py --check-docs
```

For link checks, use:

```bash
python scripts/validate.py --check-links
```

The link checker uses the GitHub API when `GITHUB_TOKEN` is available, and keeps its cache under `.omc/state/` so it does not create large dependency caches.

