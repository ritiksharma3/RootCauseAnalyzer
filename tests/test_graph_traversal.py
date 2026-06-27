from pprint import pprint
from src.graph.graph_builder import build_graph
from src.graph.graph_traversal import get_reasoning_paths

graph = build_graph()

result = get_reasoning_paths(graph, "fear")

print(result)