# stringdb-beacon

Knowledge Beacon Wrapper for the StringDb resource (https://string-db.org/)

## Overview
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses a modified version of the [Connexion](https://github.com/zalando/connexion) library on top of Flask. Take a look at `/extras/connexion`.

Take a look at the `configfile` to set important application parameters.

## Setting up the Neo4j Database

This application uses a [Neo4j](https://neo4j.com/) database. Once you've [downloaded](https://neo4j.com/download/) and installed Neo4j, you can use a cypher script located at `extras/neo4j/load.cql` to load action and alias data for *Homo sapiens*. But first you need to download data from string-db.

String-db hosts its database at https://string-db.org/cgi/download.pl. You can get subsets of the database by selecting a species, so far we have only been using *Homo sapiens*. There is a python script `extras/neo4j/download_stringdb_data.py` that can be used to download the data for *Homo sapiens*, unzip it and format it properly so that it can be loaded into the Neo4j database. This script must be run with python3, in the terminal run `python --version` to check your version.

Supposing that you have installed Neo4j into a directory named `neo4j`, you place the resulting .txt files in `neo4j/import/`. The Neo4j shell will look in this directory when trying to load the files.

Next, execute the Neo4j shell with the parameter `--file <path to load.cql>`. Supposing that you have installed neo4j in the same directory into which you cloned the string-db beacon, on Linux you might do:

```
./neo4j/bin/neo4j-shell --file string-db/extras/neo4j/load.cql
```

This will then run the `load.cql` script and import the data into your database. It may be quite slow as there is a lot of data. If you are trying to load data for species other than *Homo sapiens*, be sure to modify the number that prefixes the file name in `load.cql`. The number 9606 represents *Homo sapiens* in the string-db data.

## Quickstart with Docker

The neo4j database must be running, make sure the `configfile` is set up properly.

After the database is running and the `configfile` is set up properly, you can use [Docker](https://www.docker.com/) to run the application. Linux users can install Docker through a shell script available online:

```shell
wget https://get.docker.com -O install.sh
sh install.sh
```

Then with Docker installed, you can build an image from the `Dockerfile` provided in the main directory of this project.

```shell
cd string-db
docker build -t ncats:stringdb .
docker run --net=host ncats:stringdb
```

Now open your browser to here: http://localhost:8080/api/ui/

The Swagger definition is here: http://localhost:8080/api/swagger.json

## Notes

This beacon is a work in progress. Here are a few points that still need to be addressed
- So far the evidence and exactmatches API are not implemented.
- I have only been using data for *Homo sapiens*. We should also include mouse, rat, yeast, c. elegans, drosphila, and zebrafish species as well, to complement monarch biolink.
- I have only been using data for protein aliases and actions. Once we introduce other species we will also need to use `species.v10.5.txt` which is available in the download section of string-db. Even so, these are only three out of the many data files offered by string-db. Someone who is more familiar with the data should go through all of the data files and build up a better data model.
