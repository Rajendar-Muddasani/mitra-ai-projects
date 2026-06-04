#!/usr/bin/env python3
"""
Upload generated assets to S3.
Bucket: mitra-ai-life-assets
Region: us-west-2

Usage:
  python scripts/deploy_s3.py --type cheatsheets
  python scripts/deploy_s3.py --type projects --project project-01
  python scripts/deploy_s3.py --type shared

Requires: AWS credentials in .env or environment
"""

import argparse
import os
import mimetypes
from pathlib import Path

try:
    import boto3
    from botocore.exceptions import ClientError
except ImportError:
    print("boto3 not installed. Run: pip install boto3")
    import sys; sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

BUCKET   = "mitra-ai-life-assets"
REGION   = "us-west-2"
CDN_BASE = f"https://{BUCKET}.s3.{REGION}.amazonaws.com/"

LOCAL_CHEATSHEETS = Path("/tmp/cheatsheets")
LOCAL_PROJECTS    = Path("/tmp/projects")
LOCAL_SHARED      = Path("/tmp/shared")


def get_s3():
    return boto3.client(
        "s3",
        region_name=REGION,
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )


def upload_file(s3_client, local_path: Path, s3_key: str, public: bool = True) -> str:
    content_type = mimetypes.guess_type(str(local_path))[0] or "application/octet-stream"
    extra_args = {"ContentType": content_type}
    if public:
        extra_args["ACL"] = "public-read"

    try:
        s3_client.upload_file(str(local_path), BUCKET, s3_key, ExtraArgs=extra_args)
        url = CDN_BASE + s3_key
        print(f"  ✅ {s3_key}")
        return url
    except ClientError as e:
        print(f"  ❌ {s3_key}: {e}")
        return None


def upload_cheatsheets(s3):
    if not LOCAL_CHEATSHEETS.exists():
        print(f"⚠  No cheatsheets found at {LOCAL_CHEATSHEETS}")
        print("   Run: python scripts/generate_cheatsheets.py --all first")
        return
    pdfs = list(LOCAL_CHEATSHEETS.glob("*.pdf"))
    print(f"Uploading {len(pdfs)} cheatsheets...")
    for pdf in sorted(pdfs):
        upload_file(s3, pdf, f"cheatsheets/{pdf.name}")


def upload_project(s3, project_id: str):
    project_dir = LOCAL_PROJECTS / project_id
    if not project_dir.exists():
        print(f"⚠  No assets found at {project_dir}")
        return
    files = list(project_dir.rglob("*"))
    files = [f for f in files if f.is_file()]
    print(f"Uploading {len(files)} project assets for {project_id}...")
    for f in sorted(files):
        rel = f.relative_to(LOCAL_PROJECTS)
        upload_file(s3, f, f"projects/{rel}")


def upload_shared(s3):
    if not LOCAL_SHARED.exists():
        print(f"⚠  No shared assets found at {LOCAL_SHARED}")
        return
    files = list(LOCAL_SHARED.rglob("*"))
    files = [f for f in files if f.is_file()]
    print(f"Uploading {len(files)} shared assets...")
    for f in sorted(files):
        rel = f.relative_to(LOCAL_SHARED)
        upload_file(s3, f, f"shared/{rel}")


def main():
    parser = argparse.ArgumentParser(description="Upload assets to S3")
    parser.add_argument("--type", choices=["cheatsheets", "projects", "shared"], required=True)
    parser.add_argument("--project", help="Project ID for --type projects (e.g., project-01)")
    args = parser.parse_args()

    s3 = get_s3()

    if args.type == "cheatsheets":
        upload_cheatsheets(s3)
    elif args.type == "projects":
        if not args.project:
            print("--project required with --type projects")
            return
        upload_project(s3, args.project)
    elif args.type == "shared":
        upload_shared(s3)

    print("\nDone.")


if __name__ == "__main__":
    main()
