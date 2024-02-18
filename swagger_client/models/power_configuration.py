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


class PowerConfiguration(object):
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
        'power_source': 'PowerSource',
        'allocated_power_milliwatts': 'int'
    }

    attribute_map = {
        'power_source': 'powerSource',
        'allocated_power_milliwatts': 'allocatedPowerMilliwatts'
    }

    def __init__(self, power_source=None, allocated_power_milliwatts=None, _configuration=None):  # noqa: E501
        """PowerConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._power_source = None
        self._allocated_power_milliwatts = None
        self.discriminator = None

        self.power_source = power_source
        if allocated_power_milliwatts is not None:
            self.allocated_power_milliwatts = allocated_power_milliwatts

    @property
    def power_source(self):
        """Gets the power_source of this PowerConfiguration.  # noqa: E501


        :return: The power_source of this PowerConfiguration.  # noqa: E501
        :rtype: PowerSource
        """
        return self._power_source

    @power_source.setter
    def power_source(self, power_source):
        """Sets the power_source of this PowerConfiguration.


        :param power_source: The power_source of this PowerConfiguration.  # noqa: E501
        :type: PowerSource
        """
        if self._configuration.client_side_validation and power_source is None:
            raise ValueError("Invalid value for `power_source`, must not be `None`")  # noqa: E501

        self._power_source = power_source

    @property
    def allocated_power_milliwatts(self):
        """Gets the allocated_power_milliwatts of this PowerConfiguration.  # noqa: E501

        This field is only available when powerSource is set to auto. Contains the actual power that was allocated for the reader by the switch through negotiation.   # noqa: E501

        :return: The allocated_power_milliwatts of this PowerConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._allocated_power_milliwatts

    @allocated_power_milliwatts.setter
    def allocated_power_milliwatts(self, allocated_power_milliwatts):
        """Sets the allocated_power_milliwatts of this PowerConfiguration.

        This field is only available when powerSource is set to auto. Contains the actual power that was allocated for the reader by the switch through negotiation.   # noqa: E501

        :param allocated_power_milliwatts: The allocated_power_milliwatts of this PowerConfiguration.  # noqa: E501
        :type: int
        """

        self._allocated_power_milliwatts = allocated_power_milliwatts

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
        if issubclass(PowerConfiguration, dict):
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
        if not isinstance(other, PowerConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PowerConfiguration):
            return True

        return self.to_dict() != other.to_dict()
