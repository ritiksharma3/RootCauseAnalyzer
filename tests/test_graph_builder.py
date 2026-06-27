from src.graph.graph_builder import build_graph
graph = build_graph()
print(graph.nodes(data=True))
print(graph.edges(data=True))