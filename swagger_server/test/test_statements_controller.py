# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.statement import Statement
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestStatementsController(BaseTestCase):
    """ StatementsController integration test stubs """

    def test_get_statements(self):
        """
        Test case for get_statements

        
        """
        query_string = [('c', 'c_example'),
                        ('pageNumber', 56),
                        ('pageSize', 56),
                        ('keywords', 'keywords_example'),
                        ('semgroups', 'semgroups_example')]
        response = self.client.open('/api/statements',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
