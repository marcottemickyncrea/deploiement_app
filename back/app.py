from fastapi import FastAPI
import uvicorn
from utils import *

app = FastAPI(
    title="Spacy Science")

@app.post("/predict")
def post_predict(text: str):
    response = predict_model(text)
    return {'response': response}

if __name__=='__main__':
    uvicorn.run(app, host='0.0.0.0', port=4000)
