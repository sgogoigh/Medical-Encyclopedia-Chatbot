# Medical Encyclopedia Chatbot

A **medical knowledge chatbot** built with **LangChain**, **Google Gemini**, and **Pinecone** for fast, context-aware question answering over a medical encyclopedia dataset, using the Gale Encyclopedia. 

This project demonstrates a **Retrieval-Augmented Generation (RAG)** pipeline where user queries are matched against pre-indexed medical documents to retrieve relevant context, which is then used to generate accurate, reliable answers.


## Features

- **Conversational Medical Assistant:** Answers health and disease-related questions using your own medical dataset.  
- **Retrieval-Augmented Generation (RAG):** Combines context retrieval from Pinecone with Gemini LLM for accurate responses.  
- **Hugging Face Embeddings:** Semantic vector representation using `sentence-transformers/all-MiniLM-L6-v2`.  
- **Pinecone Vector Store:** Scalable vector database for storing and retrieving document embeddings.  
- **Flask Web App:** Lightweight and responsive frontend served with Flask.  
- **Environment Variable Management:** Secure API key management using `.env`.

## Architecture Overview

```
                ┌────────────────────────┐
                │        User Query       │
                └────────────┬────────────┘
                             │
                  (Flask Web Interface)
                             │
                             ▼
               ┌────────────────────────┐
               │   Retrieval Pipeline    │
               │ (LangChain + Pinecone) │
               └────────────────────────┘
                             │
            Retrieves top-k relevant medical docs
                             │
                             ▼
                ┌────────────────────────┐
                │  Gemini LLM (RAG Chain)│
                └────────────────────────┘
                             │
                 Generates contextual response
                             │
                             ▼
                ┌────────────────────────┐
                │   Chat UI (chat.html)  │
                └────────────────────────┘

```

## File Structure
```
├── app.py                  # Flask backend entry point
├── template.py             # create the folder structure
├── setup.py                # setting up project
├── .env                    # Stores API keys (not checked in)
├── requirements.txt        # Dependencies
├── src/
│ ├── helper.py             # Embedding & Pinecone helper functions
│ ├── prompt.py 
│ ├── init.py 
├── static/
│ └── style.css
├── test/
│ └── notebook-test.ipynb   # Creating vectors in pinecone
├── .gitignore 
└── README.md               # Project documentation
```

## Installation

### Clone this repository
```bash
git clone https://github.com/<your-username>/Medical-Encyclopedia-Chatbot.git
cd Medical-Encyclopedia-Chatbot
```

### Create and activate a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Create `.env` file to store API keys
```
PINECONE_API_KEY=your_pinecone_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### Execute
```bash
python app.py
```
___

> BY - Sunny Gogoi