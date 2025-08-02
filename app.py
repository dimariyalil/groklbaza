import streamlit as st
import pandas as pd
import plotly.express as px
import anthropic

# Page configuration
st.set_page_config(
    page_title="LilBet AI Dashboard",
    page_icon="🎲",
    layout="wide"
)

# Main title
st.title('LilBet AI Dashboard')

# Sidebar menu
st.sidebar.title("Navigation")
menu_option = st.sidebar.selectbox(
    "Choose section:",
    ["Home", "Reports", "AI Analysis", "HR", "ML", "Archives", "Settings"]
)

# Main content based on menu selection
if menu_option == "Home":
    st.header("Welcome to LilBet AI Dashboard!")
    st.write("""
    Welcome to your comprehensive AI-powered dashboard for iGaming business analytics.
    
    This platform combines:
    - 📊 Interactive dashboards and reports
    - 🤖 AI agents for intelligent analysis
    - 👥 HR management and insights
    - 🧠 Machine Learning capabilities
    
    Use the sidebar to navigate through different sections.
    """)
    
    # Quick stats placeholder
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Users", "1,234", "12%")
    with col2:
        st.metric("Revenue", "$45,678", "8%")
    with col3:
        st.metric("Active Games", "89", "3%")
    with col4:
        st.metric("AI Insights", "23", "15%")

elif menu_option == "Reports":
    st.header("Reports")
    st.info("Reports section coming soon...")

elif menu_option == "AI Analysis":
    st.header("AI Analysis")
    st.info("AI Analysis section coming soon...")

elif menu_option == "HR":
    st.header("HR Management")
    st.info("HR section coming soon...")

elif menu_option == "ML":
    st.header("Machine Learning")
    st.info("ML section coming soon...")

elif menu_option == "Archives":
    st.header("Archives")
    st.info("Archives section coming soon...")

elif menu_option == "Settings":
    st.header("Settings")
    st.info("Settings section coming soon...")