# main.py

import os
from utils import preprocessing, ner, keyword_extraction, semantic_similarity

# Set the directory containing research papers
papers_directory = 'data/papers/'

# Preprocess the data
preprocessed_text = []
for filename in os.listdir(papers_directory):
    if filename.endswith('.pdf'):
        file_path = os.path.join(papers_directory, filename)
        text = preprocessing.pdf_to_text(file_path)
        tokens = preprocessing.clean_and_tokenize(text)
        preprocessed_text.append(" ".join(tokens))

print("Data Preprocessing completed.")

# Perform Named Entity Recognition
entities_list = []
for text in preprocessed_text:
    entities = ner.perform_ner(text.split())
    entities_list.append(entities)

# Print the extracted entities
for i, entities in enumerate(entities_list):
    print(f"Document {i+1} entities:")
    for entity in entities:
        print(f"- {entity[0]} ({entity[1]})")
    print()

print("Named Entity Recognition completed.")

# Perform Keyword Extraction
top_keywords = keyword_extraction.extract_keywords(preprocessed_text, top_n=10)

# Print the top keywords for each document
for i, keywords in enumerate(top_keywords):
    print(f"Document {i+1} top keywords:")
    for keyword in keywords:
        print(f"- {keyword}")
    print()

print("Keyword Extraction completed.")

# Calculate Semantic Similarity
similarity_matrix = semantic_similarity.calculate_similarity(preprocessed_text)

print("Semantic Similarity calculation completed.")
print("Similarity Matrix:")
print(similarity_matrix)