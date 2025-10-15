# 🤖 AI Research Agent

This project is an AI-powered research assistant built using **Groq Llama 3.3** and **LangChain**. The goal of this project was not only to build a functional tool but also to gain a deeper understanding of AI agent workflows, structured data extraction, and integration of multiple APIs for information retrieval. 🚀

---

## 🔍 Project Overview

The AI Research Agent takes a research query as input, gathers information using tools like **Wikipedia** and **DuckDuckGo Search**, and produces a structured summary in JSON format. Additionally, it automatically saves the output to a text file for future reference. 📝

**Key capabilities:**

- 🌐 Fetch up-to-date information from the web.
- 📚 Retrieve accurate summaries from Wikipedia.
- 🗂 Structure information into:
  - Topic
  - Summary
  - Sources
  - Tools used
- 💾 Automatically save structured research outputs.

This project demonstrates how AI can assist with research, summarize content, and organize information efficiently. ⚡

---

## 🧠 Understanding and Learnings

From building this project, I gained:

1. **🛠 Tool Integration in AI Agents**  
   Learned how to integrate external tools like Wikipedia and DuckDuckGo Search into a LangChain agent and enable the AI to call them dynamically.

2. **📊 Structured Output with Pydantic**  
   Implemented Pydantic models to enforce strict JSON output format, ensuring reliable and easy parsing of AI responses.

3. **✍️ Prompt Engineering and Agent Design**  
   Understood the importance of designing system prompts and agent workflows to guide the AI in using tools correctly and producing structured output.

4. **🔒 Handling Secrets and GitHub Push Protection**  
   Learned best practices for managing API keys securely using `.env` and `.gitignore`, and how to clean sensitive information from Git history.

5. **⚡ Automation of Output Storage**  
   Built a mechanism to automatically save AI-generated research summaries to a file, demonstrating practical workflow automation.

---

## 🚀 Usage

1. **Install dependencies** .  
2. **Create a `.env` file** to store your API keys (Groq and Anthropic).  
3. **Run the agent**:

```bash
python main.py
