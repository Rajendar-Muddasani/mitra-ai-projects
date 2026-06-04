#!/usr/bin/env python3
"""
Validate all project YAML manifests for required fields and schema consistency.
Run: python scripts/validate_project_manifests.py
"""

import sys
import os
from pathlib import Path
import yaml

REQUIRED_FIELDS = [
    "project_id", "slug", "title", "lane", "difficulty",
    "status", "duration_weeks", "core_problem", "tech_stack",
    "deliverables", "related_courses", "seo"
]

SEO_REQUIRED = ["title", "description"]

VALID_LANES = [
    "guided-mini-project", "major-project-kit",
    "portfolio-build", "viva-submission-pack"
]

VALID_STATUSES = ["featured", "available", "coming-soon", "planned"]

VALID_DIFFICULTIES = ["beginner-friendly", "intermediate", "advanced"]

errors = []
warnings = []


def validate_manifest(path: Path) -> list[str]:
    errs = []
    try:
        data = yaml.safe_load(path.read_text())
    except yaml.YAMLError as e:
        return [f"YAML parse error in {path}: {e}"]

    for field in REQUIRED_FIELDS:
        if field not in data:
            errs.append(f"  MISSING: {field}")

    if data.get("lane") not in VALID_LANES:
        errs.append(f"  INVALID lane: {data.get('lane')} — must be one of {VALID_LANES}")

    if data.get("status") not in VALID_STATUSES:
        errs.append(f"  INVALID status: {data.get('status')} — must be one of {VALID_STATUSES}")

    if data.get("difficulty") not in VALID_DIFFICULTIES:
        errs.append(f"  INVALID difficulty: {data.get('difficulty')}")

    seo = data.get("seo", {})
    for sf in SEO_REQUIRED:
        if sf not in seo:
            errs.append(f"  MISSING seo.{sf}")
        elif len(str(seo[sf])) < 20:
            warnings.append(f"  SHORT seo.{sf} ({len(str(seo[sf]))} chars) in {path.name}")

    if "milestones" in data:
        for i, m in enumerate(data["milestones"]):
            if "title" not in m:
                errs.append(f"  milestones[{i}] missing title")

    return errs


def main():
    projects_dir = Path(__file__).parent.parent / "data" / "projects"
    manifests = sorted(projects_dir.glob("*.yaml"))

    if not manifests:
        print("⚠  No project manifests found in data/projects/")
        sys.exit(1)

    print(f"Validating {len(manifests)} project manifests...\n")
    all_ok = True

    for manifest_path in manifests:
        errs = validate_manifest(manifest_path)
        if errs:
            all_ok = False
            print(f"❌ {manifest_path.name}")
            for e in errs:
                print(e)
        else:
            print(f"✅ {manifest_path.name}")

    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  ⚠  {w}")

    print()
    if all_ok:
        print("✅ All manifests valid.")
        sys.exit(0)
    else:
        print(f"❌ Validation failed. Fix the errors above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
