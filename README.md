# AI Chatbot Using LLMs

A full-stack AI chatbot application built using FastAPI (backend) and Streamlit (frontend), integrated with a Large Language Model (LLM) API to provide human-like conversational responses.

## Objective

The objective of this project is to design and implement a full-stack AI chatbot that can interact with users in a natural and conversational manner using modern AI tools and software engineering practices.



##  Tech Stack

- **Programming Language:** Python  
- **Backend Framework:** FastAPI  
- **Frontend Framework:** Streamlit  
- **AI Model:** Large Language Model (LLM API)  
- **Version Control:** Git & GitHub


## Project Structure

coincent-ai-chatbot/
├── backend/
│   ├── main.py
│   ├── __init__.py
│
├── frontend/
│   ├── app.py
│
├── requirements.txt
├── README.md

## How to Run the Project

Follow the steps below to run the AI Chatbot locally on your system.

### Clone the Repository
```bash
git clone <your-github-repo-link>
cd coincent-ai-chatbot

### Install Dependencies
```bash
pip install -r requirements.txt

### Run Backend (FastAPI)
```bash
python -m uvicorn backend.main:app --reload

### Backend will start at:
http://127.0.0.1:8000

### Run Frontend (Streamlit)
Open a new terminal and run:
```bash
streamlit run frontend/app.py
Frontend will open in browser at:
Copy code
http://localhost:8501

## Features
- Interactive chat interface built using Streamlit  
- FastAPI backend for handling chat requests  
- Integration with Large Language Model (LLM API)  
- Human-like, casual conversational responses  
- Supports English, Hindi, and Hinglish based on user input  
- Clean separation of frontend and backend architecture