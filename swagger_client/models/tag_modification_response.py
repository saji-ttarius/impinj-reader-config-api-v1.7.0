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


class TagModificationResponse(object):
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
        'response': 'str'
    }

    attribute_map = {
        'response': 'response'
    }

    def __init__(self, response=None, _configuration=None):  # noqa: E501
        """TagModificationResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._response = None
        self.discriminator = None

        self.response = response

    @property
    def response(self):
        """Gets the response of this TagModificationResponse.  # noqa: E501


        :return: The response of this TagModificationResponse.  # noqa: E501
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this TagModificationResponse.


        :param response: The response of this TagModificationResponse.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and response is None:
            raise ValueError("Invalid value for `response`, must not be `None`")  # noqa: E501
        allowed_values = ["success", "tag-memory-overrun-error", "tag-memory-locked-error", "insufficient-power", "nonspecific-tag-error", "no-response-from-tag", "nonspecific-reader-error", "not-attempted", "failure"]  # noqa: E501
        if (self._configuration.client_side_validation and
                response not in allowed_values):
            raise ValueError(
                "Invalid value for `response` ({0}), must be one of {1}"  # noqa: E501
                .format(response, allowed_values)
            )

        self._response = response

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
        if issubclass(TagModificationResponse, dict):
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
        if not isinstance(other, TagModificationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TagModificationResponse):
            return True

        return self.to_dict() != other.to_dict()
