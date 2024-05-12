import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer
# Intern module
from app_utils import data_loading as dl

# Global Vars
ALLOWED_FILE_FORMATS=["csv", "xlsx", "xls", "pq", "parquet"]

def set_clicked():
    st.session_state.clicked = True
    
@st.cache_resource
def get_pyg_renderer(df) -> "StreamlitRenderer":
    # If you want to use feature of saving chart config, set `spec_io_mode="rw"`
    return StreamlitRenderer(df, spec="./conf/gw_config.json",  spec_io_mode="r")

# App config 
# - Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Interactive Data Explorer",
    layout="wide"
)

# App Title
st.title("Interactive Data Explorer")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

# Upload btn
st.button('Upload File', on_click=set_clicked, type="primary")

# Workflow
if st.session_state.clicked:
    uploaded_file = st.file_uploader("**Choose a file**", type=ALLOWED_FILE_FORMATS, label_visibility="visible")
    if uploaded_file is None:
        st.caption(":orange-background[:file_folder: Please upload a file]")
    else:
        # Transform data to pandas DF
        df = dl.data_loader(uploaded_file)
        if df is not None:
            # Pygwalker dataviz tool
            renderer = get_pyg_renderer(df=df)
            renderer.explorer(default_tab="data")