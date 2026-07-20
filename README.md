# Agentic Chatbot

A flexible, agent-driven chatbot designed to dynamically orchestrate tasks, use tools, and maintain contextually aware conversations. This repository contains the core logic, tool integrations, and agent workflows.

---

## 🚀 Features

*   **Tool Calling:** Automatically detects when to use external tools.
*   **Modular Architecture:** Easily swap out underlying LLM providers or add custom tools.
*   **Streaming Support:** Real-time token streaming for low-latency user experiences.

---

## 🛠️ Tech Stack

*   **Language:** Python 3.10+
*   **Frameworks:** LangChain 
*   **API Layer:** Streamlit 

---

## ⚙️ Getting Started

### Prerequisites

Make sure you have Python installed, along with `pip` and `virtualenv`.

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/rsriar1990/Agentic-Chatbot.git](https://github.com/rsriar1990/Agentic-Chatbot.git)
   cd Agentic-Chatbot

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

pip install -r requirements.txt

TAVILY_API_KEY=your_TAVILY_API_KEY_here
GROQ_API_KEY+your_GROQ_API_KEY_here

streamlit run app.py