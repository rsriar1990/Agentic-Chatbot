An agentic AI application built using LangGraph, Groq LLMs, Tavily Search, and Streamlit, supporting three powerful use cases:

1. Basic Chatbot

2. Chatbot with Web Search Tools

3. AI News Explorer (automated AI news fetching, summarization, and markdown generation)

This project demonstrates how to build multi‑node agent workflows using LangGraph, integrate external tools, and expose everything through a clean Streamlit UI.

🚀 Features
1. Basic Chatbot
A simple LLM‑powered chatbot using Groq models.
Built using a single LangGraph node (BasicChatbotNode).

2. Chatbot with Web Search Tools
An advanced chatbot capable of calling external tools (Tavily Search) using LangChain’s tool binding.

Automatic tool routing

ToolNode integration

Conditional edges via tools_condition

3. AI News Explorer
A fully automated AI news pipeline:

Fetch AI news using Tavily

Summarize news using Groq LLM

Generate Markdown file

Display formatted AI news in Streamlit

The system creates files like:

Code
./AINews/daily_summary.md
./AINews/weekly_summary.md
./AINews/monthly_summary.md
📁 Project Structure
Code
Agentic-Chatbot/
│
├── src/
│   └── langgraph_agenticai/
│       ├── graph/
│       │   └── graph_builder.py
│       ├── nodes/
│       │   ├── basic_chatbot_node.py
│       │   ├── chatbot_with_tool_node.py
│       │   └── ai_news_node.py
│       ├── tools/
│       │   └── search_tool.py
│       ├── state/
│       │   └── state.py
│       └── ui/
│           └── streamlitui/
│               ├── loadui.py
│               └── display_results.py
│
├── AINews/               # Auto‑generated markdown summaries
│   ├── daily_summary.md
│   ├── weekly_summary.md
│   └── monthly_summary.md
│
├── requirements.txt
├── README.md
└── main.py
🧠 LangGraph Architecture
GraphBuilder
Responsible for constructing three different LangGraph workflows:

Basic Chatbot Graph
Code
START → chatbot → END

Chatbot with Tools Graph
Code
START → chatbot → (conditional) → tools → chatbot → END

AI News Graph
Code
START → fetch_news → summarize_news → save_results → END

🔧 Nodes Overview
BasicChatbotNode
A simple LLM invocation:

python
return {'messages': self.llm.invoke(state['messages'])}
ChatbotWithToolNode
Binds Tavily search tools to the LLM:

python
llm_with_tools = self.llm.bind_tools(tools)
AINewsNode
Handles the full AI news workflow:

fetch_news()
Reads timeframe (daily, weekly, monthly)

Calls Tavily search API

Stores results in graph state

summarize_news()
Converts raw news into structured markdown summaries

Uses Groq LLM for summarization

save_result()
Creates AINews/ folder automatically

Writes markdown file based on timeframe

🖥️ Streamlit UI
LoadStreamlitUI
Handles:

LLM selection (Groq models)

API key input (Groq + Tavily)

Use case selection

Timeframe selection for AI News

DisplayResultStreamlit
Displays results for:

Basic Chatbot

Chatbot with Tools

AI News Explorer

For AI News, it:

Invokes the LangGraph pipeline

Reads the generated markdown file

Displays it beautifully in Streamlit

🔑 Environment Variables
You must provide:

Code
GROQ_API_KEY=
TAVILY_API_KEY=
These are entered directly in the Streamlit sidebar.

📦 Installation
1. Clone the repository
bash
git clone https://github.com/rsriar1990/Agentic-Chatbot.git
cd Agentic-Chatbot
2. Install dependencies
bash
pip install -r requirements.txt
3. Run the Streamlit app
bash
streamlit run app.py
📰 AI News Output Example
Generated markdown files look like:

markdown
# Daily AI News Summary

- **2026‑07‑22** — OpenAI releases new multimodal update  
  [Read more](https://example.com)

- **2026‑07‑21** — Google DeepMind announces robotics breakthrough  
  [Read more](https://example.com)
🛠️ Technologies Used
Component	Technology
LLM	Groq LLMs
Agent Framework	LangGraph
Tools	Tavily Search API
UI	Streamlit
Prompting	LangChain ChatPromptTemplate
File Output	Markdown generation


✨ Highlights
Fully agentic architecture

Multi‑node LangGraph workflows

Real‑time web search integration

Automated AI news summarization

Clean Streamlit UI

Modular, scalable codebase
