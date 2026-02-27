🚀 EEC Course — Large Language Models (LLM)

🔥 A hands-on repository exploring Large Language Models, LangChain workflows, Groq API integration, and advanced execution patterns through practical Python implementations.

🌟 About This Project

This repository contains structured experiments and implementations developed during the EEC LLM Course.

It demonstrates:

✨ Prompt Engineering
✨ LLM Chains & Pipelines
✨ Conditional Execution
✨ Parallel Workflows
✨ Custom Tool Integration
✨ Groq API Usage
✨ TypedDict & Pydantic Models
✨ Runnable & Lambda Patterns

This project is designed to build strong foundational and practical knowledge in LLM-based application development.

🧠 Core Concepts Covered

🔹 Basic LLM Invocation
🔹 Sequential & Conditional Chains
🔹 Parallel Processing with Runnables
🔹 Tool Creation & Integration
🔹 Environment Variable Security
🔹 Structured Output Handling
🔹 Modular Code Architecture

📂 Project Structure
EEC-Course---LLM/
│
├── groq_runner.py      → Groq API integration
├── main.py             → Entry execution file
├── chain.py            → Chain workflow examples
├── conditional.py      → Conditional execution logic
├── parallel.py         → Parallel LLM execution
├── customtool.py       → Custom tool implementation
├── runnable.py         → Runnable patterns
├── pydan2.py / pydan3.py → Pydantic examples
├── typeddict.py        → TypedDict usage
├── tool1.py / tool2.py → Tool demonstrations
├── basics.py           → LLM fundamentals
└── README.md           → Project documentation
⚙️ Installation & Setup
🔹 Step 1: Clone Repository
git clone https://github.com/Preethijenitha/EEC-Course---LLM.git
cd EEC-Course---LLM
🔹 Step 2: Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
🔹 Step 3: Install Dependencies

If you have requirements.txt:

pip install -r requirements.txt

Or install manually:

pip install langchain groq python-dotenv pydantic
🔐 Environment Variables (IMPORTANT)

Create a .env file in the root directory:

GROQ_API_KEY=your_actual_api_key_here

⚠️ Never push .env to GitHub
⚠️ Always keep secrets in environment variables

▶️ How to Run

Run main script:

python main.py

Run specific modules:

python chain.py
python conditional.py
python parallel.py
🛡️ Security Best Practices

✔️ Use .gitignore properly
✔️ Never expose API keys
✔️ Regenerate keys if leaked
✔️ Keep production secrets secure

📈 Learning Outcomes

By working through this repository, you will understand:

How LLM workflows are structured

How to build modular AI pipelines

How to integrate external APIs securely

How to design scalable LLM applications
