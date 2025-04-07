from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

# Load and split text data
data_path = "data/investment_faq.txt"
with open(data_path, "r", encoding="utf-8") as f:
    faq_list = [line.strip() for line in f if line.strip()]

# Convert to embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(faq_list)

# Save index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))
faiss.write_index(index, "data/faiss_index.index")

# Save mapping for answers
with open("data/faq_mapping.pkl", "wb") as f:
    pickle.dump(faq_list, f)

print("✅ FAISS index and FAQ mapping saved!")
