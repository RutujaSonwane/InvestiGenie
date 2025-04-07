from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from local_llm import generate_response_from_llm  # Make sure this is defined in local_llm.py

# Load embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load FAISS index from local folder
vectordb = FAISS.load_local("faiss_index", embeddings=embedding_model, allow_dangerous_deserialization=True)

def get_response(query):
    try:
        docs = vectordb.similarity_search(query)
        context = "\n".join([doc.page_content for doc in docs])

        prompt = f"Answer the question based on the context below:\n\nContext:\n{context}\n\nQuestion: {query}"
        return generate_response_from_llm(prompt)
    
    except Exception as e:
        print(f"[get_response ERROR]: {e}")
        return "Sorry, something went wrong while processing your request."

