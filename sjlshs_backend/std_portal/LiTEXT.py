import spacy
from spacy.training.example import Example


nlp = spacy.load("en_core_web_sm")
textcat = nlp.add_pipe("textcat_multilabel")
labels = ["enrollment", "schedule", "course", 
          "tvl_strands","fee", "organizations",
          "school_contact",]  # define the set of labels
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

texts = ["When is the enrollment?", "When is the deadline for enrollment?",
         "How can I enroll?",
        "What are the available strands?", "Is the stem strand available?",
         "Is the humss strand available?", "Is the tvl track available?", "Is the abm track available?",
         "What are the available tvl strands available?", "Is ICT available?",
         "What are the organizations I can join here?",
         "How much is the tuition fee?",
         "Where can I find the school's contact details?", "What is the address of the school?",
         "What is the email address of the school?",
         "What are the enrollment requirements?", "What are the registration requirements?",
         
         ]

categories = ["enrollment", "enrollment", "enrollment", 
              "course", "course", "course", "course", 
              "course", "tvl_strands", "tvl_strands", "organizations",
              "fee", "school_contact", "school_contact", "school_contact",
              "enrollment", "enrollment", 

              ]
train_textcat(texts, categories)

text = "When is the enrollment?"
predicted_category = predict_category(text)
print(predicted_category)

text = "How can i enroll?"
predicted_category = predict_category(text)
print(predicted_category)

nlp.to_disk('litext')
