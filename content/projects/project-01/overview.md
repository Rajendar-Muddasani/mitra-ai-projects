# Document Q&A Assistant — Project Overview

## What You're Building

A web application that allows users to upload PDF or text documents and ask questions in natural language. The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant chunks from the documents and answer questions using GPT-4o-mini.

## Why This Project Matters

- Demonstrates RAG — one of the most in-demand skills in AI development in 2026
- Uses real APIs (OpenAI) and a real vector database (ChromaDB)
- Produces a live deployable demo with a public URL
- Is explainable end-to-end — you can defend every architecture decision in a viva

## Target Users

- Final-year B.Tech/BCA/MCA students needing a strong AI project
- Students targeting AI/ML roles in placements
- Learners who want to understand RAG practically, not just theoretically

## Core Problem

Many knowledge-intensive tasks require searching through large documents — legal contracts, research papers, product manuals, lecture notes. A Document Q&A system automates this by letting users ask questions in plain English and receive cited, grounded answers from the document content.

## Tech Stack Rationale

| Component | Choice | Why |
|---|---|---|
| Backend API | FastAPI | Async, auto-docs, Pydantic validation |
| Embedding model | text-embedding-3-small | Cheap, high-quality, 1536 dims |
| LLM | gpt-4o-mini | ~15× cheaper than gpt-4o, fast, good enough |
| Vector DB | ChromaDB | Python-native, local persistent storage, no server needed |
| Text splitting | LangChain RecursiveCharacterTextSplitter | Handles various document formats |
| PDF parsing | PyPDF2 | Simple, lightweight |
| Deployment | Render.com free tier | Free, Docker support, easy |

## Extension Ideas

1. Add multi-document support with per-document filtering
2. Implement conversation memory (ask follow-up questions)
3. Add hybrid search (vector + BM25 keyword)
4. Deploy an admin dashboard for document management
5. Add answer quality scoring using RAGAs
6. Integrate Supabase auth so users see only their documents
7. Add support for DOCX, HTML, and Excel files
