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


class GpiTransitionEvent(object):
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
        'gpi': 'int',
        'transition': 'str'
    }

    attribute_map = {
        'gpi': 'gpi',
        'transition': 'transition'
    }

    def __init__(self, gpi=None, transition=None, _configuration=None):  # noqa: E501
        """GpiTransitionEvent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._gpi = None
        self._transition = None
        self.discriminator = None

        if gpi is not None:
            self.gpi = gpi
        if transition is not None:
            self.transition = transition

    @property
    def gpi(self):
        """Gets the gpi of this GpiTransitionEvent.  # noqa: E501

        The GPI pin for which the state transition occurred.  # noqa: E501

        :return: The gpi of this GpiTransitionEvent.  # noqa: E501
        :rtype: int
        """
        return self._gpi

    @gpi.setter
    def gpi(self, gpi):
        """Sets the gpi of this GpiTransitionEvent.

        The GPI pin for which the state transition occurred.  # noqa: E501

        :param gpi: The gpi of this GpiTransitionEvent.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                gpi is not None and gpi < 1):  # noqa: E501
            raise ValueError("Invalid value for `gpi`, must be a value greater than or equal to `1`")  # noqa: E501

        self._gpi = gpi

    @property
    def transition(self):
        """Gets the transition of this GpiTransitionEvent.  # noqa: E501

        The transition that occurred on the specified pin.  # noqa: E501

        :return: The transition of this GpiTransitionEvent.  # noqa: E501
        :rtype: str
        """
        return self._transition

    @transition.setter
    def transition(self, transition):
        """Sets the transition of this GpiTransitionEvent.

        The transition that occurred on the specified pin.  # noqa: E501

        :param transition: The transition of this GpiTransitionEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["high-to-low", "low-to-high"]  # noqa: E501
        if (self._configuration.client_side_validation and
                transition not in allowed_values):
            raise ValueError(
                "Invalid value for `transition` ({0}), must be one of {1}"  # noqa: E501
                .format(transition, allowed_values)
            )

        self._transition = transition

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
        if issubclass(GpiTransitionEvent, dict):
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
        if not isinstance(other, GpiTransitionEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GpiTransitionEvent):
            return True

        return self.to_dict() != other.to_dict()
