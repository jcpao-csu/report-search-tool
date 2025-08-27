import streamlit as st
import pandas as pd
from db_connect import get_data

pages = {
    "Police Report Search Tool": [
        st.Page("search_tool.py", title="Check Your Report Status Here")
    ],
    "Resources": [
        st.Page("faq.py", title="Frequently Asked Questions"),
        st.Page("jcpao_info.py", title="About the JCPAO")
    ],
}

# Return latest date
df = get_data()

try: # Code that might raise an exception
    df['Date Received'] = pd.to_datetime(df['Date Received'], format='%Y-%m-%d', errors='coerce')
except KeyError: # Code that runs if that exception occurs
    latest_date = "..." # System error ... 
else: # Code that runs if no exception was raised
    latest_date = df['Date Received'].max()
    latest_date = latest_date.strftime('%A, %B %#d, %Y')
finally: # Code that runs no matter what (cleanup, logging, etc.)
    st.sidebar.caption(f"Results based on system data as of {latest_date}.")

pg = st.navigation(pages) # position="hidden", expanded=True

pg.run()