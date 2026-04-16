import streamlit as st
import json
import os

# Deterministic Path Resolution
# This looks for the file relative to where this script is sitting
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, "..", "data", "graph_data.json")

def load_graph():
    if os.path.exists(data_path):
        with open(data_path, 'r') as f:
            return json.load(f)
    return None

data = load_graph()

if data:
    st.success("Nairobi-01 Node Synchronized.")
    # ... your existing agraph(data['nodes'], data['links']...) code ...
else:
    # This will help us debug exactly where the Cloud thinks the file should be
    st.error(f"Graph data not found at: {data_path}")
    st.info("System Check: Ensure 'graph_data.json' exists in the /data folder.")
