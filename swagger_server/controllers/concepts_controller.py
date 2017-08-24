import connexion
from swagger_server.models.concept import Concept
from swagger_server.models.concept_detail import ConceptDetail
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from swagger_server.database import neo4j
from swagger_server.models.conceptsconcept_id_details import ConceptsconceptIdDetails


def get_concept_details(conceptId):
    """
    get_concept_details
    Retrieves details for a specified concepts in the system, as specified by a (url-encoded) CURIE identifier of a concept known the given knowledge source.
    :param conceptId: (url-encoded) CURIE identifier of concept of interest
    :type conceptId: str

    :rtype: List[ConceptDetail]
    """

    q = """
    MATCH (protein:Protein {stringId: {conceptId}})
    RETURN
        protein.stringId as stringId,
        protein.alias as alias,
        protein.source as source
    LIMIT 1
    """

    results = neo4j.run(query=q, param={"conceptId" : conceptId})

    details = []
    for d in results:
        concept_detail = ConceptDetail()
        concept_detail.id = d["stringId"]
        concept_detail.name = d["alias"]
        concept_detail.semantic_group = "CHEM"
        concept_detail.details = [ConceptsconceptIdDetails(tag="source", value=d["source"])]

        details.append(concept_detail)

    return details


def get_concepts(keywords, semgroups=None, pageNumber=None, pageSize=None):
    """
    get_concepts
    Retrieves a (paged) list of concepts in the system
    :param keywords: a (urlencoded) space delimited set of keywords or substrings against which to match concept names and synonyms
    :type keywords: str
    :param semgroups: a (url-encoded) space-delimited set of semantic groups (specified as codes CHEM, GENE, ANAT, etc.) to which to constrain concepts matched by the main keyword search (see [SemGroups](https://metamap.nlm.nih.gov/Docs/SemGroups_2013.txt) for the full list of codes)
    :type semgroups: str
    :param pageNumber: (1-based) number of the page to be returned in a paged set of query results
    :type pageNumber: int
    :param pageSize: number of concepts per page to be returned in a paged set of query results
    :type pageSize: int

    :rtype: List[Concept]
    """

    q = """
    MATCH (protein:Protein)
    WITH
        SIZE(FILTER(x IN {filter} WHERE LOWER(protein.alias) CONTAINS LOWER(x))) AS num_matches,
        SIZE((protein)-[:ACTION]-()) as degree,
        protein as protein
    WHERE num_matches > 0 AND degree > 0
    RETURN
        protein.stringId as stringId,
        protein.alias as alias,
        protein.source as source
    ORDER BY num_matches DESC, degree DESC
    SKIP ({pageNumber} - 1) * {pageSize} LIMIT {pageSize}
    """

    results = neo4j.run(
        query=q,
        param={
            "pageNumber" : pageNumber if pageNumber != None and pageNumber > 0 else 1,
            "pageSize"   : pageSize if pageSize != None and pageSize > 0 else 10,
            "filter"     : keywords.split()
        }
    )

    return [Concept(id=d["stringId"], name=d["alias"], semantic_group="CHEM") for d in results]
