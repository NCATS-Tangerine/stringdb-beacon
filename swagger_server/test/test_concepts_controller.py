# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.concept import Concept
from swagger_server.models.concept_detail import ConceptDetail
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestConceptsController(BaseTestCase):
    """ ConceptsController integration test stubs """

    def test_get_concept_details(self):
        """
        Test case for get_concept_details

        
        """
        response = self.client.open('/api/concepts/{conceptId}'.format(conceptId='conceptId_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_concepts(self):
        """
        Test case for get_concepts

        
        """
        query_string = [('keywords', 'keywords_example'),
                        ('semgroups', 'semgroups_example'),
                        ('pageNumber', 56),
                        ('pageSize', 56)]
        response = self.client.open('/api/concepts',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
