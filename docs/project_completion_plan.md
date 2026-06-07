# Mitra AI Projects — Complete Work Plan

> This is the single task tracker for everything needed to make mitraaiprojects.com live, usable, and valuable.
> Status legend: ✅ Done · 🔶 Partial · ⬜ Not started
> Sections map to conversations: reference by Section + Task number (e.g. S2-T3).

---

## SECTION 1 — Platform Foundation

Everything under the hood that makes all other sections work.

### S1 Design & Theme
| # | Task | Status | Notes |
|---|---|---|---|
| S1-T1 | Design system — Plum Emerald theme applied sitewide | ✅ | main.css variables, hero, nav, CTA |
| S1-T2 | Mobile responsiveness — all pages | 🔶 | CSS grids responsive, needs testing on real devices |
| S1-T3 | Dark mode toggle (optional v2) | ⬜ | |
| S1-T4 | Favicon + OG image | ⬜ | 512×512 favicon, 1200×630 OG image for social share |
| S1-T5 | Page load speed audit | ⬜ | Google Lighthouse score target: 90+ |

### S1 Analytics & Tracking
| # | Task | Status | Notes |
|---|---|---|---|
| S1-T6 | GA4 wired in all pages | ✅ | G-QGY0LH6W93 |
| S1-T7 | GA4 custom events: course tab change, quiz attempt, project page view | ✅ | In main.js |
| S1-T8 | GA4 events: certificate claimed, cheatsheet download, video start | ⬜ | |
| S1-T9 | Google Search Console setup | ⬜ | After domain is live |
| S1-T10 | Sitemap.xml file | ⬜ | Static file in site/ |

### S1 Auth & Database
| # | Task | Status | Notes |
|---|---|---|---|
| S1-T11 | Supabase anon key wired in all HTML pages | ⬜ | Add `<script>window.__SUPABASE_ANON_KEY__='eyJ...'</script>` before auth.js |
| S1-T12 | Supabase tables created: contact_submissions | ⬜ | SQL in STATUS.md |
| S1-T13 | Supabase tables created: course_completions | ⬜ | SQL in STATUS.md |
| S1-T14 | Supabase tables created: project_completions | ⬜ | SQL in STATUS.md |
| S1-T15 | Login UI in nav (Sign In modal or page) | ⬜ | Auth flow: email link or Google OAuth |
| S1-T16 | User profile page (view completions, certificates) | ⬜ | /profile.html — v1 basic |

### S1 Infrastructure
| # | Task | Status | Notes |
|---|---|---|---|
| S1-T17 | GitHub Pages enabled (Settings → Pages → GitHub Actions) | ⬜ | One-time click in GitHub UI |
| S1-T18 | Domain purchased: mitraaiprojects.com on Namecheap | ⬜ | ~$11/yr |
| S1-T19 | DNS configured: A records + CNAME pointing to GitHub Pages | ⬜ | 4 A records + www CNAME |
| S1-T20 | HTTPS enforced in GitHub Pages settings | ⬜ | After DNS propagates |
| S1-T21 | AWS S3 .env configured for asset uploads | ⬜ | Copy from mitraailife.com .env |
| S1-T22 | Cloudflare Worker deployed: mitra-projects-worker | ⬜ | `wrangler deploy` in scripts/cloudflare-worker/ |

---

## SECTION 2 — Course Content

Seven course tracks. Each track has multiple topics. Each topic needs the same structure.

### What every topic needs (the content checklist)
- [ ] Plain-English explanation (what it is, when to use it, when NOT to)
- [ ] Key concepts table (3–5 bullet points)
- [ ] Code example block (runnable or readable)
- [ ] Embedded notebook (Pyodide or Colab link — see S5)
- [ ] 5-question quiz with explanations
- [ ] Cheatsheet download button (links to S3 PDF)
- [ ] Link to a related project in the Projects catalog
- [ ] Completion record (logged to Supabase on quiz pass)

### S2 Programming Track (`/courses/programming.html`) — 8 tabs
| # | Tab | Content status | Notebook | Quiz | Cheatsheet |
|---|---|---|---|---|---|
| S2-T1 | Python Basics | 🔶 Stub content | ⬜ | ⬜ | ⬜ |
| S2-T2 | Python for Data | 🔶 Stub | ⬜ | ⬜ | ⬜ |
| S2-T3 | Shell / Bash | 🔶 Stub | ⬜ | ⬜ | ⬜ |
| S2-T4 | SQL | 🔶 Stub | ⬜ | ⬜ | ⬜ |
| S2-T5 | Excel Formulas | 🔶 Stub | ⬜ | ⬜ | ⬜ |
| S2-T6 | C / C++ | 🔶 Stub | ⬜ | ⬜ | ⬜ |
| S2-T7 | JavaScript | 🔶 Stub | ⬜ | ⬜ | ⬜ |
| S2-T8 | Perl | 🔶 Stub | ⬜ | ⬜ | ⬜ |

### S2 Machine Learning Track (`/courses/ml.html`) — 10 tabs (OneNote layout)
| # | Tab | Content status | Notebook | Quiz | Cheatsheet |
|---|---|---|---|---|---|
| S2-T9 | Linear Regression | 🔶 Stub | ⬜ Colab link needed | ⬜ | ⬜ |
| S2-T10 | Classification | 🔶 Stub | ⬜ | ⬜ | ⬜ |
| S2-T11 | Tree-Based Learning | 🔶 Stub | ⬜ | ⬜ | ⬜ |
| S2-T12 | Boosting | 🔶 Stub | ⬜ | ⬜ | ⬜ |
| S2-T13 | SVM | 🔶 Stub | ⬜ | ⬜ | ⬜ |
| S2-T14 | Clustering | 🔶 Stub | ⬜ | ⬜ | ⬜ |
| S2-T15 | Anomaly Detection | 🔶 Stub | ⬜ | ⬜ | ⬜ |
| S2-T16 | Naive Bayes / LDA | 🔶 Stub | ⬜ | ⬜ | ⬜ |
| S2-T17 | Time Series | 🔶 Stub | ⬜ | ⬜ | ⬜ |
| S2-T18 | Hyperparameter Opt | 🔶 Stub | ⬜ | ⬜ | ⬜ |
> Source repos: AIML-Engineering-Lab 001–010. Link each tab to the matching Colab notebook.

### S2 Deep Learning Track (`/courses/dl.html`) — 8 tabs
| # | Tab | Status | Source |
|---|---|---|---|
| S2-T19 | Neural Network Basics | 🔶 Stub | New content |
| S2-T20 | CNNs | 🔶 Stub | AIML-Lab 054 |
| S2-T21 | RNNs / LSTMs | 🔶 Stub | AIML-Lab 015 |
| S2-T22 | Autoencoders & GANs | 🔶 Stub | AIML-Lab 014 |
| S2-T23 | Transformers | 🔶 Stub | AIML-Lab 073 |
| S2-T24 | Multimodal Models | 🔶 Stub | AIML-Lab 034 |
| S2-T25 | Transfer Learning | 🔶 Stub | New content |
| S2-T26 | Model Compression | 🔶 Stub | New content |

### S2 Generative AI Track (`/courses/genai.html`) — 8 tabs
| # | Tab | Status | Source |
|---|---|---|---|
| S2-T27 | What is GenAI | 🔶 Stub | New content |
| S2-T28 | Prompt Engineering | 🔶 Stub | New content |
| S2-T29 | RAG | 🔶 Stub | AIML-Lab 074 + chromadb-rag-tutorials |
| S2-T30 | Fine-Tuning | 🔶 Stub | AIML-Lab 075 |
| S2-T31 | Embeddings & Vector DBs | 🔶 Stub | Chroma, Pinecone, Supabase pgvector |
| S2-T32 | LLM Evaluation | 🔶 Stub | New content |
| S2-T33 | HuggingFace Ecosystem | 🔶 Stub | New content |
| S2-T34 | Kaggle with LLMs | 🔶 Stub | New content |

### S2 Agentic AI & MCP Track (`/courses/agentic.html`) — 7 tabs
| # | Tab | Status | Source |
|---|---|---|---|
| S2-T35 | What is an Agent | 🔶 Stub | New content |
| S2-T36 | LangGraph | 🔶 Stub | Private: langchain-learning-guide |
| S2-T37 | CrewAI | 🔶 Stub | Private: crewai-course-materials |
| S2-T38 | MCP Protocol | 🔶 Stub | Private: mcp-learning-guide |
| S2-T39 | OpenAI Assistants API | 🔶 Stub | New content |
| S2-T40 | Multi-Agent Systems | 🔶 Stub | New content |
| S2-T41 | Evaluation & Safety | 🔶 Stub | New content |

### S2 MLOps & Tools Track (`/courses/mlops.html`) — 7 tabs
| # | Tab | Status | Source |
|---|---|---|---|
| S2-T42 | Airflow Orchestration | 🔶 Stub | AIML-Lab 053 |
| S2-T43 | Spark & Big Data | 🔶 Stub | Private: spark-learning-guide |
| S2-T44 | Experiment Tracking | 🔶 Stub | MLflow concepts |
| S2-T45 | Kubernetes for ML | 🔶 Stub | New content |
| S2-T46 | Docker for ML | 🔶 Stub | New content |
| S2-T47 | AWS SageMaker | 🔶 Stub | New content |
| S2-T48 | CI/CD for Models | 🔶 Stub | New content |

### S2 Reinforcement Learning Track (`/courses/rl.html`) — 6 tabs (marked Planned)
| # | Tab | Status |
|---|---|---|
| S2-T49 | What is RL | ⬜ |
| S2-T50 | Q-Learning | ⬜ |
| S2-T51 | Deep Q Networks | ⬜ |
| S2-T52 | Policy Gradients | ⬜ |
| S2-T53 | PPO | ⬜ |
| S2-T54 | Real-world RL | ⬜ |

---

## SECTION 3 — Embedded Python Notebooks

**Answer: Yes, Python notebooks can be embedded in-site. Here are the options:**

### Option A — Pyodide (Recommended for v1)
Runs Python directly in the browser via WebAssembly. No server needed. Works on GitHub Pages.
- Supports: numpy, pandas, matplotlib, scikit-learn (via micropip)
- Does NOT support: PyTorch, TensorFlow (too large), file system access
- Best for: ML concept demos, data manipulation, small model training
- Integration: One `<script>` tag loads Pyodide, CodeMirror editor for input
- Load time: ~10–15 seconds first load (WebAssembly download)

### Option B — JupyterLite
Full Jupyter notebook experience that runs entirely in the browser.
- Can be hosted on GitHub Pages as a separate URL: `mitraaiprojects.com/lab/`
- Supports most of the scientific Python stack
- Students can run and modify notebooks without any setup

### Option C — Colab Links (Quickest to implement)
- Each topic gets a "Run in Colab" button linking to AIML-Engineering-Lab notebooks
- Zero implementation cost, runs on Google's infrastructure
- Limitation: students need a Google account, can't track completion

### Recommendation
- Phase 1 (launch): Colab links for all ML/DL/GenAI topics (zero effort, great UX)
- Phase 2: Pyodide embedded for Programming + ML concept demos
- Phase 3: JupyterLite for interactive full notebooks

### S3 Notebook Tasks
| # | Task | Status |
|---|---|---|
| S3-T1 | Add "Open in Colab" button component to course tab template | ⬜ |
| S3-T2 | Map all 10 ML topics to AIML-Engineering-Lab Colab URLs | ⬜ |
| S3-T3 | Map DL topics (014, 015, 034, 054, 073) to Colab URLs | ⬜ |
| S3-T4 | Integrate Pyodide loader in main.js | ⬜ |
| S3-T5 | Build interactive Python code block component | ⬜ |
| S3-T6 | Add Pyodide demos to Programming track (Python Basics tab first) | ⬜ |
| S3-T7 | Explore JupyterLite deployment on GitHub Pages subpath | ⬜ |

---

## SECTION 4 — Project Kits

### Philosophy: What We Give vs What Students Do

**We provide the scaffolding. Students do the building.**

| We Provide | Student Does |
|---|---|
| Problem statement + scope boundaries | Reads and understands the goal |
| Architecture diagram (labelled, explained) | Implements the connections |
| Skeleton code (file structure + empty functions with docstrings) | Fills in the logic |
| requirements.txt + .env.example + README template | Sets up their environment |
| Week-by-week milestone plan | Follows the plan, hits each checkpoint |
| Test cases and expected outputs | Runs tests, debugs, makes it pass |
| Concept explanation per component | Uses it to understand what they're building |
| Deployment guide (Render / Railway / Hugging Face Spaces) | Deploys their own instance |
| Report template (pre-structured) | Writes content in the structure |
| PPT template (pre-designed slides) | Fills in their outcomes |
| 20+ viva Q&A (questions + model answers) | Practices, then answers in their own words |
| Extension ideas (things to add for extra marks) | Chooses which to implement |

**What NOT to give:** Full working solution code. That would make the project meaningless.

---

### S4 How Many Projects and How to Manage

**Target: 20–30 project kits over time. Launch with 6.**

Naming: `project-01` through `project-XX` internally. Each has a human title.

**Lane distribution targets:**
- Guided Mini Projects (2–4 weeks): 6–8 kits — quick wins for 2nd/3rd year
- Major Project Kits (8–16 weeks): 8–10 kits — final-year thesis material
- Portfolio Builds (4–8 weeks): 6–8 kits — placement-focused
- Viva & Submission Packs: 4–6 support kits — add-ons for any project

**How students use it:**
1. Student picks a project by lane, topic, or tech stack
2. Reads the overview + architecture
3. Clones the skeleton repo (or copies the structure manually)
4. Follows the milestone plan week by week
5. Uses viva Q&A to prepare for presentation
6. Uses report/PPT templates for submission
7. Deploys their version for demo URL

---

### S4 Planned Project Kits (26 total)

#### Mini Projects (quick wins)
| ID | Project | Tech Stack | Status |
|---|---|---|---|
| P-M1 | Sentiment Analyzer Web App | Python, Streamlit, HuggingFace | ⬜ |
| P-M2 | Resume Parser & Scorer | Python, spaCy, PDF extraction | ⬜ |
| P-M3 | News Category Classifier | scikit-learn, TF-IDF, Streamlit | ⬜ |
| P-M4 | Personal Expense Tracker with AI | Python, pandas, OpenAI | ⬜ |
| P-M5 | CLI Chatbot with Memory | Python, OpenAI, JSON state | ⬜ |
| P-M6 | Image Caption Generator | HuggingFace BLIP, Streamlit | ⬜ |

#### Major Project Kits (thesis-ready)
| ID | Project | Tech Stack | Status |
|---|---|---|---|
| P-J1 | Document Q&A Assistant | Python, FastAPI, RAG, OpenAI, ChromaDB | 🔶 Page live, kit content partial |
| P-J2 | AI Resume Screener & Interview Copilot | Python, LLM, Streamlit | ⬜ Page stub exists |
| P-J3 | Inventory Forecasting Dashboard | Python, ARIMA, Prophet, Streamlit | ⬜ Page stub exists |
| P-J4 | Multilingual Customer Support Bot | Python, FastAPI, OpenAI, Multilingual | ⬜ |
| P-J5 | AI Attendance & Analytics Dashboard | Python, OpenCV, face_recognition, Streamlit | ⬜ |
| P-J6 | Vision-Based Quality Inspection | Python, YOLO, PyTorch, FastAPI | ⬜ |
| P-J7 | Medical Report Summarizer | Python, LLM, PDF parsing | ⬜ |
| P-J8 | Stock Price Predictor + Dashboard | Python, LSTM, Streamlit, yfinance | ⬜ |
| P-J9 | Smart FAQ Bot for College Website | RAG, ChromaDB, FastAPI | ⬜ |
| P-J10 | AI-Powered Code Review Assistant | OpenAI, GitHub API, Streamlit | ⬜ |

#### Portfolio Builds (placement-focused)
| ID | Project | Focus | Status |
|---|---|---|---|
| P-P1 | Full-Stack AI Dashboard | React + FastAPI + ML model | ⬜ |
| P-P2 | LangGraph Multi-Agent Research Tool | LangGraph, tools, memory | ⬜ |
| P-P3 | End-to-End MLOps Pipeline | Docker, MLflow, GitHub Actions | ⬜ |
| P-P4 | RAG API with Authentication | FastAPI, Supabase, OpenAI | ⬜ |
| P-P5 | Computer Vision API Service | FastAPI, YOLO, Docker, Render deploy | ⬜ |
| P-P6 | CrewAI Business Intelligence Agent | CrewAI, tools, report generation | ⬜ |

#### Viva & Submission Packs (support layer)
| ID | Pack | What's in it | Status |
|---|---|---|---|
| P-V1 | ML Project Viva Pack | 40 ML viva Q&A + common mistakes | ⬜ |
| P-V2 | DL Project Viva Pack | 30 DL viva Q&A | ⬜ |
| P-V3 | GenAI Project Viva Pack | 35 GenAI + RAG viva Q&A | ⬜ |
| P-V4 | Generic CS Project Report Template | Word + Google Docs, all sections | ⬜ |

### S4 Per-Kit Content Tasks (repeat for each kit)
| # | Task |
|---|---|
| S4-T1 | Write project overview (problem statement, scope, what you build) |
| S4-T2 | Create architecture diagram (draw.io / Excalidraw → export PNG → S3) |
| S4-T3 | Create skeleton GitHub repo (file structure + empty functions) |
| S4-T4 | Write milestone breakdown (week-by-week plan) |
| S4-T5 | Write concept explanations for each component |
| S4-T6 | Write deployment guide (Render.com or Railway step-by-step) |
| S4-T7 | Write 20+ viva Q&A |
| S4-T8 | Create report template (Google Docs link or downloadable) |
| S4-T9 | Create PPT template (Google Slides or PPTX download) |
| S4-T10 | Build the project page HTML (or generate from manifest) |
| S4-T11 | Upload hero image to S3 |
| S4-T12 | Create project YAML manifest in data/projects/ |

---

## SECTION 5 — Portfolio Building Track

### Goal
Help students and professionals build a GitHub profile that gets noticed in placement interviews and job applications.

### What "portfolio-ready" means
A student's GitHub should have:
- 3–5 projects with clean READMEs and live demo links
- Deployed instances (not just code that "works locally")
- Architecture diagrams in README
- A pinned "portfolio introduction" repo
- Projects that show breadth: one ML, one LLM/GenAI, one deployed API

### S5 Portfolio Building Tasks
| # | Task | Status |
|---|---|---|
| S5-T1 | Write "Build Your AI Portfolio" guide page (`/portfolio-guide.html`) | ⬜ |
| S5-T2 | GitHub Profile README template (markdown with project showcase format) | ⬜ |
| S5-T3 | README template per project (architecture, setup, demo link, tech stack) | ⬜ |
| S5-T4 | "Deploy your project" mini-guide: Render.com + Railway + Hugging Face Spaces | ⬜ |
| S5-T5 | LinkedIn profile optimization tips page | ⬜ |
| S5-T6 | "Portfolio checklist" printable / downloadable PDF | ⬜ |
| S5-T7 | Add "Portfolio Build" filter and page section on /projects/ | ✅ Lane filter done |
| S5-T8 | Interview preparation guide page (`/interview-prep.html`) | ⬜ |
| S5-T9 | "AI/ML Interview Questions" cheatsheet (add to cheatsheets) | ⬜ |

---

## SECTION 6 — Cheatsheets

All cheatsheets should be A4 PDF, dark-themed, downloadable, hosted on S3.

| # | Title | Markdown source | PDF generated | S3 uploaded |
|---|---|---|---|---|
| C1 | Python Basics | ✅ | ⬜ | ⬜ |
| C2 | Python for Data (Pandas / NumPy) | ⬜ | ⬜ | ⬜ |
| C3 | SQL Quick Reference | ✅ | ⬜ | ⬜ |
| C4 | Shell / Bash | ⬜ | ⬜ | ⬜ |
| C5 | Excel Formula Bible | ⬜ | ⬜ | ⬜ |
| C6 | C/C++ Memory | ⬜ | ⬜ | ⬜ |
| C7 | ML Models at a Glance | ⬜ | ⬜ | ⬜ |
| C8 | Deep Learning Layers | ⬜ | ⬜ | ⬜ |
| C9 | GenAI Prompt Patterns | ⬜ | ⬜ | ⬜ |
| C10 | AI for Developers Prompts | ⬜ | ⬜ | ⬜ |
| C11 | AIML Interview Prep | ⬜ | ⬜ | ⬜ |
| C12 | Portfolio & GitHub Profile | ⬜ | ⬜ | ⬜ |

**To generate PDFs:** `python scripts/generate_cheatsheets.py --all`
**To upload to S3:** `python scripts/deploy_s3.py --type cheatsheets`

---

## SECTION 7 — Tools Coverage

The platform should help learners understand and use the most important AI/ML tools. Each tool should appear in at least one course tab or project kit.

### Core Python Stack
| Tool | Course tab | Project using it |
|---|---|---|
| numpy | Programming → Python for Data | P-M3 |
| pandas | Programming → Python for Data | P-J3 |
| matplotlib / seaborn | Programming → Python for Data | P-J3 |
| scikit-learn | ML all tabs | P-M3, P-J2 |
| XGBoost / LightGBM | ML → Boosting | P-J3 |

### Deep Learning
| Tool | Course tab | Project using it |
|---|---|---|
| PyTorch | DL → Neural Networks | P-J6, P-P5 |
| TensorFlow/Keras | DL → CNNs | P-J5 |
| HuggingFace Transformers | DL → Transformers, GenAI | P-M6, P-J7 |
| YOLO (Ultralytics) | DL → CNNs | P-J6, P-P5 |

### LLM & GenAI
| Tool | Course tab | Project using it |
|---|---|---|
| OpenAI API | GenAI → Prompt Eng | P-J1, P-J4, P-J10 |
| LangChain | GenAI → RAG | P-J1, P-J9 |
| LangGraph | Agentic → LangGraph | P-P2 |
| CrewAI | Agentic → CrewAI | P-P6 |
| ChromaDB | GenAI → RAG | P-J1, P-J9 |
| Pinecone | GenAI → Vector DBs | P-P4 |

### Backend & Deployment
| Tool | Course tab | Project using it |
|---|---|---|
| FastAPI | MLOps | P-J1, P-J4, P-P4, P-P5 |
| Streamlit | — | P-M1, P-J2, P-J3, P-J5 |
| Docker | MLOps → Docker | P-P3, P-P5 |
| GitHub Actions | MLOps → CI/CD | P-P3 |
| MLflow | MLOps → Experiment Tracking | P-P3 |
| Render.com deploy | Deployment guides | All portfolio builds |

### Data & Databases
| Tool | Course tab | Project using it |
|---|---|---|
| SQL | Programming → SQL | P-P4 |
| Supabase | — | P-P4 |
| MongoDB | — | Future project |
| Airflow | MLOps → Airflow | Future project |

---

## SECTION 8 — Certificates

| # | Task | Status |
|---|---|---|
| S8-T1 | Certificate HTML template | ⬜ |
| S8-T2 | Unique certificate ID generation (UUID on Supabase) | ⬜ |
| S8-T3 | Certificate verification page (`/verify.html?id=xxx`) | ⬜ |
| S8-T4 | PDF download of certificate | ⬜ |
| S8-T5 | Certificate wording reviewed for legal compliance (no degree claims) | ⬜ |

---

## SECTION 9 — Legal & Support Pages

| # | Page | Status |
|---|---|---|
| S9-T1 | Privacy Policy | ✅ `/privacy.html` |
| S9-T2 | Terms of Service | ✅ `/terms.html` |
| S9-T3 | About page | ✅ `/about.html` |
| S9-T4 | Contact form (Supabase insert) | 🔶 Form exists, Supabase table not created yet |
| S9-T5 | FAQ page | ✅ `/faq.html` |
| S9-T6 | How It Works page | ✅ `/how-it-works.html` |
| S9-T7 | Portfolio Guide page | ⬜ |
| S9-T8 | Interview Prep page | ⬜ |

---

## SECTION 10 — Launch Checklist (Go-Live Gate)

Do not announce or share the site publicly until ALL of these are green.

| # | Item | Status |
|---|---|---|
| L1 | Domain purchased and DNS configured | ⬜ |
| L2 | HTTPS enforced | ⬜ |
| L3 | GitHub Pages enabled and first deploy green | ⬜ |
| L4 | Supabase anon key wired in all pages | ⬜ |
| L5 | Supabase tables created | ⬜ |
| L6 | Contact form tested end-to-end | ⬜ |
| L7 | Home page content final and approved | ✅ |
| L8 | At least 1 course with full content (ML recommended) | ⬜ |
| L9 | At least 2 project kits with full content | ⬜ |
| L10 | At least 5 cheatsheets uploaded to S3 | ⬜ |
| L11 | Mobile responsiveness verified on real device | ⬜ |
| L12 | GA4 verified in Google Analytics dashboard | ⬜ |
| L13 | All nav links working, no broken pages | 🔶 |
| L14 | OG image set (social share preview) | ⬜ |
| L15 | Google Search Console verified | ⬜ |

---

## Work Order (Recommended sequence)

**Sprint 1 — Get it live with minimal content**
1. S1-T17: Enable GitHub Pages
2. S1-T11: Wire Supabase key
3. S1-T12/13/14: Create Supabase tables
4. S1-T18–S1-T20: Buy domain, configure DNS, HTTPS
5. S9-T4: Test contact form end to end
6. S3-T2: Add Colab links to ML course
7. C1+C3: Generate first 2 cheatsheets, upload to S3
8. P-J1: Complete Document Q&A project kit content
9. Verify L1–L15

**Sprint 2 — Fill course content**
10. ML track: complete all 10 tab content + quizzes
11. Programming track: complete Python Basics + SQL tabs
12. Generate remaining cheatsheets

**Sprint 3 — Project kits**
13. Complete P-J2 (Resume Screener) full kit
14. Complete P-J3 (Forecasting Dashboard) full kit
15. Build 2 mini project kits (P-M1, P-M2)

**Sprint 4 — Portfolio building track**
16. Portfolio guide page
17. GitHub README templates
18. Interview prep page

---

*Last updated: 2026-06-07. Reference tasks as S<section>-T<number> in conversation.*
