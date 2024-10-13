from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

import requests
import os
import json
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if os.environ.get('REACT_APP_OPENAI_API_KEY'):
    os.environ['OPENAI_API_KEY'] = os.environ.get('REACT_APP_OPENAI_API_KEY')

vector_store = None

def create_vector_store(embeddings):
    docs = []
    # Load all PDFs in pdf folder
    for file in os.listdir("pdf"):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(f"pdf/{file}")
            docs += loader.load()    
    return FAISS.from_documents(docs, embeddings)

vector_db_path = f'./databases/faiss.db'
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
if os.path.exists(vector_db_path):
    vector_store = FAISS.load_local(vector_db_path, embeddings, allow_dangerous_deserialization=True)
else:
    print("Creating new vector store...")
    os.makedirs(os.path.dirname(vector_db_path), exist_ok=True)
    # Create faiss database
    vector_store = create_vector_store(embeddings)
    vector_store.save_local(vector_db_path)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/search/")
def search(query: str):
    neighbors = vector_store.similarity_search_with_score(query, k=3, fetch_k=3)
    print(neighbors)
    return [
        {
            "content": neighbor[0].page_content,
            "score": float(neighbor[1]),
            "metadata": neighbor[0].metadata
        }
        for neighbor in neighbors
    ]

    
    
# Publish pdfs as static files
@app.get("/pdf/{file}")
def read_pdf(file: str):
    return FileResponse(f"pdf/{file}")