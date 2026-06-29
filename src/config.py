import os

# Base directory setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODELS_DIR = os.path.join(BASE_DIR, "models")

# Data paths
DATASET_PATH = os.path.join(DATA_DIR, "emotion_dataset.csv")
GRAPH_JSON_PATH = os.path.join(DATA_DIR, "knowledge_graph.json")
GITA_JSON_PATH = os.path.join(DATA_DIR, "gita_principles.json")

# Model paths
VECTORIZER_PATH = os.path.join(MODELS_DIR, "tfidf_vectorizer.pkl")
MODEL_PATH = os.path.join(MODELS_DIR, "emotion_classifier.pkl")

# Frozen global labels
EMOTION_LABELS = [
    "fear",
    "anxiety",
    "anger",
    "sadness",
    "confidence",
    "confusion"
]

# Hugging Face Settings
USE_HUGGINGFACE = True  # Enabled as requested by user
HF_MODEL_NAME = "typeform/distilbert-base-uncased-mnli"

