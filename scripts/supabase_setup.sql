-- ═══════════════════════════════════════════════════
-- Mitra AI Projects — Supabase Database Setup
-- Run this entire file in Supabase Dashboard → SQL Editor → New Query
-- ═══════════════════════════════════════════════════

-- Contact form submissions
CREATE TABLE IF NOT EXISTS contact_submissions (
  id           uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  name         text,
  email        text NOT NULL,
  college      text,
  interest     text,
  message      text,
  source       text DEFAULT 'mitraaiprojects.com',
  created_at   timestamptz DEFAULT now()
);

-- Course topic completions (one row per user per topic)
CREATE TABLE IF NOT EXISTS course_completions (
  id           uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id      uuid REFERENCES auth.users(id) ON DELETE CASCADE,
  course_id    text NOT NULL,
  topic_slug   text NOT NULL,
  completed_at timestamptz DEFAULT now(),
  UNIQUE(user_id, course_id, topic_slug)
);

-- Project kit completions (one row per user per project)
CREATE TABLE IF NOT EXISTS project_completions (
  id           uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id      uuid REFERENCES auth.users(id) ON DELETE CASCADE,
  project_id   text NOT NULL,
  completed_at timestamptz DEFAULT now(),
  UNIQUE(user_id, project_id)
);

-- Certificate records
CREATE TABLE IF NOT EXISTS certificates (
  id             uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id        uuid REFERENCES auth.users(id) ON DELETE CASCADE,
  cert_type      text NOT NULL,  -- 'course' or 'project'
  ref_id         text NOT NULL,  -- course_id or project_id
  user_name      text,
  issued_at      timestamptz DEFAULT now(),
  UNIQUE(user_id, cert_type, ref_id)
);

-- Enable Row Level Security on all tables
ALTER TABLE contact_submissions  ENABLE ROW LEVEL SECURITY;
ALTER TABLE course_completions   ENABLE ROW LEVEL SECURITY;
ALTER TABLE project_completions  ENABLE ROW LEVEL SECURITY;
ALTER TABLE certificates         ENABLE ROW LEVEL SECURITY;

-- RLS Policies
-- Anyone can submit a contact form (no auth required)
CREATE POLICY "public_insert_contact"
  ON contact_submissions FOR INSERT
  WITH CHECK (true);

-- Only the owning user can read/write their completions
CREATE POLICY "user_completions_course"
  ON course_completions FOR ALL
  USING (auth.uid() = user_id);

CREATE POLICY "user_completions_project"
  ON project_completions FOR ALL
  USING (auth.uid() = user_id);

-- Only the owning user can read/write their certificates
CREATE POLICY "user_certificates"
  ON certificates FOR ALL
  USING (auth.uid() = user_id);

-- Allow anyone to verify a certificate by ID (public read)
CREATE POLICY "public_verify_certificate"
  ON certificates FOR SELECT
  USING (true);

-- Add tested_out column to course_completions (run if upgrading existing install)
ALTER TABLE course_completions ADD COLUMN IF NOT EXISTS tested_out boolean DEFAULT false;
ALTER TABLE course_completions ADD COLUMN IF NOT EXISTS score integer;
