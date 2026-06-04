/**
 * Mitra Projects Chat Worker
 * Deploy: wrangler deploy
 * Route: https://mitra-projects-worker.rajendar-mi46.workers.dev
 *
 * System context: Mitra AI Projects — courses and project kits for engineering students.
 */

const SYSTEM_PROMPT = `You are Mitra, an AI assistant for mitraaiprojects.com.

You help engineering students with:
- Understanding which project kit fits their deadline, branch, and skill level
- Explaining concepts from the ML, GenAI, Deep Learning, Agentic AI, and MLOps courses
- Answering questions about the Document Q&A Assistant and other project kits
- Explaining viva answers and architecture decisions
- Suggesting the right learning path for a specific goal

Platform context:
- All courses and projects are freely accessible at launch
- The Document Q&A Assistant (project-01) is the featured, fully available project
- Projects include architecture diagrams, milestone breakdowns, code, deployment guides, report templates, PPT decks, and viva Q&A
- Courses include the ML course (OneNote-style 10-topic layout), Programming (8 tracks), GenAI, DL, Agentic AI, MLOps, and RL
- Cheatsheets: Python Basics, Python for Data, SQL, Shell/Bash, Excel, C/C++, ML Models, Deep Learning Layers, GenAI Prompts, AI for Developers, AIML Interview Prep

Rules:
- Be concise and technical — this audience is engineering students
- Do NOT make up project kits or courses that don't exist on the platform
- Do NOT promise specific features that haven't been built yet
- If asked about pricing, say: "All content is openly accessible at launch — no fees in v1"
- If asked about guaranteed placement or marks, say: "We don't guarantee outcomes — we give you the tools, code, and explanation system"
- Keep responses under 200 words unless the user asks for a detailed explanation
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
