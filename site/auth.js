/* ═══════════════════════════════════════════════════
   Mitra AI Projects — Auth (Supabase)
   Integration point: mirrors mitraailife.com auth.js
   ═══════════════════════════════════════════════════ */

const SUPABASE_URL  = 'https://kuriwaysdlqnzqqzabts.supabase.co';
const SUPABASE_ANON = window.__SUPABASE_ANON_KEY__ || '';

let supabase = null;
let currentUser = null;

async function initAuth() {
  if (typeof window.supabase_createClient === 'function') {
    supabase = window.supabase_createClient(SUPABASE_URL, SUPABASE_ANON);
    window.supabase = supabase;

    const { data: { session } } = await supabase.auth.getSession();
    currentUser = session?.user || null;
    window.currentUser = currentUser;

    updateAuthUI();

    supabase.auth.onAuthStateChange((_event, session) => {
      currentUser = session?.user || null;
      window.currentUser = currentUser;
      updateAuthUI();
    });
  }
}

function updateAuthUI() {
  const loginBtn  = document.getElementById('loginBtn');
  const logoutBtn = document.getElementById('logoutBtn');
  const userLabel = document.getElementById('userLabel');

  if (currentUser) {
    if (loginBtn)  loginBtn.style.display  = 'none';
    if (logoutBtn) logoutBtn.style.display = 'inline-flex';
    if (userLabel) userLabel.textContent   = currentUser.email?.split('@')[0] || 'You';
  } else {
    if (loginBtn)  loginBtn.style.display  = 'inline-flex';
    if (logoutBtn) logoutBtn.style.display = 'none';
    if (userLabel) userLabel.textContent   = '';
  }
}

async function signInWithGoogle() {
  if (!supabase) return;
  await supabase.auth.signInWithOAuth({
    provider: 'google',
    options: { redirectTo: window.location.origin }
  });
}

async function signOut() {
  if (!supabase) return;
  await supabase.auth.signOut();
}

async function recordCourseCompletion(courseId, topicSlug) {
  if (!supabase || !currentUser) return;
  await supabase.from('course_completions').upsert({
    user_id:    currentUser.id,
    course_id:  courseId,
    topic_slug: topicSlug,
    completed_at: new Date().toISOString()
  });
}

async function recordProjectCompletion(projectId) {
  if (!supabase || !currentUser) return;
  await supabase.from('project_completions').upsert({
    user_id:      currentUser.id,
    project_id:   projectId,
    completed_at: new Date().toISOString()
  });
}

document.addEventListener('DOMContentLoaded', () => {
  initAuth();

  document.getElementById('loginBtn')?.addEventListener('click', signInWithGoogle);
  document.getElementById('logoutBtn')?.addEventListener('click', signOut);
});

window.MitraAuth = { signInWithGoogle, signOut, recordCourseCompletion, recordProjectCompletion };
