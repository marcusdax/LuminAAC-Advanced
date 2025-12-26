"""
AAC Interface - Redirect to the main frontend
This file is kept for compatibility with existing deployments
"""

import streamlit as st
import subprocess
import sys
import os

def main():
    """Redirect to the main frontend or provide compatibility interface"""
    
    st.title("LuminAAC - AAC Interface")
    st.markdown("---")
    
    st.header("Welcome to LuminAAC")
    st.write("""
    This interface provides access to the LuminAAC Advanced AAC System.
    
    **Note:** This is a compatibility interface. For the full experience, please use:
    - `simple_frontend_fixed.py` (recommended)
    - `frontend_simple.py` (alternative)
    """)
    
    # Option to launch the main frontend
    if st.button("Launch Full Frontend"):
        try:
            # Try to launch the main frontend
            result = subprocess.run([
                sys.executable, 
                os.path.join(os.path.dirname(__file__), "simple_frontend_fixed.py")
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                st.success("Full frontend launched successfully!")
                st.info("Please check your browser for the new interface")
            else:
                st.error(f"Failed to launch frontend: {result.stderr}")
                
        except Exception as e:
            st.error(f"Error launching frontend: {e}")
    
    # Basic AAC functionality
    st.markdown("---")
    st.subheader("Basic Communication")
    
    message = st.text_input("Enter your message:")
    
    if st.button("Send Message"):
        if message:
            st.success(f"Message: {message}")
            st.info("This would be processed by the LuminAAC backend")
        else:
            st.warning("Please enter a message first")
    
    # Backend connection test
    if st.button("Test Backend Connection"):
        try:
            import requests
            response = requests.get("http://localhost:8000", timeout=5)
            if response.status_code == 200:
                st.success("✅ Backend is connected and working!")
                st.json(response.json())
            else:
                st.error(f"❌ Backend returned status {response.status_code}")
        except Exception as e:
            st.error(f"❌ Could not connect to backend: {e}")
            st.info("Please start the backend: python backend_complete.py")

if __name__ == "__main__":
    main()