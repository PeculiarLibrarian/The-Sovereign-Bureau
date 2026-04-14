import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import json

st.set_page_config(layout="wide", page_title="PADI Living Library")

# Custom Styling to match your screenshot
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

st.title("PADI Sovereign Bureau: Living Library of Access")
st.sidebar.header("Node Stats")

# Load the serialized triples
try:
    with open("data/graph_data.json", "r") as f:
        data = json.load(f)
    
    nodes = []
    edges = []

    # Map Groups to Colors (Matching your Screenshot)
    colors = {"Subject": "#ff4b4b", "Object": "#1c83e1", "Value": "#00d4ff"}

    for node in data["nodes"]:
        nodes.append(Node(id=node["id"], 
                          label=node["id"], 
                          size=25 if node["group"] == "Subject" else 15,
                          color=colors.get(node["group"], "#ffffff")))

    for link in data["links"]:
        edges.append(Edge(source=link["source"], 
                          target=link["target"], 
                          label=link["label"]))

    config = Config(width=1000, 
                    height=600, 
                    directed=True,
                    nodeHighlightBehavior=True, 
                    highlightColor="#F7A7A6",
                    collapsible=False)

    st.sidebar.metric("Active Triples", len(data["links"]))
    st.sidebar.write("Node: Nairobi-01-Standard")

    return_value = agraph(nodes=nodes, edges=edges, config=config)

except FileNotFoundError:
    st.error("Graph data not found. Run the Liaison script first.")
