import matplotlib.pyplot as plt
import networkx as nx

from src.graph.graph_builder import build_graph


def visualize_graph():

    G = build_graph()

    plt.figure(figsize=(14, 10))

    pos = nx.spring_layout(G, seed=42)

    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=1800
    )

    nx.draw_networkx_edges(
        G,
        pos,
        arrows=True
    )

    nx.draw_networkx_labels(
        G,
        pos,
        font_size=8
    )

    edge_labels = nx.get_edge_attributes(G, "relation")

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_size=6
    )

    plt.title("Knowledge Graph")

    plt.axis("off")

    plt.show()


if __name__ == "__main__":
    visualize_graph()