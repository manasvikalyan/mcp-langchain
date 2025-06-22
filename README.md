# 🧠 MCP LangChain Agent with Tool Servers

This project is a **modular, multi-tool LLM agent system** using [LangChain](https://www.langchain.com/), [LangGraph](https://github.com/langchain-ai/langgraph), [Groq](https://console.groq.com/), and [FastMCP](https://github.com/langchain-ai/langgraph/tree/main/libs/mcp).

It demonstrates how an LLM can **intelligently call external tools (math, weather, news)** hosted as local servers, simulating a **plugin-based AI agent system**.

---

## 🚀 Features

- ✅ **Local tool servers** for math, weather, and news (with FastMCP)
- ✅ **LLM reasoning with Groq’s Qwen model**
- ✅ **Agent framework via LangGraph’s ReAct agent**
- ✅ **Multi-tool orchestration using MultiServerMCPClient**
- ✅ **Interactive CLI loop for natural language queries**

---

## 🛠️ What I Built & Tested

### 1. **Math Server (`mathserver.py`)**
- Built with FastMCP
- Provides basic arithmetic tools: `add`, `subtract`, `multiply`
- Uses `stdio` transport

### 2. **Weather Server (`weatherserver.py`)**
- Returns mock weather info for a city
- Hosted via HTTP (`streamable-http`)

### 3. **News Server (`newsserver.py`)**
- Returns latest headlines for a topic (mocked)
- Uses `stdio` transport

### 4. **Client Agent (`client.py`)**
- Uses `MultiServerMCPClient` to connect to all 3 servers
- Creates a **Groq-powered LangChain ReAct Agent**
- Runs an interactive CLI loop to ask questions like:
  - “What’s (5 + 7) x 3?”
  - “What’s the weather in Delhi?”
  - “Give me news on AI.”

---

