import os
import json
import networkx as nx
from src.config import GRAPH_JSON_PATH

def build_graph() -> nx.DiGraph:
    """
    Loads nodes and edges from knowledge_graph.json and returns a NetworkX DiGraph.
    """
    if not os.path.exists(GRAPH_JSON_PATH):
        raise FileNotFoundError(f"Knowledge graph file not found at {GRAPH_JSON_PATH}")
        
    with open(GRAPH_JSON_PATH, 'r', encoding="utf-8") as f:
        data = json.load(f)
        
    G = nx.DiGraph()
    
    # Add nodes with attributes
    for node in data.get("nodes", []):
        node_id = node["id"].lower()  # Force lowercase
        G.add_node(
            node_id, 
            label=node.get("label", node_id.capitalize()), 
            type=node.get("type", "concept")
        )
        
    # Add edges with attributes
    for edge in data.get("edges", []):
        source = edge["source"].lower()
        target = edge["target"].lower()
        G.add_edge(source, target, relation=edge.get("relation", "connected_to"))
        
    return G

if __name__ == "__main__":
    # Test builder
    G = build_graph()
    print("Graph Build Test:")
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(f"Nodes: {list(G.nodes(data=True))}")
    print(f"Edges: {list(G.edges(data=True))}")
