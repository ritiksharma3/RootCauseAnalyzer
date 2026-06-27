import json
from pathlib import Path

import networkx as nx


def build_graph():
    """
    Load the knowledge graph from JSON
    and return a NetworkX directed graph.
    """

    project_root = Path(__file__).resolve().parents[2]
    graph_path = project_root / "data" / "knowledge_graph.json"

    with open(graph_path, "r", encoding="utf-8") as f:
        graph_data = json.load(f)

    G = nx.DiGraph()

    # Add nodes
    for node in graph_data["nodes"]:
        G.add_node(
            node["id"],
            label=node["label"],
            type=node["type"]
        )

    # Add edges
    for edge in graph_data["edges"]:
        G.add_edge(
            edge["source"],
            edge["target"],
            relation=edge["relation"]
        )

    return G