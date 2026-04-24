#!/usr/bin/env python3
"""Upload a Markdown file to Confluence using the REST API."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

import markdown
import requests
from dotenv import load_dotenv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", required=True, help="Path to Markdown file")
    parser.add_argument("--title", help="Page title; defaults to file stem")
    parser.add_argument("--space", required=True, help="Confluence space key")
    parser.add_argument("--parent-id", help="Optional parent page ID")
    parser.add_argument("--dry-run", action="store_true", help="Print payload without uploading")
    return parser.parse_args()


def markdown_to_storage(markdown_text: str) -> str:
    return markdown.markdown(markdown_text, extensions=["tables", "fenced_code"])


def main() -> int:
    args = parse_args()
    load_dotenv()

    base_url = os.environ.get("CONFLUENCE_URL")
    token = os.environ.get("CONFLUENCE_TOKEN")
    if not base_url or not token:
        raise SystemExit("CONFLUENCE_URL and CONFLUENCE_TOKEN must be set")

    source = Path(args.file).expanduser().resolve()
    markdown_text = source.read_text(encoding="utf-8")
    payload = {
        "type": "page",
        "title": args.title or source.stem,
        "space": {"key": args.space},
        "body": {
            "storage": {
                "value": markdown_to_storage(markdown_text),
                "representation": "storage",
            }
        },
    }
    if args.parent_id:
        payload["ancestors"] = [{"id": int(args.parent_id)}]

    if args.dry_run:
        print(payload)
        return 0

    response = requests.post(
        f"{base_url.rstrip('/')}/rest/api/content",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=60,
    )
    response.raise_for_status()
    data = response.json()
    print(f"created page {data['id']}: {data['title']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
