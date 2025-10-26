# Text Search Engine using TF-IDF and IDF

A simple Python project that implements a **text search engine** using the **TF-IDF** algorithm and **Cosine Similarity**.  
It also calculates **IDF (Inverse Document Frequency)** for all words in a given collection of text files.

---

## Overview

This project demonstrates how to:
- Automatically read all `.txt` files from a folder
- Compute **IDF** (to measure word importance)
- Build a **TF-IDF vectorizer** for all documents
- Allow the user to enter a **search query**
- Rank and display the most relevant documents using **cosine similarity**

---

## Project Structure
```bash
text-search-engine/
│
├── documents/ # Folder containing text documents
│ ├── doc1.txt
│ ├── doc2.txt
│ └── ...
│
├── idf_calculator.py # Calculates IDF values for all words
├── search_engine.py # TF-IDF search engine using cosine similarity
├── requirements.txt # Dependencies for the project
└── README.md # Project documentation
```

---

## Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/text-search-engine.git
cd text-search-engine
```

2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
3️⃣ Add Text Documents
```bash
Put your .txt files in the documents/ folder.
Example structure:
documents/
├── doc1.txt
├── doc2.txt
├── doc3.txt
```

Usage
▶ Run the IDF Calculator

To calculate the top words by their IDF score, run:
```bash
python idf_calculator.py
```

Sample Output:
🔹 10 words with the highest IDF value:
- changing: 1.6094
- world: 1.6094
- subset: 1.6094
- deep: 1.6094
- learning: 0.9163
- machine: 0.9163
- is: 0.5108

▶ Run the Search Engine

To perform text search using TF-IDF:
```bash
python search_engine.py
```

You will be prompted to enter a query:
```bash
Enter your query: machine learning
```
Output Example:
🔹 Related docs:
- doc2.txt (Similarity: 0.8423)
- doc1.txt (Similarity: 0.6347)
- doc4.txt (Similarity: 0.2984)

---
🧮 IDF Formula

The mathematical formula used in this project:

IDF(t)=log(N / df(t) + 1)

Where:

N = total number of documents

df(t) = number of documents containing the term t

This helps determine how important each word is across all documents.

Technologies Used

Python 3.x

scikit-learn (TF-IDF Vectorizer, Cosine Similarity)

math & collections modules

---

📊 Example Folder Layout
```bash
📂 text-search-engine/
 ┣ 📂 documents/
 ┃ ┣ 📜 doc1.txt
 ┃ ┣ 📜 doc2.txt
 ┃ ┗ 📜 doc3.txt
 ┣ 📜 idf_calculator.py
 ┣ 📜 search_engine.py
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
```

