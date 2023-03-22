import spacy
from spacy.training.example import Example

nlp = spacy.load("en_core_web_sm")
textcat = nlp.add_pipe("textcat_multilabel")
labels = ["enrollment", "schedule", "course", "fee"]  # define the set of labels
for label in labels:
    textcat.add_label(label)

def train_textcat(texts, categories):
    train_data = []
    for text, category in zip(texts, categories):
        doc = nlp.make_doc(text)
        cats = {label: label == category for label in labels}
        train_data.append(Example.from_dict(doc, {"cats": cats}))
    optimizer = nlp.begin_training()
    for i in range(15):
        losses = {}
        for batch in spacy.util.minibatch(train_data, size=8):
            nlp.update(batch, sgd=optimizer, losses=losses)
        print(losses)

def predict_category(text):
    doc = nlp(text)
    label_scores = doc.cats
    print(label_scores)
    predicted_label = max(label_scores, key=label_scores.get)
    return predicted_label

texts = ["When is the enrollment?", "What is the deadline for enrollment?",
         "How can I enroll?", "What are the available strands?"]
categories = ["enrollment", "enrollment", "enrollment", "course"]
train_textcat(texts, categories)

text = "When is the enrollment?"
predicted_category = predict_category(text)
print(predicted_category)

text = "How can i enroll?"
predicted_category = predict_category(text)
print(predicted_category)
