# confluence-knowledge-workflows

Patterns and lightweight tooling for moving Markdown-based working knowledge into structured Confluence workflows.

## Why this exists

Many teams naturally work in Markdown first: notes, incident writeups, meeting summaries, backlog drafts, research logs. But long-term discoverability and institutional memory often live in Confluence. Without a clean bridge between those formats, teams duplicate work, lose structure, and create documentation debt.

This repository documents that operating model and ships a minimal CLI workflow for it.

## What is inside

- templates for Markdown pages that convert cleanly into wiki documentation
- examples of source note shapes that remain useful before and after publication
- publishing principles for Markdown-first documentation teams
- small CLI tools for uploading Markdown and downloading page bodies

## Repository structure

```text
.
├── templates/
├── examples/
├── docs/
├── tools/
│   ├── confluence_uploader.py
│   └── confluence_downloader.py
└── .env.example
```

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install markdown requests python-dotenv html2text
cp .env.example .env
```

## Usage

Upload a Markdown note:

```bash
python tools/confluence_uploader.py --file examples/sample_meeting_note.md --space OPS --dry-run
python tools/confluence_uploader.py --file examples/sample_meeting_note.md --space OPS --parent-id 123456
```

Download a Confluence page body:

```bash
python tools/confluence_downloader.py --page-id 123456 --output exported_note.md
```

## Design principles

- write once in a format that remains reusable
- keep note structure stable across documents
- prefer compact operational summaries over long prose
- preserve source context, links, and decisions
- keep documentation close to task systems and execution workflows

## License

MIT
