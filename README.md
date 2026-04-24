# confluence-knowledge-workflows

Patterns for moving Markdown-based working knowledge into structured Confluence workflows.

## Why this exists

Many teams naturally work in Markdown first: notes, incident writeups, meeting summaries, backlog drafts, research logs. But long-term discoverability and institutional memory often live in Confluence. Without a clean bridge between those formats, teams duplicate work, lose structure, and create documentation debt.

This repository documents patterns for reducing that gap.

## What it solves

- duplication between source notes and final wiki pages
- inconsistent structure across meetings and projects
- weak links between notes, backlog items, and follow-up actions
- documentation that becomes hard to reuse after publication

## What is inside

- templates for Markdown pages that convert cleanly into wiki documentation
- patterns for publishing structured notes into Confluence spaces
- conventions for linking meetings, backlogs, incidents, and follow-up pages
- examples of source note shapes that remain useful before and after publication

## Typical use cases

- meeting minutes
- project backlogs
- incident documentation
- vendor research notes
- requirement drafts
- operational runbooks

## Design principles

- write once in a format that remains reusable
- keep note structure stable across documents
- prefer compact operational summaries over long prose
- preserve source context, links, and decisions
- keep documentation close to task systems and execution workflows

## Repository structure

```text
.
├── templates/
│   ├── meeting_note.md
│   ├── incident_note.md
│   └── backlog_item.md
├── examples/
│   └── sample_meeting_note.md
└── docs/
    └── publishing_principles.md
```

## Positioning

This repository is about knowledge operations, not just documentation. The goal is to make working notes reusable by product, analytics, operations, and engineering teams.

## License

MIT
