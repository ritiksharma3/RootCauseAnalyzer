import os
import pickle
from src.config import VECTORIZER_PATH, MODEL_PATH, EMOTION_LABELS, USE_HUGGINGFACE, HF_MODEL_NAME
from src.nlp.preprocess import preprocess_text

# Module-level cache for models
_vectorizer = None
_classifier = None
_hf_pipeline = None

def _load_models():
    """
    Lazily loads the classifier. Uses Hugging Face zero-shot pipeline if configured,
    otherwise loads the local TF-IDF and Logistic Regression models.
    """
    global _vectorizer, _classifier, _hf_pipeline
    
    if USE_HUGGINGFACE:
        if _hf_pipeline is None:
            try:
                from transformers import pipeline
                print(f"Loading Hugging Face zero-shot classification pipeline: {HF_MODEL_NAME}...")
                _hf_pipeline = pipeline("zero-shot-classification", model=HF_MODEL_NAME)
                print("Hugging Face model loaded successfully.")
            except ImportError:
                print("Warning: transformers/torch not installed. Falling back to local pickle models...")
                # Temporarily toggle off to attempt loading pickles
                _load_pickle_models()
    else:
        _load_pickle_models()

def _load_pickle_models():
    """
    Loads local TF-IDF vectorizer and Logistic Regression classifier pickles.
    """
    global _vectorizer, _classifier
    if _vectorizer is None or _classifier is None:
        if not os.path.exists(VECTORIZER_PATH) or not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                "Model files are missing. Please run `python src/ml/train_model.py` first to train the classifier."
            )
        with open(VECTORIZER_PATH, 'rb') as f:
            _vectorizer = pickle.load(f)
        with open(MODEL_PATH, 'rb') as f:
            _classifier = pickle.load(f)

def predict_emotion(text: str) -> dict:
    """
    Predicts the dominant emotion and probabilities from raw text.
    Supports Hugging Face zero-shot classification or TF-IDF + Logistic Regression.
    
    Input:
        text: str
    Output:
        dict: {
            "emotion": str,
            "confidence": float,
            "probabilities": {emotion: float, ...}
        }
    """
    _load_models()
    cleaned = preprocess_text(text)
    
    # Handle empty text input gracefully
    if not cleaned:
        probs = {label: round(1.0 / len(EMOTION_LABELS), 4) for label in EMOTION_LABELS}
        return {
            "emotion": "confusion",  # Default baseline choice
            "confidence": probs["confusion"],
            "probabilities": probs
        }
        
    # Run Hugging Face zero-shot classification if pipeline is loaded
    if _hf_pipeline is not None:
        result = _hf_pipeline(text, candidate_labels=EMOTION_LABELS)
        labels = result['labels']
        scores = result['scores']
        
        probs_dict = {label: float(score) for label, score in zip(labels, scores)}
        
        # Ensure all EMOTION_LABELS are represented
        for label in EMOTION_LABELS:
            if label not in probs_dict:
                probs_dict[label] = 0.0
                
        dominant_emotion = max(probs_dict, key=probs_dict.get)
        confidence = probs_dict[dominant_emotion]
        
        return {
            "emotion": dominant_emotion,
            "confidence": round(confidence, 4),
            "probabilities": {k: round(v, 4) for k, v in probs_dict.items()}
        }
    else:
        # Run local Logistic Regression classifier
        vec = _vectorizer.transform([cleaned])
        probs_array = _classifier.predict_proba(vec)[0]
        classes = _classifier.classes_
        
        # Map classes to their probabilities
        probs_dict = {str(c): float(p) for c, p in zip(classes, probs_array)}
        
        # Ensure all EMOTION_LABELS are represented
        for label in EMOTION_LABELS:
            if label not in probs_dict:
                probs_dict[label] = 0.0
                
        # Find the dominant emotion
        dominant_emotion = max(probs_dict, key=probs_dict.get)
        confidence = probs_dict[dominant_emotion]
        
        return {
            "emotion": dominant_emotion,
            "confidence": round(confidence, 4),
            "probabilities": {k: round(v, 4) for k, v in probs_dict.items()}
        }

if __name__ == "__main__":
    # Test execution
    try:
        res = predict_emotion("I feel nervous and scared")
        print("Prediction result:")
        print(res)
    except Exception as e:
        print("Could not run predict_emotion:", e)
