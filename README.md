# AI Agentic Runtime Engine 🚀

A production-grade, stateful agentic framework that enables autonomous execution of code with built-in security, persistence, and observability.

## 🛠 Tech Stack
- **Frameworks**: LangGraph, FastAPI, LangChain
- **LLM**: Groq (Llama-3.3-70b-versatile)
- **Runtime Security**: Docker-isolated sandboxing
- **Persistence**: SQLite-based checkpointing (SqliteSaver)

## 🏗 Key Engineering Highlights
- **Stateful Workflow**: Leveraged `LangGraph` to manage complex, cyclic agentic workflows with persistent state management.
- **Secure Execution**: Implemented a sandbox layer using `DockerManager` to safely execute untrusted LLM-generated code.
- **Resilience**: Engineered robust error handling for API deprecation and environment configuration, ensuring zero-downtime during model transitions.

## 🚀 How to Run
1. Clone the repo: `git clone https://github.com/vibhutidureja/ai-agent-runtime.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment: Create a `.env` file with `GROQ_API_KEY=your_key_here`
4. Run: `uvicorn src.api.main:app --reload`
