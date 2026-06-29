# AI-powered Psychological Root Cause Analyzer

An offline, explainable AI system designed as an educational and reflective tool. It analyzes a user's written feelings, predicts the dominant emotion using supervised machine learning, traverses a psychological/philosophical knowledge graph to find root causes, and recommends practical Bhagavad Gita-inspired actions.

---

## ⚠️ Disclaimer
This system is an **educational and reflective tool** only. It does **not** provide clinical diagnosis or medical/psychological treatment. If you are experiencing mental health challenges, please seek support from a licensed professional.

---

## Architecture Overview
The project is divided into four distinct modules:
1. **NLP / Emotion Classifier**: Preprocesses text and uses TF-IDF + Logistic Regression to classify the text into one of six emotions (`fear`, `anxiety`, `anger`, `sadness`, `confidence`, `confusion`).
2. **Knowledge Graph**: Builds a directed graph mapping emotions to psychological concepts (root causes and mental patterns) and performs Breadth-First Search (BFS) to retrieve reasoning paths.
3. **Recommendation Engine & Explanation**: Matches concepts to Gita principles and generates a readable explanation.
4. **Streamlit UI**: Coordinates inputs, displays metrics, visualizes the reasoning graph, and outputs explanations.

---

## Folder Structure
```
psych_root_cause_analyzer/
|-- app.py
|-- requirements.txt
|-- README.md
|-- data/
|   |-- emotion_dataset.csv
|   |-- knowledge_graph.json
|   |-- gita_principles.json
|-- models/
|   |-- tfidf_vectorizer.pkl
|   |-- emotion_classifier.pkl
|-- src/
|   |-- __init__.py
|   |-- config.py
|   |-- nlp/
|   |   |-- preprocess.py
|   |-- ml/
|   |   |-- train_model.py
|   |   |-- predict_emotion.py
|   |-- graph/
|   |   |-- graph_builder.py
|   |   |-- graph_traversal.py
|   |-- recommendation/
|   |   |-- recommendation_engine.py
|   |-- explainability/
|   |   |-- explanation_generator.py
|   |-- ui/
|       |-- display_graph.py
|       |-- display_results.py
|-- tests/
    |-- test_predict_emotion.py
    |-- test_graph_traversal.py
    |-- test_recommendation_engine.py
```

---

## Setup & Running
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Train the model:
   ```bash
   python src/ml/train_model.py
   ```
3. Run unit tests:
   ```bash
   pytest
   ```
4. Launch the Streamlit application:
   ```bash
   streamlit run app.py
   ```
