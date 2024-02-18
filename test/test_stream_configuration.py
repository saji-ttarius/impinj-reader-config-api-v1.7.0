# coding: utf-8

"""
    Impinj Reader Configuration REST API

    This API provides an interface for configuring RFID operations and reporting streams on Impinj Readers as well as updating Impinj Reader firmware and configuring system settings.  When retrieved from a reader, this OpenAPI Document is dynamically updated based on the capabilities of the reader. See the '/openapi.json' path.   # noqa: E501

    OpenAPI spec version: 1.7.0
    Contact: developer-feedback@impinj.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.stream_configuration import StreamConfiguration  # noqa: E501
from swagger_client.rest import ApiException


class TestStreamConfiguration(unittest.TestCase):
    """StreamConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStreamConfiguration(self):
        """Test StreamConfiguration"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.stream_configuration.StreamConfiguration()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
