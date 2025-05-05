from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

text = "This paper describes the evaluation methods used in our experiment."
labels = ["Introduction", "Methodology", "Results", "Conclusion"]

result = classifier(text, labels)

print(result)
