import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

responses = {
    "when to enroll": {"spring": "January 1 - April 30", "summer": "May 1 - August 31", "fall": "September 1 - December 31"},
    "how to enroll": "You can enroll online or in person. Please visit our website for more information.",
    "where to enroll": "You can enroll at our main campus or at any of our satellite locations. Please visit our website for more information."
}

patterns = [
    [{"LOWER": "when"}, {"LOWER": "to"}, {"LOWER": "enroll"}],
    [{"LOWER": "how"}, {"LOWER": "to"}, {"LOWER": "enroll"}],
    [{"LOWER": "where"}, {"LOWER": "to"}, {"LOWER": "enroll"}]
]

for pattern in patterns:
    matcher.add("Enrollment", [pattern])

def get_response(doc):
    matches = matcher(doc)
    if matches:
        match_id, start, end = matches[0]
        query = doc[start:end].text
        if query in responses:
            return responses[query]
    return None

doc = nlp("Where can i enroll??")
response = get_response(doc)
if response:
    print(response)
else:
    print("Sorry, I don't know the answer.")