# AI Agent Builder

**AI Agent Builder** is a powerful, customizable platform where users can:
- Provide their own **system prompt**
- Select an **LLM model** of choice
- Submit queries and get AI-powered responses  
This project integrates advanced AI tooling for flexibility, real-time search, and multi-model support.

---

## 🚀 Features
- **Custom System Prompt** — Define your agent’s personality and behavior.
- **Multi-Model Support** — Choose from different Large Language Models.
- **Web Search Integration** — Powered by Tavily for live information.
- **Modular Architecture** — Streamlit (frontend) + FastAPI (backend).
- **Agent Orchestration** — LangGraph for advanced workflows.
- **LLM Integration** — LangChain for seamless model invocation.

---

## 🛠️ Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
- **Agent Framework:** [LangGraph](https://www.langchain.com/langgraph)
- **LLM Orchestration:** [LangChain](https://www.langchain.com/)
- **Web Search Tool:** [Tavily](https://tavily.com/)

---

## 📂 Project Structure
ai-agent-builder/
│ ── backend.py # FastAPI backend
│ ── agent.py # LangGraph agent setup
│ ├── front.py # Streamlit UI
├── README.md # Project documentation
└── .env.example # Environment variables template

yaml
Copy
Edit

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/ai-agent-builder.git
cd ai-agent-builder
2️⃣ Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Configure Environment Variables
Copy .env.example to .env and fill in your API keys:

ini
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
▶️ Running the Project
Start Backend (FastAPI)
bash
Copy
Edit
cd backend
uvicorn main:app --reload
Start Frontend (Streamlit)
bash
Copy
Edit
cd frontend
streamlit run app.py
📌 Example Use Case
Open the Streamlit interface.

Enter a system prompt to define your AI agent's personality.

Select a preferred LLM model from the dropdown.

Type your query.

Get AI-generated responses — with live web search results if needed.