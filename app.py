
import streamlit as st

# Function to reset session state
def reset_form():
    for key in ["name", "email", "purpose"]:
        del st.session_state[key]  # Clears session state
    st.rerun()  # Force rerun to clear the form

# Initialize session state variables only if they don't exist
if "name" not in st.session_state:
    st.session_state.name = ""
if "email" not in st.session_state:
    st.session_state.email = ""
if "purpose" not in st.session_state:
    st.session_state.purpose = "Home"  # Default selection

st.header("TERMINATOR")

# Create form
with st.form("my_form"):
    name = st.text_input("NAME", value=st.session_state.name, key="name")
    purpose = st.selectbox("PURPOSE", ['Home', 'Society', 'Warehouse', 'Retail Store'], index=['Home', 'Society', 'Warehouse', 'Retail Store'].index(st.session_state.purpose), key="purpose")
    email = st.text_input("EMAIL ID", value=st.session_state.email, key="email")
    
    submitted = st.form_submit_button("Interested")

    if submitted:
        st.success("Thank you for your interest! 🎉")

        # Clear the session state and rerun the app
        reset_form()
