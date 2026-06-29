import os
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

from src.config import DATASET_PATH, VECTORIZER_PATH, MODEL_PATH, MODELS_DIR
from src.nlp.preprocess import preprocess_text

def train_and_evaluate():
    """
    Trains TF-IDF vectorizer and Logistic Regression classifier on the labeled CSV dataset,
    evaluates performance, and serializes the pipeline models.
    """
    print(f"Loading dataset from: {DATASET_PATH}")
    if not os.path.exists(DATASET_PATH):
        raise FileNotFoundError(f"Dataset not found at {DATASET_PATH}")
        
    df = pd.read_csv(DATASET_PATH)
    
    # Preprocess text
    print("Preprocessing training text...")
    df['cleaned_text'] = df['text'].apply(preprocess_text)
    
    X = df['cleaned_text']
    y = df['emotion']
    
    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    print("Fitting TF-IDF Vectorizer...")
    X_vectorized = vectorizer.fit_transform(X)
    
    # Initialize and train Logistic Regression
    print("Training Logistic Regression classifier...")
    classifier = LogisticRegression(max_iter=1000, random_state=42)
    classifier.fit(X_vectorized, y)
    
    # Predict and evaluate on the training set (since it's a seed dataset)
    y_pred = classifier.predict(X_vectorized)
    acc = accuracy_score(y, y_pred)
    print(f"Training Accuracy: {acc:.4f}")
    print("\nClassification Report:")
    print(classification_report(y, y_pred))
    
    # Ensure models directory exists
    os.makedirs(MODELS_DIR, exist_ok=True)
    
    # Save the vectorizer and classifier
    print(f"Saving vectorizer to {VECTORIZER_PATH}")
    with open(VECTORIZER_PATH, 'wb') as f:
        pickle.dump(vectorizer, f)
        
    print(f"Saving model to {MODEL_PATH}")
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(classifier, f)
        
    print("Training complete successfully!")

if __name__ == "__main__":
    train_and_evaluate()
