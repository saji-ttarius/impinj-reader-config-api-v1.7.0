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


class KafkaBootstrapServerConfiguration(object):
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
        'hostname': 'str',
        'port': 'int'
    }

    attribute_map = {
        'hostname': 'hostname',
        'port': 'port'
    }

    def __init__(self, hostname=None, port=None, _configuration=None):  # noqa: E501
        """KafkaBootstrapServerConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._hostname = None
        self._port = None
        self.discriminator = None

        self.hostname = hostname
        if port is not None:
            self.port = port

    @property
    def hostname(self):
        """Gets the hostname of this KafkaBootstrapServerConfiguration.  # noqa: E501

        The hostname to use for connecting to the Kafka broker.  # noqa: E501

        :return: The hostname of this KafkaBootstrapServerConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this KafkaBootstrapServerConfiguration.

        The hostname to use for connecting to the Kafka broker.  # noqa: E501

        :param hostname: The hostname of this KafkaBootstrapServerConfiguration.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and hostname is None:
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                hostname is not None and len(hostname) > 253):
            raise ValueError("Invalid value for `hostname`, length must be less than or equal to `253`")  # noqa: E501
        if (self._configuration.client_side_validation and
                hostname is not None and len(hostname) < 1):
            raise ValueError("Invalid value for `hostname`, length must be greater than or equal to `1`")  # noqa: E501
        if (self._configuration.client_side_validation and
                hostname is not None and not re.search(r'^[^,]+$', hostname)):  # noqa: E501
            raise ValueError(r"Invalid value for `hostname`, must be a follow pattern or equal to `/^[^,]+$/`")  # noqa: E501

        self._hostname = hostname

    @property
    def port(self):
        """Gets the port of this KafkaBootstrapServerConfiguration.  # noqa: E501

        The TCP port to use for connecting to the Kafka broker.  # noqa: E501

        :return: The port of this KafkaBootstrapServerConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this KafkaBootstrapServerConfiguration.

        The TCP port to use for connecting to the Kafka broker.  # noqa: E501

        :param port: The port of this KafkaBootstrapServerConfiguration.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                port is not None and port > 65535):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self._configuration.client_side_validation and
                port is not None and port < 1):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `1`")  # noqa: E501

        self._port = port

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
        if issubclass(KafkaBootstrapServerConfiguration, dict):
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
        if not isinstance(other, KafkaBootstrapServerConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KafkaBootstrapServerConfiguration):
            return True

        return self.to_dict() != other.to_dict()
