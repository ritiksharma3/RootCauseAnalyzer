import matplotlib.pyplot as plt
import networkx as nx
from src.graph.graph_builder import build_graph

def draw_reasoning_graph(highlight_path: list = None):
    """
    Renders the knowledge graph using NetworkX and Matplotlib, highlighting
    the traversal path if provided.
    
    Input:
        highlight_path: list of strings (the traversal path)
    Output:
        matplotlib.figure.Figure: The styled graph plot.
    """
    G = build_graph()
    
    # Create the figure with a dark slate background to look premium
    fig, ax = plt.subplots(figsize=(9, 5), facecolor="#1e222a")
    ax.set_facecolor("#1e222a")
    
    # Calculate node layouts (use shell or spring layout with custom tuning)
    pos = nx.spring_layout(G, seed=101, k=1.8, iterations=50)
    
    # Parse highlighted nodes and edges
    highlighted_nodes = set()
    if highlight_path:
        for node in highlight_path:
            highlighted_nodes.add(node.lower().strip())
            
    highlighted_edges = []
    if highlight_path and len(highlight_path) > 1:
        for i in range(len(highlight_path) - 1):
            u = highlight_path[i].lower().strip()
            v = highlight_path[i+1].lower().strip()
            highlighted_edges.append((u, v))
            
    # Node colors: highlights get gold; otherwise styled by type
    node_colors = []
    for node in G.nodes():
        if node in highlighted_nodes:
            node_colors.append("#ffb86c")  # Highlight: Soft orange-amber
        else:
            ntype = G.nodes[node].get("type", "")
            if ntype == "emotion":
                node_colors.append("#8be9fd")  # Emotion: cyan/blue
            elif ntype == "root_cause":
                node_colors.append("#ff5555")  # Root cause: red-pink
            elif ntype == "mental_pattern":
                node_colors.append("#bd93f9")  # Mental pattern: purple
            else:
                node_colors.append("#6272a4")  # Other/Virtues: gray-blue
                
    # Edge colors and widths: highlights get gold, rest dark slate
    edge_colors = []
    edge_widths = []
    for u, v in G.edges():
        if (u, v) in highlighted_edges:
            edge_colors.append("#ffb86c")
            edge_widths.append(2.8)
        else:
            edge_colors.append("#44475a")
            edge_widths.append(1.2)
            
    # Draw node shapes
    nx.draw_networkx_nodes(
        G, pos, 
        ax=ax, 
        node_size=1000, 
        node_color=node_colors, 
        edgecolors="#282a36", 
        linewidths=1.5
    )
    
    # Draw directed edges (arrows)
    nx.draw_networkx_edges(
        G, pos, 
        ax=ax, 
        edgelist=list(G.edges()), 
        edge_color=edge_colors, 
        width=edge_widths, 
        arrowsize=18, 
        arrowstyle="-|>", 
        connectionstyle="arc3,rad=0.1"
    )
    
    # Draw label text
    labels = {node: G.nodes[node].get("label", node) for node in G.nodes()}
    nx.draw_networkx_labels(
        G, pos, 
        labels=labels, 
        ax=ax, 
        font_size=8, 
        font_color="#f8f8f2", 
        font_weight="bold"
    )
    
    # Draw edge relation text
    edge_labels = {(u, v): d.get("relation", "").replace("_", " ") for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(
        G, pos, 
        edge_labels=edge_labels, 
        ax=ax, 
        font_size=7, 
        font_color="#6272a4",
        bbox=dict(facecolor="#1e222a", edgecolor="none", alpha=0.85)
    )
    
    plt.title("Psychological Root Cause Knowledge Graph", color="#f8f8f2", fontsize=12, fontweight="bold", pad=12)
    plt.axis("off")
    fig.tight_layout()
    return fig

if __name__ == "__main__":
    # Test drawing
    fig = draw_reasoning_graph(["fear", "attachment", "anxiety", "overthinking"])
    plt.savefig("test_graph.png")
    print("Graph image saved to test_graph.png.")
