# utils/ner.py

import spacy

# Load the pre-trained NER model
nlp = spacy.load("en_core_web_trf")

# Function to perform NER on preprocessed text
def perform_ner(text):
    doc = nlp(" ".join(text))
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
    return entities