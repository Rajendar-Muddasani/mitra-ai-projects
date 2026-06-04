#!/usr/bin/env python3
"""
Generate project HTML pages from YAML manifests and content Markdown.
This script is a build helper — the primary project pages are hand-authored HTML.
Use this to generate stub pages for new projects from manifests.

Run: python scripts/build_project_pages.py --project project-02
"""

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)

DATA_DIR    = Path(__file__).parent.parent / "data" / "projects"
CONTENT_DIR = Path(__file__).parent.parent / "content" / "projects"
OUTPUT_DIR  = Path(__file__).parent.parent / "site" / "projects"


def load_manifest(project_id: str) -> dict:
    path = DATA_DIR / f"{project_id}.yaml"
    if not path.exists():
        print(f"Manifest not found: {path}")
        sys.exit(1)
    return yaml.safe_load(path.read_text())


def render_tech_tags(tech_stack: list) -> str:
    return "".join(f'<span class="tag">{t}</span>' for t in tech_stack)


def render_deliverable_pills(deliverables: list) -> str:
    return "".join(f'<span class="deliverable-pill">{d}</span>' for d in deliverables)


def render_milestones(milestones: list) -> str:
    if not milestones:
        return ""
    html = []
    for m in milestones:
        week = m.get("week", "")
        title = m.get("title", "")
        output = m.get("output", "")
        html.append(f"""
        <div class="milestone-card">
          <div class="milestone-num">0{week}</div>
          <div class="milestone-body">
            <div class="milestone-tag">Week {week}</div>
            <h4>{title}</h4>
            {"<p>" + output + "</p>" if output else ""}
          </div>
        </div>""")
    return "\n".join(html)


def generate_page(manifest: dict) -> str:
    slug          = manifest["slug"]
    title         = manifest["title"]
    difficulty    = manifest["difficulty"]
    duration      = manifest["duration_weeks"]
    core_problem  = manifest["core_problem"]
    tech_stack    = manifest.get("tech_stack", [])
    deliverables  = manifest.get("deliverables", [])
    milestones    = manifest.get("milestones", [])
    seo           = manifest.get("seo", {})
    seo_title     = seo.get("title", title + " — Mitra AI Projects")
    seo_desc      = seo.get("description", "")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{seo_title}</title>
  <meta name="description" content="{seo_desc}">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-QGY0LH6W93"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-QGY0LH6W93');</script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Baloo+2:wght@700;800&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/main.css">
</head>
<body>
<nav class="nav">
  <div class="nav-inner container">
    <a href="/" class="nav-brand"><div class="nav-logo">M</div><span>Mitra<span class="teal">AI</span> Projects</span></a>
    <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">☰</button>
    <ul class="nav-links">
      <li><a href="/courses/">Courses</a></li>
      <li><a href="/projects/" class="active">Projects</a></li>
      <li><a href="/cheatsheets.html">Cheatsheets</a></li>
      <li><a href="/contact.html">Contact</a></li>
    </ul>
    <div class="nav-auth"><button class="btn btn-ghost btn-sm" id="loginBtn">Sign In</button></div>
  </div>
</nav>

<section class="project-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a><span class="breadcrumb-sep">›</span><a href="/projects/">Projects</a><span class="breadcrumb-sep">›</span><span>{title}</span></div>
    <div class="project-meta-strip">
      <span class="badge badge-primary">Project Kit</span>
      <span class="badge badge-muted">~{duration} weeks</span>
      <span class="badge badge-muted">{difficulty.title()}</span>
    </div>
    <h1>{title}</h1>
    <p>{core_problem}</p>
    <div class="tags">{render_tech_tags(tech_stack)}</div>
    <div class="project-deliverables">{render_deliverable_pills(deliverables)}</div>
    <div style="margin-top:2rem;">
      <a href="#milestones" class="btn btn-primary btn-lg">Start Building →</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div id="milestones" style="margin-top:2rem;">
      <div class="section-tag" style="text-align:left;margin-bottom:0.75rem;">milestone breakdown</div>
      <h2>Build Plan</h2>
      <div style="display:flex;flex-direction:column;gap:1rem;margin-top:1.5rem;">
        {render_milestones(milestones)}
      </div>
    </div>

    <div class="completion-banner" style="margin-top:3rem;">
      <div class="completion-icon">🎓</div>
      <div class="completion-body">
        <h3>Mark Complete</h3>
        <p>Track your progress and claim a completion certificate.</p>
      </div>
      <button class="btn btn-primary claim-certificate">Mark Complete →</button>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="container">
    <div class="footer-bottom">
      <span>© 2026 Mitra AI Life.</span>
      <div class="footer-legal"><a href="/privacy.html">Privacy</a><a href="/terms.html">Terms</a></div>
    </div>
  </div>
</footer>
<div class="chat-widget"><button class="chat-btn" aria-label="Open AI chat">💬</button></div>
<script src="/assets/js/main.js"></script>
<script src="/auth.js"></script>
<script src="/mitra-chat.js"></script>
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="Generate project page from manifest")
    parser.add_argument("--project", required=True, help="Project ID (e.g., project-02)")
    parser.add_argument("--dry-run", action="store_true", help="Print output without writing")
    args = parser.parse_args()

    manifest = load_manifest(args.project)
    html     = generate_page(manifest)

    if args.dry_run:
        print(html)
        return

    output_path = OUTPUT_DIR / f"{manifest['slug']}.html"
    output_path.write_text(html, encoding="utf-8")
    print(f"✅ Generated: {output_path}")


if __name__ == "__main__":
    main()
