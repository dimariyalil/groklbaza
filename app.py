import streamlit as st
import pandas as pd
import plotly.express as px
import anthropic
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="lbazaGr AI Dashboard",
    page_icon="🚀",
    layout="wide"
)

# Main title
st.title('lbazaGr AI Dashboard')

# Sidebar with collapsible menu
st.sidebar.title("Navigation")

# Main menu sections with expanders for submenus
selected_section = None
selected_subsection = None

# Home (no submenu)
if st.sidebar.button("🏠 Home"):
    selected_section = "Home"

# Reports with submenu
with st.sidebar.expander("📊 Reports"):
    if st.button("CRM Reports"):
        selected_section = "Reports"
        selected_subsection = "CRM Reports"
    if st.button("P&L Reports"):
        selected_section = "Reports"
        selected_subsection = "P&L Reports"
    if st.button("Partners Reports"):
        selected_section = "Reports"
        selected_subsection = "Partners Reports"
    if st.button("Admin Reports"):
        selected_section = "Reports"
        selected_subsection = "Admin Reports"

# AI Analysis with submenu
with st.sidebar.expander("🤖 AI Analysis"):
    if st.button("AI Chat"):
        selected_section = "AI Analysis"
        selected_subsection = "AI Chat"
    if st.button("Agents Overview"):
        selected_section = "AI Analysis"
        selected_subsection = "Agents Overview"
    if st.button("Insights & Recommendations"):
        selected_section = "AI Analysis"
        selected_subsection = "Insights & Recommendations"

# HR with submenu
with st.sidebar.expander("👥 HR"):
    if st.button("Employee Database"):
        selected_section = "HR"
        selected_subsection = "Employee Database"
    if st.button("KPI Tracking"):
        selected_section = "HR"
        selected_subsection = "KPI Tracking"
    if st.button("Recruiting"):
        selected_section = "HR"
        selected_subsection = "Recruiting"
    if st.button("Org Structure"):
        selected_section = "HR"
        selected_subsection = "Org Structure"

# ML Analytics with submenu
with st.sidebar.expander("🧠 ML Analytics"):
    if st.button("AutoML Models"):
        selected_section = "ML Analytics"
        selected_subsection = "AutoML Models"
    if st.button("Predictive Forecasts"):
        selected_section = "ML Analytics"
        selected_subsection = "Predictive Forecasts"
    if st.button("Anomaly Detection"):
        selected_section = "ML Analytics"
        selected_subsection = "Anomaly Detection"
    if st.button("Data Visualization"):
        selected_section = "ML Analytics"
        selected_subsection = "Data Visualization"

# Archives with submenu
with st.sidebar.expander("📂 Archives"):
    if st.button("Data History"):
        selected_section = "Archives"
        selected_subsection = "Data History"
    if st.button("Search & Compare"):
        selected_section = "Archives"
        selected_subsection = "Search & Compare"
    if st.button("Export"):
        selected_section = "Archives"
        selected_subsection = "Export"

# Settings with submenu
with st.sidebar.expander("⚙️ Settings"):
    if st.button("User Preferences"):
        selected_section = "Settings"
        selected_subsection = "User Preferences"
    if st.button("API Keys"):
        selected_section = "Settings"
        selected_subsection = "API Keys"
    if st.button("Backup & Restore"):
        selected_section = "Settings"
        selected_subsection = "Backup & Restore"

# Default to Home if nothing selected
if selected_section is None:
    selected_section = "Home"

# Main content based on selection
if selected_section == "Home":
    st.header("Welcome to lbazaGr AI Dashboard!")
    st.write("""
    Comprehensive AI-powered platform for business management and analytics.
    
    This platform combines:
    - 📊 Interactive dashboards and reports
    - 🤖 AI agents for intelligent analysis
    - 👥 HR management and insights
    - 🧠 Machine Learning capabilities
    """)
    
    # KPI Cards as requested
    st.subheader("Key Performance Indicators")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Revenue", "$1,000", "5.2%")
    with col2:
        st.metric("Churn Rate", "15%", "-2.1%")
    with col3:
        st.metric("Traffic", "5,000", "12.3%")
    
    # Simple line chart with fake data
    st.subheader("Revenue Trend")
    try:
        # Test: Create simple DataFrame and display chart
        chart_data = pd.DataFrame({
            'Date': ['2025-01', '2025-02', '2025-03', '2025-04', '2025-05'],
            'Value': [100, 200, 150, 300, 250]
        })
        
        fig = px.line(chart_data, x='Date', y='Value', 
                     title="Monthly Revenue Trend",
                     markers=True)
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Error creating chart: {e}")

elif selected_section == "Reports":
    if selected_subsection:
        st.header(f"{selected_subsection}")
        st.info(f"{selected_subsection} functionality coming soon...")
    else:
        st.header("Reports Dashboard")
        
        # File uploader for data analysis
        st.subheader("Upload Data File")
        uploaded_file = st.file_uploader(
            "Choose a file", 
            type=['xlsx', 'csv'],
            help="Upload Excel or CSV files for analysis"
        )
        
        if uploaded_file is not None:
            try:
                # Test: Handle file upload and display data
                if uploaded_file.name.endswith('.xlsx'):
                    df = pd.read_excel(uploaded_file)
                else:
                    df = pd.read_csv(uploaded_file)
                
                st.success(f"File uploaded successfully! Shape: {df.shape}")
                
                # Basic filters
                st.subheader("Data Filters")
                search_term = st.text_input("Search in data:", placeholder="Type to filter...")
                
                # Apply search filter if provided
                if search_term:
                    # Simple string search across all columns
                    mask = df.astype(str).apply(lambda x: x.str.contains(search_term, case=False, na=False)).any(axis=1)
                    filtered_df = df[mask]
                    st.info(f"Showing {len(filtered_df)} of {len(df)} rows matching '{search_term}'")
                else:
                    filtered_df = df
                
                # Display data table
                st.subheader("Data Preview")
                st.dataframe(filtered_df, use_container_width=True)
                
                # Basic statistics
                if len(filtered_df) > 0:
                    st.subheader("Basic Statistics")
                    st.write(filtered_df.describe())
                    
            except Exception as e:
                st.error(f"Error processing file: {e}")
                st.info("Please ensure the file is a valid Excel (.xlsx) or CSV (.csv) file")

elif selected_section == "AI Analysis":
    if selected_subsection:
        st.header(f"{selected_subsection}")
        st.info(f"{selected_subsection} functionality coming soon...")
    else:
        st.header("AI Analysis")
        st.info("Select a specific AI analysis tool from the sidebar")

elif selected_section == "HR":
    if selected_subsection:
        st.header(f"{selected_subsection}")
        st.info(f"{selected_subsection} functionality coming soon...")
    else:
        st.header("HR Management")
        st.info("Select a specific HR tool from the sidebar")

elif selected_section == "ML Analytics":
    if selected_subsection:
        st.header(f"{selected_subsection}")
        st.info(f"{selected_subsection} functionality coming soon...")
    else:
        st.header("Machine Learning Analytics")
        st.info("Select a specific ML tool from the sidebar")

elif selected_section == "Archives":
    if selected_subsection:
        st.header(f"{selected_subsection}")
        st.info(f"{selected_subsection} functionality coming soon...")
    else:
        st.header("Archives")
        st.info("Select a specific archive tool from the sidebar")

elif selected_section == "Settings":
    if selected_subsection:
        st.header(f"{selected_subsection}")
        st.info(f"{selected_subsection} functionality coming soon...")
    else:
        st.header("Settings")
        st.info("Select a specific setting from the sidebar")

# Test: Run and check menu expands, file upload works, charts display
# Test: Navigate through different sections and verify functionality