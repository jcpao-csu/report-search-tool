"""
db_connect.py
Author: Joseph Cho, ujcho@jacksongov.org
Date: 07/16/2025
Description:    Migrate data source to NeonDB for enhanced data security
"""

import psycopg2
from psycopg2 import pool, sql, OperationalError
from psycopg2.extras import RealDictCursor
import pandas as pd
from datetime import datetime
import streamlit as st

# --- Initialize database connection pool --- 

# Define get_database_session() 
@st.cache_resource
def get_database_session(database_url):
    try: 
        # Create a database session object that points to the URL.
        return pool.SimpleConnectionPool(1, 10, database_url) # Initialize connection pool
    except OperationalError as e:
        st.error("Network is blocking connection to the database server. Please try again on a different network/internet connection. If you continue to experience problems, please reach out to Joseph Cho at ujcho@jacksongov.org.")
        return None

# Establish NEON database connection (via psycopg2)
database_url = st.secrets["neonDB"]["database_url"]

try:
    db_connection = get_database_session(database_url)
except Exception as e:
    print(f"{e}")
    st.stop()

# --- Define get_data() function --- 
@st.cache_data
def get_data(_connection_pool=db_connection):
    """Return pandas DataFrame of employee_info_view table"""

    conn = _connection_pool.getconn()
    try:
        # Open cursor to perform database operations
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            try:
                query = sql.SQL("SELECT * FROM police_reports;") # ; not required for psycopg
                cur.execute(query)
                results = cur.fetchall()
                df = pd.DataFrame(results)

                if df.empty:
                    return pd.DataFrame()
                else:
                    return df
                
            except psycopg2.Error as e:
                st.error(f"Problem with loading data: {e}")
                return pd.DataFrame()

    finally:
        _connection_pool.putconn(conn) # Return conn to pool
