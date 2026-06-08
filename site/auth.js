/* ═══════════════════════════════════════════════════
   Mitra AI Projects — Auth (Supabase JS v2)
   Requires: /config.js (sets window.__SUPABASE_ANON_KEY__)
   Requires: Supabase JS CDN loaded before this file
   ═══════════════════════════════════════════════════ */

const SUPABASE_URL  = 'https://kuriwaysdlqnzqqzabts.supabase.co';
const SUPABASE_ANON = window.__SUPABASE_ANON_KEY__ || '';

let supabase = null;
let currentUser = null;

async function initAuth() {
  // Supabase JS v2 CDN exposes window.supabase.createClient
  if (!window.supabase?.createClient || !SUPABASE_ANON || SUPABASE_ANON === 'YOUR_SUPABASE_ANON_KEY_HERE') return;

  supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON);
  window._supabaseClient = supabase;

  const { data: { session } } = await supabase.auth.getSession();
  currentUser = session?.user || null;
  window.currentUser = currentUser;

  updateAuthUI();

  supabase.auth.onAuthStateChange((_event, session) => {
    currentUser = session?.user || null;
    window.currentUser = currentUser;
    updateAuthUI();
    if (currentUser) window.dispatchEvent(new CustomEvent('mitra:signed-in', { detail: currentUser }));
  });
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

async function signInWithEmail(email) {
  if (!supabase) return { error: 'Not connected' };
  return supabase.auth.signInWithOtp({
    email,
    options: { emailRedirectTo: window.location.origin }
  });
}

async function signOut() {
  if (!supabase) return;
  await supabase.auth.signOut();
}

async function recordCourseCompletion(courseId, topicSlug, score, testedOut) {
  if (!supabase || !currentUser) return;
  await supabase.from('course_completions').upsert({
    user_id:      currentUser.id,
    course_id:    courseId,
    topic_slug:   topicSlug,
    completed_at: new Date().toISOString(),
    score:        score || null,
    tested_out:   testedOut || false
  }, { onConflict: 'user_id,course_id,topic_slug' });
}

async function recordProjectCompletion(projectId) {
  if (!supabase || !currentUser) return;
  await supabase.from('project_completions').upsert({
    user_id:      currentUser.id,
    project_id:   projectId,
    completed_at: new Date().toISOString()
  }, { onConflict: 'user_id,project_id' });
}

async function recordCertificate(certType, refId, userName) {
  if (!supabase || !currentUser) return null;
  const { data } = await supabase.from('certificates').upsert({
    user_id:   currentUser.id,
    cert_type: certType,
    ref_id:    refId,
    user_name: userName || currentUser.email?.split('@')[0],
    issued_at: new Date().toISOString()
  }, { onConflict: 'user_id,cert_type,ref_id' }).select().single();
  return data;
}

async function getUserCompletions() {
  if (!supabase || !currentUser) return { courses: [], projects: [], certificates: [] };
  const [courses, projects, certificates] = await Promise.all([
    supabase.from('course_completions').select('*').eq('user_id', currentUser.id),
    supabase.from('project_completions').select('*').eq('user_id', currentUser.id),
    supabase.from('certificates').select('*').eq('user_id', currentUser.id)
  ]);
  return {
    courses:      courses.data || [],
    projects:     projects.data || [],
    certificates: certificates.data || []
  };
}

document.addEventListener('DOMContentLoaded', () => {
  // Inject userLabel and logoutBtn next to loginBtn if not already in the HTML
  const loginBtn = document.getElementById('loginBtn');
  if (loginBtn && !document.getElementById('logoutBtn')) {
    const label = document.createElement('a');
    label.id = 'userLabel';
    label.href = '/profile.html';
    label.style.cssText = 'display:none;font-size:0.85rem;color:var(--muted);font-weight:600;text-decoration:none;margin-right:0.25rem;';
    const logout = document.createElement('button');
    logout.id = 'logoutBtn';
    logout.className = 'btn btn-ghost btn-sm';
    logout.style.display = 'none';
    logout.textContent = 'Sign Out';
    loginBtn.parentNode.insertBefore(label, loginBtn);
    loginBtn.parentNode.appendChild(logout);
  }

  initAuth();
  document.getElementById('loginBtn')?.addEventListener('click', () => window.openSignInModal?.());
  document.getElementById('logoutBtn')?.addEventListener('click', signOut);
});

window.MitraAuth = {
  signInWithGoogle, signInWithEmail, signOut,
  recordCourseCompletion, recordProjectCompletion, recordCertificate,
  getUserCompletions,
  getUser: () => currentUser
};
