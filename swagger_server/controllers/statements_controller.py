import connexion
from swagger_server.models.statement import Statement
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from swagger_server.models.statement_subject import StatementSubject
from swagger_server.models.statement_object import StatementObject
from swagger_server.models.statement_predicate import StatementPredicate

from swagger_server.database import neo4j

def get_statements(c, pageNumber=None, pageSize=None, keywords=None, semgroups=None):
    """
    get_statements
    Given a list of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of exactly matching concepts, retrieves a paged list of concept-relations where either the subject or object concept matches at least one concept in the input list
    :param c: set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of exactly matching concepts to be used in a search for associated concept-relation statements
    :type c: List[str]
    :param pageNumber: (1-based) number of the page to be returned in a paged set of query results
    :type pageNumber: int
    :param pageSize: number of concepts per page to be returned in a paged set of query results
    :type pageSize: int
    :param keywords: a (url-encoded, space-delimited) string of keywords or substrings against which to match the subject, predicate or object names of the set of concept-relations matched by any of the input exact matching concepts
    :type keywords: str
    :param semgroups: a (url-encoded, space-delimited) string of semantic groups (specified as codes CHEM, GENE, ANAT, etc.) to which to constrain the subject or object concepts associated with the query seed concept (see [SemGroups](https://metamap.nlm.nih.gov/Docs/SemGroups_2013.txt) for the full list of codes)
    :type semgroups: str

    :rtype: List[Statement]
    """

    query = """
    MATCH (a:Protein)-[r:ACTION]-(b:Protein)
    WHERE
        (NOT a.alias IS NULL) AND
        (NOT b.alias IS NULL) AND
        ANY (x in {conceptIds} WHERE
            LOWER(a.stringId) = LOWER(x)
            OR
            LOWER(a.stringId) = LOWER(x)
        )
    RETURN
        a.stringId as id_a,
        a.alias as alias_a,
        b.stringId as id_b,
        b.alias as alias_b,
        r.mode as relation,
        ID(r) as relation_id
    SKIP ({pageNumber} - 1) * {pageSize} LIMIT {pageSize}
    """

    results = neo4j.run(
        query,
        {
            "pageNumber" : pageNumber if pageNumber != None and pageNumber > 0 else 1,
            "pageSize"   : pageSize if pageSize != None and pageSize > 0 else 10,
            "conceptIds" : c if c != None else []
        }
    )

    statements = []

    for row in results:
        statement = Statement()
        statement_object = StatementObject()
        statement_subject = StatementSubject()
        statement_predicate = StatementPredicate()

        statement_object.name = row["alias_a"]
        statement_object.id = row["id_a"]

        statement_subject.name = row["alias_b"]
        statement_subject.id = row["id_b"]

        statement_predicate.name = row["relation"]
        statement_predicate.id = str(row["relation_id"])

        statement.subject = statement_subject
        statement.object = statement_object
        statement.predicate = statement_predicate
        statement.id = str(row["relation_id"])

        statements.append(statement)


    return statements
