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


class AntennaHubInfo(object):
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
        'antenna_hub_states': 'list[AntennaHubState]'
    }

    attribute_map = {
        'status': 'status',
        'antenna_hub_states': 'antennaHubStates'
    }

    def __init__(self, status=None, antenna_hub_states=None, _configuration=None):  # noqa: E501
        """AntennaHubInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status = None
        self._antenna_hub_states = None
        self.discriminator = None

        self.status = status
        if antenna_hub_states is not None:
            self.antenna_hub_states = antenna_hub_states

    @property
    def status(self):
        """Gets the status of this AntennaHubInfo.  # noqa: E501

        Antenna-hub configuration status.  # noqa: E501

        :return: The status of this AntennaHubInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AntennaHubInfo.

        Antenna-hub configuration status.  # noqa: E501

        :param status: The status of this AntennaHubInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["Enabled", "Disabled"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def antenna_hub_states(self):
        """Gets the antenna_hub_states of this AntennaHubInfo.  # noqa: E501

        A list of all reader antenna ports and information about connected antenna-hubs.  # noqa: E501

        :return: The antenna_hub_states of this AntennaHubInfo.  # noqa: E501
        :rtype: list[AntennaHubState]
        """
        return self._antenna_hub_states

    @antenna_hub_states.setter
    def antenna_hub_states(self, antenna_hub_states):
        """Sets the antenna_hub_states of this AntennaHubInfo.

        A list of all reader antenna ports and information about connected antenna-hubs.  # noqa: E501

        :param antenna_hub_states: The antenna_hub_states of this AntennaHubInfo.  # noqa: E501
        :type: list[AntennaHubState]
        """

        self._antenna_hub_states = antenna_hub_states

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
        if issubclass(AntennaHubInfo, dict):
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
        if not isinstance(other, AntennaHubInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AntennaHubInfo):
            return True

        return self.to_dict() != other.to_dict()
