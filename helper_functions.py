"""
helper_functions.py
Author: Joseph Cho, ujcho@jacksongov.org
Date: 02/19/2025
Description:    Create dict functions for FAQ and Glossary sections
More Info:      FAQs and Glossary definitions are created by adding .txt files to the FAQ and GLOSSARY directories, respectively 
"""

from pathlib import Path

def faq_dict(path_str):
    """Create dict for FAQs"""
    output_dict = {}
    faq_path = Path(path_str)
    for item in list(faq_path.iterdir()):
        if item.is_file() and item.suffix == '.txt':
            file = item.stem
            if 'answer' not in file: # If .txt contains question
                q_num = int(file[1:2])
                if q_num not in output_dict:
                    output_dict[q_num] = {}
                output_dict[q_num]['question'] = item.read_text() # Add question to sub-dict
            elif 'answer' in file: # Else if .txt contains answer 
                q_num = int(file[1:2])
                if q_num not in output_dict:
                    output_dict[q_num] = {}
                output_dict[q_num]['answer'] = item.read_text() # Add answer to sub-dict

    return output_dict 

def glossary_dict(path_str):
    """Create dict for Glossary"""
    output_dict = {}
    glossary_path = Path(path_str)
    for item in list(glossary_path.iterdir()):
        if item.is_file() and item.suffix == '.txt':
            output_dict[item.stem] = item.read_text() # Add glossary definition to dict
            
    return output_dict 