# 🧠 Agentic RAG

A lightweight Agentic Retrieval-Augmented Generation (RAG) system built with LangGraph, LangChain, FAISS, and Azure OpenAI that intelligently decides whether retrieval is required before answering a question.

## 🚀 Overview

This project demonstrates how to:
1. Build an agent-like workflow using LangGraph
2. Use a Router LLM to decide if context retrieval is needed
3. Retrieve relevant chunks using FAISS vector search
4. Use Azure OpenAI GPT models to generate accurate, context-aware answers
5. Maintain a clean, modular code structure for real-world applications

🧩 **Tech Stack**
- 🐍 Python 3.10+
- 🔗 LangChain for document + LLM orchestration
- 🔀 LangGraph for multi-step state-based workflows
- ⚡ FAISS for vector similarity search
- 🧬 Azure OpenAI Embeddings
- 🤖 Azure OpenAI GPT for natural language generation

## 📂 Project Structure
```bash
agentic_rag/
│
├── config/
│   └── settings.py
│
├── llms/
│   ├── router_llm.py
│   └── rag_llm.py
│
├── embeddings/
│   └── embeddings.py
│
├── vectorstore/
│   └── store.py
│
├── graph/
│   ├── nodes.py
│   └── workflow.py
│
├── main.py
└── requirements.txt
```

## 🛠 Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/vatsallolariya/Agentic-RAG.git
cd agentic_rag
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
# or
source .venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
Or using uv:
```bash
uv init
uv add -r requirements.txt
```

## 🔐 Azure OpenAI Configuration
Create a .env file in the root directory:
```bash
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_CHAT_DEPLOYMENT==
AZURE_OPENAI_EMBED_DEPLOYMENT=
AZURE_OPENAI_API_VERSION=
```
Your credentials will be automatically loaded through python-dotenv.

## ▶️ Usage
Run the main program:
```bash
python main.py
```

Example:
```bash
print(ask_question("Explain LangGraph."))
```

## 🧩 LangGraph Workflow Diagram
<img width="143" height="432" alt="graph" src="https://github.com/user-attachments/assets/8cfb6c74-9906-4f19-94e9-4c2a2589c3f3" />

## ✅ Example Queries (YES & NO Scenarios)
✔ 1. YES — Retrieval Needed
```bash
Query
"What is LangGraph and how does it work?"

Why YES?
Because the answer requires factual information stored in your FAISS vector database.

Router Output
YES

Flow
Retrieve documents → Generate answer using context
```

❌ 2. NO — Retrieval Not Needed
```bash
Query:
"Tell me a joke."

Why NO?
The question does not require document knowledge — the LLM already knows how to answer.

Router Output:
NO

Flow:
Skip retrieval → Generate direct answer
```

