# utils/text_summarization.py

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text, num_sentences=3):
    # Create a plaintext parser
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    
    # Create an LSA summarizer
    summarizer = LsaSummarizer()
    
    # Summarize the text
    summary = summarizer(parser.document, num_sentences)
    
    # Convert the summary to plain text
    summary_text = " ".join([str(sentence) for sentence in summary])
    
    return summary_text