import streamlit as st


def page_summary_body():

    st.header("Project Overview")

    st.info(
        f"Scams and fraudulent activity are a growing problem in New Zealand, "
        f"costing the economy up to $9.8b/yr, says Serious Fraud Office. "
        f"Auckland Capital Bank (ACB) wants to identify markers for fraud, minimize "
        f"financial loss, safeguard customers, and provide optimal fraud prevention advice."
    )
    
    st.write(
        f"* For more information about this project please visit the "
        f"[Project README file](https://github.com/denham-ed/fraud-detection) in the project's GitHub repo.")

    st.success(
        "The project has 2 business requirements:\n"
        "1. ACB would like to understand the patterns in the transaction data "
        "to better understand the most relevant variables correlated to a fraudulent transaction.\n"
        "2. ACB would like to be able to 'flag' potentially fraudulent transactions "
        "at Point of Sale for further investigation."
    )

    st.divider()

    st.caption(
        "NOTE: The scenario presented is fictional and was undertaken for the developer's "
        "Data Analytics milestone project as part of Code Institute's Diploma in Full Stack Software "
        "Development."
    )
    