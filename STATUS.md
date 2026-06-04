# mitraaiprojects.com — Build Status
> Last updated: 2026-06-04. Hand this file to VS Code Copilot to continue work.
> Master plan: `docs/mitraaiprojects-master-plan.md` — single source of truth.

---

## ✅ Fully Ready (no code changes needed)

| Item | File(s) | Notes |
|---|---|---|
| Home page | `site/index.html` | Hero, dual-lane, featured cards, trust strip, CTA |
| Courses index | `site/courses/index.html` | All 7 track cards, status badges |
| ML course (OneNote) | `site/courses/ml.html` | Left-sidebar 10-tab layout, all topics, quizzes, code panels |
| Programming course | `site/courses/programming.html` | 8-tab layout, AI prompts, quizzes, code examples |
| Deep Learning course | `site/courses/dl.html` | 8-tab layout, full content |
| Generative AI course | `site/courses/genai.html` | 8-tab layout, RAG architecture diagram |
| Agentic AI & MCP | `site/courses/agentic.html` | 7-tab layout, LangGraph/CrewAI/MCP code |
| MLOps & Tools | `site/courses/mlops.html` | 7-tab layout, Airflow/Spark/MLflow/Docker |
| Reinforcement Learning | `site/courses/rl.html` | 6-tab layout, labeled "Planned" per master plan |
| Projects catalog | `site/projects/index.html` | 6 project cards, lane explanation, deliverables grid |
| Document Q&A project | `site/projects/document-qa-assistant.html` | Full kit: arch diagram, 6 milestones, code, deployment, 10 viva Q&A, quiz |
| Cheatsheets page | `site/cheatsheets.html` | 11 cheatsheet cards, all linked to S3 paths |
| How It Works | `site/how-it-works.html` | 4-step process, two-lane explainer |
| FAQ | `site/faq.html` | Accordion FAQ, FAQ schema markup |
| About | `site/about.html` | Story, two-lane explainer, Mitra comparison table |
| Contact | `site/contact.html` | 5-field form, Supabase insert hook, interest dropdown |
| Privacy Policy | `site/privacy.html` | Full policy, GA4/Supabase/third-party disclosure |
| Terms of Service | `site/terms.html` | Full terms, academic integrity clause |
| CSS design system | `site/assets/css/main.css` | Dark teal, OneNote layout, tab system, quiz, mobile-first |
| Main JS | `site/assets/js/main.js` | Tabs, OneNote, quiz engine, GA4, FAQ, contact, chat, certificate |
| Auth stub | `site/auth.js` | Supabase OAuth, completion recording hooks |
| Chatbot widget | `site/mitra-chat.js` | Cloudflare Worker chat, inline CSS, mobile-ready |
| Project manifests | `data/projects/project-01/02/03.yaml` | All validated, required fields present |
| Course manifests | `data/courses/ml.yaml`, `programming.yaml` | Topic lists, source repos, cheatsheet refs |
| Data files | `data/featured-projects.json`, `data/faq.json` | Structured data for dynamic use |
| Content Markdown | `content/projects/project-01/overview.md`, `viva.md` | Full 20-question viva set |
| Cheatsheet sources | `content/cheatsheets/python-basics.md`, `sql-quick-reference.md` | Ready for PDF generation |
| Python scripts | `scripts/validate_project_manifests.py` | ✅ Runs and passes |
| Python scripts | `scripts/generate_cheatsheets.py` | Ready, needs `reportlab` + `python scripts/generate_cheatsheets.py --all` |
| Python scripts | `scripts/build_project_pages.py` | Generates stub pages from manifests |
| Python scripts | `scripts/deploy_s3.py` | Uploads to S3, needs AWS creds in `.env` |
| Cloudflare Worker | `scripts/cloudflare-worker/mitra-projects-worker.js` | Projects chat context, needs `wrangler deploy` |
| GitHub Actions | `.github/workflows/pages.yml` | Deploys `site/` to Pages on push to `main` |
| Root config | `.gitignore`, `.env.example`, `CNAME`, `README.md` | All present |

---

## 🔌 Ready but Needs Real Values Wired In

These files exist and have the correct structure — they just need live credentials or runtime values.

| What | File | Action needed |
|---|---|---|
| Supabase anon key | `site/auth.js` line 6 | Add `<script>window.__SUPABASE_ANON_KEY__ = 'eyJ...'</script>` before `auth.js` loads, OR inject at build time |
| OpenAI key for worker | `scripts/cloudflare-worker/mitra-projects-worker.js` | Set `OPENAI_API_KEY` secret via `wrangler secret put OPENAI_API_KEY` |
| AWS creds for S3 | `.env` (copy from `.env.example`) | Fill `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` |
| Cheatsheet PDFs | S3 `cheatsheets/` prefix | Run `generate_cheatsheets.py --all` then `deploy_s3.py --type cheatsheets` |
| Project hero images | S3 `projects/project-01/hero/` | Generate with DALL-E 3, upload via `deploy_s3.py --type projects --project project-01` |

---

## 🔶 Stubbed — Content Needs Building

These pages/sections have correct structure but placeholder or minimal content.

| Item | File | What to add |
|---|---|---|
| Project 02 page | NOT YET CREATED — run `python scripts/build_project_pages.py --project project-02` | Then flesh out with real milestones and viva Q&A |
| Project 03 page | NOT YET CREATED | Same as above |
| Project 04–06 pages | NOT YET CREATED | Will be planned later per master plan |
| ML notebook links | `site/courses/ml.html` (Colab links in each panel) | Replace placeholder `notebook.ipynb` URLs with real AIML-Engineering-Lab Colab links |
| DL notebook links | `site/courses/dl.html` | Same — add real repo links for 014, 015, 034, 054, 073 |
| RL course full content | `site/courses/rl.html` | Currently overview-level only — marked "Planned" |
| Contact form backend | `site/mitra-chat.js` + `site/auth.js` | Supabase `contact_submissions` table must be created in Supabase dashboard |
| Disqus comments | Not yet wired on project pages | Add Disqus embed block to project pages when ready; shortname: `mitra-ai-life` |
| Video embeds | Project pages (`<video>` tag section) | Add `<video>` elements once videos are generated and uploaded to S3 |
| Cheatsheet PDFs (content) | `content/cheatsheets/` | Still need: `shell-bash.md`, `python-for-data.md`, `excel-formula-bible.md`, `c-cpp-memory.md`, `ml-models-at-a-glance.md`, `deep-learning-layers.md`, `genai-prompt-patterns.md`, `ai-for-developers.md`, `aiml-interview-prep.md` |
| ML/DL/GenAI course YAML | `data/courses/` | Add `dl.yaml`, `genai.yaml`, `agentic.yaml`, `mlops.yaml`, `rl.yaml` |

---

## 🚀 Deploy Checklist

Steps to go live on GitHub Pages:

```bash
# 1. Commit and push (CNAME, .gitignore, .env.example already set up)
git add .
git commit -m "Initial production build — mitraaiprojects.com"
git push origin main

# 2. In GitHub repo Settings → Pages → Source: GitHub Actions
# 3. First deploy runs automatically via .github/workflows/pages.yml
# 4. Site live at: https://rajendar-muddasani.github.io/mitra-ai-projects/

# 5. When custom domain is ready:
# - Add DNS CNAME record: mitraaiprojects.com → rajendar-muddasani.github.io
# - CNAME file already committed (mitraaiprojects.com)
# - Enable HTTPS in Pages settings

# 6. Local dev server (so absolute /paths/ work)
cd site && python3 -m http.server 8080
# Open: http://localhost:8080
```

---

## 🛠 Next Tasks (Priority Order)

### P1 — Deploy blockers
1. **Enable GitHub Pages** → Settings → Pages → Source: GitHub Actions → push `main`
2. **Wire Supabase anon key** → add `<script>` before `auth.js` in all pages (or build-time inject)
3. **Create Supabase tables**: `contact_submissions`, `course_completions`, `project_completions` (schemas below)

### P2 — Content gaps
4. **Generate remaining cheatsheet Markdown** → 9 more `.md` files in `content/cheatsheets/`
5. **Run cheatsheet PDF pipeline** → `generate_cheatsheets.py --all` → `deploy_s3.py --type cheatsheets`
6. **Build project-02 and project-03 pages** → run `build_project_pages.py` → flesh out manually
7. **Fix AIML-Engineering-Lab Colab links** in `site/courses/ml.html` — replace `notebook.ipynb` with real URLs

### P3 — Polish and integrations
8. **Deploy Cloudflare Worker** → `cd scripts/cloudflare-worker && wrangler deploy`
9. **Generate project hero images** → DALL-E 3 → upload to S3 → update YAML assets section
10. **Add Disqus** to project pages (shortname: `mitra-ai-life`)
11. **Generate overview videos** for project-01 → follow master plan §27 video workflow

---

## Supabase Table Schemas (run in Supabase SQL editor)

```sql
-- Contact form submissions
CREATE TABLE contact_submissions (
  id           uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  name         text,
  email        text NOT NULL,
  college      text,
  interest     text,
  message      text,
  source       text DEFAULT 'mitraaiprojects.com',
  created_at   timestamptz DEFAULT now()
);

-- Course completions
CREATE TABLE course_completions (
  id           uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id      uuid REFERENCES auth.users(id) ON DELETE CASCADE,
  course_id    text NOT NULL,
  topic_slug   text NOT NULL,
  completed_at timestamptz DEFAULT now(),
  UNIQUE(user_id, course_id, topic_slug)
);

-- Project completions
CREATE TABLE project_completions (
  id           uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id      uuid REFERENCES auth.users(id) ON DELETE CASCADE,
  project_id   text NOT NULL,
  completed_at timestamptz DEFAULT now(),
  UNIQUE(user_id, project_id)
);

-- RLS policies
ALTER TABLE contact_submissions ENABLE ROW LEVEL SECURITY;
ALTER TABLE course_completions ENABLE ROW LEVEL SECURITY;
ALTER TABLE project_completions ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone can insert contact" ON contact_submissions FOR INSERT WITH CHECK (true);
CREATE POLICY "Users see own completions" ON course_completions FOR ALL USING (auth.uid() = user_id);
CREATE POLICY "Users see own project completions" ON project_completions FOR ALL USING (auth.uid() = user_id);
```

---

## Key File Map (for Copilot context)

```
site/assets/css/main.css          ← ALL styles — edit this for any visual change
site/assets/js/main.js            ← ALL client JS — tab switching, quiz, GA4, forms
site/auth.js                      ← Supabase auth — wire anon key here
site/mitra-chat.js                ← Chatbot widget — change WORKER_URL here

site/index.html                   ← Home page
site/courses/ml.html              ← OneNote two-panel layout (most complex page)
site/courses/programming.html     ← Standard 8-tab layout (reference pattern for new courses)
site/projects/document-qa-assistant.html ← Full project kit pattern (reference for new projects)

data/projects/project-01.yaml    ← Manifest schema reference
scripts/validate_project_manifests.py ← Run after editing any YAML
scripts/generate_cheatsheets.py  ← Run to produce PDFs
scripts/deploy_s3.py             ← Run to upload to S3

.github/workflows/pages.yml      ← Deploy pipeline — push main to trigger
CNAME                             ← mitraaiprojects.com
docs/mitraaiprojects-master-plan.md ← Single source of truth — read before making decisions
```

---

## Design Tokens (for any CSS work)
```css
--primary:    #00d4aa   /* teal — main action color */
--bg-dark:    #0d1117   /* page background */
--surface:    #161b22   /* cards, sidebar */
--surface-2:  #1c2333   /* nested surfaces */
--accent:     #f0b429   /* amber — badges, callouts only */
--text:       #e6edf3   /* body text */
--muted:      #7d8590   /* secondary text */
--border:     rgba(0,212,170,0.12)
--border-dim: rgba(255,255,255,0.06)
--purple:     #7c3aed   /* certificates, rare accents */

/* Hero gradient */
background: linear-gradient(160deg, #0d1117 0%, #0d2818 50%, #0a2520 100%);

/* Fonts */
Baloo 2 → headings
Nunito  → body
JetBrains Mono → code, labels, tags
```
