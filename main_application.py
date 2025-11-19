"""
Main Streamlit application for LuminAAC frontend
"""

import streamlit as st
from user_interface.aac_interface import AACUserInterface
from caretaker_interface.dashboard import CaretakerDashboard

def main():
    """Run the appropriate interface based on user type"""
    
    st.sidebar.title("🎵 LuminAAC Portal")
    st.sidebar.markdown("---")
    
    user_type = st.sidebar.selectbox(
        "Select Interface", 
        ["AAC User", "Caretaker"],
        help="Choose the interface that matches your role"
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("""
    **About LuminAAC:**
    Advanced AAC system with AI-powered communication and therapeutic support.
    """)
    
    if user_type == "AAC User":
        user_interface = AACUserInterface()
        user_interface.setup_user_interface()
    else:
        caretaker_dashboard = CaretakerDashboard()
        caretaker_dashboard.setup_caretaker_interface()

if __name__ == "__main__":
    main()