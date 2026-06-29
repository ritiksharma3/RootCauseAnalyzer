import unittest
from src.recommendation.recommendation_engine import get_recommendations

class TestRecommendationEngine(unittest.TestCase):
    
    def test_get_recommendations_valid_concepts(self):
        """
        Verifies that get_recommendations returns a list of dictionaries with 
        correct keys for valid mapped concepts.
        """
        concepts = ["attachment", "overthinking"]
        recs = get_recommendations(concepts)
        
        self.assertIsInstance(recs, list)
        self.assertEqual(len(recs), 2)
        
        for r in recs:
            self.assertIsInstance(r, dict)
            self.assertIn("concept", r)
            self.assertIn("principle", r)
            self.assertIn("recommendation", r)
            self.assertIn("chapter_reference", r)
            self.assertIn("gita_idea", r)
            self.assertIn(r["concept"], concepts)

    def test_get_recommendations_falls_back_to_emotion(self):
        """
        Verifies that recommendations are returned for a detected emotion even
        when the graph traversal supplies no matching conceptual nodes.
        """
        recs = get_recommendations(["fear"])
        self.assertIsInstance(recs, list)
        self.assertGreaterEqual(len(recs), 1)
        self.assertEqual(recs[0]["concept"], "fear")

    def test_get_recommendations_invalid_concepts(self):
        """
        Verifies that requesting recommendations for unmapped concepts
        skips them and returns an empty list without throwing errors.
        """
        recs = get_recommendations(["random_nonexistent_concept"])
        self.assertIsInstance(recs, list)
        self.assertEqual(len(recs), 0)

if __name__ == "__main__":
    unittest.main()
