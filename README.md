# AI-powered Psychological Root Cause Analyzer

An Explainable AI project that analyzes a user's emotional text input, identifies the dominant emotion using Machine Learning, discovers possible psychological root causes through a Knowledge Graph, and provides reflective recommendations inspired by the Bhagavad Gita.

> Educational project only.
> This application is **NOT** intended for clinical diagnosis or mental health treatment.

---

## Features

- Emotion Classification using TF-IDF + Logistic Regression
- Explainable AI Pipeline
- Knowledge Graph Traversal
- Root Cause Analysis
- Rule-based Recommendation Engine
- Bhagavad Gita Inspired Principles
- Interactive Streamlit Dashboard
- Fully Offline (No APIs)
- Modular Python Architecture

---

## Technology Stack

- Python 3.11+
- Streamlit
- Scikit-learn
- NetworkX
- Pandas
- NumPy
- Joblib
- Matplotlib

---

## Project Architecture

User Input

↓

Text Preprocessing

↓

TF-IDF Vectorization

↓

Logistic Regression Emotion Classifier

↓

Knowledge Graph Traversal

↓

Root Cause Detection

↓

Recommendation Engine

↓

Explainability Module

↓

Streamlit Dashboard

---

## Folder Structure

```text
src/
ml/
graph/
recommendation/
explainability/
ui/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/username/psychological-root-cause-analyzer.git

cd psychological-root-cause-analyzer
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Workflow

1. Enter emotional text.
2. Detect dominant emotion.
3. Traverse Knowledge Graph.
4. Discover possible root causes.
5. Generate recommendations.
6. Display explainable reasoning.

---

## Team Structure

### Member 1

Machine Learning

### Member 2

Knowledge Graph

### Member 3

Recommendation Engine

### Member 4

Streamlit Integration

---

## Future Improvements

- BERT-based emotion classification
- Multi-language support
- Interactive graph visualization
- Better explanation generation
- Larger emotion dataset

---

## Disclaimer

This project is intended for educational and research purposes only.

It should never replace professional psychological or medical advice.

---

## License

MIT License
