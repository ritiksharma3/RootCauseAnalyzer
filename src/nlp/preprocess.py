import re

def preprocess_text(text: str) -> str:
    """
    Cleans raw user input by converting it to lowercase, removing punctuation, 
    and stripping extra whitespaces.
    """
    if not isinstance(text, str):
        return ""
    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Strip whitespace
    text = text.strip()
    return text
