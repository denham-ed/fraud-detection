import streamlit as st
from src.data_management import load_transaction_data


def page_factors_of_fraud_body():
    st.header("Factors of Fraud")

    df = load_transaction_data()

    st.info(
        "The senior management team at Auckland Capital Bank (ACB) "
        "want to better undeststand the patterns from their transaction data "
        "in order to identify the most relevant variables correlated "
        "to a churned customer."
    )

    if st.checkbox("Inspect Transaction Data"):
        st.write(
            f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns.\n\n"
            f"The first 10, used to give an indication of the format of the data, are below.")

        st.write(df.head(10))

    st.divider()

    st.subheader("Correlation Study")


    st.subheader("Conclusions")

    st.success(
        "1. Transactions occuring more than 60.27km from home are more likely "
        "to be fraudulent than transactions closer to home. (Hypothesis 1)\n"
        "   * Rather than a linear relationship, there appears to be a 'tipping "
        "point' at which point the transaction is more likely to be fraudulent.\n\n"
        "2. Transactions that occur online are more likely to be fraudulent than "
        "transactions made offline. (Hypothesis 2)\n\n"
        "Also and significantly:\n"
        "* Transactions that are more than 4.08x the median purchase price are "
        "more likely to be fraudulent than smaller transactions.\n"
        "  * Rather than a linear relationship, there appears to be a 'tipping "
        "point' at which point the transaction is more likely to be fraudulent."
    )


    st.divider()

    st.caption(
        "NOTE: The scenario presented is fictional and was undertaken for the developer's "
        "Data Analytics milestone project as part of Code Institute's Diploma in Full Stack Software "
        "Development."
    )
    

    