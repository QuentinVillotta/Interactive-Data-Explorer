
import pandas as pd
import streamlit as st
import base64
import json
import pickle
import uuid
import re
from pygwalker.api.streamlit import StreamlitRenderer

# Intern module
from app_utils import data_loading as dl

def set_clicked():
    st.session_state.clicked = True
    
# You should cache your pygwalker renderer, if you don't want your memory to explode
@st.cache_resource
def get_pyg_renderer(df) -> "StreamlitRenderer":
    # If you want to use feature of saving chart config, set `spec_io_mode="rw"`
    return StreamlitRenderer(df, dark="light", spec="./conf/gw_config.json", spec_io_mode="rw")

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Interactive Data Explorer",
    layout="wide"
)

# Title
st.title("Interactive Data Explorer")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

st.button('Upload File', on_click=set_clicked, type="primary")
if st.session_state.clicked:
    uploaded_file = st.file_uploader("**Choose a file**", type=["csv", "xlsx","xls"], label_visibility="visible")
    if uploaded_file is  None:
        st.caption(":orange-background[:file_folder: Please upload a file]")
    else:
        data = dl.data_loader(uploaded_file)
        if data is not None:
            # Pygwalker dataviz tool
            renderer = get_pyg_renderer(df=data)
            renderer.explorer()