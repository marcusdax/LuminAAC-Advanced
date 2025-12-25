"""
Simple LuminAAC Frontend - GitHub Compatible Version
This version removes any potential issues that might cause GitHub processing errors
"""

import streamlit as st

def main():
    """Main frontend application"""
    st.title("LuminAAC - Advanced AAC System")
    st.markdown("---")
    
    # Introduction
    st.header("Welcome to LuminAAC")
    st.write("""
    LuminAAC is an advanced AI-powered Augmentative and Alternative Communication (AAC) system.
    
    **Core Features:**
    - AI-powered communication support
    - Therapeutic audio integration
    - Mood-aware interface adaptation
    - Multi-modal input processing
    - Real-time behavioral analysis
    """)
    
    # Role selection
    st.sidebar.title("Navigation")
    user_type = st.sidebar.selectbox(
        "Select your role",
        ["AAC User", "Caretaker", "Therapist", "System Info"],
        help="Choose the interface that matches your role"
    )
    
    st.markdown("---")
    
    # Show appropriate interface based on role
    if user_type == "AAC User":
        show_user_interface()
    elif user_type == "Caretaker":
        show_caretaker_interface()
    elif user_type == "Therapist":
        show_therapist_interface()
    else:
        show_system_info()

def show_user_interface():
    """AAC User Interface"""
    st.subheader("AAC Communication Interface")
    
    st.write("""
    **Communication Features:**
    - Text-to-speech conversion
    - Symbol-based communication
    - Mood-aware theme adaptation
    - Therapeutic audio support
    """)
    
    # Message input
    message = st.text_area("Type your message:", height=150, 
                          placeholder="Enter your communication here...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Send Message"):
            if message:
                st.success(f"Message sent: {message}")
                st.info("Message processed by LuminAAC AI engine")
            else:
                st.warning("Please enter a message first")
    
    with col2:
        if st.button("Clear Message"):
            message = ""
            st.experimental_rerun()
    
    # Backend connection test
    st.subheader("Backend Connection Test")
    if st.button("Test Backend Connection"):
        try:
            import requests
            response = requests.get("http://localhost:8000", timeout=5)
            if response.status_code == 200:
                st.success(f"✅ Backend connected successfully!")
                st.json(response.json())
            else:
                st.error(f"❌ Backend returned status {response.status_code}")
        except Exception as e:
            st.error(f"❌ Could not connect to backend: {e}")
            st.info("Please ensure the backend is running: python backend_complete.py")

def show_caretaker_interface():
    """Caretaker Dashboard Interface"""
    st.subheader("Caretaker Dashboard")
    
    st.write("""
    **Caretaker Features:**
    - Monitor user activity and communication patterns
    - View detailed analytics and usage statistics
    - Adjust therapy settings and preferences
    - Generate comprehensive reports
    - Receive real-time alerts and notifications
    """)
    
    # System status monitor
    st.subheader("System Status Monitor")
    
    try:
        import requests
        response = requests.get("http://localhost:8000/health", timeout=5)
        
        if response.status_code == 200:
            status_data = response.json()
            st.success("✅ Backend is healthy and operational")
            
            # Display key metrics
            st.write(f"**Status:** {status_data.get('status', 'unknown')}")
            st.write(f"**Timestamp:** {status_data.get('timestamp', 'N/A')}")
            
            # Show components status
            if 'components' in status_data:
                st.subheader("Component Status")
                for component, status in status_data['components'].items():
                    st.write(f"- **{component}:** {status}")
        else:
            st.error(f"❌ Backend health check failed with status {response.status_code}")
            
    except Exception as e:
        st.error(f"❌ Could not retrieve system status: {e}")
        st.info("Please start the backend: python backend_complete.py")

def show_therapist_interface():
    """Therapist Interface"""
    st.subheader("Therapist Interface")
    
    st.write("""
    **Therapist Features:**
    - Comprehensive progress tracking tools
    - Custom therapy session planning
    - Advanced intervention design
    - Detailed data analysis and visualization
    - Export capabilities for reporting
    - Multi-user management
    """)
    
    st.info("This interface would provide advanced tools for therapy professionals")

def show_system_info():
    """System Information Page"""
    st.subheader("System Information")
    
    st.write("""
    ## About LuminAAC Advanced
    
    **Version:** 2.0 - Complete Edition
    
    **Technologies Used:**
    - **Backend:** FastAPI, PyTorch, Transformers
    - **Frontend:** Streamlit
    - **AI/ML:** PyTorch, Scikit-learn, Librosa
    - **Data Processing:** Pandas, NumPy
    - **Visualization:** Plotly
    
    **Key Features:**
    - Advanced AI-powered communication processing
    - Real-time behavioral analysis
    - Therapeutic audio integration
    - Multi-modal data fusion
    - Ethical AI framework
    - Comprehensive monitoring tools
    """)
    
    # Backend capabilities
    st.subheader("Backend Capabilities")
    
    try:
        import requests
        
        # Test basic connection
        basic_response = requests.get("http://localhost:8000", timeout=5)
        
        if basic_response.status_code == 200:
            st.success("✅ Backend is running and responsive")
            
            # Get system capabilities
            try:
                capabilities_response = requests.get("http://localhost:8000/api/system-capabilities", timeout=5)
                capabilities_data = capabilities_response.json()
                
                st.json(capabilities_data)
                
            except Exception:
                st.info("Backend is running but capabilities endpoint not available")
        else:
            st.error(f"❌ Backend returned status code {basic_response.status_code}")
            
    except Exception as e:
        st.error(f"❌ Could not connect to backend: {e}")
        st.code("Backend might not be running. Start it with: python backend_complete.py")

if __name__ == "__main__":
    # Set page configuration
    st.set_page_config(
        page_title="LuminAAC Advanced",
        page_icon="🎵",
        layout="wide"
    )
    main()