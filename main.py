# main.py

import os
import time
from utils import preprocessing, ner, keyword_extraction, semantic_similarity, text_summarization, ip_identification, visualization

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

# Perform Text Summarization
summaries = []
for text in preprocessed_text:
    summary = text_summarization.summarize_text(text, num_sentences=3)
    summaries.append(summary)

# Print the summaries for each document
for i, summary in enumerate(summaries):
    print(f"Document {i+1} summary:")
    print(summary)
    print()

print("Text Summarization completed.")

# Perform IP Identification
ip_keywords = ["patent", "invention", "intellectual property", "trade secret"]
potential_ip_documents = []

for i, text in enumerate(preprocessed_text):
    if ip_identification.identify_potential_ip(text, ip_keywords):
        potential_ip_documents.append(i+1)

# Print the potential IP documents
if potential_ip_documents:
    print("Potential IP found in the following documents:")
    for doc_id in potential_ip_documents:
        print(f"- Document {doc_id}")
else:
    print("No potential IP identified in the documents.")

print("IP Identification completed.")

# Perform Visualization
print("Generating keyword graph...")
visualization.create_keyword_graph(top_keywords)
print("Keyword graph saved to outputs/keyword_graph.png")

# Export outputs to files
print("Exporting outputs to files...")

with open("outputs/named_entities.txt", "w") as f:
    for i, entities in enumerate(entities_list):
        f.write(f"Document {i+1} entities:\n")
        for entity in entities:
            f.write(f"- {entity[0]} ({entity[1]})\n")
        f.write("\n")

with open("outputs/top_keywords.txt", "w") as f:
    for i, keywords in enumerate(top_keywords):
        f.write(f"Document {i+1} top keywords:\n")
        for keyword in keywords:
            f.write(f"- {keyword}\n")
        f.write("\n")

with open("outputs/summaries.txt", "w") as f:
    for i, summary in enumerate(summaries):
        f.write(f"Document {i+1} summary:\n")
        f.write(summary)
        f.write("\n\n")

with open("outputs/potential_ip.txt", "w") as f:
    if potential_ip_documents:
        f.write("Potential IP found in the following documents:\n")
        for doc_id in potential_ip_documents:
            f.write(f"- Document {doc_id}\n")
    else:
        f.write("No potential IP identified in the documents.\n")

print("Output files saved to the outputs folder.")

# Enhanced terminal reporting
print("\nIPMiner - Identifying Potential IP from Research Papers")
print("=" * 50)

steps = [
    "Data Preprocessing",
    "Named Entity Recognition",
    "Keyword Extraction",
    "Semantic Similarity Calculation",
    "Text Summarization",
    "IP Identification",
    "Visualization"
]

for step in steps:
    print(f"\nPerforming {step}...")
    time.sleep(1)
    print("[" + "=" * 20 + ">]")
    print(f"{step} completed.")

print("\nIPMiner process completed successfully!")