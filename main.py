import os
import time
from colorama import Fore, Style
from utils import preprocessing, ner, keyword_extraction, semantic_similarity, text_summarization, ip_identification, visualization, loading

# Set the directory containing research papers
papers_directory = 'data/papers/'

def main():
    print(f"{Fore.BLUE}")
    print(f"██╗██████╗ ███╗   ███╗██╗███╗   ██╗███████╗██████╗ ")
    print(f"██║██╔══██╗████╗ ████║██║████╗  ██║██╔════╝██╔══██╗")
    print(f"██║██████╔╝██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝")
    print(f"██║██╔═══╝ ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗")
    print(f"██║██║     ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║")
    print(f"╚═╝╚═╝     ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝")
    print(f"{Style.RESET_ALL}")
    print()

    # Preprocess the data
    print("PERFORMING DATA PREPROCESSING...")
    total_files = len(os.listdir(papers_directory))
    preprocessed_text = []
    for i, filename in enumerate(os.listdir(papers_directory)):
        if filename.endswith('.pdf'):
            file_path = os.path.join(papers_directory, filename)
            text = preprocessing.pdf_to_text(file_path)
            tokens = preprocessing.clean_and_tokenize(text)
            preprocessed_text.append(" ".join(tokens))
            loading.display_progress_bar("DATA PREPROCESSING", i+1, total_files)

    loading.display_progress_bar("DATA PREPROCESSING", total_files, total_files)  # Ensure the progress bar is fully loaded

    print(f"DATA PREPROCESSING COMPLETE. {Fore.RED}{len(preprocessed_text)}{Style.RESET_ALL} documents processed.")
    print()

    # Perform Named Entity Recognition
    print("PERFORMING NAMED ENTITY RECOGNITION...")
    loading.display_loading_indicator("NER PROCESSING")
    entities_list = []
    total_documents = len(preprocessed_text)
    for i, text in enumerate(preprocessed_text):
        entities = ner.perform_ner(text.split())
        entities_list.append(entities)
        loading.display_progress_bar("NER PROCESSING", i+1, total_documents)

    print(f"NAMED ENTITY RECOGNITION COMPLETE. {Fore.RED}{total_documents}{Style.RESET_ALL} documents processed.")
    print()

    # Perform Keyword Extraction
    print("PERFORMING KEYWORD EXTRACTION...")
    loading.display_loading_indicator("KEYWORD EXTRACTION")
    top_keywords = keyword_extraction.extract_keywords(preprocessed_text, top_n=10)
    loading.display_progress_bar("KEYWORD EXTRACTION", 1, 1)  # Simulate progress bar for a single step
    print("KEYWORD EXTRACTION COMPLETE.")
    print()

    # Calculate Semantic Similarity
    print("CALCULATING SEMANTIC SIMILARITY...")
    loading.display_loading_indicator("SEMANTIC SIMILARITY")
    similarity_matrix = semantic_similarity.calculate_similarity(preprocessed_text)
    loading.display_progress_bar("SEMANTIC SIMILARITY", 1, 1)  # Simulate progress bar for a single step
    print("SEMANTIC SIMILARITY CALCULATION COMPLETE.")
    print()

    # Perform Text Summarization
    print("PERFORMING TEXT SUMMARIZATION...")
    loading.display_loading_indicator("TEXT SUMMARIZATION")
    summaries = []
    for i, text in enumerate(preprocessed_text):
        summary = text_summarization.summarize_text(text, num_sentences=3)
        summaries.append(summary)
        loading.display_progress_bar("TEXT SUMMARIZATION", i+1, total_documents)

    print(f"TEXT SUMMARIZATION COMPLETE. {Fore.RED}{total_documents}{Style.RESET_ALL} documents summarized.")
    print()

    # Perform IP Identification
    print("PERFORMING IP IDENTIFICATION...")
    loading.display_loading_indicator("IP IDENTIFICATION")
    ip_keywords = ["patent", "invention", "intellectual property", "trade secret"]
    potential_ip_documents = []
    for i, text in enumerate(preprocessed_text):
        if ip_identification.identify_potential_ip(text, ip_keywords):
            potential_ip_documents.append(i+1)
        loading.display_progress_bar("IP IDENTIFICATION", i+1, total_documents)

    print(f"IP IDENTIFICATION COMPLETE. {Fore.RED}{len(potential_ip_documents)}{Style.RESET_ALL} documents identified as potential IP.")
    print()

    # Perform Visualization
    print("GENERATING KEYWORD GRAPH...")
    loading.display_loading_indicator("KEYWORD GRAPH")
    visualization.create_keyword_graph(top_keywords)
    loading.display_progress_bar("KEYWORD GRAPH", 1, 1)  # Simulate progress bar for a single step
    print("KEYWORD GRAPH SAVED TO OUTPUTS/KEYWORD_GRAPH.PNG")
    print()

    # Export outputs to files
    print("EXPORTING OUTPUTS TO FILES...")
    loading.display_loading_indicator("EXPORTING")
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

    loading.display_progress_bar("EXPORTING", 1, 1)  # Simulate progress bar for a single step
    print(f"OUTPUT FILES SAVED TO THE OUTPUTS FOLDER.")
    print()
    print("IPMINER PROCESS COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    main()