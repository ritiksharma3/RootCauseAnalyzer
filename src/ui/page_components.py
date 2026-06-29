from html import escape
from typing import Any, Callable, Dict, List

import matplotlib.pyplot as plt
import streamlit as st

from src.explainability.explanation_generator import generate_explanation
from src.graph.graph_traversal import get_reasoning_paths
from src.ml.predict_emotion import predict_emotion
from src.recommendation.recommendation_engine import get_recommendations
from src.ui.display_graph import draw_reasoning_graph
from src.ui.display_results import display_emotion_probabilities

DISCLAIMER = (
    "This tool is for educational reflection and explainable AI demonstration only. "
    "It is not a medical diagnosis, therapy, or emergency support system."
)
PAGES = ("landing", "journey", "details", "transition", "chat_analysis")


def _safe(value: Any) -> str:
    return escape(str(value))


def initialize_session_state() -> None:
    if "page" not in st.session_state:
        st.session_state.page = "landing"
    st.session_state.setdefault(
        "user_profile",
        {
            "age": "",
            "gender": "Prefer not to say",
            "current_state": "Calm",
            "trigger_context": "",
        },
    )
    st.session_state.setdefault("analysis_text", "")
    st.session_state.setdefault("analysis_result", None)


def go_to_page(page: str) -> None:
    if page in PAGES:
        st.session_state.page = page
        st.rerun()


def render_sidebar() -> None:
    with st.sidebar:
        st.markdown("<div class='sidebar-panel'>", unsafe_allow_html=True)
        st.markdown("<h3>ॐ Scripture Console</h3>", unsafe_allow_html=True)
        st.markdown(
            "<p>Navigate the guided flow of emotion detection, root-cause reasoning, and Gita-style reflection.</p>",
            unsafe_allow_html=True,
        )
        st.markdown("<h4>Journey Steps</h4>", unsafe_allow_html=True)
        st.markdown(
            "<ul>"
            "<li>Emotion Detection</li>"
            "<li>Root Cause Graph</li>"
            "<li>Gita Wisdom</li>"
            "<li>Explainable Reflection</li>"
            "</ul>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div class='footer-note'>Current page: {_safe(st.session_state.get('page', 'landing').replace('_', ' ').title())}</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)


def render_landing_page() -> None:
    st.markdown(
        f"""
<section class="scripture-hero">
  <div class="particle-field"></div>
  <div class="aura"></div>
  <div class="scripture-frame"></div>
  <div class="copy-block">
    <div class="eyebrow">Vedic Gita Scriptures Interface</div>
    <h1 class="title-xl">Psychological Root Cause Analyzer</h1>
    <p class="subtitle">Emotion Intelligence through NLP, Knowledge Graphs, and Gita-Inspired Reasoning</p>
    <p class="sutra-line">From emotion to insight, from confusion to clarity.</p>
    <p class="body-copy">An offline explainable AI system that detects emotional patterns, maps them to root-cause reasoning paths, and presents reflective Gita-inspired insights.</p>
    <div class="disclaimer-inline">{DISCLAIMER}</div>
  </div>
</section>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    if st.button("Begin Inner Analysis", type="primary", use_container_width=True):
        go_to_page("journey")


def render_journey_page() -> None:
    card_html = "".join(
        '<div class="scripture-card">'
        '<div class="card-symbol"></div>'
        f'<h3>{_safe(title)}</h3>'
        f'<p>{_safe(copy)}</p>'
        '</div>'
        for title, copy in [
            (
                "Emotion Detection",
                "NLP estimates the dominant emotional pattern and confidence spread.",
            ),
            (
                "Root Cause Graph",
                "A knowledge graph traces possible root-cause reasoning paths.",
            ),
            (
                "Gita Wisdom",
                "Scripture-inspired rules surface reflective principles and practices.",
            ),
            (
                "Explainable Reflection",
                "The final output shows how the model, graph, and rules connected.",
            ),
        ]
    )
    st.markdown(
        f"""
<section class="scripture-panel">
  <div class="particle-field"></div>
  <div class="section-copy">
    <div class="eyebrow">Guided Analysis Path</div>
    <h1>Four lenses before the analysis</h1>
    <p class="body-copy">A modern AI flow presented like a reflective manuscript: detect, reason, retrieve wisdom, and explain.</p>
  </div>
  <div class="journey-grid">{card_html}</div>
</section>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    if st.button("Continue", type="primary", use_container_width=True):
        go_to_page("details")


def render_details_page() -> None:
    profile = st.session_state.get("user_profile", {})
    st.markdown(
        """
<section class="form-scroll">
  <div class="particle-field"></div>
  <div class="section-copy">
    <div class="eyebrow">Personalization Scroll</div>
    <h1>Share a little context</h1>
    <p class="body-copy">These details personalize displayed reflection text only. They are not used for medical diagnosis.</p>
  </div>
</section>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    with st.form("details_form"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input(
                "Age",
                min_value=10,
                max_value=100,
                value=int(profile.get("age", 25)) if str(profile.get("age", "")).isdigit() else 25,
                step=1,
            )
        with col2:
            gender_options = ["Prefer not to say", "Male", "Female", "Other"]
            gender = st.selectbox(
                "Gender",
                gender_options,
                index=gender_options.index(profile.get("gender", "Prefer not to say"))
                if profile.get("gender") in gender_options
                else 0,
            )
        state_options = ["Calm", "Confused", "Anxious", "Sad", "Angry", "Fearful", "Confident"]
        current_state = st.selectbox(
            "Current emotional state",
            state_options,
            index=state_options.index(profile.get("current_state", "Calm"))
            if profile.get("current_state") in state_options
            else 0,
        )
        trigger_context = st.text_area(
            "Optional situation/context",
            value=profile.get("trigger_context", ""),
            placeholder="What situation triggered this feeling?",
            height=120,
        )
        submitted = st.form_submit_button("Next", type="primary", use_container_width=True)
        if submitted:
            st.session_state.user_profile = {
                "age": age,
                "gender": gender,
                "current_state": current_state,
                "trigger_context": trigger_context,
            }
            go_to_page("transition")


def render_transition_page() -> None:
    st.markdown(
        """
<section class="scripture-hero">
  <div class="particle-field"></div>
  <div class="aura"></div>
  <div class="scripture-frame"></div>
  <div class="transition-copy">
    <div class="eyebrow">Stillness Before Reasoning</div>
    <h1 class="title-xl">Let the mind become still before the root is revealed.</h1>
    <p class="body-copy">The system will now listen, classify, reason through the graph, and return an explainable reflection.</p>
    <div class="scripture-scene">
      <div class="scroll-card"></div>
      <div class="guide-mark"></div>
    </div>
  </div>
</section>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    if st.button("Continue to Analysis", type="primary", use_container_width=True):
        go_to_page("chat_analysis")


def _run_backend_analysis(user_text: str) -> Dict[str, Any]:
    emotion_result = predict_emotion(user_text)
    emotion = emotion_result.get("emotion", "unknown")
    graph_result = get_reasoning_paths(emotion)
    recommendation_inputs = [emotion] + graph_result.get("related_concepts", [])
    recommendations = get_recommendations(recommendation_inputs)
    explanation = generate_explanation(emotion, graph_result.get("paths", []), recommendations)
    return {
        "user_text": user_text,
        "emotion_result": emotion_result,
        "graph_result": graph_result,
        "recommendations": recommendations,
        "explanation": explanation,
    }


def _profile_card(profile: Dict[str, Any]) -> str:
    trigger = _safe(profile.get("trigger_context") or "No situation/context shared.")
    return (
        '<div class="profile-card">'
        '<div class="eyebrow">Reflection Profile</div>'
        f'<h3>{_safe(profile.get("current_state", "Calm"))}</h3>'
        f'<p>Age: {_safe(profile.get("age", "N/A"))}</p>'
        f'<p>Gender: {_safe(profile.get("gender", "N/A"))}</p>'
        f'<p>Context: {trigger}</p>'
        '</div>'
    )


def _status_chips() -> None:
    chips = ["NLP", "Emotion Model", "Knowledge Graph", "Gita Rules", "Explainability"]
    html = "".join(f'<div class="status-chip">{chip}</div>' for chip in chips)
    st.markdown(f'<div class="chip-row">{html}</div>', unsafe_allow_html=True)


def _recommendation_cards(recommendations: List[Dict[str, Any]]) -> None:
    if not recommendations:
        st.info("No Gita wisdom recommendation was found for the detected graph concepts.")
        return
    cards = []
    for rec in recommendations:
        cards.append(
            '<div class="recommend-card">'
            f'<div class="eyebrow">{_safe(str(rec.get("concept", "")).replace("_", " ").title())}</div>'
            f'<h3>{_safe(rec.get("principle", "Principle"))}</h3>'
            f'<p><strong>Recommendation:</strong> {_safe(rec.get("recommendation", "N/A"))}</p>'
            f'<p><strong>Practical step:</strong> {_safe(rec.get("practical_step", "N/A"))}</p>'
            f'<p><strong>Reference:</strong> {_safe(rec.get("chapter_reference", "N/A"))}</p>'
            '</div>'
        )
    st.markdown(f'<div class="recommend-grid">{"".join(cards)}</div>', unsafe_allow_html=True)


def _chat_bubble(role: str, text: str, delay: str = "") -> None:
    safe_text = _safe(text).replace("\n", "<br>")
    st.markdown(
        f'<div class="chat-bubble {role} {delay}"><strong>{"You" if role == "user" else "Analyzer"}</strong><p>{safe_text}</p></div>',
        unsafe_allow_html=True,
    )


def _render_chat_result(result: Dict[str, Any]) -> None:
    _chat_bubble("user", result.get("user_text", ""))
    _chat_bubble("ai", "I detected the dominant emotional pattern.", "delay-1")
    display_emotion_probabilities(result["emotion_result"].get("probabilities", {}), result["emotion_result"].get("emotion", "unknown"))

    _chat_bubble("ai", "Now mapping this emotion into the root-cause graph.", "delay-2")
    st.markdown('<div class="graph-card">', unsafe_allow_html=True)
    if result["graph_result"].get("paths"):
        fig = draw_reasoning_graph(result["graph_result"].get("paths", [])[0])
        st.pyplot(fig)
        plt.close(fig)
    else:
        st.info("No graph path could be rendered.")
    st.markdown('</div>', unsafe_allow_html=True)

    _chat_bubble("ai", "A Gita-inspired reflective principle has been found.", "delay-3")
    _recommendation_cards(result.get("recommendations", []))

    final_text = str(result.get("explanation", "No explanation was generated."))
    _chat_bubble("ai", final_text, "delay-4")


def render_chat_analysis_page() -> None:
    profile = st.session_state.get("user_profile", {})
    st.markdown(
        f"""
<section class="chat-shell">
  <div class="particle-field"></div>
  <div class="chat-header">
    <div class="section-copy">
      <div class="eyebrow">AI Reflection Dashboard</div>
      <h1>Scripture-Inspired Analysis Console</h1>
      <p class="body-copy">Describe what you are feeling. The system will classify the pattern, reason through the graph, retrieve a Gita-inspired principle, and explain the result.</p>
    </div>
    {_profile_card(profile)}
  </div>
</section>
        """,
        unsafe_allow_html=True,
    )
    _status_chips()
    st.markdown('<div class="chat-panel">', unsafe_allow_html=True)
    with st.form("analysis_form"):
        user_text = st.text_area(
            "Describe what you are feeling or thinking right now",
            value=st.session_state.get("analysis_text", ""),
            placeholder="Describe what you are feeling or thinking right now...",
            height=155,
        )
        submitted = st.form_submit_button("Analyze", type="primary", use_container_width=True)

    if submitted:
        st.session_state.analysis_text = user_text
        if not user_text.strip():
            st.error("Please enter some text before analyzing.")
        else:
            with st.spinner("Listening, classifying, traversing the graph, and preparing a reflection..."):
                st.session_state.analysis_result = _run_backend_analysis(user_text)

    if st.session_state.get("analysis_result"):
        _render_chat_result(st.session_state.analysis_result)
        if st.button("Start New Reflection", use_container_width=True):
            st.session_state.analysis_result = None
            st.session_state.analysis_text = ""
            st.rerun()
    else:
        _chat_bubble("ai", "I am ready. Share a thought or feeling, and I will return an educational graph-based reflection.")

    st.markdown('</div>', unsafe_allow_html=True)
    st.caption(DISCLAIMER)
