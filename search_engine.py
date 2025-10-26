# ---------------------- search_engine.py ----------------------
import os
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------- Reading text files from the documents folder
folder_path = r"documents" 
documents = []
file_names = []

for file in os.listdir(folder_path):
    if file.endswith(".txt"):
        file_path = os.path.join(folder_path, file)
        with open(file_path, "r") as f:
            documents.append(f.read().lower())
            file_names.append(file)

# ---------------------- Creating a TF-IDF model
vectorizer = TfidfVectorizer()
Tfidf_matrix = vectorizer.fit_transform(documents).toarray()


# ---------------------- Receive Query from the user
query = input("enter your query: ").lower()
query_vector = vectorizer.transform([query])

# ---------------------- find similar docs with cosine similarity
cosine_similarities = cosine_similarity(query_vector, Tfidf_matrix).flatten()

# ---------------------- Sort results by most similar
sorted_indices = cosine_similarities.argsort()[::-1]

# ---------------------- Show 5 Top docs
print("\n related docs:")
for index in sorted_indices[:5]:
    print(f"- {file_names[index]} (Similarity: {cosine_similarities[index]:.4f})")