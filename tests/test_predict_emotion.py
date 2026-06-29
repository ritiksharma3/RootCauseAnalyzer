import unittest
from unittest.mock import patch, MagicMock
from src.ml.predict_emotion import predict_emotion

class TestPredictEmotion(unittest.TestCase):
    
    def test_predict_emotion_contract(self):
        """
        Verifies that predict_emotion returns the correct dictionary keys,
        a valid dominant emotion, and a populated probabilities dict.
        """
        mock_pipeline = MagicMock()
        mock_pipeline.return_value = {
            "labels": ["fear", "anxiety", "anger", "sadness", "confidence", "confusion"],
            "scores": [0.82, 0.09, 0.06, 0.01, 0.01, 0.01]
        }
        
        with patch('src.ml.predict_emotion._hf_pipeline', mock_pipeline), \
             patch('src.ml.predict_emotion._load_models'):
             
            result = predict_emotion("I feel nervous and scared")
            
            # Verify contract keys
            self.assertIsInstance(result, dict)
            self.assertIn("emotion", result)
            self.assertIn("confidence", result)
            self.assertIn("probabilities", result)
            
            # Verify values
            self.assertEqual(result["emotion"], "fear")
            self.assertEqual(result["confidence"], 0.82)
            self.assertEqual(result["probabilities"]["fear"], 0.82)
            self.assertEqual(len(result["probabilities"]), 6)

    def test_predict_emotion_empty_input(self):
        """
        Verifies that empty string or whitespace inputs are handled gracefully
        without throwing exceptions.
        """
        result = predict_emotion("")
        self.assertEqual(result["emotion"], "confusion")
        self.assertGreater(result["confidence"], 0.1)
        self.assertEqual(len(result["probabilities"]), 6)

if __name__ == "__main__":
    unittest.main()
