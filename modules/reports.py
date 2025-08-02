"""
Reports module for lbazaGr Dashboard
Handles data loading, filtering, and export functionality
"""

import pandas as pd
import streamlit as st
from datetime import datetime, date
from io import StringIO


def load_data(uploaded_file):
    """
    Load data from uploaded Excel or CSV file
    
    Args:
        uploaded_file: Streamlit file uploader object
        
    Returns:
        pandas.DataFrame: Loaded data or None if error
    """
    try:
        if uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            st.error("Unsupported file format. Please upload .xlsx or .csv files.")
            return None
            
        # Convert date columns if they exist
        for col in df.columns:
            if 'date' in col.lower() or 'time' in col.lower():
                try:
                    df[col] = pd.to_datetime(df[col], errors='ignore')
                except:
                    pass
                    
        return df
        
    except Exception as e:
        st.error(f"Error loading file: {str(e)}")
        return None


def filter_data(df, search_term=None, date_range=None, date_column=None):
    """
    Filter DataFrame based on search term and date range
    
    Args:
        df (pd.DataFrame): Input DataFrame
        search_term (str): Text to search in Name/Country columns
        date_range (tuple): Start and end dates
        date_column (str): Column name for date filtering
        
    Returns:
        pandas.DataFrame: Filtered DataFrame
    """
    filtered_df = df.copy()
    
    # Text search filter
    if search_term:
        # Search in specific columns (Name, Country) if they exist
        search_columns = []
        for col in ['Name', 'Country', 'name', 'country']:
            if col in df.columns:
                search_columns.append(col)
        
        if search_columns:
            # Search in specific columns
            mask = False
            for col in search_columns:
                mask |= filtered_df[col].astype(str).str.contains(
                    search_term, case=False, na=False
                )
        else:
            # Search across all columns if Name/Country not found
            mask = filtered_df.astype(str).apply(
                lambda x: x.str.contains(search_term, case=False, na=False)
            ).any(axis=1)
            
        filtered_df = filtered_df[mask]
    
    # Date range filter
    if date_range and date_column and date_column in df.columns:
        start_date, end_date = date_range
        try:
            # Ensure date column is datetime
            filtered_df[date_column] = pd.to_datetime(filtered_df[date_column])
            
            # Filter by date range
            mask = (filtered_df[date_column].dt.date >= start_date) & \
                   (filtered_df[date_column].dt.date <= end_date)
            filtered_df = filtered_df[mask]
        except Exception as e:
            st.warning(f"Could not filter by date: {str(e)}")
    
    return filtered_df


def export_csv(df, filename="filtered_data"):
    """
    Convert DataFrame to CSV for download
    
    Args:
        df (pd.DataFrame): DataFrame to export
        filename (str): Base filename for download
        
    Returns:
        str: CSV data as string
    """
    try:
        return df.to_csv(index=False)
    except Exception as e:
        st.error(f"Error exporting data: {str(e)}")
        return None


def get_date_columns(df):
    """
    Identify potential date columns in DataFrame
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        list: List of column names that might contain dates
    """
    date_columns = []
    
    for col in df.columns:
        # Check column name
        if any(word in col.lower() for word in ['date', 'time', 'created', 'updated']):
            date_columns.append(col)
        # Check data type
        elif df[col].dtype == 'datetime64[ns]':
            date_columns.append(col)
        # Check if values look like dates
        elif df[col].dtype == 'object':
            try:
                sample = df[col].dropna().iloc[0] if not df[col].dropna().empty else None
                if sample and pd.to_datetime(sample, errors='coerce') is not pd.NaT:
                    date_columns.append(col)
            except:
                pass
                
    return date_columns


def display_report_stats(df):
    """
    Display basic statistics and info about the dataset
    
    Args:
        df (pd.DataFrame): DataFrame to analyze
    """
    if df is not None and len(df) > 0:
        # Basic info
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Rows", len(df))
        with col2:
            st.metric("Total Columns", len(df.columns))
        with col3:
            st.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024:.1f} KB")
        
        # Data types summary
        st.subheader("Column Information")
        info_df = pd.DataFrame({
            'Column': df.columns,
            'Type': [str(dtype) for dtype in df.dtypes],
            'Non-Null Count': [df[col].count() for col in df.columns],
            'Null Count': [df[col].isnull().sum() for col in df.columns]
        })
        st.dataframe(info_df, use_container_width=True)
        
        # Basic statistics for numeric columns
        numeric_columns = df.select_dtypes(include=['number']).columns
        if len(numeric_columns) > 0:
            st.subheader("Numeric Data Statistics")
            st.dataframe(df[numeric_columns].describe(), use_container_width=True)
    else:
        st.warning("No data to display statistics.")


# Test functions
def test_reports_module():
    """
    Test function to verify reports module functionality
    """
    # Test with sample data
    test_data = {
        'Name': ['User1', 'User2', 'User3'],
        'Country': ['USA', 'UK', 'Germany'],
        'Date': ['2025-01-01', '2025-01-02', '2025-01-03'],
        'Value': [100, 200, 300]
    }
    test_df = pd.DataFrame(test_data)
    test_df['Date'] = pd.to_datetime(test_df['Date'])
    
    # Test filtering
    filtered = filter_data(test_df, search_term="User1")
    assert len(filtered) == 1, "Text filtering failed"
    
    # Test CSV export
    csv_data = export_csv(test_df)
    assert csv_data is not None, "CSV export failed"
    
    # Test date column detection
    date_cols = get_date_columns(test_df)
    assert 'Date' in date_cols, "Date column detection failed"
    
    return True