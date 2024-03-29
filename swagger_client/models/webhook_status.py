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


class WebhookStatus(object):
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
        'http_status_code': 'int',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'status': 'status',
        'http_status_code': 'httpStatusCode',
        'timestamp': 'timestamp'
    }

    def __init__(self, status=None, http_status_code=None, timestamp=None, _configuration=None):  # noqa: E501
        """WebhookStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status = None
        self._http_status_code = None
        self._timestamp = None
        self.discriminator = None

        self.status = status
        if http_status_code is not None:
            self.http_status_code = http_status_code
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def status(self):
        """Gets the status of this WebhookStatus.  # noqa: E501

        The general status of the webhook. The \"pending\" state indicates that the webhook is active, but has not published since being enabled or since the last reader reboot. The \"http-error\" state occurs if the server replied with an error code. The \"network-error\" state indicates that the server could not be reached.   # noqa: E501

        :return: The status of this WebhookStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WebhookStatus.

        The general status of the webhook. The \"pending\" state indicates that the webhook is active, but has not published since being enabled or since the last reader reboot. The \"http-error\" state occurs if the server replied with an error code. The \"network-error\" state indicates that the server could not be reached.   # noqa: E501

        :param status: The status of this WebhookStatus.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["disabled", "pending", "active", "http-error", "network-error"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def http_status_code(self):
        """Gets the http_status_code of this WebhookStatus.  # noqa: E501

        The HTTP status code of the most recent webhook request to the server. This property will be absent if the webhook is pending, disabled or experiencing a network error.   # noqa: E501

        :return: The http_status_code of this WebhookStatus.  # noqa: E501
        :rtype: int
        """
        return self._http_status_code

    @http_status_code.setter
    def http_status_code(self, http_status_code):
        """Sets the http_status_code of this WebhookStatus.

        The HTTP status code of the most recent webhook request to the server. This property will be absent if the webhook is pending, disabled or experiencing a network error.   # noqa: E501

        :param http_status_code: The http_status_code of this WebhookStatus.  # noqa: E501
        :type: int
        """

        self._http_status_code = http_status_code

    @property
    def timestamp(self):
        """Gets the timestamp of this WebhookStatus.  # noqa: E501

        The time at which the last request was attempted. This property will be absent if the webhook is pending or disabled.   # noqa: E501

        :return: The timestamp of this WebhookStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this WebhookStatus.

        The time at which the last request was attempted. This property will be absent if the webhook is pending or disabled.   # noqa: E501

        :param timestamp: The timestamp of this WebhookStatus.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

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
        if issubclass(WebhookStatus, dict):
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
        if not isinstance(other, WebhookStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookStatus):
            return True

        return self.to_dict() != other.to_dict()
