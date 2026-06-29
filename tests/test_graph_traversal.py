import unittest
from src.graph.graph_traversal import get_reasoning_paths

class TestGraphTraversal(unittest.TestCase):
    
    def test_graph_traversal_valid_emotion(self):
        """
        Verifies that get_reasoning_paths retrieves correct BFS paths and 
        related concepts for a known emotion.
        """
        result = get_reasoning_paths("fear")
        
        self.assertIsInstance(result, dict)
        self.assertEqual(result["start_emotion"], "fear")
        self.assertIn("paths", result)
        self.assertIn("related_concepts", result)
        
        # Path should start with fear and traverse to attachment, anxiety, overthinking
        first_path = result["paths"][0]
        self.assertEqual(first_path[0], "fear")
        self.assertIn("attachment", first_path)
        
        # The starting emotion should NOT be in the related concepts list
        self.assertNotIn("fear", result["related_concepts"])
        self.assertGreater(len(result["related_concepts"]), 0)

    def test_graph_traversal_missing_node(self):
        """
        Verifies that querying a node not present in the graph returns a 
        graceful response without exceptions.
        """
        result = get_reasoning_paths("nonexistent_emotion")
        
        self.assertEqual(result["start_emotion"], "nonexistent_emotion")
        self.assertEqual(result["paths"], [["nonexistent_emotion"]])
        self.assertEqual(result["related_concepts"], [])

if __name__ == "__main__":
    unittest.main()
