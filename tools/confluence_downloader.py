#!/usr/bin/env python3
"""Download a Confluence page body and save it as Markdown-like text."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

import html2text
import requests
from dotenv import load_dotenv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--page-id", required=True, help="Confluence page ID")
    parser.add_argument("--output", required=True, help="Output Markdown file")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    load_dotenv()

    base_url = os.environ.get("CONFLUENCE_URL")
    token = os.environ.get("CONFLUENCE_TOKEN")
    if not base_url or not token:
        raise SystemExit("CONFLUENCE_URL and CONFLUENCE_TOKEN must be set")

    response = requests.get(
        f"{base_url.rstrip('/')}/rest/api/content/{args.page_id}",
        params={"expand": "body.storage,title"},
        headers={"Authorization": f"Bearer {token}"},
        timeout=60,
    )
    response.raise_for_status()
    data = response.json()

    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.body_width = 0
    markdown_text = converter.handle(data["body"]["storage"]["value"])

    output = Path(args.output).expanduser().resolve()
    output.write_text(markdown_text, encoding="utf-8")
    print(f"saved {data['title']} to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
