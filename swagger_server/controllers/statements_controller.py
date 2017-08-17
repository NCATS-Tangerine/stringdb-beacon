import connexion
from swagger_server.models.statement import Statement
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from flask import jsonify

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
    return jsonify(c)
