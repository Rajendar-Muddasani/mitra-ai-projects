/* ═══════════════════════════════════════════════════
   Mitra AI Projects — Main JavaScript
   ═══════════════════════════════════════════════════ */

/* ── GA4 Analytics helper ── */
const GA_ID = 'G-QGY0LH6W93';

function trackEvent(name, params = {}) {
  if (typeof gtag === 'function') {
    gtag('event', name, params);
  }
}

/* ── Navigation ── */
function initNav() {
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (!toggle || !links) return;

  toggle.addEventListener('click', () => {
    links.classList.toggle('open');
    toggle.setAttribute('aria-expanded', links.classList.contains('open'));
  });

  // Close on outside click
  document.addEventListener('click', (e) => {
    if (!toggle.contains(e.target) && !links.contains(e.target)) {
      links.classList.remove('open');
    }
  });

  // Mark active link
  const path = window.location.pathname;
  document.querySelectorAll('.nav-links a').forEach(a => {
    if (a.getAttribute('href') && path.includes(a.getAttribute('href').replace('/', ''))) {
      a.classList.add('active');
    }
  });
}

/* ── Standard tabs ── */
function initTabs(container) {
  const btns = container.querySelectorAll('.tab-btn');
  const panels = container.querySelectorAll('.tab-panel');

  function activate(idx) {
    btns.forEach((b, i) => {
      b.classList.toggle('active', i === idx);
      b.setAttribute('aria-selected', i === idx);
    });
    panels.forEach((p, i) => p.classList.toggle('active', i === idx));
    trackEvent('tab_change', { tab_label: btns[idx]?.dataset.label || btns[idx]?.textContent });
  }

  btns.forEach((btn, i) => {
    btn.addEventListener('click', () => activate(i));
  });

  if (btns.length) activate(0);
}

/* ── OneNote tabs (ml.html) ── */
function initOneNoteTabs() {
  const tabs = document.querySelectorAll('.onenote-tab');
  const panels = document.querySelectorAll('.onenote-panel');
  const mobileSelect = document.querySelector('.onenote-mobile-select');

  function activate(idx) {
    tabs.forEach((t, i) => t.classList.toggle('active', i === idx));
    panels.forEach((p, i) => p.classList.toggle('active', i === idx));
    if (mobileSelect) mobileSelect.selectedIndex = idx;
    trackEvent('tab_change', { tab_label: tabs[idx]?.querySelector('.onenote-tab-text')?.textContent });
  }

  tabs.forEach((tab, i) => tab.addEventListener('click', () => activate(i)));

  if (mobileSelect) {
    mobileSelect.addEventListener('change', (e) => activate(+e.target.value));
  }

  if (tabs.length) activate(0);
}

/* ── FAQ accordion ── */
function initFAQ() {
  document.querySelectorAll('.faq-item').forEach(item => {
    const btn = item.querySelector('.faq-q');
    if (!btn) return;
    btn.addEventListener('click', () => {
      const wasOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
      if (!wasOpen) item.classList.add('open');
    });
  });
}

/* ── Quiz engine ── */
function initQuizzes() {
  document.querySelectorAll('.quiz-block').forEach(block => {
    const submitBtn = block.querySelector('.quiz-submit');
    const resultEl = block.querySelector('.quiz-result');
    if (!submitBtn) return;

    submitBtn.addEventListener('click', () => {
      const questions = block.querySelectorAll('.quiz-q');
      let correct = 0;
      let answered = 0;

      questions.forEach(q => {
        const selected = q.querySelector('input[type="radio"]:checked');
        const options = q.querySelectorAll('.quiz-option');
        const correctVal = q.dataset.correct;

        options.forEach(opt => {
          opt.classList.remove('correct', 'wrong');
          const input = opt.querySelector('input');
          if (input && input.value === correctVal) opt.classList.add('correct');
        });

        if (selected) {
          answered++;
          if (selected.value === correctVal) {
            correct++;
          } else {
            selected.closest('.quiz-option').classList.add('wrong');
          }
        }
      });

      if (answered < questions.length) {
        if (resultEl) resultEl.textContent = 'Please answer all questions.';
        return;
      }

      const pct = Math.round((correct / questions.length) * 100);
      if (resultEl) {
        resultEl.textContent = `Score: ${correct}/${questions.length} (${pct}%)`;
        resultEl.className = 'quiz-result ' + (pct >= 60 ? 'pass' : '');
      }

      trackEvent('quiz_attempt', { score: pct });
      if (pct === 100) trackEvent('quiz_perfect');
    });

    const retryBtn = block.querySelector('.quiz-retry');
    if (retryBtn) {
      retryBtn.addEventListener('click', () => {
        block.querySelectorAll('input[type="radio"]').forEach(r => r.checked = false);
        block.querySelectorAll('.quiz-option').forEach(o => o.classList.remove('correct', 'wrong'));
        if (resultEl) { resultEl.textContent = ''; resultEl.className = 'quiz-result'; }
      });
    }
  });
}

/* ── Cheatsheet download tracking ── */
function initCheatsheetTracking() {
  document.querySelectorAll('[data-track="cheatsheet"]').forEach(btn => {
    btn.addEventListener('click', () => {
      trackEvent('cheatsheet_download', { name: btn.dataset.name });
    });
  });
}

/* ── Contact form ── */
function initContactForm() {
  const form = document.querySelector('.contact-form-el');
  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const btn = form.querySelector('button[type="submit"]');
    const originalText = btn.textContent;
    btn.textContent = 'Sending…';
    btn.disabled = true;

    const data = Object.fromEntries(new FormData(form));

    try {
      const client = window._supabaseClient;
      if (client) {
        await client.from('contact_submissions').insert([{
          name: data.name,
          email: data.email,
          college: data.college,
          interest: data.interest,
          message: data.message,
          source: 'mitraaiprojects.com'
        }]);
      }

      trackEvent('contact_form_submit');
      form.innerHTML = '<div class="completion-banner"><div class="completion-icon">✅</div><div class="completion-body"><h3>Message received!</h3><p>We\'ll get back to you within 2 business days.</p></div></div>';
    } catch (err) {
      btn.textContent = originalText;
      btn.disabled = false;
      alert('Something went wrong. Please email us directly at hello@mitraaiprojects.com');
    }
  });
}

/* ── Smooth scroll for anchor links ── */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', (e) => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
}

/* ── Video tracking ── */
function initVideoTracking() {
  document.querySelectorAll('video').forEach(video => {
    let started = false;
    let halfway = false;

    video.addEventListener('play', () => {
      if (!started) {
        started = true;
        trackEvent('video_start', { src: video.currentSrc });
      }
    });

    video.addEventListener('timeupdate', () => {
      if (!halfway && video.duration && video.currentTime / video.duration >= 0.5) {
        halfway = true;
        trackEvent('video_50_percent', { src: video.currentSrc });
      }
    });
  });
}

/* ── Certificate claim ── */
function initCertificate() {
  const claimBtn = document.querySelector('.claim-certificate');
  if (!claimBtn) return;

  claimBtn.addEventListener('click', async () => {
    trackEvent('certificate_claimed', { page: window.location.pathname });
    const { supabase, currentUser } = window;
    if (!supabase || !currentUser) {
      document.querySelector('#loginBtn')?.click();
      return;
    }
    alert('Certificate generation coming soon. Your completion has been recorded.');
  });
}

/* ── Sign-in modal ── */
function initSignInModal() {
  const modal = document.createElement('div');
  modal.id = 'signInModal';
  modal.className = 'auth-modal-overlay';
  modal.setAttribute('role', 'dialog');
  modal.setAttribute('aria-modal', 'true');
  modal.setAttribute('aria-label', 'Sign in to Mitra AI Projects');
  modal.innerHTML = `
    <div class="auth-modal-card">
      <button class="auth-modal-close" aria-label="Close" onclick="window.closeSignInModal()">✕</button>
      <div class="auth-modal-brand">
        <div class="nav-logo">M</div>
        <span style="font-family:'Baloo 2',sans-serif;font-weight:800;font-size:1.1rem;">Mitra<span class="teal">AI</span> Projects</span>
      </div>
      <h2 class="auth-modal-title">Sign in to track progress</h2>
      <p class="auth-modal-sub">Save your course completions, project milestones, and earn certificates.</p>
      <button class="btn btn-primary auth-google-btn" onclick="window.MitraAuth?.signInWithGoogle()">
        <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <path d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844a4.14 4.14 0 01-1.796 2.716v2.259h2.908c1.702-1.567 2.684-3.875 2.684-6.615z" fill="#fff" opacity=".9"/>
          <path d="M9 18c2.43 0 4.467-.806 5.956-2.18l-2.908-2.259c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332A8.997 8.997 0 009 18z" fill="#fff" opacity=".8"/>
          <path d="M3.964 10.71A5.41 5.41 0 013.682 9c0-.593.102-1.17.282-1.71V4.958H.957A8.996 8.996 0 000 9c0 1.452.348 2.827.957 4.042l3.007-2.332z" fill="#fff" opacity=".7"/>
          <path d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0A8.997 8.997 0 00.957 4.958L3.964 7.29C4.672 5.163 6.656 3.58 9 3.58z" fill="#fff" opacity=".6"/>
        </svg>
        Continue with Google
      </button>
      <div class="auth-divider"><span>or</span></div>
      <div class="auth-email-form">
        <input type="email" id="authEmailInput" class="auth-email-input" placeholder="your@email.com" autocomplete="email" />
        <button class="btn btn-outline auth-email-btn" id="authEmailBtn">Send magic link</button>
      </div>
      <p class="auth-modal-notice" id="authNotice"></p>
    </div>`;

  document.body.appendChild(modal);

  // Close on overlay click
  modal.addEventListener('click', (e) => {
    if (e.target === modal) window.closeSignInModal();
  });

  // Close on Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('open')) window.closeSignInModal();
  });

  // Email magic link
  document.getElementById('authEmailBtn')?.addEventListener('click', async () => {
    const email = document.getElementById('authEmailInput')?.value?.trim();
    const notice = document.getElementById('authNotice');
    if (!email || !email.includes('@')) {
      if (notice) { notice.textContent = 'Please enter a valid email.'; notice.style.color = 'var(--danger)'; }
      return;
    }
    const btn = document.getElementById('authEmailBtn');
    btn.textContent = 'Sending…';
    btn.disabled = true;

    const result = await window.MitraAuth?.signInWithEmail(email);
    if (result?.error) {
      if (notice) { notice.textContent = 'Could not send link. Please try Google sign-in.'; notice.style.color = 'var(--danger)'; }
      btn.textContent = 'Send magic link';
      btn.disabled = false;
    } else {
      if (notice) { notice.textContent = `✅ Magic link sent to ${email}. Check your inbox!`; notice.style.color = 'var(--success)'; }
      btn.textContent = 'Sent!';
    }
  });
}

window.openSignInModal = () => {
  const modal = document.getElementById('signInModal');
  if (modal) { modal.classList.add('open'); document.body.style.overflow = 'hidden'; }
};
window.closeSignInModal = () => {
  const modal = document.getElementById('signInModal');
  if (modal) { modal.classList.remove('open'); document.body.style.overflow = ''; }
};

/* ── Mobile select for OneNote ── */
function buildMobileSelect() {
  const tabs = document.querySelectorAll('.onenote-tab');
  const select = document.querySelector('.onenote-mobile-select');
  if (!select || !tabs.length) return;

  tabs.forEach((tab, i) => {
    const opt = document.createElement('option');
    opt.value = i;
    opt.textContent = tab.querySelector('.onenote-tab-text')?.textContent || `Topic ${i + 1}`;
    select.appendChild(opt);
  });
}

/* ── Init all ── */
document.addEventListener('DOMContentLoaded', () => {
  initNav();
  initFAQ();
  initQuizzes();
  initCheatsheetTracking();
  initContactForm();
  initSmoothScroll();
  initVideoTracking();
  initCertificate();
  buildMobileSelect();
  initOneNoteTabs();

  document.querySelectorAll('.tab-layout').forEach(initTabs);
  initSignInModal();
});
