import streamlit as st
import matplotlib.pyplot as plt

# Import custom modules
from src.ml.predict_emotion import predict_emotion
from src.graph.graph_traversal import get_reasoning_paths
from src.recommendation.recommendation_engine import get_recommendations
from src.explainability.explanation_generator import generate_explanation
from src.ui.display_graph import draw_reasoning_graph
from src.ui.display_results import display_emotion_probabilities, display_recommendation_cards

# 1. Page Configuration
st.set_page_config(
    page_title="Psychological Root Cause Analyzer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Premium Custom CSS Styling
st.markdown("""
    <style>
    /* Premium dark-theme background and typography */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #ff79c6, #bd93f9, #8be9fd);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
        text-align: center;
    }
    
    .subtitle {
        font-size: 1.1rem;
        color: #abb2bf;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Educational safety disclaimer box */
    .disclaimer-box {
        background-color: rgba(255, 85, 85, 0.1);
        border: 1px solid #ff5555;
        border-radius: 8px;
        padding: 12px 20px;
        margin-bottom: 25px;
    }
    .disclaimer-box h4 {
        margin: 0 0 6px 0;
        color: #ff5555;
        font-weight: 600;
    }
    .disclaimer-box p {
        margin: 0;
        color: #f8f8f2;
        font-size: 0.9rem;
        line-height: 1.4;
    }
    
    /* Explanatory glassmorphic card */
    .explanation-card {
        background-color: rgba(189, 147, 249, 0.08);
        border: 1px solid rgba(189, 147, 249, 0.25);
        border-radius: 8px;
        padding: 20px;
        margin-top: 15px;
        line-height: 1.6;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    /* Metric Card styling */
    .metric-card {
        background-color: #21252b;
        border-radius: 6px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 1px solid #2e3440;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Main Dashboard Layout
st.markdown("<div class='main-title'>🧠 Psychological Root Cause Analyzer</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Reflective AI mapping mental patterns & emotions to Gita-inspired wisdom</div>", unsafe_allow_html=True)

# Safety Disclaimer (Mandatory Rule)
st.markdown("""
<div class="disclaimer-box">
    <h4>⚠️ Educational & Reflective Tool Disclaimer</h4>
    <p>This application is designed solely for self-reflection and educational purposes based on historical and philosophical principles. 
    It is <strong>not</strong> a clinical diagnosis system and does <strong>not</strong> replace professional medical or mental health support. 
    If you are experiencing severe distress or crisis, please seek immediate help from a licensed professional counselor or healthcare provider.</p>
</div>
""", unsafe_allow_html=True)

# Sidebar with Example Inputs and Information
with st.sidebar:
    st.image("https://img.icons8.com/color/96/yoga.png", width=70)
    st.markdown("### About the Analyzer")
    st.write(
        "This project implements an offline, explainable AI system that traces emotions to core cognitive "
        "concepts and suggests reflective guidance."
    )
    
    st.markdown("---")
    st.markdown("### Interactive Presets")
    st.write("Click a preset feeling below to auto-populate the entry box:")
    
    preset_1 = st.button("I feel scared that I will fail and everyone will judge me.")
    preset_2 = st.button("I feel tensed and worried about tomorrow's presentation.")
    preset_3 = st.button("I am furious because my teammates ignored my hard work.")
    preset_4 = st.button("I feel heavy-hearted, sad, and lonely today.")
    preset_5 = st.button("I believe in myself and know I can tackle this challenge.")
    preset_6 = st.button("I am highly confused and indecisive about my career paths.")

# Text Box Input Setup
user_input = ""
if preset_1:
    user_input = "I feel scared that I will fail and everyone will judge me."
elif preset_2:
    user_input = "I feel tensed and worried about tomorrow's presentation."
elif preset_3:
    user_input = "I am furious because my teammates ignored my hard work."
elif preset_4:
    user_input = "I feel heavy-hearted, sad, and lonely today."
elif preset_5:
    user_input = "I believe in myself and know I can tackle this challenge."
elif preset_6:
    user_input = "I am highly confused and indecisive about my career paths."

st.markdown("### ✍️ Express Your Current Feeling or Situation")
user_text = st.text_area(
    label="Describe what is happening or what you are feeling in detail:",
    value=user_input,
    height=120,
    placeholder="E.g., I feel restless and scared of making mistakes in my new job..."
)

# 4. Run Analysis Pipeline
if st.button("🔍 Trace Root Causes", type="primary"):
    if not user_text.strip():
        st.warning("Please type a feeling or select a preset before running the analysis.")
    else:
        with st.spinner("Analyzing emotion and traversing knowledge base..."):
            try:
                # Execution Pipeline Contracts
                emotion_result = predict_emotion(user_text)
                emotion = emotion_result["emotion"]
                confidence = emotion_result["confidence"]
                
                graph_result = get_reasoning_paths(emotion)
                paths = graph_result["paths"]
                concepts = graph_result["related_concepts"]
                
                recommendations = get_recommendations(concepts)
                
                explanation = generate_explanation(
                    emotion,
                    paths,
                    recommendations
                )
                
                # 5. UI Render Results
                st.markdown("---")
                
                # Split layout: Left column = Metrics & Text Explanation, Right column = Graph Visualization & Rules
                col_left, col_right = st.columns([1, 1], gap="large")
                
                with col_left:
                    st.subheader("🎯 Primary Analysis")
                    
                    # Highlight dominant emotion metrics
                    emotion_colors = {
                        "fear": "#ff5555",
                        "anxiety": "#bd93f9",
                        "anger": "#ffb86c",
                        "sadness": "#8be9fd",
                        "confidence": "#50fa7b",
                        "confusion": "#f1fa8c"
                    }
                    accent_color = emotion_colors.get(emotion, "#ffb86c")
                    
                    st.markdown(f"""
                        <div class="metric-card">
                            <span style="font-size: 0.9rem; color: #abb2bf; text-transform: uppercase; font-weight: bold;">Dominant Emotion</span>
                            <h2 style="margin: 5px 0; color: {accent_color}; font-size: 2.2rem;">{emotion.upper()}</h2>
                            <span style="font-size: 1rem; color: #f8f8f2;">Match Confidence: <strong>{int(confidence*100)}%</strong></span>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Explainability Paragraph Box
                    st.subheader("📖 Root-Cause Explanation")
                    st.markdown(f"""
                        <div class="explanation-card">
                            {explanation}
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Probability breakdowns
                    st.markdown("<br>", unsafe_allow_html=True)
                    display_emotion_probabilities(emotion_result["probabilities"], emotion)
                    
                with col_right:
                    st.subheader("🕸️ Graph Reasoning Path")
                    
                    # Draw Matplotlib Graph figure
                    fig = draw_reasoning_graph(paths[0] if paths else None)
                    st.pyplot(fig)
                    plt.close(fig) # Prevent memory leaks
                    
                    # List recommendations cards
                    st.markdown("<br>", unsafe_allow_html=True)
                    display_recommendation_cards(recommendations)
                    
            except Exception as e:
                st.error(f"Error executing analysis: {e}")
                st.exception(e)
