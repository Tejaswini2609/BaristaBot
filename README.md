# BaristaBot
#The code provided implements a Q&A system for a restaurant called "TT's Cafe" using Streamlit, Langchain, and Groq.
Environment Variables:
Loads environment variables from a .env file using dotenv. The Groq API key is fetched from the environment.
Groq Model Setup:
Initializes the Groq model (gemma2-9b-it) using the Groq API key, which is used for generating responses based on user input.
Ollama Embeddings and FAISS Vector Store:
Uses Ollama embeddings (gemma2:2b) to convert text data into vector representations.
Loads a pre-built FAISS index (faiss_index) which stores the embeddings, allowing for fast similarity searches.
Retriever Setup:
Configures a retriever to fetch the top 6 relevant documents based on similarity to the user’s query.
Streamlit UI:
Streamlit is used to create a simple web interface where users can ask questions related to TT's Cafe.
The st.text_input() function collects the user's query.
Chat Prompt Template:
Defines a system prompt that instructs the model to answer questions politely and in favor of the restaurant, using context retrieved from the FAISS index.
Retrieval-Augmented Generation (RAG):
The system retrieves the top relevant documents based on the query using the retriever, then generates a response by combining the context with the user's query.
A create_stuff_documents_chain and create_retrieval_chain are used to set up the RAG pipeline.
Error Handling:
The script includes basic error handling for missing API keys, failed index loading, and query processing errors. If any of these errors occur, appropriate messages are shown in the Streamlit UI.
Workflow:
The user inputs a query through the Streamlit interface.
The system retrieves relevant information from the FAISS index based on the query.
The model generates a polite and helpful response based on the retrieved context.
The response is displayed on the Streamlit page.





🌟 Instructions for Generating a New API Key
To ensure the application keeps running, each user must generate their own API key.


