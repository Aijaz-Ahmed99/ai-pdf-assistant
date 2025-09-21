import streamlit as st

# only show logout if logged in
if st.session_state.get("authenticated", False):
    if st.button("🚪 Logout"):
        # Clear session state values
        st.session_state["authenticated"] = False
        st.session_state.pop("token", None)   # remove token if present
        st.success("You have been logged out!")
