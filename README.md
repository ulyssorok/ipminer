# IPMiner

IPMiner is a Python-based project that identifies potential intellectual property (IP) from a large corpus of research papers. It performs various natural language processing tasks such as data preprocessing, named entity recognition, keyword extraction, semantic similarity calculation, text summarization, and IP identification.

## Project Status: Version 1.0 - In Development
IPMiner is currently in version 1.0 and under active development. As such, it is subject to significant changes and improvements. The current release is intended for early testing, feedback, and contributions from the community.

## Features

- Data preprocessing: Converts PDF files to plain text and performs text cleaning and tokenization.
- Named Entity Recognition (NER): Identifies and extracts relevant entities from the preprocessed text.
- Keyword Extraction: Extracts important keywords and phrases from the research papers using the TF-IDF algorithm.
- Semantic Similarity: Calculates the cosine similarity between research papers to identify related ideas or technologies.
- Text Summarization: Generates concise summaries of the research papers using the LSA summarization technique.
- IP Identification: Identifies potential IP based on keyword matching.
- Visualization: Creates a keyword graph to visualize the relationships between documents and keywords.
- Output Export: Exports the extracted named entities, top keywords, summaries, and potential IP documents to separate text files.

## Installation

1. Clone the repository: git clone https://github.com/ulyssorok/IPMiner.git
2. Navigate to the project directory: cd IPMiner
3. Install the required dependencies: pip install -r requirements.txt

## Usage

1. Place your research papers (PDF files) in the `data/papers/` directory.
2. Run the `main.py` script: python main.py
3. The script will process the research papers, perform various NLP tasks, and generate output files in the `outputs/` directory.

## Output

The following output files will be generated in the `outputs/` directory:

- `named_entities.txt`: Contains the extracted named entities for each document.
- `top_keywords.txt`: Contains the top keywords for each document.
- `summaries.txt`: Contains the generated summaries for each document.
- `potential_ip.txt`: Contains the identified potential IP documents.
- `keyword_graph.png`: Visualization of the keyword graph.

## Requirements

The project requires the following dependencies:

- Python 3.x
- PyPDF2
- spaCy
- scikit-learn
- sumy
- matplotlib
- networkx

The full list of dependencies can be found in the `requirements.txt` file.

## License

This project is licensed under the [MIT License](LICENSE).

