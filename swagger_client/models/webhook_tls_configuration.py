# coding: utf-8

"""
    Impinj Reader Configuration REST API

    This API provides an interface for configuring RFID operations and reporting streams on Impinj Readers as well as updating Impinj Reader firmware and configuring system settings.  When retrieved from a reader, this OpenAPI Document is dynamically updated based on the capabilities of the reader. See the '/openapi.json' path.   # noqa: E501

    OpenAPI spec version: 1.7.0
    Contact: developer-feedback@impinj.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class WebhookTlsConfiguration(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'verify_server': 'bool'
    }

    attribute_map = {
        'verify_server': 'verifyServer'
    }

    def __init__(self, verify_server=True, _configuration=None):  # noqa: E501
        """WebhookTlsConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._verify_server = None
        self.discriminator = None

        if verify_server is not None:
            self.verify_server = verify_server

    @property
    def verify_server(self):
        """Gets the verify_server of this WebhookTlsConfiguration.  # noqa: E501

        If true, the authenticity and hostname of the TLS/SSL certificate provided by the server will be verified. Setting to false is not recommended in production environments and is not secure, but it may be useful for development environments with self-signed or otherwise invalid certificates.   # noqa: E501

        :return: The verify_server of this WebhookTlsConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._verify_server

    @verify_server.setter
    def verify_server(self, verify_server):
        """Sets the verify_server of this WebhookTlsConfiguration.

        If true, the authenticity and hostname of the TLS/SSL certificate provided by the server will be verified. Setting to false is not recommended in production environments and is not secure, but it may be useful for development environments with self-signed or otherwise invalid certificates.   # noqa: E501

        :param verify_server: The verify_server of this WebhookTlsConfiguration.  # noqa: E501
        :type: bool
        """

        self._verify_server = verify_server

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(WebhookTlsConfiguration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WebhookTlsConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookTlsConfiguration):
            return True

        return self.to_dict() != other.to_dict()
