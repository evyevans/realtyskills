#!/usr/bin/env python3
"""Build reviewable Agensi listing metadata from the public skill catalog."""

import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TAG_BY_CATEGORY = {
    "leads-and-prospecting": "lead-generation",
    "listings-and-marketing": "marketing",
    "client-communication-and-referrals": "client-communication",
    "market-research-and-pricing": "market-research",
    "deals-and-investment-analysis": "investment-analysis",
    "transactions-and-documents": "business-operations",
    "property-management": "business-operations",
    "compliance-and-risk": "compliance",
    "brokerage-operations-and-crm": "crm",
}


def main():
    catalog = json.loads((ROOT / "catalog.json").read_text())
    listings = []
    for skill in catalog["skills"]:
        entry = ROOT / skill["path"]
        frontmatter = re.split(r"^---\s*$", entry.read_text(), maxsplit=2, flags=re.M)
        if len(frontmatter) != 3:
            raise ValueError(f"Missing frontmatter: {entry}")
        skill_version = yaml.safe_load(frontmatter[1])["metadata"]["version"]
        package = ROOT / "dist" / f"{skill['id']}.zip"
        if not package.is_file():
            raise FileNotFoundError(package)
        description = (
            f"{skill['task']}. For {skill['audience'].lower()}. "
            f"Provide: {skill['inputs']}. "
            f"Produces: {skill['output']}. "
            f"Jurisdiction: {skill['jurisdiction']}. "
            "Free and MIT licensed. Source: https://github.com/evyevans/realtyskills."
        )
        listings.append({
            "id": skill["id"],
            "name": skill["title"],
            "summary": skill["task"],
            "description": description,
            "pricing_type": "free",
            "version": skill_version,
            "tags": ["real-estate", TAG_BY_CATEGORY[skill["category"]]],
            "keywords": ["real estate", skill["category"].replace("-", " ")],
            "source_path": str(Path(skill["path"]).parent),
            "zip_path": str(package.relative_to(ROOT)),
            "zip_sha256": hashlib.sha256(package.read_bytes()).hexdigest(),
        })
    output = ROOT / "dist" / "agensi-listings.json"
    output.write_text(json.dumps({"version": 1, "listings": listings}, indent=2) + "\n")
    print(f"Prepared {len(listings)} free listings: {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
