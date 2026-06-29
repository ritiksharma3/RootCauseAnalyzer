import os
import json
from src.config import GITA_JSON_PATH


def _resolve_principle_key(concept: str, principles_db: dict) -> str | None:
    """Resolve a user-facing concept to a known Gita wisdom entry."""
    normalized = concept.lower().strip().replace(" ", "_").replace("-", "_")
    if normalized in principles_db:
        return normalized

    aliases = {
        "overthinking": "anxiety",
        "worry": "anxiety",
        "worried": "anxiety",
        "nervous": "fear",
        "scared": "fear",
        "afraid": "fear",
        "sad": "sadness",
        "depressed": "sadness",
        "grieving": "grief",
        "lonely": "loneliness",
        "uncertain": "uncertainty",
        "confused": "confusion",
        "frustrated": "frustration",
        "stressed": "stress",
        "angry": "anger",
        "jealous": "jealousy",
        "proud": "pride",
        "hopeful": "hope",
        "grateful": "gratitude",
        "loving": "love",
        "happy": "happiness",
    }
    return aliases.get(normalized)


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
    seen = set()

    for concept in concepts:
        concept_lower = concept.lower().strip()
        if not concept_lower or concept_lower in seen:
            continue

        resolved_key = _resolve_principle_key(concept_lower, principles_db)
        if resolved_key:
            data = principles_db[resolved_key]
            recommendations.append({
                "concept": concept_lower,
                "principle": data.get("principle", "N/A"),
                "recommendation": data.get("recommendation", "N/A"),
                "practical_step": data.get("recommendation", "N/A"),
                "chapter_reference": data.get("chapter_reference", "N/A"),
                "gita_idea": data.get("gita_idea", "N/A")
            })
            seen.add(concept_lower)

    return recommendations

if __name__ == "__main__":
    # Test recommendation engine
    test_concepts = ["attachment", "overthinking"]
    res = get_recommendations(test_concepts)
    print("Recommendation Engine Test:")
    print(res)
