from fastapi import FastAPI
import uvicorn
import utils

app = FastAPI(
    title="Spacy Science")

@app.post("/predict")
def post_predict(response: dict):
    response = utils.predict_model(response['text'])
    return response

if __name__=='__main__':
    uvicorn.run(app, host='0.0.0.0', port=4000)
