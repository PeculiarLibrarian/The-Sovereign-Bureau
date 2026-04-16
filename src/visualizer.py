import os
import streamlit as st

# This logic works regardless of whether the 'root' is the repo or the folder
possible_paths = [
    "the-sovereign-bureau/data/graph_data.json", # Root-level view
    "data/graph_data.json",                      # Folder-level view
    "../data/graph_data.json"                    # Script-relative view
]

data_path = None
for p in possible_paths:
    if os.path.exists(p):
        data_path = p
        break

if not data_path:
    st.error("Sovereign Protocol Failure: graph_data.json not found in any known sector.")
    st.info(f"Current Working Directory: {os.getcwd()}")
    st.info(f"Directory Contents: {os.listdir('.')}")
