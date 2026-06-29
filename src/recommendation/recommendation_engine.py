import os
import json
from src.config import GITA_JSON_PATH

def get_recommendations(concepts: list[str]) -> list[dict]:
    """
    Retrieves Gita-inspired principles and reflections for a list of psychological concepts.
    
    Input:
        concepts: list[str]
    Output:
        list[dict]: A list of recommendation dictionaries containing keys:
                    'concept', 'principle', 'recommendation', 'chapter_reference', and 'gita_idea'.
    """
    if not os.path.exists(GITA_JSON_PATH):
        raise FileNotFoundError(f"Gita principles file not found at {GITA_JSON_PATH}")
        
    with open(GITA_JSON_PATH, 'r', encoding="utf-8") as f:
        principles_db = json.load(f)
        
    recommendations = []
    
    for concept in concepts:
        concept_lower = concept.lower().strip()
        if concept_lower in principles_db:
            data = principles_db[concept_lower]
            recommendations.append({
                "concept": concept_lower,
                "principle": data.get("principle", "N/A"),
                "recommendation": data.get("recommendation", "N/A"),
                "chapter_reference": data.get("chapter_reference", "N/A"),
                "gita_idea": data.get("gita_idea", "N/A")  # Added as rich metadata
            })
            
    return recommendations

if __name__ == "__main__":
    # Test recommendation engine
    test_concepts = ["attachment", "overthinking"]
    res = get_recommendations(test_concepts)
    print("Recommendation Engine Test:")
    print(res)
