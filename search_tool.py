import streamlit as st
import pandas as pd


st.title("Enter your Police Report Number")

df = pd.read_csv("test.csv", encoding='utf-8')

report_number = st.text_input(label="Enter your Police Report Number", label_visibility="hidden")

if st.button("Search", icon=":material/search:"):
    if len(report_number) >= 5: 
        result = df[df['Police Report Number'].str.contains(report_number, case=False, na=False)]
        if not result.empty:
            total_cases = len(result)
            counter = 0

            st.write(f"We found {total_cases} case(s) associated with Police Report *#{report_number}*:")
            
            for i, row in result.iterrows():
                counter += 1
                
                if row['Case Status'].upper()=='RECEIVED':
                    st.write(f"Case ({counter}/{total_cases}) was :red[**RECEIVED**] on {row['Date Received']} and submitted by the {row['Submitting Agency']}.\nThis case is likely under review and pending criminal charges.")
                elif row['Case Status'].upper()=='FILED':
                    url = f"https://www.courts.mo.gov/cnet/cases/newHeader.do?inputVO.caseNumber={row['Court Number']}&inputVO.courtId=CT16&inputVO.isTicket=false"
                    st.write(f"Case ({counter}/{total_cases}) was :red[**FILED**] by our Office on {row['Date Filed']} and was submitted by the {row['Submitting Agency']} for review on {row['Date Received']}.\nYou can find more information regarding this case on Case.net: [Court Number {row['Court Number']}]({url}).")
                elif row['Case Status'].upper()=='NOT FILED':
                    st.write(f"The Jackson County Prosecuting Attorney's Office :red[**DECLINED TO FILE CHARGES**] on Case ({counter}/{total_cases}) on {row['Date Not Filed']} due to the following reason(s): {row['Reason Not Filed']}.\nThis case was submitted by the {row['Submitting Agency']} for review on {row['Date Received']}.")
                elif row['Case Status'].upper()=='DISPOSED':
                    url = f"https://www.courts.mo.gov/cnet/cases/newHeader.do?inputVO.caseNumber={row['Court Number']}&inputVO.courtId=CT16&inputVO.isTicket=false"
                    st.write(f"Case ({counter}/{total_cases}) was :red[**DISPOSED**] on {row['Date Disposed']} with the following outcome(s): {row['Disposed Outcome']}.\nThis case was submitted by the {row['Submitting Agency']} for review on {row['Date Received']}.\nYou can find more information regarding this case on Case.net: [Court Number {row['Court Number']}]({url}).")
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

