FROM continuumio/miniconda3

WORKDIR /home/app

RUN pip install -r requirements.txt

COPY . .

CMD streamlit run app.py --server.port $PORT