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


class AntennaDisconnectedEvent(object):
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
        'antenna_port': 'AntennaPort'
    }

    attribute_map = {
        'antenna_port': 'antennaPort'
    }

    def __init__(self, antenna_port=None, _configuration=None):  # noqa: E501
        """AntennaDisconnectedEvent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._antenna_port = None
        self.discriminator = None

        self.antenna_port = antenna_port

    @property
    def antenna_port(self):
        """Gets the antenna_port of this AntennaDisconnectedEvent.  # noqa: E501


        :return: The antenna_port of this AntennaDisconnectedEvent.  # noqa: E501
        :rtype: AntennaPort
        """
        return self._antenna_port

    @antenna_port.setter
    def antenna_port(self, antenna_port):
        """Sets the antenna_port of this AntennaDisconnectedEvent.


        :param antenna_port: The antenna_port of this AntennaDisconnectedEvent.  # noqa: E501
        :type: AntennaPort
        """
        if self._configuration.client_side_validation and antenna_port is None:
            raise ValueError("Invalid value for `antenna_port`, must not be `None`")  # noqa: E501

        self._antenna_port = antenna_port

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
        if issubclass(AntennaDisconnectedEvent, dict):
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
        if not isinstance(other, AntennaDisconnectedEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AntennaDisconnectedEvent):
            return True

        return self.to_dict() != other.to_dict()
