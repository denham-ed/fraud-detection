import streamlit as st
from app_pages.multipage import MultiPage


from app_pages.page_factors_of_fraud import page_factors_of_fraud_body
from app_pages.page_summary import page_summary_body

app = MultiPage(app_name="Auckland Capital Bank's Frauditor")
app.add_page("Project Overview",page_summary_body)
app.add_page("Factors of Fraud Study", page_factors_of_fraud_body)

app.run()