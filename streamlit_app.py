import streamlit as st

pages = {
    "Police Report Search Tool": [
        st.Page("search_tool.py", title="Check Your Report Status Here")
    ],
    "Resources": [
        st.Page("faq.py", title="Frequently Asked Questions"),
        st.Page("jcpao_info.py", title="About the JCPAO")
    ],
}


st.sidebar.caption("Results based on system data as of August 13, 2025.")
pg = st.navigation(pages) # position="hidden", expanded=True

pg.run()