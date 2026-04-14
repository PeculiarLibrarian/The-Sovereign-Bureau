import json
from rdflib import Graph

def generate_graph_data(ttl_path, output_path):
    g = Graph()
    g.parse(ttl_path, format="turtle")
    
    nodes = []
    links = []
    seen_nodes = set()

    for s, p, o in g:
        # Process Subject
        s_label = str(s).split('#')[-1] or str(s).split('/')[-1]
        if s_label not in seen_nodes:
            nodes.append({"id": s_label, "group": "Subject"})
            seen_nodes.add(s_label)
        
        # Process Object
        o_label = str(o).split('#')[-1] or str(o).split('/')[-1]
        if o_label not in seen_nodes:
            # Differentiate Literals from URIs
            group = "Value" if "http" not in str(o) else "Object"
            nodes.append({"id": o_label, "group": group})
            seen_nodes.add(o_label)
            
        # Create Link (Predicate)
        p_label = str(p).split('#')[-1] or str(p).split('/')[-1]
        links.append({"source": s_label, "target": o_label, "label": p_label})

    graph_payload = {"nodes": nodes, "links": links}
    
    with open(output_path, 'w') as f:
        json.dump(graph_payload, f, indent=4)
    
    print(f"[BUREAU] Graph serialized: {len(nodes)} nodes, {len(links)} links.")
    return len(g)

if __name__ == "__main__":
    count = generate_graph_data("ontology/padi_core.ttl", "data/graph_data.json")
    print(f"[BUREAU] Nairobi-01-Node Online. {count} triples active.")
