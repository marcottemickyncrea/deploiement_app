import spacy
import os

def predict_model(text: str) -> list:
    repertoire_actuel = os.getcwd()
    model = os.path.join(repertoire_actuel, 'model-last')
    nlp = spacy.load(model)
    doc = nlp(text)
    response = []
    for ent in doc.ents:
        response.append({ent.text: ent.label_})

    return {'response': response}
