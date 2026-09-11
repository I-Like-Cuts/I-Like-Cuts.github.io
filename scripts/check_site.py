"""Dependency-free smoke check for the static Pages publishing directory."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

PUBLIC = Path(__file__).resolve().parents[1] / "public"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = set()
        self.references = []

    def handle_starttag(self, tag, attrs):
        self.tags.add(tag)
        for name, value in attrs:
            if name in {"href", "src"} and value:
                self.references.append(value)


def main():
    errors = []
    if not (PUBLIC / "index.html").is_file():
        errors.append("public/index.html is missing")
    for path in PUBLIC.rglob("*"):
        if path.is_symlink():
            errors.append(f"Symlinks are not supported: {path.relative_to(PUBLIC)}")
        if path.suffix == ".html" and path.is_file():
            source = path.read_text(encoding="utf-8")
            page = Page()
            page.feed(source)
            if "<!doctype html>" not in source.lower():
                errors.append(f"Missing HTML doctype: {path.name}")
            if not {"html", "head", "title", "body", "main", "h1"} <= page.tags:
                errors.append(f"Missing document structure: {path.name}")
            for reference in page.references:
                url = urlsplit(reference)
                if url.scheme or url.netloc or not url.path:
                    continue
                if url.path.startswith("/"):
                    errors.append(f"Use relative URLs for project Pages: {reference}")
                    continue
                target = (path.parent / unquote(url.path)).resolve()
                if not target.is_relative_to(PUBLIC.resolve()) or not target.exists():
                    errors.append(f"Missing or unpublished asset: {reference}")
    if errors:
        raise SystemExit("\n".join(errors))
    print("Site smoke check passed: document structure and local asset paths.")


if __name__ == "__main__":
    main()
