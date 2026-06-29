from collections import deque
from src.graph.graph_builder import build_graph

def get_reasoning_paths(emotion: str, max_depth: int = 3) -> dict:
    """
    Traverses the knowledge graph using BFS starting from the given emotion
    to identify psychological root-cause chains and related concepts.
    
    Input:
        emotion: str
        max_depth: int (default 3)
    Output:
        dict: {
            "start_emotion": str,
            "paths": list of lists of strings,
            "related_concepts": list of strings
        }
    """
    emotion = emotion.lower().strip()
    G = build_graph()
    
    # If the emotion is not in the graph, return empty lists gracefully
    if emotion not in G:
        return {
            "start_emotion": emotion,
            "paths": [[emotion]],
            "related_concepts": []
        }
        
    paths = []
    # Queue stores paths: [ [node1], [node1, node2], ... ]
    queue = deque([[emotion]])
    
    while queue:
        current_path = queue.popleft()
        current_node = current_path[-1]
        
        # Edge limit: a path with N edges has N+1 nodes.
        # If we have reached the max edge depth, stop expanding this path.
        if len(current_path) - 1 >= max_depth:
            paths.append(current_path)
            continue
            
        successors = list(G.successors(current_node))
        
        # If it's a leaf node, we cannot traverse further
        if not successors:
            paths.append(current_path)
            continue
            
        # Otherwise, extend the path for each non-cyclic successor
        extended = False
        for successor in successors:
            if successor not in current_path:
                queue.append(current_path + [successor])
                extended = True
                
        # If we couldn't extend (e.g. all successors would create cycles), keep this path
        if not extended:
            paths.append(current_path)
            
    # Filter paths to keep only maximal/longest paths (remove subpaths)
    maximal_paths = []
    for p in paths:
        is_subpath = False
        for other_p in paths:
            if p != other_p and len(p) < len(other_p) and other_p[:len(p)] == p:
                is_subpath = True
                break
        if not is_subpath:
            maximal_paths.append(p)
            
    # Collect unique concepts traversed (excluding the starting emotion)
    related_concepts = []
    for path in maximal_paths:
        for node in path[1:]:
            if node not in related_concepts:
                related_concepts.append(node)
                
    return {
        "start_emotion": emotion,
        "paths": maximal_paths,
        "related_concepts": related_concepts
    }

if __name__ == "__main__":
    # Test traversal
    res = get_reasoning_paths("fear")
    print("Traversal Test (Fear):")
    print(res)
    
    res2 = get_reasoning_paths("anger")
    print("\nTraversal Test (Anger):")
    print(res2)
