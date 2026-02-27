<hr>

<h1 align="center">🚀 EEC COURSE — LARGE LANGUAGE MODELS (LLM)</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" />
  <img src="https://img.shields.io/badge/Domain-Generative%20AI-purple.svg" />
  <img src="https://img.shields.io/badge/Focus-LLM%20Engineering-orange.svg" />
  <img src="https://img.shields.io/badge/Status-Active-success.svg" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg" />
</p>

<p align="center">
  <b>A Structured Learning Repository for Understanding, Building, and Deploying Large Language Models</b>
</p>

<p align="center">
  Theory • Hands-on Implementation • Prompt Engineering • LLM Workflows • Real-World Applications
</p>

<hr>

---

## 📌 About This Repository

This repository documents my structured learning journey in **Large Language Models (LLMs)** as part of the EEC Course.

It covers:

- Core theoretical foundations of LLMs  
- Transformer architecture concepts  
- Prompt engineering techniques  
- Retrieval-Augmented Generation (RAG)  
- Tool usage & Agents  
- Practical implementation using Python  
- Real-world mini projects and experiments  

This repo is designed to serve as:
- 📚 A learning reference  
- 🧪 A hands-on experimentation space  
- 💼 A portfolio-ready showcase  

---

## 🧠 Topics Covered

- Introduction to Generative AI  
- Evolution of Language Models  
- Transformers Architecture  
- Tokenization & Embeddings  
- LLM Workflows  
- Prompt Engineering Strategies  
- RAG (Retrieval-Augmented Generation)  
- Agents & Tool Calling  
- Vector Databases  
- API-based LLM Integration  
- Mini Projects & Practical Exercises  

---

## 🛠️ Tech Stack

- Python  
- Jupyter Notebook  
- OpenAI / LLM APIs  
- LangChain (if used)  
- Vector Databases  
- Git & GitHub  

---

## 📂 Project Structure
LLM-Project/
│
├── main.py            # Entry point of the application
├── groq_runner.py     # Groq API integration layer
├── basics.py          # Basic LLM usage examples
├── chain.py           # Sequential chain workflows
├── conditional.py     # Conditional logic execution
├── parallel.py        # Parallel runnable examples
├── runnable.py        # Runnable pattern demonstrations
│
├── customtool.py      # Custom tool integration
├── tool1.py           # Tool example 1
├── tool2.py           # Tool example 2
│
├── typeddict.py       # Structured output using TypedDict
├── pydan2.py          # Structured output using Pydantic
│
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
---

## ⚙️ Installation & Setup

# 1️⃣ Clone Repository
git clone https://github.com/Preethijenitha/EEC-Course---LLM.git
cd EEC-Course---LLM
# 2️⃣ Create Virtual Environment (Mac/Linux)
python3 -m venv venv
source venv/bin/activate
# 2️⃣ Create Virtual Environment (Windows)
python -m venv venv
venv\Scripts\activate
# 3️⃣ Install Dependencies
pip install -r requirements.txt
# 4️⃣ Create .env File (Mac/Linux)
echo "GROQ_API_KEY=your_api_key_here" > .env
# ▶️ Run the Project
python main.py

