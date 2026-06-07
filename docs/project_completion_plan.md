# Mitra AI Projects — Complete Work Plan

> Reference tasks as **S\<section\>-T\<number\>** in conversation (e.g. S1-T3).
> Status: ✅ Done · 🔶 Partial · ❌ Not started

---

## S1 — Platform Foundation

| ID | Task | Status | Notes |
|---|---|---|---|
| S1-T1 | Plum Emerald theme — CSS variables, hero, nav, CTA | ✅ | main.css |
| S1-T2 | Fix dark hero on inner pages (.hero-sm, .project-hero) | ✅ | Light plum gradient |
| S1-T3 | Fix teal remnants — all rgba colors updated to plum | ✅ | |
| S1-T4 | Mobile nav — white background, shadow | ✅ | |
| S1-T5 | Mobile responsiveness — grid collapse, hero, tabs | 🔶 | CSS done, needs real device test |
| S1-T6 | Favicon SVG | ✅ | site/favicon.svg, linked in all pages |
| S1-T7 | OG image (1200×630) for social share preview | ❌ | Upload to S3 shared/ |
| S1-T8 | Page load speed — Google Lighthouse 90+ | ❌ | After content is in |
| S1-T9 | GA4 wired in all pages | ✅ | G-QGY0LH6W93 |
| S1-T10 | GA4 custom events (tab change, quiz, cert, video, download) | ✅ | All in main.js |
| S1-T11 | Google Search Console setup | ❌ | After domain live |
| S1-T12 | sitemap.xml in site/ root | ✅ | All 18 pages listed |
| S1-T13 | Supabase anon key — config.js wired in all pages | ✅ | Edit site/config.js with real key |
| S1-T14 | Supabase table: contact_submissions | ❌ | Manual: run scripts/supabase_setup.sql |
| S1-T15 | Supabase table: course_completions | ❌ | Manual: same SQL file |
| S1-T16 | Supabase table: project_completions + certificates | ❌ | Manual: same SQL file |
| S1-T17 | Login UI — Sign In modal (Google + email magic link) | ✅ | Injected via main.js |
| S1-T18 | User profile page /profile.html | ✅ | Shows completions + certificates |
| S1-T19 | GitHub Pages enabled (Settings → Pages → GitHub Actions) | ❌ | One click in GitHub UI |
| S1-T20 | Domain purchased: mitraaiprojects.com on Namecheap | ❌ | ~$11/yr |
| S1-T21 | DNS: 4 A records + www CNAME → GitHub Pages | ❌ | After S1-T20 |
| S1-T22 | HTTPS enforced in GitHub Pages settings | ❌ | After S1-T21 |
| S1-T23 | AWS S3 .env configured for asset uploads | ❌ | Copy from mitraailife .env |
| S1-T24 | Cloudflare Worker deployed: mitra-projects-worker | ❌ | `wrangler deploy` |

---

## S2 — Course Content

> Every topic needs: explanation · code example · Colab/Pyodide notebook · 5-question quiz · cheatsheet link · completion record

### Programming Track — 8 tabs
| ID | Tab | Content | Notebook | Quiz | Cheatsheet |
|---|---|---|---|---|---|
| S2-T1 | Python Basics | 🔶 Stub | ❌ | ❌ | ❌ |
| S2-T2 | Python for Data (Pandas/NumPy) | 🔶 Stub | ❌ | ❌ | ❌ |
| S2-T3 | Shell / Bash | 🔶 Stub | ❌ | ❌ | ❌ |
| S2-T4 | SQL | 🔶 Stub | ❌ | ❌ | ❌ |
| S2-T5 | Excel Formulas | 🔶 Stub | ❌ | ❌ | ❌ |
| S2-T6 | C / C++ | 🔶 Stub | ❌ | ❌ | ❌ |
| S2-T7 | JavaScript | 🔶 Stub | ❌ | ❌ | ❌ |
| S2-T8 | Perl | 🔶 Stub | ❌ | ❌ | ❌ |

### Machine Learning Track — 10 tabs (OneNote layout)
| ID | Tab | Content | Colab link | Quiz | Cheatsheet |
|---|---|---|---|---|---|
| S2-T9 | Linear Regression | 🔶 Stub | ❌ AIML-Lab 001 | ❌ | ❌ |
| S2-T10 | Classification | 🔶 Stub | ❌ AIML-Lab 002 | ❌ | ❌ |
| S2-T11 | Tree-Based Learning | 🔶 Stub | ❌ AIML-Lab 003 | ❌ | ❌ |
| S2-T12 | Boosting | 🔶 Stub | ❌ AIML-Lab 004 | ❌ | ❌ |
| S2-T13 | SVM | 🔶 Stub | ❌ AIML-Lab 005 | ❌ | ❌ |
| S2-T14 | Clustering | 🔶 Stub | ❌ AIML-Lab 006 | ❌ | ❌ |
| S2-T15 | Anomaly Detection | 🔶 Stub | ❌ AIML-Lab 007 | ❌ | ❌ |
| S2-T16 | Naive Bayes / LDA | 🔶 Stub | ❌ AIML-Lab 008 | ❌ | ❌ |
| S2-T17 | Time Series | 🔶 Stub | ❌ AIML-Lab 009 | ❌ | ❌ |
| S2-T18 | Hyperparameter Opt | 🔶 Stub | ❌ AIML-Lab 010 | ❌ | ❌ |

### Deep Learning Track — 8 tabs
| ID | Tab | Content | Source repo | Quiz | Cheatsheet |
|---|---|---|---|---|---|
| S2-T19 | Neural Network Basics | 🔶 Stub | New content | ❌ | ❌ |
| S2-T20 | CNNs | 🔶 Stub | AIML-Lab 054 | ❌ | ❌ |
| S2-T21 | RNNs / LSTMs | 🔶 Stub | AIML-Lab 015 | ❌ | ❌ |
| S2-T22 | Autoencoders & GANs | 🔶 Stub | AIML-Lab 014 | ❌ | ❌ |
| S2-T23 | Transformers | 🔶 Stub | AIML-Lab 073 | ❌ | ❌ |
| S2-T24 | Multimodal Models | 🔶 Stub | AIML-Lab 034 | ❌ | ❌ |
| S2-T25 | Transfer Learning | 🔶 Stub | New content | ❌ | ❌ |
| S2-T26 | Model Compression | 🔶 Stub | New content | ❌ | ❌ |

### Generative AI Track — 8 tabs
| ID | Tab | Content | Source | Quiz | Cheatsheet |
|---|---|---|---|---|---|
| S2-T27 | What is GenAI | 🔶 Stub | New | ❌ | ❌ |
| S2-T28 | Prompt Engineering | 🔶 Stub | New | ❌ | ❌ |
| S2-T29 | RAG | 🔶 Stub | AIML-Lab 074 | ❌ | ❌ |
| S2-T30 | Fine-Tuning | 🔶 Stub | AIML-Lab 075 | ❌ | ❌ |
| S2-T31 | Embeddings & Vector DBs | 🔶 Stub | New | ❌ | ❌ |
| S2-T32 | LLM Evaluation | 🔶 Stub | New | ❌ | ❌ |
| S2-T33 | HuggingFace Ecosystem | 🔶 Stub | New | ❌ | ❌ |
| S2-T34 | Kaggle with LLMs | 🔶 Stub | New | ❌ | ❌ |

### Agentic AI & MCP Track — 7 tabs
| ID | Tab | Content | Source | Quiz | Cheatsheet |
|---|---|---|---|---|---|
| S2-T35 | What is an Agent | 🔶 Stub | New | ❌ | ❌ |
| S2-T36 | LangGraph | 🔶 Stub | Private: langchain-learning-guide | ❌ | ❌ |
| S2-T37 | CrewAI | 🔶 Stub | Private: crewai-course-materials | ❌ | ❌ |
| S2-T38 | MCP Protocol | 🔶 Stub | Private: mcp-learning-guide | ❌ | ❌ |
| S2-T39 | OpenAI Assistants API | 🔶 Stub | New | ❌ | ❌ |
| S2-T40 | Multi-Agent Systems | 🔶 Stub | New | ❌ | ❌ |
| S2-T41 | Evaluation & Safety | 🔶 Stub | New | ❌ | ❌ |

### MLOps & Tools Track — 7 tabs
| ID | Tab | Content | Source | Quiz | Cheatsheet |
|---|---|---|---|---|---|
| S2-T42 | Airflow Orchestration | 🔶 Stub | AIML-Lab 053 | ❌ | ❌ |
| S2-T43 | Spark & Big Data | 🔶 Stub | spark-learning-guide | ❌ | ❌ |
| S2-T44 | Experiment Tracking (MLflow) | 🔶 Stub | New | ❌ | ❌ |
| S2-T45 | Kubernetes for ML | 🔶 Stub | New | ❌ | ❌ |
| S2-T46 | Docker for ML | 🔶 Stub | New | ❌ | ❌ |
| S2-T47 | AWS SageMaker | 🔶 Stub | New | ❌ | ❌ |
| S2-T48 | CI/CD for Models | 🔶 Stub | New | ❌ | ❌ |

### Key Concepts & Tools Track — 8 tabs (NEW)
| ID | Tab | Content | Notes |
|---|---|---|---|
| S2-T49 | GPU Training on Kaggle (free T4/P100) | ❌ | How to enable GPU, time limits, saving work |
| S2-T50 | Google Colab — free & pro | ❌ | GPU usage, Drive mount, session persistence |
| S2-T51 | AWS EC2 with GPU (p2/p3 instances) | ❌ | Setup guide, cost management, spot instances |
| S2-T52 | PyTorch — foundations | ❌ | Tensors, autograd, training loop, GPU move |
| S2-T53 | TensorFlow / Keras — foundations | ❌ | Model API, callbacks, saving, export |
| S2-T54 | PyTorch vs TensorFlow — when to use which | ❌ | Side-by-side comparison, industry usage |
| S2-T55 | Jupyter & VS Code for ML | ❌ | Notebook best practices, extensions, debugging |
| S2-T56 | Git & GitHub for ML Projects | ❌ | .gitignore for models, DVC basics, clean commits |

### Reinforcement Learning Track — 6 tabs (Planned later)
| ID | Tab | Status |
|---|---|---|
| S2-T57 | What is RL | ❌ |
| S2-T58 | Q-Learning | ❌ |
| S2-T59 | Deep Q Networks | ❌ |
| S2-T60 | Policy Gradients | ❌ |
| S2-T61 | PPO | ❌ |
| S2-T62 | Real-world RL | ❌ |

---

## S3 — Embedded Notebooks

> **DECISION (final, do not revisit):** Use **JupyterLite only**. No Colab links, no Pyodide.
>
> - Colab opens externally (Google's site), notebooks live in student's Google Drive — not in our platform. Adds no value to our UX and creates intermediate/throwaway work.
> - Pyodide requires building a custom editor, has no notebook persistence.
> - **JupyterLite** runs entirely in-browser, saves to student's browser IndexedDB (persistent across sessions), exports `.ipynb` anytime, familiar Jupyter UI, deploys to GitHub Pages for free via one GitHub Action template. This is the final production solution.
>
> How it works for students: Notebooks live at `mitraaiprojects.com/lab/`. Each course tab embeds the relevant notebook via `<iframe>`. Student opens it, does their work, closes tab, comes back later — work is still there. Can export `.ipynb` to save locally or continue on another device.

| ID | Task | Status |
|---|---|---|
| S3-T1 | Set up JupyterLite repo (use jupyterlite/demo GitHub template) | ❌ |
| S3-T2 | Configure GitHub Action to deploy JupyterLite to /lab/ subpath | ❌ |
| S3-T3 | Create starter .ipynb notebooks for ML track (10 notebooks, one per topic) | ❌ |
| S3-T4 | Create starter .ipynb notebooks for Programming track (Python Basics first) | ❌ |
| S3-T5 | Create starter .ipynb notebooks for Key Concepts track (PyTorch, TF) | ❌ |
| S3-T6 | Create starter .ipynb notebooks for DL track (sourced from AIML-Lab 014,015,034,054,073) | ❌ |
| S3-T7 | Embed JupyterLite iframe component in course tab HTML panels | ❌ |
| S3-T8 | Test persistence: close browser, reopen, verify notebook state is retained | ❌ |

---

## S4 — Project Kits

### Philosophy: What We Give vs What Students Do
| We Provide (Scaffold) | Student Does (Build) |
|---|---|
| Problem statement + scope | Reads, understands, adapts to their college requirement |
| Architecture diagram + explanation | Implements the connections between components |
| Skeleton code (file structure + empty functions with docstrings) | Fills in the actual logic |
| requirements.txt + .env.example + README template | Sets up environment, fills in their details |
| Week-by-week milestone plan | Follows the plan, hits checkpoints |
| Test cases + expected outputs | Runs tests, debugs, makes it pass |
| Deployment guide (Render/Railway step-by-step) | Deploys their own live instance |
| Report template (pre-structured A4) | Writes their own content in the structure |
| PPT template (10-slide pre-designed) | Fills in their outcomes and screenshots |
| 20+ viva Q&A (questions + model answers) | Practices, then answers in their own words |
| Extension ideas for extra marks | Chooses which to implement |

### Per-Kit Content Checklist (repeat for each project)
| # | Deliverable | Notes |
|---|---|---|
| K-1 | Project overview page (HTML) | Use build_project_pages.py + flesh out |
| K-2 | Architecture diagram | draw.io / Excalidraw → PNG → S3 |
| K-3 | Skeleton GitHub repo | File structure + empty functions + docstrings |
| K-4 | Milestone breakdown (week-by-week) | 4–8 milestones depending on lane |
| K-5 | Concept explanations per component | Why each tech choice was made |
| K-6 | Deployment guide | Render.com or Railway step-by-step |
| K-7 | 20+ Viva Q&A | Questions + model answers |
| K-8 | Report template | Google Docs or DOCX download link |
| K-9 | PPT template | Google Slides or PPTX |
| K-10 | YAML manifest in data/projects/ | Validated by validate_project_manifests.py |
| K-11 | Hero image | DALL-E 3 → S3 |

### Mini Projects (2–4 weeks, 2nd/3rd year)
| ID | Project | Tech Stack | Page | Kit complete |
|---|---|---|---|---|
| P-M1 | Sentiment Analyzer Web App | Streamlit, HuggingFace | ❌ | ❌ |
| P-M2 | Resume Parser & Scorer | Python, spaCy, PDF | ❌ | ❌ |
| P-M3 | News Category Classifier | scikit-learn, TF-IDF | ❌ | ❌ |
| P-M4 | Personal Expense Tracker with AI | Python, pandas, OpenAI | ❌ | ❌ |
| P-M5 | CLI Chatbot with Memory | Python, OpenAI, JSON | ❌ | ❌ |
| P-M6 | Image Caption Generator | HuggingFace BLIP, Streamlit | ❌ | ❌ |

### Major Project Kits (8–16 weeks, final-year)
| ID | Project | Tech Stack | Page | Kit complete |
|---|---|---|---|---|
| P-J1 | Document Q&A Assistant | FastAPI, RAG, OpenAI, ChromaDB | 🔶 Live | 🔶 Partial |
| P-J2 | AI Resume Screener & Interview Copilot | LLM, Streamlit, PDF parsing | 🔶 Stub | ❌ |
| P-J3 | Inventory Forecasting Dashboard | ARIMA, Prophet, Streamlit | 🔶 Stub | ❌ |
| P-J4 | Multilingual Customer Support Bot | FastAPI, OpenAI | ❌ | ❌ |
| P-J5 | AI Attendance & Analytics Dashboard | OpenCV, face_recognition | ❌ | ❌ |
| P-J6 | Vision-Based Quality Inspection | YOLO, PyTorch, FastAPI | ❌ | ❌ |
| P-J7 | Medical Report Summarizer | LLM, PDF parsing | ❌ | ❌ |
| P-J8 | Stock Price Predictor + Dashboard | LSTM, Streamlit, yfinance | ❌ | ❌ |
| P-J9 | Smart FAQ Bot for College Website | RAG, ChromaDB, FastAPI | ❌ | ❌ |
| P-J10 | AI-Powered Code Review Assistant | OpenAI, GitHub API | ❌ | ❌ |

### Portfolio Builds (4–8 weeks, freshers + placement)
| ID | Project | Focus | Page | Kit complete |
|---|---|---|---|---|
| P-P1 | Full-Stack AI Dashboard | React + FastAPI + ML model | ❌ | ❌ |
| P-P2 | LangGraph Multi-Agent Research Tool | LangGraph, tools, memory | ❌ | ❌ |
| P-P3 | End-to-End MLOps Pipeline | Docker, MLflow, GitHub Actions | ❌ | ❌ |
| P-P4 | RAG API with Authentication | FastAPI, Supabase, OpenAI | ❌ | ❌ |
| P-P5 | Computer Vision API Service | FastAPI, YOLO, Docker, Render | ❌ | ❌ |
| P-P6 | CrewAI Business Intelligence Agent | CrewAI, tools, reports | ❌ | ❌ |

### Viva & Submission Packs
| ID | Pack | Status |
|---|---|---|
| P-V1 | ML Project Viva Pack (40 Q&A) | ❌ |
| P-V2 | DL Project Viva Pack (30 Q&A) | ❌ |
| P-V3 | GenAI + RAG Viva Pack (35 Q&A) | ❌ |
| P-V4 | Generic CS Report Template (Word + Google Docs) | ❌ |

---

## S5 — Portfolio Building Track

| ID | Task | Status | Notes |
|---|---|---|---|
| S5-T1 | /portfolio-guide.html page | ❌ | What makes a portfolio-ready GitHub profile |
| S5-T2 | GitHub Profile README template | ❌ | Markdown with project showcase layout |
| S5-T3 | Project README template (architecture, setup, demo link) | ❌ | |
| S5-T4 | "Deploy your project" guide: Render + Railway + HF Spaces | ❌ | Step-by-step |
| S5-T5 | LinkedIn profile optimization tips | ❌ | For AI/ML job seekers |
| S5-T6 | Portfolio checklist PDF (downloadable) | ❌ | What to have before applying |
| S5-T7 | /interview-prep.html page | ❌ | ML/DL/GenAI interview questions + answers |
| S5-T8 | "AI/ML Interview Questions" cheatsheet | ❌ | Add to cheatsheets page |

---

## S6 — Cheatsheets

| ID | Title | Markdown source | PDF generated | S3 uploaded |
|---|---|---|---|---|
| C1 | Python Basics | ✅ | ❌ | ❌ |
| C2 | Python for Data (Pandas / NumPy) | ❌ | ❌ | ❌ |
| C3 | SQL Quick Reference | ✅ | ❌ | ❌ |
| C4 | Shell / Bash | ❌ | ❌ | ❌ |
| C5 | Excel Formula Bible | ❌ | ❌ | ❌ |
| C6 | C/C++ Memory Cheatsheet | ❌ | ❌ | ❌ |
| C7 | ML Models at a Glance | ❌ | ❌ | ❌ |
| C8 | Deep Learning Layers | ❌ | ❌ | ❌ |
| C9 | GenAI Prompt Patterns | ❌ | ❌ | ❌ |
| C10 | AI for Developers Prompts | ❌ | ❌ | ❌ |
| C11 | AIML Interview Prep | ❌ | ❌ | ❌ |
| C12 | Portfolio & GitHub Profile Guide | ❌ | ❌ | ❌ |

> Generate: `python scripts/generate_cheatsheets.py --all`
> Upload: `python scripts/deploy_s3.py --type cheatsheets`

---

## S7 — Tools Coverage Map

| Tool | Where taught | Which project uses it |
|---|---|---|
| numpy | Programming T2 | P-M3, P-J3 |
| pandas | Programming T2 | P-J3, P-J5 |
| matplotlib | Programming T2 | P-J3 |
| scikit-learn | ML all tabs | P-M3, P-J2 |
| XGBoost / LightGBM | ML T12 Boosting | P-J3 |
| PyTorch | Key Concepts T52, DL T20 | P-J6, P-P5 |
| TensorFlow / Keras | Key Concepts T53, DL T20 | P-J5 |
| HuggingFace Transformers | DL T23, GenAI T33 | P-M6, P-J7 |
| YOLO (Ultralytics) | DL T20 CNNs | P-J6, P-P5 |
| OpenAI API | GenAI T28 | P-J1, P-J4, P-J10 |
| LangChain | GenAI T29 RAG | P-J1, P-J9 |
| LangGraph | Agentic T36 | P-P2 |
| CrewAI | Agentic T37 | P-P6 |
| ChromaDB | GenAI T29 | P-J1, P-J9 |
| FastAPI | MLOps | P-J1, P-J4, P-P4, P-P5 |
| Streamlit | — | P-M1, P-J2, P-J3, P-J5 |
| Docker | MLOps T46 | P-P3, P-P5 |
| MLflow | MLOps T44 | P-P3 |
| GitHub Actions | MLOps T48 | P-P3 |
| Kaggle GPU | Key Concepts T49 | All DL projects |
| Google Colab | Key Concepts T50 | All DL projects |
| AWS EC2 GPU | Key Concepts T51 | Advanced builds |
| Render.com | Deployment guides | All portfolio builds |
| Supabase | — | P-P4 |
| Git / GitHub | Key Concepts T56 | All projects |

---

## S8 — Certificates

| ID | Task | Status |
|---|---|---|
| S8-T1 | Certificate HTML template | ❌ |
| S8-T2 | Unique certificate ID (UUID in Supabase on quiz pass) | ❌ |
| S8-T3 | Certificate verify page /verify.html?id=xxx | ❌ |
| S8-T4 | PDF download of certificate | ❌ |
| S8-T5 | Legal wording reviewed (no degree/accreditation claims) | ❌ |

---

## S9 — Legal & Support Pages

| ID | Page | Status |
|---|---|---|
| S9-T1 | Privacy Policy /privacy.html | ✅ |
| S9-T2 | Terms of Service /terms.html | ✅ |
| S9-T3 | About /about.html | ✅ |
| S9-T4 | Contact form (Supabase insert) | 🔶 Form exists, Supabase table not created |
| S9-T5 | FAQ /faq.html | ✅ |
| S9-T6 | How It Works /how-it-works.html | ✅ |
| S9-T7 | Portfolio Guide /portfolio-guide.html | ❌ |
| S9-T8 | Interview Prep /interview-prep.html | ❌ |

---

## S10 — Launch Checklist (Go-Live Gate)

Do NOT share or announce the site until all are ✅.

| ID | Gate | Status |
|---|---|---|
| L1 | Domain purchased and DNS configured | ❌ |
| L2 | HTTPS enforced | ❌ |
| L3 | GitHub Pages enabled, first deploy green | ❌ |
| L4 | Supabase anon key wired in all pages | ❌ |
| L5 | Supabase tables created and tested | ❌ |
| L6 | Contact form tested end-to-end | ❌ |
| L7 | Home page content final | ✅ |
| L8 | At least 1 course with full content (ML recommended) | ❌ |
| L9 | At least 2 project kits with full content | ❌ |
| L10 | At least 5 cheatsheets uploaded to S3 | ❌ |
| L11 | Mobile verified on real device | ❌ |
| L12 | GA4 confirmed in Google Analytics dashboard | ❌ |
| L13 | All nav links working, no 404 pages | 🔶 |
| L14 | OG image set (social share preview) | ❌ |
| L15 | Google Search Console verified | ❌ |

---

## How We Work

No sprints, no phases. We work **section by section** in order: S1 → S2 → S3 → S4 → S5 → S6 → S7 → S8 → S9 → S10.

Every task we complete gets marked ✅ in this file. When all rows in a section are ✅, that section is done and we move to the next.

Reference any task as **S\<section\>-T\<number\>** (e.g. "let's do S1-T19") or by launch gate **L\<number\>** to keep conversations precise.

> **No intermediate/throwaway work.** Every task done here is the final production version deployed for real users.

---

*Last updated: 2026-06-07. Reference by S\<n\>-T\<n\> or L\<n\> in conversation.*
