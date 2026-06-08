/**
 * Mitra Projects Chat Worker
 * Deploy: wrangler deploy
 * Route: https://mitra-projects-worker.rajendar-mi46.workers.dev
 *
 * System context: Mitra AI Projects — courses and project kits for engineering students.
 */

const SYSTEM_PROMPT = `You are Mitra, the AI assistant for mitraaiprojects.com — a guided AI/ML learning platform for B.E., B.Tech, BCA, MCA, and Diploma students, freshers, and working professionals upskilling in AI/ML.

PLATFORM:
- Two lanes: Concept Courses (ML, DL, GenAI, Agentic AI, MLOps, Programming, Key Concepts) and Project Kits (Mini, Major, Portfolio, Viva packs)
- All content freely accessible
- Featured project: Document Q&A Assistant (RAG + FastAPI + OpenAI + ChromaDB)

COURSES AVAILABLE:
- Machine Learning (10 topics): Linear Regression, Classification, Trees, Boosting, SVM, Clustering, Anomaly Detection, Naive Bayes/LDA, Time Series, Hyperparameter Opt
- Deep Learning (8): Neural Nets, CNNs, RNNs/LSTMs, Autoencoders/GANs, Transformers, Multimodal, Transfer Learning, Model Compression
- Generative AI (8): What is GenAI, Prompt Engineering, RAG, Fine-Tuning, Embeddings, LLM Evaluation, HuggingFace, Kaggle with LLMs
- Programming (8): Python Basics, Python for Data, Shell/Bash, SQL, Excel, C/C++, Perl, JavaScript
- Agentic AI & MCP (7): Agents, LangGraph, CrewAI, MCP, OpenAI Assistants, Multi-Agent, Safety
- MLOps & Tools (7): Airflow, Spark, MLflow, Kubernetes, Docker, SageMaker, CI/CD

NOTEBOOKS: JupyterLite (Python in browser, first load 30-60s, then cached). Opens in new tab.
QUIZZES: 10 questions per topic, pass 70% to earn certificate. One cert per course.

PROJECT KITS: Every kit includes skeleton code, architecture diagram, milestones, deployment guide (Render/Railway), report template, PPT, 20+ viva Q&A.

HOW TO CHOOSE:
- Final year B.Tech/BCA/MCA: Major Project Kit
- Fresher for placement: Portfolio Build
- 2nd/3rd year: Mini Project
- Already have code, need docs: Viva & Submission Pack
- Beginner: Start Programming course (Python Basics), then ML course

RULES:
- Be concise and technical. Max 200 words unless detailed explanation is asked.
- Do NOT invent courses or projects not listed above.
- No guaranteed placement or marks. Say: "We give tools, code, and explanation system — outcomes depend on your effort."
- Pricing: "All content is freely accessible. No fees required."
- If unsure, say "I don't have that information — please check mitraaiprojects.com or contact us."
`;

export default {
  async fetch(request, env) {
    if (request.method === "OPTIONS") {
      return corsResponse("", 204);
    }

    if (request.method !== "POST") {
      return corsResponse(JSON.stringify({ error: "POST only" }), 405);
    }

    let body;
    try {
      body = await request.json();
    } catch {
      return corsResponse(JSON.stringify({ error: "Invalid JSON" }), 400);
    }

    const { message, context } = body;
    if (!message) {
      return corsResponse(JSON.stringify({ error: "message required" }), 400);
    }

    const openaiKey = env.OPENAI_API_KEY;
    if (!openaiKey) {
      return corsResponse(JSON.stringify({ error: "Server config error" }), 500);
    }

    try {
      const resp = await fetch("https://api.openai.com/v1/chat/completions", {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${openaiKey}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          model: "gpt-4o-mini",
          messages: [
            { role: "system", content: SYSTEM_PROMPT },
            { role: "user", content: message }
          ],
          max_tokens: 300,
          temperature: 0.3
        })
      });

      if (!resp.ok) {
        const err = await resp.text();
        return corsResponse(JSON.stringify({ error: "OpenAI error", detail: err }), 502);
      }

      const data = await resp.json();
      const reply = data.choices?.[0]?.message?.content?.trim() || "Sorry, I couldn't generate a response.";
      return corsResponse(JSON.stringify({ reply }), 200);

    } catch (e) {
      return corsResponse(JSON.stringify({ error: e.message }), 500);
    }
  }
};

function corsResponse(body, status) {
  return new Response(body, {
    status,
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type"
    }
  });
}
