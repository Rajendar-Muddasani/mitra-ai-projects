# Document Q&A Assistant — Viva Questions & Answers

## Full Set of 20 Viva Questions

### Architecture & Design

**Q1: What is RAG and why did you choose it over direct LLM answering?**

RAG stands for Retrieval-Augmented Generation. Instead of asking the LLM to answer from its training data (which may be outdated or wrong), RAG retrieves relevant context from your own documents and injects it into the prompt. This grounds the answer in the actual document, reduces hallucinations, and allows domain-specific Q&A without retraining the model. Direct LLM answering would hallucinate freely — it has no access to your specific document.

**Q2: What is a vector embedding? Why cosine similarity instead of keyword matching?**

A vector embedding is a dense numerical representation (array of floats) of text. Semantically similar texts have similar vectors. Cosine similarity measures the angle between two vectors — it finds semantically similar text even when exact words differ. Example: "charges for delayed remittance" is semantically similar to "penalty for late payment" — cosine similarity catches this, keyword matching doesn't.

**Q3: What is ChromaDB and why did you use it?**

ChromaDB is an open-source vector database optimized for storing and searching embedding vectors. It supports persistent local storage, metadata filtering, and fast HNSW-based approximate nearest-neighbor search. I used it because it's Python-native, requires no separate server setup, is free, and is well-suited for datasets up to a few million vectors.

**Q4: How did you chunk the document? What chunk size and overlap?**

I used recursive character text splitting with chunk size 500 characters and overlap 100 characters. Chunking splits the document into manageable pieces that fit in the context window. Overlap ensures sentences at chunk boundaries aren't completely lost across two chunks.

**Q5: What is the difference between the embedding model and the chat model?**

The embedding model (text-embedding-3-small) converts text into a numerical vector for similarity search — it doesn't generate text. The chat model (gpt-4o-mini) generates the natural language answer based on the retrieved context. They serve completely different purposes in the pipeline.

### Implementation Details

**Q6: How does your system handle hallucinations?**

Three approaches: (1) System prompt explicitly instructs the LLM to answer ONLY from the provided context and say "I don't know" if the answer isn't there. (2) Source chunk is returned alongside the answer for user verification. (3) Temperature is set to 0.1 for deterministic, less creative output.

**Q7: What is FastAPI and why not Flask?**

FastAPI is async by default, generates OpenAPI documentation automatically, and validates request/response data with Pydantic. It handles concurrent OpenAI API calls efficiently due to async support. Flask is synchronous by default and lacks built-in data validation — it's slower for I/O-bound workloads like waiting for LLM responses.

**Q8: What is the difference between gpt-4o-mini and gpt-4o?**

gpt-4o-mini is approximately 15× cheaper per token and responds faster. For Q&A tasks where the context is already pre-retrieved and structured, it performs nearly as well as gpt-4o. For a student project with limited API budget, it's the right choice.

**Q9: Explain the DELETE /documents/{doc_id} endpoint.**

It must: (1) Remove all vector embeddings stored in ChromaDB for that doc_id using collection.delete(where={"doc_id": doc_id}), and (2) delete the original file from storage. If only the file is deleted but vectors remain, users could still query ghost data from that document.

**Q10: How do you handle PDF files with images or scanned text?**

The current implementation uses PyPDF2, which only extracts text from text-layer PDFs. For scanned PDFs (image-only), we'd need OCR — tools like pytesseract, pdfplumber, or LlamaParse. This is listed as a known limitation and an extension idea.

### Performance & Scalability

**Q11: What happens if the user uploads a very large PDF (500+ pages)?**

Currently: It processes synchronously, which could time out. Better approaches: (1) Process asynchronously in a background task (FastAPI BackgroundTasks), (2) Show a progress indicator, (3) Implement chunked uploads. This is a known limitation for v1.

**Q12: How many documents can ChromaDB handle?**

ChromaDB with HNSW index can handle millions of vectors locally with good performance. For this project, with 500-character chunks and typical documents being 10–50 pages, a single collection might have 10,000–100,000 vectors — well within ChromaDB's local capacity.

**Q13: How would you scale this to thousands of users?**

Replace local ChromaDB with Pinecone or Supabase pgvector (managed, distributed). Replace file storage with S3. Add Redis caching for frequently asked questions. Move to a multi-worker deployment (Gunicorn + Uvicorn workers). Add rate limiting per user.

### Deployment & DevOps

**Q14: What is Docker and why did you use it?**

Docker packages the application and all its dependencies into a container image. This ensures the app runs identically across different machines — development, staging, and production. The Dockerfile defines exactly how to build the image, eliminating "works on my machine" problems.

**Q15: What environment variables does your app need?**

OPENAI_API_KEY (required — for embeddings and chat), CHROMA_PERSIST_PATH (optional — where to store ChromaDB data), MAX_FILE_SIZE_MB (optional — limit upload size), PORT (set by hosting platform).

### Testing & Quality

**Q16: How did you test the RAG quality?**

Manual testing: uploaded known documents and asked questions whose answers I knew. Verified source citations were accurate. For automated testing: wrote unit tests for the chunking logic and integration tests for the /query endpoint using pytest. For production: RAGAs framework can measure faithfulness and answer relevance automatically.

**Q17: What are the known limitations of your system?**

(1) Text-only PDFs — no OCR for scanned documents. (2) Synchronous large PDF processing may time out. (3) ChromaDB local storage isn't horizontally scalable. (4) No user authentication in v1 — anyone can access any document. (5) Render free tier cold starts (~10s delay after idle).

### Concepts

**Q18: What is the difference between fine-tuning and RAG for domain-specific Q&A?**

Fine-tuning trains the model's weights on your domain data — expensive, requires dataset preparation, and the knowledge is baked into the model (static). RAG retrieves current data at inference time — cheaper, flexible, supports dynamic or frequently updated documents, and can cite sources. For document Q&A with changing content, RAG is almost always the better choice.

**Q19: What is the role of temperature in the OpenAI API call?**

Temperature controls the randomness of the model's output. Temperature = 0: always picks the highest-probability token (deterministic, factual). Temperature = 1: more creative and varied. For factual Q&A, we use 0.1 — slightly above 0 to avoid completely rigid outputs while staying close to the most likely answer.

**Q20: How would you add conversation memory to this system?**

Store conversation history in the thread: each time the user asks a follow-up question, include the previous Q&A turns in the context. Implementation: use LangChain's ConversationBufferMemory or store messages in a session dict keyed by user_id. Limit: as history grows, it consumes context window. Solution: implement a sliding window or summarization of old turns.
