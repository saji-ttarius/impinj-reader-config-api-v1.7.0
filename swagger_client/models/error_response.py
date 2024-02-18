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


class ErrorResponse(object):
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
        'message': 'str',
        'invalid_property_id': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'message': 'message',
        'invalid_property_id': 'invalidPropertyId',
        'detail': 'detail'
    }

    def __init__(self, message=None, invalid_property_id=None, detail=None, _configuration=None):  # noqa: E501
        """ErrorResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._message = None
        self._invalid_property_id = None
        self._detail = None
        self.discriminator = None

        self.message = message
        if invalid_property_id is not None:
            self.invalid_property_id = invalid_property_id
        if detail is not None:
            self.detail = detail

    @property
    def message(self):
        """Gets the message of this ErrorResponse.  # noqa: E501

        A message with information about the error.  # noqa: E501

        :return: The message of this ErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorResponse.

        A message with information about the error.  # noqa: E501

        :param message: The message of this ErrorResponse.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def invalid_property_id(self):
        """Gets the invalid_property_id of this ErrorResponse.  # noqa: E501

        A schema pointer to the invalid property of the request.  # noqa: E501

        :return: The invalid_property_id of this ErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._invalid_property_id

    @invalid_property_id.setter
    def invalid_property_id(self, invalid_property_id):
        """Sets the invalid_property_id of this ErrorResponse.

        A schema pointer to the invalid property of the request.  # noqa: E501

        :param invalid_property_id: The invalid_property_id of this ErrorResponse.  # noqa: E501
        :type: str
        """

        self._invalid_property_id = invalid_property_id

    @property
    def detail(self):
        """Gets the detail of this ErrorResponse.  # noqa: E501

        Additional details about the error.  # noqa: E501

        :return: The detail of this ErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ErrorResponse.

        Additional details about the error.  # noqa: E501

        :param detail: The detail of this ErrorResponse.  # noqa: E501
        :type: str
        """

        self._detail = detail

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
        if issubclass(ErrorResponse, dict):
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
        if not isinstance(other, ErrorResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorResponse):
            return True

        return self.to_dict() != other.to_dict()