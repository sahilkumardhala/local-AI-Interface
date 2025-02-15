import streamlit as st

# Define Light and Dark Themes
LIGHT_THEME = """
    <style>
        body, .stApp, .stfont, .stAlertContainer  {
            background-color: white !important;
            color: black !important;
        }
        .stMarkdown, .stTitle, .stTextInput, .stButton, .stRadio {
            color: black !important;
        }
    </style>
"""

DARK_THEME = """
    <style>
        body, .stApp, .stfont, .stAlertContainer  {
            background-color: #0e1117 !important;
            color: white !important;
        }
        .stMarkdown, .stTitle, .stTextInput, .stButton, .stRadio {
            color: white !important;
        }
    </style>
"""

# Function to Apply Theme
def apply_theme():
    """Applies the selected theme based on session state."""

    # Initialize theme state if not set
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True  # Default to Light Mode

    # Toggle Dark Mode and update session state
        st.session_state.dark_mode = st.toggle("🌙 Dark Mode", value=st.session_state.dark_mode)
        st.markdown(DARK_THEME, unsafe_allow_html=True)
        st.markdown("---")

    else:
        st.session_state.dark_mode = False

    # Toggle Light Mode and update session state
        st.session_state.dark_mode = st.toggle("☀️ light Mode", value=st.session_state.dark_mode)
        st.markdown(LIGHT_THEME, unsafe_allow_html=True)
        # st.session_state.dark_mode = st.session_state.clear()
        st.markdown("---")
