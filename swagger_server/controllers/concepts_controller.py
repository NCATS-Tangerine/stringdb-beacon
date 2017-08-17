import connexion
from swagger_server.models.concept import Concept
from swagger_server.models.concept_detail import ConceptDetail
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_concept_details(conceptId):
    """
    get_concept_details
    Retrieves details for a specified concepts in the system, as specified by a (url-encoded) CURIE identifier of a concept known the given knowledge source. 
    :param conceptId: (url-encoded) CURIE identifier of concept of interest
    :type conceptId: str

    :rtype: List[ConceptDetail]
    """
    return 'do some magic!'


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
    return 'do some magic!'
