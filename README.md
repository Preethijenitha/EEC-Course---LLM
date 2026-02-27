##📘 EEC Course — LLM

A repository for Large Language Model (LLM) based experiments and examples learned from the EEC Course.

##🧠 Overview

This project contains Python scripts exploring foundational LLM concepts and practical experiments including:

🛠️ Prompt engineering basics

🔗 Chain of thought pipelines

🔍 Conditional tools and custom tools

🔄 Parallel execution patterns

🧬 Groq API implementation (secure use via environment variables)

🤖 Sample workflows for LLM-centric functions

⚠️ Note: API keys or other secrets are not included for security.

##📁 Project Structure
File	Description
groq_runner.py	Example script integrating Groq API
main.py	Entry point to run sample tasks
chain.py	Script demonstrating chained logic
customtool.py	Implementation of a custom tool/module
conditional.py	Scripts with conditional execution logic
others	Supporting experiment scripts
🚀 Getting Started
##💡 Prerequisites

Install dependencies (assuming Python 3.9+):

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
##🔑 API Keys & Environment Variables

Create a .env file in the project root and add your keys:

GROQ_API_KEY=your_groq_api_key_here

This file must not be committed — it’s excluded by .gitignore.

##📦 Usage

Run the main script:

python main.py

Open specific modules for individual experiments:

python chain.py
python conditional.py
##💻 Development

To contribute or add more LLM experiments:

Fork the repository

Create a branch

Add tests or docs

Submit a pull request

##🔐 Security

Never commit .env

Regenerate API keys if they’re ever leaked

Use environment variable libraries (e.g., python-dotenv) for secure loading
