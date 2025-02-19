import streamlit as st

st.title("Glossary")

st.subheader("Stages of a Case", divider=True)
st.write("For purposes of clarity, the Jackson County Prosecuting Attorney's Office breaks down the status of criminal cases into four broad categories:")

# Definition - Received
with st.expander("1 - Case Received"):
    st.write('''
        The submitting law enforcement agency, *finding probable cause*, has completed an investigation 
        or arrested the suspect(s) believed to have been responsible for the reported crime and has 
        formally submitted the case to the Office for review.
    ''')

# Definition - Filed
with st.expander("2 - Case Filed"):
    st.write('''
        The Prosecuting Attorney's Office, upon review of the evidence and facts of the case, files charges in 
        Court if it finds the suspect *guilty beyond a reasonable doubt*.
    ''')

# Definition - Not Filed
with st.expander("3 - Case Not Filed"):
    st.write('''
        Alternatively, if the Prosecuting Attorney's Office does not find the suspect guilty *beyond a reasonable doubt*
        following review of the evidence and facts of the case, it will decline to file charges in Court. Common reasons to 
        decline filing charges include:
        * Insufficient evidence to prove guilt *beyond a reasonable doubt*
        * Referred to Other Jurisdiction
        * Self-Defense
        * **Pending Further Investigation** (prosecutor returns case to the submitting agency to gather additional evidence prior to making a filing decision)
    ''')

# Definition - Disposed
with st.expander("4 - Case Disposed"):
    st.write('''
        The case is closed. Common disposition outcomes include: 
        * Guilty plea
        * (Non-)Guilty verdict from trial
        * Defendant entered diversion program
        * **Nolle prosequi** (prosecutor dismisses criminal charges)
    ''')

