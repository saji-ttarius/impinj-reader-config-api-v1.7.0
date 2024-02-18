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


class StreamConfiguration(object):
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
        'event_buffer_size': 'int',
        'event_per_second_limit': 'int',
        'event_age_limit_minutes': 'int',
        'keep_alive_interval_seconds': 'int'
    }

    attribute_map = {
        'event_buffer_size': 'eventBufferSize',
        'event_per_second_limit': 'eventPerSecondLimit',
        'event_age_limit_minutes': 'eventAgeLimitMinutes',
        'keep_alive_interval_seconds': 'keepAliveIntervalSeconds'
    }

    def __init__(self, event_buffer_size=None, event_per_second_limit=None, event_age_limit_minutes=None, keep_alive_interval_seconds=None, _configuration=None):  # noqa: E501
        """StreamConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._event_buffer_size = None
        self._event_per_second_limit = None
        self._event_age_limit_minutes = None
        self._keep_alive_interval_seconds = None
        self.discriminator = None

        if event_buffer_size is not None:
            self.event_buffer_size = event_buffer_size
        if event_per_second_limit is not None:
            self.event_per_second_limit = event_per_second_limit
        if event_age_limit_minutes is not None:
            self.event_age_limit_minutes = event_age_limit_minutes
        if keep_alive_interval_seconds is not None:
            self.keep_alive_interval_seconds = keep_alive_interval_seconds

    @property
    def event_buffer_size(self):
        """Gets the event_buffer_size of this StreamConfiguration.  # noqa: E501

        Number of events that can be stored on the reader waiting for future delivery.  If the bufferSize is 0 then no buffer is created and no history will be saved.   # noqa: E501

        :return: The event_buffer_size of this StreamConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._event_buffer_size

    @event_buffer_size.setter
    def event_buffer_size(self, event_buffer_size):
        """Sets the event_buffer_size of this StreamConfiguration.

        Number of events that can be stored on the reader waiting for future delivery.  If the bufferSize is 0 then no buffer is created and no history will be saved.   # noqa: E501

        :param event_buffer_size: The event_buffer_size of this StreamConfiguration.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                event_buffer_size is not None and event_buffer_size > 300000):  # noqa: E501
            raise ValueError("Invalid value for `event_buffer_size`, must be a value less than or equal to `300000`")  # noqa: E501
        if (self._configuration.client_side_validation and
                event_buffer_size is not None and event_buffer_size < 0):  # noqa: E501
            raise ValueError("Invalid value for `event_buffer_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._event_buffer_size = event_buffer_size

    @property
    def event_per_second_limit(self):
        """Gets the event_per_second_limit of this StreamConfiguration.  # noqa: E501

        Maximum number of events that may be delivered per second. This setting can be used to throttle the delivery of events during peak transmission times such as when replaying history during a new connection. Care should be taken to not set this value lower than the normal event generation rate of the reader or the queue attached to the HTTP stream will fill up and events will be purged. A value of Zero (0) means that no eventsPerSecondLimit is applied.   # noqa: E501

        :return: The event_per_second_limit of this StreamConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._event_per_second_limit

    @event_per_second_limit.setter
    def event_per_second_limit(self, event_per_second_limit):
        """Sets the event_per_second_limit of this StreamConfiguration.

        Maximum number of events that may be delivered per second. This setting can be used to throttle the delivery of events during peak transmission times such as when replaying history during a new connection. Care should be taken to not set this value lower than the normal event generation rate of the reader or the queue attached to the HTTP stream will fill up and events will be purged. A value of Zero (0) means that no eventsPerSecondLimit is applied.   # noqa: E501

        :param event_per_second_limit: The event_per_second_limit of this StreamConfiguration.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                event_per_second_limit is not None and event_per_second_limit > 100000):  # noqa: E501
            raise ValueError("Invalid value for `event_per_second_limit`, must be a value less than or equal to `100000`")  # noqa: E501
        if (self._configuration.client_side_validation and
                event_per_second_limit is not None and event_per_second_limit < 0):  # noqa: E501
            raise ValueError("Invalid value for `event_per_second_limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._event_per_second_limit = event_per_second_limit

    @property
    def event_age_limit_minutes(self):
        """Gets the event_age_limit_minutes of this StreamConfiguration.  # noqa: E501

        Maximum age of any event in the history buffer.  Any event older than this will be purged automatically from the buffer without the generation of an OverflowEvent.  Use this value to configure the maximum event lifetime for the history buffer.   # noqa: E501

        :return: The event_age_limit_minutes of this StreamConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._event_age_limit_minutes

    @event_age_limit_minutes.setter
    def event_age_limit_minutes(self, event_age_limit_minutes):
        """Sets the event_age_limit_minutes of this StreamConfiguration.

        Maximum age of any event in the history buffer.  Any event older than this will be purged automatically from the buffer without the generation of an OverflowEvent.  Use this value to configure the maximum event lifetime for the history buffer.   # noqa: E501

        :param event_age_limit_minutes: The event_age_limit_minutes of this StreamConfiguration.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                event_age_limit_minutes is not None and event_age_limit_minutes > 1440):  # noqa: E501
            raise ValueError("Invalid value for `event_age_limit_minutes`, must be a value less than or equal to `1440`")  # noqa: E501
        if (self._configuration.client_side_validation and
                event_age_limit_minutes is not None and event_age_limit_minutes < 1):  # noqa: E501
            raise ValueError("Invalid value for `event_age_limit_minutes`, must be a value greater than or equal to `1`")  # noqa: E501

        self._event_age_limit_minutes = event_age_limit_minutes

    @property
    def keep_alive_interval_seconds(self):
        """Gets the keep_alive_interval_seconds of this StreamConfiguration.  # noqa: E501

        The keep-alive interval in seconds. If no events (or previous keep-alive) have been transmitted in this amount of time a newline (CRLF) will be sent. If this field is updated and no events are available, a keep-alive will be immediately sent.   # noqa: E501

        :return: The keep_alive_interval_seconds of this StreamConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._keep_alive_interval_seconds

    @keep_alive_interval_seconds.setter
    def keep_alive_interval_seconds(self, keep_alive_interval_seconds):
        """Sets the keep_alive_interval_seconds of this StreamConfiguration.

        The keep-alive interval in seconds. If no events (or previous keep-alive) have been transmitted in this amount of time a newline (CRLF) will be sent. If this field is updated and no events are available, a keep-alive will be immediately sent.   # noqa: E501

        :param keep_alive_interval_seconds: The keep_alive_interval_seconds of this StreamConfiguration.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                keep_alive_interval_seconds is not None and keep_alive_interval_seconds > 300):  # noqa: E501
            raise ValueError("Invalid value for `keep_alive_interval_seconds`, must be a value less than or equal to `300`")  # noqa: E501
        if (self._configuration.client_side_validation and
                keep_alive_interval_seconds is not None and keep_alive_interval_seconds < 1):  # noqa: E501
            raise ValueError("Invalid value for `keep_alive_interval_seconds`, must be a value greater than or equal to `1`")  # noqa: E501

        self._keep_alive_interval_seconds = keep_alive_interval_seconds

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
        if issubclass(StreamConfiguration, dict):
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
        if not isinstance(other, StreamConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StreamConfiguration):
            return True

        return self.to_dict() != other.to_dict()