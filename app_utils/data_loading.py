import pandas as pd
import os
import streamlit as st

def data_loader(uploaded_file):
    """
    Load data from a CSV or Excel file.

    Parameters:
    file_path (str): Path to the file to be loaded.

    Returns:
    DataFrame or None: A pandas DataFrame containing the loaded data, or None if loading fails.
    """
    try:
        # Check file extension to determine the appropriate loader
        _, file_extension = os.path.splitext(uploaded_file.name)

        if file_extension.lower() == '.csv':
            # Load data from CSV
            data = pd.read_csv(uploaded_file)
            return data
        elif file_extension.lower() in ['.xls', '.xlsx']:
            # Load data from Excel
            data = pd.read_excel(uploaded_file)
            return data
        else:
            st.caption(":x: :red[Unsupported file type. Please provide a CSV or Excel file]")
            return None

    except Exception as e:
        print(f"Error loading data: {e}")
        return None
