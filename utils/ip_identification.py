# utils/ip_identification.py

import re

def identify_potential_ip(text, keywords):
    # Convert the text and keywords to lowercase
    text = text.lower()
    keywords = [keyword.lower() for keyword in keywords]
    
    # Check if any keyword is present in the text
    for keyword in keywords:
        if keyword in text:
            return True
    
    return False