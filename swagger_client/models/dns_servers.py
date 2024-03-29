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


class DnsServers(object):
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
        'static_dns_servers': 'list[DnsServerAddress]',
        'dynamic_dns_servers': 'list[DnsServerAddress]'
    }

    attribute_map = {
        'static_dns_servers': 'staticDnsServers',
        'dynamic_dns_servers': 'dynamicDnsServers'
    }

    def __init__(self, static_dns_servers=None, dynamic_dns_servers=None, _configuration=None):  # noqa: E501
        """DnsServers - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._static_dns_servers = None
        self._dynamic_dns_servers = None
        self.discriminator = None

        self.static_dns_servers = static_dns_servers
        if dynamic_dns_servers is not None:
            self.dynamic_dns_servers = dynamic_dns_servers

    @property
    def static_dns_servers(self):
        """Gets the static_dns_servers of this DnsServers.  # noqa: E501


        :return: The static_dns_servers of this DnsServers.  # noqa: E501
        :rtype: list[DnsServerAddress]
        """
        return self._static_dns_servers

    @static_dns_servers.setter
    def static_dns_servers(self, static_dns_servers):
        """Sets the static_dns_servers of this DnsServers.


        :param static_dns_servers: The static_dns_servers of this DnsServers.  # noqa: E501
        :type: list[DnsServerAddress]
        """
        if self._configuration.client_side_validation and static_dns_servers is None:
            raise ValueError("Invalid value for `static_dns_servers`, must not be `None`")  # noqa: E501

        self._static_dns_servers = static_dns_servers

    @property
    def dynamic_dns_servers(self):
        """Gets the dynamic_dns_servers of this DnsServers.  # noqa: E501


        :return: The dynamic_dns_servers of this DnsServers.  # noqa: E501
        :rtype: list[DnsServerAddress]
        """
        return self._dynamic_dns_servers

    @dynamic_dns_servers.setter
    def dynamic_dns_servers(self, dynamic_dns_servers):
        """Sets the dynamic_dns_servers of this DnsServers.


        :param dynamic_dns_servers: The dynamic_dns_servers of this DnsServers.  # noqa: E501
        :type: list[DnsServerAddress]
        """

        self._dynamic_dns_servers = dynamic_dns_servers

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
        if issubclass(DnsServers, dict):
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
        if not isinstance(other, DnsServers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DnsServers):
            return True

        return self.to_dict() != other.to_dict()
