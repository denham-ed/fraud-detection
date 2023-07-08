import streamlit as st
from app_pages.multipage import MultiPage



app = MultiPage(app_name="Auckland Capital Bank's Frauditor")


app.run()