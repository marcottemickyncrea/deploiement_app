import spacy

def predict_model(text: str) -> list:
    nlp = spacy.load("model-last")
    doc = nlp(text)
    response = []
    for ent in doc.ents:
        response.append({ent.text: ent.label_})

    return {'response': response}
