from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings

from langchain_pinecone import Pinecone as PineconeVectorStore

from langchain_core.runnables import RunnablePassthrough

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from src.prompt import *
import os

# Flask backend
app = Flask(__name__)

# loading api keys
load_dotenv()

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
GEMINI_API_KEY=os.environ.get('GEMINI_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

if GEMINI_API_KEY:
    os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
print("API Keys loaded")

# HuggingFace embeddings
embeddings = download_hugging_face_embeddings()

print("Embeddings loaded")

# Loading existings indices from pinecone
index_name = 'medical-encyclopedia'
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)
print("Indices loaded")

# setting retriever
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})
print("Retriver loaded")

# gemini as llm
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens = 5000,
    api_key=GEMINI_API_KEY
)
print("LLM set")

# conversation chain creation
rag_chain = (
    {"context": retriever | (lambda docs: "\n\n".join([d.page_content for d in docs])),
     "question": RunnablePassthrough()}
    | system_prompt
    | llm
)
print("Chain created")

# basic default route
@app.route("/")
def index():
    return render_template('chat.html')

# the chats and responses
@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke(msg)
    print("Response : ", response.content)
    return str(response.content)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= False)