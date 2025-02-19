"""
helper_functions.py
Author: Joseph Cho, ujcho@jacksongov.org
Date: 02/19/2025
Description:    Create dict functions for FAQ and Glossary sections
More Info:      FAQs and Glossary definitions are created by adding .txt files to the FAQ and GLOSSARY directories, respectively 
"""

from pathlib import Path

def faq_dict(faq_path):
    """Create dict for FAQs"""
    output_dict = {}
    
    for item in faq_path.iterdir():
        if item.is_file() and item.suffix == '.txt':
            parts = item.stem.split('_')
            if len(parts) == 1:
                q_num = parts[0][1:]
                if q_num not in output_dict:
                    output_dict[q_num] = {}
                output_dict[q_num]['question'] = item.read_text()
            elif len(parts) == 2 and parts[1] == 'answer':
                q_num = parts[0][1:]
                if q_num not in output_dict:
                    output_dict[q_num] = {}
                output_dict[q_num]['answer'] = item.read_text()

    return output_dict 

def glossary_dict(glossary_path):
    """Create dict for Glossary"""
    output_dict = {}

    for item in glossary_path.iterdir():
        if item.is_file() and item.suffix == '.txt':
            part
    return output_dict 