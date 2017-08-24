FROM ubuntu:latest

WORKDIR /home

RUN apt-get update && apt-get install -y python3 python3-pip git

RUN pip3 install --upgrade pip && \
    pip3 install -U setuptools && \
    pip3 install neo4j-driver

COPY . string-db

RUN pip3 install -e string-db/extras/connexion/ && \
    pip3 install -r string-db/requirements.txt

WORKDIR /home/string-db

ENTRYPOINT ["python3", "-m", "swagger_server"]
