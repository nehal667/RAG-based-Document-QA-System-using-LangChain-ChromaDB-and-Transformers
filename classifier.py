# classifier.py
from transformers import pipeline

class SectionClassifier:
    def __init__(self):
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    def classify(self, text: str) -> str:
        labels = ["Introduction", "Methodology", "Results", "Discussion", "Conclusion", "References"]
        result = self.classifier(text, candidate_labels=labels)
        return result["labels"][0]  # Return the top predicted label
