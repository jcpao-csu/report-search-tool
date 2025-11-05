import streamlit as st
import pandas as pd

from db_connect import get_data

st.title("Enter your Police Report Number")

df = get_data()
df = df.drop("id", axis=1)

report_number = st.text_input(label="Enter your Police Report Number", label_visibility="hidden")

if st.button("Search", icon=":material/search:"):
    if len(report_number) >= 5: 
        # result = df[df['Police Report Number'].str.contains(report_number, case=False, na=False)]
        result = df[df['Police Report Number'].fillna('').str.lower() == report_number.lower()] # Exact string matches, instead of all partial matches; many NA (missing) report_nums in table
        if not result.empty:
            total_cases = len(result)
            counter = 0

            st.write(f"We found {total_cases} case(s) associated with Police Report *#{report_number}*:")
            
            for i, row in result.iterrows():
                counter += 1
                
                if row['Case Status'].upper()=='RECEIVED':
                    st.markdown(f"Case ({counter}/{total_cases}) was :blue[**RECEIVED**] on :yellow-background[***{row['Date Received'] or 'Date Unknown'}***] and submitted by the {row['Submitting Agency']}.\nThis case is likely under review and pending criminal charges.")
                elif row['Case Status'].upper()=='FILED':
                    url = f"https://www.courts.mo.gov/cnet/cases/newHeader.do?inputVO.caseNumber={row['Court Number']}&inputVO.courtId=CT16&inputVO.isTicket=false"
                    st.markdown(f"Case ({counter}/{total_cases}) was :blue[**FILED**] by our Office on :yellow-background[***{row['Date Filed'] or 'Date Unknown'}***] and was submitted by the {row['Submitting Agency']} for review on {row['Date Received'] or 'Date Unknown'}.\nYou can find more information regarding this case on Case.net: [Court Number {row['Court Number']}]({url}).")
                elif row['Case Status'].upper()=='NOT FILED':
                    st.markdown(f"The Jackson County Prosecuting Attorney's Office :blue[**DECLINED TO FILE CHARGES**] on Case ({counter}/{total_cases}) on :yellow-background[***{row['Date Not Filed'] or 'Date Unknown'}***] due to the following reason(s): {row['Reason Not Filed']}.\nThis case was submitted by the {row['Submitting Agency']} for review on {row['Date Received'] or 'Date Unknown'}.")
                elif row['Case Status'].upper()=='DISPOSED':
                    url = f"https://www.courts.mo.gov/cnet/cases/newHeader.do?inputVO.caseNumber={row['Court Number']}&inputVO.courtId=CT16&inputVO.isTicket=false"
                    st.markdown(f"Case ({counter}/{total_cases}) was :blue[**DISPOSED**] on :yellow-background[***{row['Date Disposed'] or 'Date Unknown'}***] with the following outcome(s): {row['Disposed Outcome']}.\nThis case was submitted by the {row['Submitting Agency']} for review on {row['Date Received'] or 'Date Unknown'}.\nYou can find more information regarding this case on Case.net: [Court Number {row['Court Number']}]({url}).")
            cleaned = result.dropna(axis=1, how='all')
            st.dataframe(cleaned, hide_index=True)
        else:
            st.write('''
                We could not match your Police Report Number to those of any cases submitted to our Office. 
                This means the reported incident is still under investigation and has yet to be submitted 
                to our Office, or the incident has been submitted to another jurisdiction (e.g., municipal, juvenile, or federal court).
            ''')
    else:
        st.write("*Your report number must be at least five characters long.*")

st.write("If your case was filed by our Office, you can find the latest information regarding the case on CaseNet [here](https://www.courts.mo.gov/cnet/caseNoSearch.do).")

