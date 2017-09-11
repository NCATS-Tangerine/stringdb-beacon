FROM python:3

RUN pip install neo4j-driver

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY swagger_server /home/swagger_server

WORKDIR /home

ENTRYPOINT ["python3", "-m", "swagger_server"]
