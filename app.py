import streamlit as st
from src.ui.custom_styles import load_custom_css
from src.ui.page_components import (
    initialize_session_state,
    render_sidebar,
    render_landing_page,
    render_journey_page,
    render_details_page,
    render_transition_page,
    render_chat_analysis_page,
)

st.set_page_config(
    page_title="Vedic Gita Root Cause Analyzer",
    page_icon="📿",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_custom_css()
initialize_session_state()
render_sidebar()

st.markdown("<div style='max-width: 1200px; margin: auto;'>", unsafe_allow_html=True)
if st.session_state.page == "landing":
    render_landing_page()
elif st.session_state.page == "journey":
    render_journey_page()
elif st.session_state.page == "details":
    render_details_page()
elif st.session_state.page == "transition":
    render_transition_page()
elif st.session_state.page == "chat_analysis":
    render_chat_analysis_page()
else:
    st.error("Unknown page state. Please refresh the app.")
st.markdown("</div>", unsafe_allow_html=True)
