import streamlit as st


def page_project_hypothesis_body():

    st.header("Project Hypotheses")

    st.info(
        f"The Senior Management team of ACB have put forward two hypotheses for testing during this study: \n\n"
        f"1. The further away from home that a transaction occurs, the more likely it is to be fraudulent.\n"

        f"* A customer survey showed our customers appreciate fibre Optic. "
        f"* Online transactions are more likely to be fraudulent than in-person transactions. "
    )

    st.write(
        "Validating these hypotheses will allow ACB to better protect themselves and their customers from "
        "loss due to fraudulent activity by detecting possible fraud at point in their transaction data."
        )
    
    st.divider()

    st.caption(
        "NOTE: The scenario presented is fictional and was undertaken for the developer's "
        "Data Analytics milestone project as part of Code Institute's Diploma in Full Stack Software "
        "Development."
    )




