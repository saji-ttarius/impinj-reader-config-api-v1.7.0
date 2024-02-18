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


class OverflowEvent(object):
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
        'first_event_timestamp': 'datetime',
        'last_event_timestamp': 'datetime',
        'events_purged': 'int',
        'events_remaining': 'int'
    }

    attribute_map = {
        'first_event_timestamp': 'firstEventTimestamp',
        'last_event_timestamp': 'lastEventTimestamp',
        'events_purged': 'eventsPurged',
        'events_remaining': 'eventsRemaining'
    }

    def __init__(self, first_event_timestamp=None, last_event_timestamp=None, events_purged=None, events_remaining=None, _configuration=None):  # noqa: E501
        """OverflowEvent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._first_event_timestamp = None
        self._last_event_timestamp = None
        self._events_purged = None
        self._events_remaining = None
        self.discriminator = None

        if first_event_timestamp is not None:
            self.first_event_timestamp = first_event_timestamp
        if last_event_timestamp is not None:
            self.last_event_timestamp = last_event_timestamp
        if events_purged is not None:
            self.events_purged = events_purged
        if events_remaining is not None:
            self.events_remaining = events_remaining

    @property
    def first_event_timestamp(self):
        """Gets the first_event_timestamp of this OverflowEvent.  # noqa: E501

        The timestamp of the first event that was purged from the buffer.  # noqa: E501

        :return: The first_event_timestamp of this OverflowEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._first_event_timestamp

    @first_event_timestamp.setter
    def first_event_timestamp(self, first_event_timestamp):
        """Sets the first_event_timestamp of this OverflowEvent.

        The timestamp of the first event that was purged from the buffer.  # noqa: E501

        :param first_event_timestamp: The first_event_timestamp of this OverflowEvent.  # noqa: E501
        :type: datetime
        """

        self._first_event_timestamp = first_event_timestamp

    @property
    def last_event_timestamp(self):
        """Gets the last_event_timestamp of this OverflowEvent.  # noqa: E501

        The timestamp of the last event that was purged from the buffer.  # noqa: E501

        :return: The last_event_timestamp of this OverflowEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._last_event_timestamp

    @last_event_timestamp.setter
    def last_event_timestamp(self, last_event_timestamp):
        """Sets the last_event_timestamp of this OverflowEvent.

        The timestamp of the last event that was purged from the buffer.  # noqa: E501

        :param last_event_timestamp: The last_event_timestamp of this OverflowEvent.  # noqa: E501
        :type: datetime
        """

        self._last_event_timestamp = last_event_timestamp

    @property
    def events_purged(self):
        """Gets the events_purged of this OverflowEvent.  # noqa: E501

        The number of events that were purged from the buffer.  # noqa: E501

        :return: The events_purged of this OverflowEvent.  # noqa: E501
        :rtype: int
        """
        return self._events_purged

    @events_purged.setter
    def events_purged(self, events_purged):
        """Sets the events_purged of this OverflowEvent.

        The number of events that were purged from the buffer.  # noqa: E501

        :param events_purged: The events_purged of this OverflowEvent.  # noqa: E501
        :type: int
        """

        self._events_purged = events_purged

    @property
    def events_remaining(self):
        """Gets the events_remaining of this OverflowEvent.  # noqa: E501

        The number of events that remained in the buffer after it was purged.  # noqa: E501

        :return: The events_remaining of this OverflowEvent.  # noqa: E501
        :rtype: int
        """
        return self._events_remaining

    @events_remaining.setter
    def events_remaining(self, events_remaining):
        """Sets the events_remaining of this OverflowEvent.

        The number of events that remained in the buffer after it was purged.  # noqa: E501

        :param events_remaining: The events_remaining of this OverflowEvent.  # noqa: E501
        :type: int
        """

        self._events_remaining = events_remaining

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
        if issubclass(OverflowEvent, dict):
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
        if not isinstance(other, OverflowEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OverflowEvent):
            return True

        return self.to_dict() != other.to_dict()
