# bazi-analysis

`bazi-analysis` is a Codex skill for structured BaZi / Four Pillars analysis using an 实战派 workflow. It supports deterministic chart generation, ten-god preprocessing, root summary, cold/dry season markers, tomb-storehouse markers, priority scans, and topic-specific analysis references.

This repository is packaged as a clean release directory for GitHub. The actual skill lives in `bazi-analysis/`.

## Install For Codex

Use the skill as a repo-scoped skill:

```bash
mkdir -p .agents/skills
cp -R bazi-analysis .agents/skills/bazi-analysis
```

Or install it as a user-scoped skill:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R bazi-analysis "$HOME/.agents/skills/bazi-analysis"
```

Invoke it explicitly with:

```text
$bazi-analysis
```

Codex reads `bazi-analysis/SKILL.md` as the main instruction file. `bazi-analysis/agents/openai.yaml` provides Codex App metadata.

## Other Agent Entrypoints

The skill also includes lightweight compatibility entrypoints:

- `bazi-analysis/CLAUDE.md` for Claude / Claude Code
- `bazi-analysis/TRAE.md` for Trae or Tree-style agents
- `bazi-analysis/WORKBUDDY.md` for Workbuddy-style agents

These files only point agents back to `SKILL.md`; they do not duplicate the workflow.

## Requirements

- Python 3
- No network access is required for normal chart generation.
- The bundled `scripts/vendor/lunar_python/` package is used by the chart engine.

## Verify

From the repository root:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py bazi-analysis
PYTHONDONTWRITEBYTECODE=1 python3 bazi-analysis/scripts/chart_cli.py --calendar solar --year 1990 --month 5 --day 12 --hour 14 --minute 30 --gender male --da-yun-count 2
```

Expected result: the validator reports `Skill is valid!`, and the chart command prints the four pillars, preprocessing summary, and major luck cycles.

## Repository Contents

```text
bazi-analysis/
├── SKILL.md
├── agents/openai.yaml
├── CLAUDE.md
├── TRAE.md
├── WORKBUDDY.md
├── scripts/
└── references/
```

## Notes

This skill is a structured interpretive framework. Do not present BaZi output as scientific, medical, legal, or financial fact.

Before publishing this repository publicly, verify the redistribution terms for the bundled third-party `lunar_python` code under `bazi-analysis/scripts/vendor/lunar_python/`.
