import streamlit as st

def display_emotion_probabilities(probabilities: dict, dominant_emotion: str):
    """
    Renders the classification probabilities using custom styled horizontal bars
    and indicators for the dominant emotion.
    """
    st.subheader("📊 Emotion Probability Breakdown")
    
    # Sort probabilities descending
    sorted_probs = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)
    
    # Color theme mappings for vibrant and premium look
    color_map = {
        "fear": "#ff5555",       # Coral Red
        "anxiety": "#bd93f9",    # Soft Lavender
        "anger": "#ffb86c",      # Warm Amber
        "sadness": "#8be9fd",    # Cyan Blue
        "confidence": "#50fa7b", # Mint Green
        "confusion": "#f1fa8c"   # Pastel Yellow
    }
    
    for emotion, prob in sorted_probs:
        label = emotion.capitalize()
        is_dominant = (emotion == dominant_emotion)
        color = color_map.get(emotion, "#6272a4")
        pct = int(prob * 100)
        
        # Display name and indicator
        col1, col2 = st.columns([1, 4])
        with col1:
            if is_dominant:
                st.markdown(f"**{label} 🌟**")
            else:
                st.markdown(f"<span style='color: #6272a4;'>{label}</span>", unsafe_allow_html=True)
        with col2:
            st.progress(prob)
            st.markdown(
                f"<div style='text-align: right; font-size: 0.75rem; color: {color}; margin-top: -10px; font-weight: bold;'>"
                f"{pct}% match"
                f"</div>", 
                unsafe_allow_html=True
            )

def display_recommendation_cards(recommendations: list[dict]):
    """
    Renders recommendation rules inside premium styled glassmorphic containers.
    """
    st.subheader("💡 Philosophical & Reflective Recommendations")
    
    if not recommendations:
        st.info("No matching recommendations found for the traversed concepts.")
        return
        
    for rec in recommendations:
        concept = rec["concept"].capitalize()
        principle = rec["principle"]
        recommendation = rec["recommendation"]
        reference = rec["chapter_reference"]
        gita_idea = rec.get("gita_idea", "")
        
        card_html = f"""
        <div style="
            background-color: #21252b; 
            border-left: 4px solid #ffb86c; 
            border-radius: 6px;
            padding: 16px; 
            margin-bottom: 16px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
        ">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: bold; color: #ffb86c; font-size: 1.05rem;">🔑 Root Cause: {concept}</span>
                <span style="background-color: #2c313c; color: #abb2bf; font-size: 0.75rem; padding: 3px 8px; border-radius: 12px; font-weight: bold;">
                    {reference}
                </span>
            </div>
            <div style="font-weight: 600; color: #f8f8f2; margin-bottom: 6px; font-size: 0.95rem;">
                Principle: {principle}
            </div>
            <div style="font-style: italic; color: #8be9fd; margin-bottom: 12px; font-size: 0.9rem; border-left: 2px solid #6272a4; padding-left: 8px;">
                "{gita_idea}"
            </div>
            <div style="color: #abb2bf; font-size: 0.9rem; line-height: 1.4;">
                <strong>Reflective Action:</strong> {recommendation}
            </div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
