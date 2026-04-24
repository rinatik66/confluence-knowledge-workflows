# confluence-knowledge-workflows

Patterns for moving Markdown-based working knowledge into structured Confluence workflows.

## Why

Many teams think in Markdown first: notes, incident writeups, meeting summaries, backlog drafts, research logs. But execution and long-term discoverability often live in Confluence. The gap between those two worlds creates duplication and operational drag.

This repository documents a workflow for reducing that gap.

## What is inside

- templates for Markdown pages that convert cleanly into wiki documentation
- patterns for publishing structured notes into Confluence spaces
- conventions for linking notes, meetings, backlogs, and follow-up pages
- examples of source note shapes that are friendly to later publishing

## Typical use cases

- meeting minutes
- project backlogs
- incident documentation
- vendor research notes
- requirement drafts
- operational runbooks

## Design principles

- write once in a format that remains reusable
- keep note structure stable across meetings and projects
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

This repository is about knowledge operations, not just documentation. The goal is to make notes reusable by product, analytics, operations, and engineering teams.

## License

MIT
