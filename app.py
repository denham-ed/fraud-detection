import streamlit as st
from app_pages.multipage import MultiPage


from app_pages.page_factors_of_fraud import page_factors_of_fraud_body

app = MultiPage(app_name="Auckland Capital Bank's Frauditor")
app.add_page("Factors of Fraud TBC", page_factors_of_fraud_body)

app.run()