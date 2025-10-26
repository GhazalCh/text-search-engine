# ---------------------- idf_calculator.py ----------------------
import os
import math
from collections import Counter

# ---------------------- Specify the path to the documents folder
folder_path = r"documents" # The path to the folder where the .txt files are located.
documents = []
file_names = []

# ---------------------- Read .txt files
for file in os.listdir(folder_path):
    if file.endswith(".txt"):
        file_path = os.path.join(folder_path, file)
        with open(file_path, "r") as f:
            documents.append(f.read().lower())
            file_names.append(file)

# ---------------------- IDF Methode
# ---------------------- Tokenizing documents
tokenized_docs = [doc.split() for doc in documents]

# ---------------------- Calculate DF (Document Frequency)
dataframe = Counter()
total_docs = len(tokenized_docs)

for doc in tokenized_docs:
    unique_words = set(doc)
    for word in unique_words:
        dataframe[word] += 1

# ---------------------- Calculate IDF for each word
idf = {}
for word, freq in dataframe.items():
    idf[word] = math.log(total_docs / (freq + 1))

# ---------------------- Show 10 words with the highest IDF value
sorted_idf = sorted(idf.items(), key=lambda x: x[1], reverse=True)[:10]

print("10 word with most IDF:")
for word, score in sorted_idf:
    print(f"- {word}: {score:.4f}")