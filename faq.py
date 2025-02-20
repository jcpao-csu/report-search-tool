import streamlit as st
from pathlib import Path

from helper_functions import faq_dict, glossary_dict

# Import content 
faqs = faq_dict('FAQ')
faqs_keys = (list(faqs.keys())).sort()
sorted_faqs = {q_num: faqs[q_num] for q_num in faqs_keys}

glossary_terms = glossary_dict('GLOSSARY')
glossary_keys = (list(glossary_terms.keys())).sort()
sorted_glossary = {term: glossary_terms[term] for term in glossary_keys}

st.title("Frequently Asked Questions")

for n, sub_dict in sorted_faqs.items(): # For question number, sub_dict in FAQ directory 
    # for q, a in sub_dict.items(): # For question, answer in sub_dict 
    with st.expander(sub_dict['question']):
        st.divider()
        st.write(sub_dict['answer'])

st.subheader("Glossary - Stages of a Case", divider=True)
st.write("For purposes of clarity, the Jackson County Prosecuting Attorney's Office breaks down the status of criminal cases into four broad categories:")

for term, definition in sorted_glossary.items(): # For term, definition in GLOSSARY directory 
    term_bold = f"**{term}**"
    with st.expander(term_bold):
        st.divider()
        st.write(definition)

