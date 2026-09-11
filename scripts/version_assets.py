"""Version local HTML asset links so browsers reload assets after deployment."""

import hashlib
import re
from pathlib import Path
from urllib.parse import parse_qsl, unquote, urlencode, urlsplit, urlunsplit

PUBLIC = Path(__file__).resolve().parents[1] / "public"
REFERENCE = re.compile(r'\b(?:href|src)\s*=\s*([\x22\x27])([^\x22\x27]+)\1', re.IGNORECASE)


def version_assets(root=PUBLIC):
    root = root.resolve()
    for page in root.rglob("*.html"):
        def replace(match):
            url = urlsplit(match.group(2))
            if url.scheme or url.netloc or not url.path:
                return match.group(0)
            asset = (page.parent / unquote(url.path)).resolve()
            if not asset.is_relative_to(root) or not asset.is_file() or asset.suffix == ".html":
                return match.group(0)
            digest = hashlib.sha256(asset.read_bytes()).hexdigest()[:16]
            query = [(key, value) for key, value in parse_qsl(url.query) if key != "v"]
            query.append(("v", digest))
            reference = urlunsplit(url._replace(query=urlencode(query)))
            return match.group(0).replace(match.group(2), reference, 1)

        source = page.read_text(encoding="utf-8")
        page.write_text(REFERENCE.sub(replace, source), encoding="utf-8")
    print("Versioned local stylesheet, image and script links for publication.")


if __name__ == "__main__":
    version_assets()
