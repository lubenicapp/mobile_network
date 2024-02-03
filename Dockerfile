FROM python:3.12-slim

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
EXPOSE 80

WORKDIR api/

COPY Pipfile Pipfile.lock ./

RUN pip3 install pipenv && \
    pipenv requirements > requirements.txt && \
    pip install -r requirements.txt

COPY ./app ./app
COPY ./data/ ./data
COPY ./test/ ./test
