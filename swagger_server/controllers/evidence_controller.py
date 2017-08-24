import connexion
from swagger_server.models.evidence import Evidence
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_evidence(statementId, keywords=None, pageNumber=None, pageSize=None):
    """
    get_evidence
    Retrieves a (paged) list of annotations cited as evidence for a specified concept-relationship statement
    :param statementId: (url-encoded) CURIE identifier of the concept-relationship statement (\&quot;assertion\&quot;, \&quot;claim\&quot;) for which associated evidence is sought
    :type statementId: str
    :param keywords: (url-encoded, space delimited) keyword filter to apply against the label field of the annotation
    :type keywords: str
    :param pageNumber: (1-based) number of the page to be returned in a paged set of query results
    :type pageNumber: int
    :param pageSize: number of cited references per page to be returned in a paged set of query results
    :type pageSize: int

    :rtype: List[Evidence]
    """
    return [Evidence(label='string-db says so!', id='stringdb:0', date="0000-00-00")]
