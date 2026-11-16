#!/usr/bin/env python3
"""Build one artifact index across all Inera FHIR IGs.

Reads the IG catalog (registry.json) and each IG's package-list.json from the
shared web root, then collects the artifacts of every published version and of
each IG's current CI build. The artifacts of a build come from IG Publisher's
assets/js/artifacts-table-data.js (the data behind artifacts.html). Builds made
before that file existed fall back to the ImplementationGuide resource.

Every artifact gets the IG id and version, so the page can filter on them.

Usage: build_artifacts_index.py [--web-root URL] [--ci-base URL] [--out FILE]
"""

import argparse
import datetime
import html
import json
import re
import sys
import urllib.error
import urllib.request

# Canonical base of the published IGs. package-list.json paths start with it;
# they are fetched from --web-root, which is the same place until
# fhir.inera.se points at the web root.
CANONICAL_ROOT = "https://fhir.inera.se/ig"

# IG Publisher's grouping ids (gid) -> (category, subcategory)
GROUPS = {
    "-dyn-capabilitystatement": ("Beteende", "Förmågedeklarationer"),
    "-dyn-searchparameter": ("Beteende", "Sökparametrar"),
    "-dyn-operationdefinition": ("Beteende", "Operationsdefinitioner"),
    "-dyn-subscriptiontopic": ("Beteende", "Prenumerationsämnen"),
    "-req-requirements": ("Krav", "Formella krav"),
    "-req-actordefinition": ("Krav", "Aktörsdefinitioner"),
    "-str-profile": ("Strukturer", "Resursprofiler"),
    "-str-extension": ("Strukturer", "Extensiondefinitioner"),
    "-str-logicalmodel": ("Strukturer", "Logiska modeller"),
    "-term-codesystem": ("Terminologi", "Kodsystem"),
    "-term-valueset": ("Terminologi", "Värdemängder"),
    "-term-namingsystem": ("Terminologi", "Namnsystem"),
    "-map-conceptmap": ("Terminologi", "Konceptmappningar"),
    "-ex-example": ("Exempel", "Exempelinstanser"),
}

# Category of a grouping id not in GROUPS, from its prefix
PREFIXES = {"dyn": "Beteende", "req": "Krav", "str": "Strukturer",
            "term": "Terminologi", "map": "Terminologi", "ex": "Exempel"}

# Resource type (and StructureDefinition kind) -> (category, subcategory), for
# builds without artifacts-table-data.js
TYPES = {
    "StructureDefinition:resource": ("Strukturer", "Resursprofiler"),
    "StructureDefinition:extension": ("Strukturer", "Extensiondefinitioner"),
    "StructureDefinition:logical": ("Strukturer", "Logiska modeller"),
    "StructureDefinition:complex-type": ("Strukturer", "Datatypsprofiler"),
    "StructureDefinition:primitive-type": ("Strukturer", "Datatypsprofiler"),
    "CapabilityStatement": ("Beteende", "Förmågedeklarationer"),
    "SearchParameter": ("Beteende", "Sökparametrar"),
    "OperationDefinition": ("Beteende", "Operationsdefinitioner"),
    "SubscriptionTopic": ("Beteende", "Prenumerationsämnen"),
    "Krav": ("Krav", "Formella krav"),
    "ActorDefinition": ("Krav", "Aktörsdefinitioner"),
    "CodeSystem": ("Terminologi", "Kodsystem"),
    "ValueSet": ("Terminologi", "Värdemängder"),
    "ConceptMap": ("Terminologi", "Konceptmappningar"),
    "NamingSystem": ("Terminologi", "Namnsystem"),
}


def fetch(url):
    """Return the body of url as text, or None if it does not exist."""
    req = urllib.request.Request(url, headers={"User-Agent": "inera-artifact-index"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def fetch_json(url):
    text = fetch(url)
    return json.loads(text) if text is not None else None


def plain(text, limit=400):
    """Description as plain text: tags removed, whitespace collapsed, shortened."""
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = html.unescape(text)
    text = re.sub(r"[*_`#>\[\]]", "", text)  # leftover Markdown markup
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def rows_from_table_data(base, text):
    """Artifacts from IG Publisher's artifacts-table-data.js."""
    m = re.search(r"=\s*(\{.*\})\s*;?\s*$", text, re.S)
    data = json.loads(m.group(1))
    lang = next(iter(data))  # the IG's (first) language
    rows = []
    for r in data[lang].get("rows", []):
        gid = r.get("gid", "")
        if gid in GROUPS:
            cat, sub = GROUPS[gid]
        else:
            # An IG-defined or new grouping: the category from the id's prefix,
            # the subcategory as the IG names it ("Kategori: Underkategori")
            cat = PREFIXES.get(gid.lstrip("-").split("-")[0], "Övrigt")
            sub = r.get("g", "").split(": ", 1)[-1]
        rows.append({
            "c": cat,
            "s": sub,
            "n": r.get("n", ""),
            "i": r.get("i", ""),
            "t": r.get("t", ""),
            "u": f"{base}/{r['u']}" if r.get("u") else base,
            "d": plain(r.get("d", "")),
        })
    return rows


def rows_from_ig_resource(base, ig):
    """Artifacts from the ImplementationGuide resource (older builds)."""
    rows = []
    for res in ig.get("definition", {}).get("resource", []):
        ref = res.get("reference", {}).get("reference", "")
        rtype, _, rid = ref.partition("/")
        kind = next((e.get("valueString") for e in res.get("extension", [])
                     if e.get("url", "").endswith("/resource-information")), rtype)
        if res.get("exampleBoolean") or res.get("exampleCanonical") or res.get("isExample"):
            cat, sub = "Exempel", "Exempelinstanser"
        else:
            cat, sub = TYPES.get(kind, TYPES.get(rtype, ("Övrigt", rtype)))
        rows.append({
            "c": cat,
            "s": sub,
            "n": res.get("name") or rid,
            "i": rid,
            "t": rtype,
            "u": f"{base}/{rtype}-{rid}.html",
            "d": plain(res.get("description", "")),
        })
    return rows


def artifacts(base):
    """Artifacts of the build at base, or None if no source is found there."""
    text = fetch(f"{base}/assets/js/artifacts-table-data.js")
    if text is not None:
        return rows_from_table_data(base, text), "artifacts-table-data.js"
    manifest = fetch_json(f"{base}/package.manifest.json")
    if manifest is None:
        return None, None
    ig = fetch_json(f"{base}/ImplementationGuide-{manifest['name']}.json")
    if ig is None:
        return None, None
    return rows_from_ig_resource(base, ig), "ImplementationGuide"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--web-root", default="https://inera-ab.github.io/fhir-portal/ig",
                    help="URL of the shared web root (the folder with registry.json)")
    ap.add_argument("--ci-base", default="https://inera-ab.github.io",
                    help="URL under which each IG repo's CI build is published")
    ap.add_argument("--out", default="docs/artifacts/artifacts-data.json")
    args = ap.parse_args()
    web_root = args.web_root.rstrip("/")

    catalog = fetch_json(f"{web_root}/registry.json") or {}
    igs, rows, problems = [], [], []

    for name, entry in sorted(catalog.items(), key=lambda kv: kv[1].get("title", kv[0]).lower()):
        slug = entry.get("slug", name)
        plist = fetch_json(f"{web_root}/{slug}/package-list.json") or {}
        builds = []
        for v in plist.get("list", []):
            if v.get("version") == "current" or v.get("status") == "ci-build":
                continue
            path = v["path"].rstrip("/").replace(CANONICAL_ROOT, web_root, 1)
            builds.append({"version": v["version"], "status": "published",
                           "date": v.get("date", ""), "url": path})
        # The CI build lives on the IG repo's own GitHub Pages. The repo name
        # comes from the catalog: GitHub Pages paths are case-sensitive.
        builds.append({"version": "current", "status": "ci",
                       "date": "", "url": f"{args.ci_base.rstrip('/')}/{name}"})

        ig = {"id": plist.get("package-id", ""), "name": name, "slug": slug,
              "title": entry.get("title", name), "versions": []}
        for b in builds:
            found, source = artifacts(b["url"])
            if found is None:
                problems.append(f"{name} {b['version']}: no artifact data at {b['url']}")
                continue
            if not ig["id"] and b["status"] == "ci":
                manifest = fetch_json(f"{b['url']}/package.manifest.json") or {}
                ig["id"] = manifest.get("name", "")
                b["label"] = manifest.get("version", "")
            ig["versions"].append({**b, "source": source, "count": len(found)})
            key = f"{name}|{b['version']}"
            rows.extend({**r, "k": key} for r in found)
            print(f"{name} {b['version']}: {len(found)} artifacts ({source})", file=sys.stderr)
        if ig["versions"]:
            igs.append(ig)

    out = {
        "generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "igs": igs,
        "rows": rows,
    }
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    for p in problems:
        print(f"warning: {p}", file=sys.stderr)
    print(f"{len(rows)} artifacts from {sum(len(i['versions']) for i in igs)} builds "
          f"of {len(igs)} IGs -> {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
