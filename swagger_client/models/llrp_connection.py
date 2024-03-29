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


class LlrpConnection(object):
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
        'status': 'str',
        'peer_address': 'str'
    }

    attribute_map = {
        'status': 'status',
        'peer_address': 'peerAddress'
    }

    def __init__(self, status=None, peer_address=None, _configuration=None):  # noqa: E501
        """LlrpConnection - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status = None
        self._peer_address = None
        self.discriminator = None

        self.status = status
        if peer_address is not None:
            self.peer_address = peer_address

    @property
    def status(self):
        """Gets the status of this LlrpConnection.  # noqa: E501

        The status of the LLRP connection.  # noqa: E501

        :return: The status of this LlrpConnection.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LlrpConnection.

        The status of the LLRP connection.  # noqa: E501

        :param status: The status of this LlrpConnection.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["disabled", "connected", "disconnected"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def peer_address(self):
        """Gets the peer_address of this LlrpConnection.  # noqa: E501

        IP address of the connected device. Will contain either an IPv4 address in dot-decimal format, or an IPv6 address compliant with RFC-5952. Will only be present if status is connected.   # noqa: E501

        :return: The peer_address of this LlrpConnection.  # noqa: E501
        :rtype: str
        """
        return self._peer_address

    @peer_address.setter
    def peer_address(self, peer_address):
        """Sets the peer_address of this LlrpConnection.

        IP address of the connected device. Will contain either an IPv4 address in dot-decimal format, or an IPv6 address compliant with RFC-5952. Will only be present if status is connected.   # noqa: E501

        :param peer_address: The peer_address of this LlrpConnection.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                peer_address is not None and len(peer_address) > 64):
            raise ValueError("Invalid value for `peer_address`, length must be less than or equal to `64`")  # noqa: E501

        self._peer_address = peer_address

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
        if issubclass(LlrpConnection, dict):
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
        if not isinstance(other, LlrpConnection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LlrpConnection):
            return True

        return self.to_dict() != other.to_dict()
