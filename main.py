import os
from utils import preprocessing, ner

# Set the directory containing research papers
papers_directory = 'data/papers/'

# Preprocess the data
preprocessed_text = []
for filename in os.listdir(papers_directory):
    if filename.endswith('.pdf'):
        file_path = os.path.join(papers_directory, filename)
        text = preprocessing.pdf_to_text(file_path)
        tokens = preprocessing.clean_and_tokenize(text)
        preprocessed_text.append(tokens)

print("Data Preprocessing completed.")

# Perform Named Entity Recognition
entities_list = []
for text in preprocessed_text:
    entities = ner.perform_ner(text)
    entities_list.append(entities)

# Print the extracted entities
for i, entities in enumerate(entities_list):
    print(f"Document {i+1} entities:")
    for entity in entities:
        print(f"- {entity[0]} ({entity[1]})")
    print()

print("Named Entity Recognition completed.")