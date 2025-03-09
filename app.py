import streamlit as st


with st.form("my_form"):
   st.header("TERMINATOR")
   st.text_input("NAME")
   purpose = st.selectbox('PURPOSE', ['Home','Society','Warehouse','Retail Store'])
   st.text_input("EMAIL ID")
   st.form_submit_button('Interested')

