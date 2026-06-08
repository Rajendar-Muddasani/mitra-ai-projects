/* ═══════════════════════════════════════════════════
   Mitra AI Projects — Chat Widget
   Worker: https://mitra-projects-worker.rajendar-mi46.workers.dev
   Model: gpt-4o-mini (cheapest, fast)
   Reference: content/chatbot/*.md (knowledge base)
   ═══════════════════════════════════════════════════ */

const WORKER_URL = 'https://mitra-projects-worker.rajendar-mi46.workers.dev';

const chatHTML = `
<div id="mitra-chat-panel" class="mitra-chat-panel" style="display:none" aria-label="Mitra AI chat">
  <div class="mitra-chat-header">
    <span>🤖 Mitra AI</span>
    <button id="mitra-chat-close" aria-label="Close chat">✕</button>
  </div>
  <div id="mitra-chat-messages" class="mitra-chat-messages">
    <div class="mitra-chat-msg bot">
      Hi! I'm Mitra AI. Ask me anything about courses, projects, or how to get started. 👋
    </div>
  </div>
  <div class="mitra-chat-input-row">
    <input id="mitra-chat-input" type="text" placeholder="Ask a question…" autocomplete="off" />
    <button id="mitra-chat-send">→</button>
  </div>
</div>
<style>
.mitra-chat-panel {
  position: fixed; bottom: 5rem; right: 1.5rem; z-index: 201;
  width: min(380px, calc(100vw - 2rem));
  background: #fff; border: 1px solid rgba(107,33,168,0.2);
  border-radius: 14px; box-shadow: 0 8px 48px rgba(107,33,168,0.15);
  display: flex; flex-direction: column; overflow: hidden;
}
.mitra-chat-header {
  background: #6b21a8; padding: 0.75rem 1rem;
  display: flex; justify-content: space-between; align-items: center;
  font-weight: 700; color: #fff; font-size: 0.9rem;
}
.mitra-chat-header button {
  background: none; border: none; color: rgba(255,255,255,0.7); cursor: pointer; font-size: 1rem;
}
.mitra-chat-messages {
  flex: 1; overflow-y: auto; padding: 1rem; max-height: 320px;
  display: flex; flex-direction: column; gap: 0.6rem;
}
.mitra-chat-msg {
  padding: 0.6rem 0.85rem; border-radius: 10px;
  font-size: 0.875rem; line-height: 1.5; max-width: 88%;
}
.mitra-chat-msg.bot {
  background: #faf5ff; color: #1a0533; align-self: flex-start;
}
.mitra-chat-msg.user {
  background: #6b21a8; color: #fff;
  align-self: flex-end; border: none;
}
.mitra-chat-input-row {
  display: flex; gap: 0.5rem; padding: 0.75rem; border-top: 1px solid rgba(107,33,168,0.1);
}
.mitra-chat-input-row input {
  flex: 1; background: #faf5ff; border: 1px solid rgba(107,33,168,0.15);
  border-radius: 8px; padding: 0.55rem 0.75rem; color: #1a0533;
  font-size: 0.875rem; outline: none;
}
.mitra-chat-input-row input:focus { border-color: #fff; }
.mitra-chat-input-row button {
  background: #6b21a8; color: #fff; border: none;
  border-radius: 8px; padding: 0.5rem 0.85rem; cursor: pointer;
  font-weight: 700; font-size: 1rem; transition: background 0.15s;
}
.mitra-chat-input-row button:hover { background: #7c3aed; }
</style>
`;

function initChat() {
  const widget = document.querySelector('.chat-widget');
  if (!widget) return;

  widget.insertAdjacentHTML('beforebegin', chatHTML);

  const panel  = document.getElementById('mitra-chat-panel');
  const input  = document.getElementById('mitra-chat-input');
  const msgs   = document.getElementById('mitra-chat-messages');
  const chatBtn = widget.querySelector('.chat-btn');
  const closeBtn = document.getElementById('mitra-chat-close');
  const sendBtn  = document.getElementById('mitra-chat-send');

  chatBtn?.addEventListener('click', () => {
    panel.style.display = panel.style.display === 'none' ? 'flex' : 'none';
    if (panel.style.display === 'flex') input?.focus();
  });

  closeBtn?.addEventListener('click', () => { panel.style.display = 'none'; });

  async function sendMessage() {
    const text = input?.value?.trim();
    if (!text) return;

    appendMsg(text, 'user');
    input.value = '';

    const typing = appendMsg('…', 'bot');

    try {
      const res = await fetch(WORKER_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text, context: 'mitraaiprojects' })
      });
      const data = await res.json();
      typing.textContent = data.reply || 'Sorry, I could not get a response.';
    } catch {
      typing.textContent = 'Connection error. Please try again.';
    }

    msgs.scrollTop = msgs.scrollHeight;
    if (typeof trackEvent === 'function') trackEvent('chat_message_sent');
  }

  sendBtn?.addEventListener('click', sendMessage);
  input?.addEventListener('keydown', (e) => { if (e.key === 'Enter') sendMessage(); });

  function appendMsg(text, role) {
    const div = document.createElement('div');
    div.className = `mitra-chat-msg ${role}`;
    div.textContent = text;
    msgs?.appendChild(div);
    msgs.scrollTop = msgs.scrollHeight;
    return div;
  }
}

document.addEventListener('DOMContentLoaded', initChat);
