def generate_explanation(emotion: str, paths: list, recommendations: list) -> str:
    """
    Generates a natural-language explanation combining the detected emotion,
    traversal paths, root causes, and Gita principles.
    
    Input:
        emotion: str
        paths: list of lists of strings
        recommendations: list of dicts
    Output:
        str: A human-readable, reflective explanation paragraph.
    """
    if not paths or not paths[0] or len(paths[0]) == 0:
        return (
            "The system classified your state, but could not map it to the psychological knowledge base. "
            "Please try describing your feelings or situation in more detail."
        )
        
    # Format the reasoning paths
    path_strings = []
    for path in paths:
        path_strings.append(" ➔ ".join([node.capitalize() for node in path]))
    path_text = " & ".join(path_strings)
    
    emotion_cap = emotion.capitalize()
    
    if not recommendations:
        return (
            f"The analyzer detected the dominant emotion as **{emotion_cap}** (reasoning chain: {path_text}). "
            f"In this instance, no specific recommendation rules were matched. "
            f"Please remember this tool is for personal reflection and not clinical diagnosis."
        )
        
    # Retrieve the primary recommendation details
    primary = recommendations[0]
    concept_cap = primary["concept"].capitalize()
    principle = primary["principle"]
    gita_idea = primary["gita_idea"]
    rec_text = primary["recommendation"]
    ref = primary["chapter_reference"]
    
    explanation = (
        f"The analyzer detected the dominant emotion as **{emotion_cap}** (reasoning chain: {path_text}). "
        f"This state is connected to the deeper psychological root cause of **{concept_cap}**. "
        f"According to the Bhagavad Gita's teaching on **{principle}** ({ref}), "
        f"the underlying idea is: *\"{gita_idea}\"* "
        f"For self-reflection, it is recommended to: {rec_text}"
    )
    
    return explanation

if __name__ == "__main__":
    # Test explanation generator
    test_paths = [["fear", "attachment", "anxiety", "overthinking"]]
    test_recs = [
        {
            "concept": "attachment",
            "principle": "Detachment from results",
            "recommendation": "Shift attention from outcome fear to present effort.",
            "chapter_reference": "Chapter 2, Verse 47",
            "gita_idea": "Focus on action, not only on the fruits of action."
        }
    ]
    res = generate_explanation("fear", test_paths, test_recs)
    print("Explanation Generator Test:")
    print(res)
