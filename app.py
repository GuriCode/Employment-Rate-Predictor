import streamlit as st
from Predict_page import show_predict_page
from employee_page import show_employment_page



page = st.sidebar.selectbox("Explore Or Predict", ("Predict Graduation Rate", "Predict Employment Rate"))

if page == "Predict Graduation Rate":
    show_predict_page()
elif page=="Predict Employment Rate"  :
    show_employment_page()  
