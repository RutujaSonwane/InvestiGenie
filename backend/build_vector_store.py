from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import shutil

# Step 1: Delete old index if exists
if os.path.exists("faiss_index"):
    shutil.rmtree("faiss_index")
    print("🧹 Old FAISS index deleted.")

# Step 2: Load all PDFs
doc_folder = "docs"
documents = []

for filename in os.listdir(doc_folder):
    if filename.endswith(".pdf"):
        path = os.path.join(doc_folder, filename)
        loader = PyPDFLoader(path)
        docs = loader.load()
        print(f"✅ Loaded {filename} with {len(docs)} pages")
        documents.extend(docs)

# Step 3: Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# (Optional) Add source metadata
for chunk in chunks:
    chunk.metadata["source"] = "investment_docs"

# Step 4: Create embeddings and build FAISS
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = FAISS.from_documents(chunks, embedding_model)

# Step 5: Save the index
vectordb.save_local("faiss_index")
print("✅ FAISS index created and saved!")
