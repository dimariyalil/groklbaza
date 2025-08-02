import streamlit as st
import pandas as pd
import plotly.express as px
import anthropic
from datetime import datetime, date
from modules.reports import load_data, filter_data, export_csv, get_date_columns, display_report_stats

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
    st.header("Reports Dashboard")
    
    # Reports submenu using radio buttons
    report_type = st.radio(
        "Select Report Type:",
        ["CRM Reports", "P&L Reports", "Partners Reports", "Admin Reports"],
        horizontal=True
    )
    
    st.subheader(f"{report_type}")
    
    # File uploader for data analysis
    st.subheader("📁 Upload Data File")
    uploaded_file = st.file_uploader(
        "Choose a file", 
        type=['xlsx', 'csv'],
        help="Upload Excel or CSV files for analysis"
    )
    
    if uploaded_file is not None:
        # Test: Use modules.reports functions for data processing
        df = load_data(uploaded_file)
        
        if df is not None:
            st.success(f"✅ File uploaded successfully! Shape: {df.shape}")
            
            # Advanced filters section
            st.subheader("🔍 Data Filters")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Text search filter
                search_term = st.text_input(
                    "Search in Name/Country:", 
                    placeholder="Type to filter...",
                    help="Search in Name or Country columns"
                )
            
            with col2:
                # Date range filter
                date_columns = get_date_columns(df)
                date_column = None
                date_range = None
                
                if date_columns:
                    date_column = st.selectbox(
                        "Date Column for filtering:",
                        ["None"] + date_columns
                    )
                    
                    if date_column != "None":
                        # Get min/max dates from the column
                        try:
                            min_date = pd.to_datetime(df[date_column]).min().date()
                            max_date = pd.to_datetime(df[date_column]).max().date()
                            
                            date_range = st.date_input(
                                "Date Range:",
                                value=(min_date, max_date),
                                min_value=min_date,
                                max_value=max_date,
                                help="Select date range for filtering"
                            )
                            
                            if len(date_range) == 2:
                                date_range = (date_range[0], date_range[1])
                            else:
                                date_range = None
                                
                        except Exception as e:
                            st.warning(f"Could not parse dates in {date_column}")
                            date_column = None
                else:
                    st.info("No date columns detected in the data")
            
            # Apply filters using modules.reports function
            filtered_df = filter_data(
                df, 
                search_term=search_term if search_term else None,
                date_range=date_range,
                date_column=date_column if date_column != "None" else None
            )
            
            # Show filter results
            if search_term or (date_range and date_column != "None"):
                st.info(f"Showing {len(filtered_df)} of {len(df)} rows after filtering")
            
            # Export functionality
            if len(filtered_df) > 0:
                col1, col2 = st.columns([3, 1])
                
                with col2:
                    # Download button for filtered data
                    csv_data = export_csv(filtered_df, f"{report_type.lower().replace(' ', '_')}_data")
                    if csv_data:
                        st.download_button(
                            label="📥 Download CSV",
                            data=csv_data,
                            file_name=f"{report_type.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                            mime="text/csv",
                            help="Download filtered data as CSV file"
                        )
            
            # Display data table
            st.subheader("📊 Data Preview")
            st.dataframe(filtered_df, use_container_width=True)
            
            # Display statistics using modules.reports function
            if len(filtered_df) > 0:
                with st.expander("📈 Data Statistics", expanded=False):
                    display_report_stats(filtered_df)
    
    else:
        # Show instructions when no file uploaded
        st.info("👆 Upload an Excel (.xlsx) or CSV (.csv) file to start analyzing data")
        
        # Show sample data format
        with st.expander("📋 Expected Data Format", expanded=False):
            st.write("Your data should contain columns like:")
            sample_data = pd.DataFrame({
                'Name': ['User1', 'User2', 'User3'],
                'Country': ['USA', 'UK', 'Germany'],
                'Date': ['2025-01-01', '2025-01-02', '2025-01-03'],
                'Value': [100, 200, 300]
            })
            st.dataframe(sample_data)

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