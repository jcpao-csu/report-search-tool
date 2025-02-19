import streamlit as st

# st.sidebar.markdown("Jackson County Prosecuting Attorney's Office")

pages = {
    "Police Report Search Tool": [
        st.Page("search_tool.py", title="Check Your Report Status Here")
    ],
    "Resources": [
        st.Page("more_info.py", title="For More Information"),
        st.Page("glossary.py", title="Glossary"),
        st.Page("jcpao_info.py", title="About the JCPAO")
    ],
}


st.sidebar.caption("Results based on system data as of 2025-01-28")
pg = st.navigation(pages)

pg.run()