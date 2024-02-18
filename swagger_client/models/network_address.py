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


class NetworkAddress(object):
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
        'protocol': 'NetworkProtocol',
        'address_mode': 'str',
        'address': 'str',
        'prefix': 'int',
        'gateway': 'str'
    }

    attribute_map = {
        'protocol': 'protocol',
        'address_mode': 'addressMode',
        'address': 'address',
        'prefix': 'prefix',
        'gateway': 'gateway'
    }

    def __init__(self, protocol=None, address_mode=None, address=None, prefix=None, gateway=None, _configuration=None):  # noqa: E501
        """NetworkAddress - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._protocol = None
        self._address_mode = None
        self._address = None
        self._prefix = None
        self._gateway = None
        self.discriminator = None

        self.protocol = protocol
        self.address_mode = address_mode
        if address is not None:
            self.address = address
        if prefix is not None:
            self.prefix = prefix
        if gateway is not None:
            self.gateway = gateway

    @property
    def protocol(self):
        """Gets the protocol of this NetworkAddress.  # noqa: E501


        :return: The protocol of this NetworkAddress.  # noqa: E501
        :rtype: NetworkProtocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this NetworkAddress.


        :param protocol: The protocol of this NetworkAddress.  # noqa: E501
        :type: NetworkProtocol
        """
        if self._configuration.client_side_validation and protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def address_mode(self):
        """Gets the address_mode of this NetworkAddress.  # noqa: E501

        The addressing mode for the interface.  # noqa: E501

        :return: The address_mode of this NetworkAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_mode

    @address_mode.setter
    def address_mode(self, address_mode):
        """Sets the address_mode of this NetworkAddress.

        The addressing mode for the interface.  # noqa: E501

        :param address_mode: The address_mode of this NetworkAddress.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and address_mode is None:
            raise ValueError("Invalid value for `address_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["dynamic", "static"]  # noqa: E501
        if (self._configuration.client_side_validation and
                address_mode not in allowed_values):
            raise ValueError(
                "Invalid value for `address_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(address_mode, allowed_values)
            )

        self._address_mode = address_mode

    @property
    def address(self):
        """Gets the address of this NetworkAddress.  # noqa: E501

        The IP address of the interface. Could be either an IPv4 address in dot-decimal format or an IPv6 address compliant with RFC-5952. The `protocol` property provides the expected network protocol version of the address.   # noqa: E501

        :return: The address of this NetworkAddress.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this NetworkAddress.

        The IP address of the interface. Could be either an IPv4 address in dot-decimal format or an IPv6 address compliant with RFC-5952. The `protocol` property provides the expected network protocol version of the address.   # noqa: E501

        :param address: The address of this NetworkAddress.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                address is not None and len(address) > 64):
            raise ValueError("Invalid value for `address`, length must be less than or equal to `64`")  # noqa: E501

        self._address = address

    @property
    def prefix(self):
        """Gets the prefix of this NetworkAddress.  # noqa: E501

        The network prefix length of the interface. A typical value is 24 for IPv4 and 64 for IPv6.   # noqa: E501

        :return: The prefix of this NetworkAddress.  # noqa: E501
        :rtype: int
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this NetworkAddress.

        The network prefix length of the interface. A typical value is 24 for IPv4 and 64 for IPv6.   # noqa: E501

        :param prefix: The prefix of this NetworkAddress.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                prefix is not None and prefix > 128):  # noqa: E501
            raise ValueError("Invalid value for `prefix`, must be a value less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                prefix is not None and prefix < 8):  # noqa: E501
            raise ValueError("Invalid value for `prefix`, must be a value greater than or equal to `8`")  # noqa: E501

        self._prefix = prefix

    @property
    def gateway(self):
        """Gets the gateway of this NetworkAddress.  # noqa: E501

        The gateway address of the interface. Could be either an IPv4 address in dot-decimal format or an IPv6 address compliant with RFC-5952.   # noqa: E501

        :return: The gateway of this NetworkAddress.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this NetworkAddress.

        The gateway address of the interface. Could be either an IPv4 address in dot-decimal format or an IPv6 address compliant with RFC-5952.   # noqa: E501

        :param gateway: The gateway of this NetworkAddress.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                gateway is not None and len(gateway) > 64):
            raise ValueError("Invalid value for `gateway`, length must be less than or equal to `64`")  # noqa: E501

        self._gateway = gateway

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
        if issubclass(NetworkAddress, dict):
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
        if not isinstance(other, NetworkAddress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkAddress):
            return True

        return self.to_dict() != other.to_dict()
