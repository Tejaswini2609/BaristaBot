import os
from dotenv import load_dotenv
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
import streamlit as st

load_dotenv()
groq_api_key = os.getenv("groq_api_key")
model = ChatGroq(model="gemma2-9b-it",groq_api_key = groq_api_key)
embeddings = OllamaEmbeddings(model="gemma2:2b")
mydb = FAISS.load_local("faiss_index",embeddings=embeddings,allow_dangerous_deserialization=True)
retriever = mydb.as_retriever(search_type='similarity',search_kwargs={"k":6})

st.title("Welcome to TT's Cafe")
query = st.chat_input("Ask me anything: ")
system_prompt = (
    "You are an assistant for a question answering tasks. "
    "for a restaurant called as TT's caffe."
    "Use the following pieces of retrieved context to answer the question."
    "Make sure the answers are in the favour of restaurant."
    "Be very polite while answering."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ('human',"{input}"),
    ]
)

if query:
    question_answer_chain = create_stuff_documents_chain(model,prompt)
    rag_chain = create_retrieval_chain(retriever,question_answer_chain)

    response = rag_chain.invoke({"input":query})
    st.write(response["answer"])