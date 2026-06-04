# mitra-ai-projects

Production static site for **mitraaiprojects.com** — guided AI and ML project kits for engineering students.

> Part of the Mitra AI Life family. Separate from mitraailife.com (beginner/family focus). This site is technical, code-first, and project-first.

## Quick start

```bash
# Serve locally (from site/ root so absolute paths work)
cd site && python3 -m http.server 8080
# Open: http://localhost:8080
```

## Repo structure

```
mitra-ai-projects/
├── site/                    # Static website (deployed to GitHub Pages)
│   ├── index.html           # Home
│   ├── courses/             # Course pages (ml, dl, genai, agentic, mlops, rl, programming)
│   ├── projects/            # Project pages (catalog + individual)
│   ├── cheatsheets.html
│   ├── how-it-works.html
│   ├── faq.html
│   ├── about.html
│   ├── contact.html
│   ├── privacy.html
│   ├── terms.html
│   ├── assets/
│   │   ├── css/main.css     # Full design system (dark teal)
│   │   └── js/main.js       # Tab switching, quiz engine, GA4, FAQ
│   ├── auth.js              # Supabase auth integration
│   └── mitra-chat.js        # Cloudflare Worker chatbot widget
├── data/                    # YAML/JSON manifests
│   ├── projects/            # project-01.yaml, project-02.yaml ...
│   ├── courses/             # ml.yaml, programming.yaml ...
│   ├── featured-projects.json
│   └── faq.json
├── content/                 # Markdown source content
│   ├── projects/project-01/ # overview.md, viva.md, module-01.md ...
│   └── cheatsheets/         # python-basics.md, sql-quick-reference.md ...
├── scripts/                 # Python build/validation/upload scripts
│   ├── validate_project_manifests.py
│   ├── generate_cheatsheets.py
│   ├── build_project_pages.py
│   ├── deploy_s3.py
│   └── cloudflare-worker/mitra-projects-worker.js
├── docs/
│   └── mitraaiprojects-master-plan.md  # Single source of truth
├── .github/workflows/pages.yml          # GitHub Pages deploy workflow
├── .env.example
├── CNAME                                # mitraaiprojects.com
└── .gitignore
```

## Deployment

Automatic via GitHub Actions on push to `main`:
1. Workflow uploads `site/` as a GitHub Pages artifact
2. GitHub Pages serves it at `https://rajendar-muddasani.github.io/mitra-ai-projects/` (pre-domain)
3. Once `CNAME` is wired and DNS is pointed: `https://mitraaiprojects.com`

To enable:
- Go to repo Settings → Pages → Source: GitHub Actions
- Push to main to trigger first deploy

## Python scripts

```bash
# Activate venv first
source .venv/bin/activate

# Validate all project manifests
python scripts/validate_project_manifests.py

# Generate cheatsheet PDFs
python scripts/generate_cheatsheets.py --all

# Upload cheatsheets to S3
python scripts/deploy_s3.py --type cheatsheets

# Generate stub page for a new project
python scripts/build_project_pages.py --project project-02

# Upload project assets
python scripts/deploy_s3.py --type projects --project project-01
```

## Design system

- Colors: `--primary: #00d4aa`, `--bg-dark: #0d1117`, `--surface: #161b22`, `--accent: #f0b429`
- Fonts: Baloo 2 (headings), Nunito (body), JetBrains Mono (code/labels)
- Hero gradient: `linear-gradient(160deg, #0d1117 0%, #0d2818 50%, #0a2520 100%)`
- All styles in `site/assets/css/main.css`

## GA4

Measurement ID: `G-QGY0LH6W93` — already wired in all pages.

## Infrastructure

| Service | Usage | Key |
|---|---|---|
| GitHub Pages | Site hosting | main branch → site/ folder |
| AWS S3 | Assets (PDFs, images, videos) | mitra-ai-life-assets, us-west-2 |
| Supabase | Auth + completions DB | kuriwaysdlqnzqqzabts.supabase.co |
| Cloudflare Workers | Chatbot API | mitra-chat-worker + mitra-projects-worker |
| GA4 | Analytics | G-QGY0LH6W93 |
| OpenAI | Chatbot, image generation | gpt-4o-mini, text-embedding-3-small |

## Master plan

See `docs/mitraaiprojects-master-plan.md` — single source of truth. Do not create alternate planning documents.
