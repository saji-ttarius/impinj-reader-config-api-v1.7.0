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


class ReaderEvent(object):
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
        'event_type': 'str',
        'timestamp': 'datetime',
        'tag_inventory_event': 'TagInventoryEvent',
        'antenna_connected_event': 'AntennaConnectedEvent',
        'antenna_disconnected_event': 'AntennaDisconnectedEvent',
        'inventory_status_event': 'InventoryStatusEvent',
        'antenna_activation_event': 'AntennaActivationEvent',
        'overflow_event': 'OverflowEvent'
    }

    attribute_map = {
        'hostname': 'hostname',
        'event_type': 'eventType',
        'timestamp': 'timestamp',
        'tag_inventory_event': 'tagInventoryEvent',
        'antenna_connected_event': 'antennaConnectedEvent',
        'antenna_disconnected_event': 'antennaDisconnectedEvent',
        'inventory_status_event': 'inventoryStatusEvent',
        'antenna_activation_event': 'antennaActivationEvent',
        'overflow_event': 'overflowEvent'
    }

    def __init__(self, hostname=None, event_type=None, timestamp=None, tag_inventory_event=None, antenna_connected_event=None, antenna_disconnected_event=None, inventory_status_event=None, antenna_activation_event=None, overflow_event=None, _configuration=None):  # noqa: E501
        """ReaderEvent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._hostname = None
        self._event_type = None
        self._timestamp = None
        self._tag_inventory_event = None
        self._antenna_connected_event = None
        self._antenna_disconnected_event = None
        self._inventory_status_event = None
        self._antenna_activation_event = None
        self._overflow_event = None
        self.discriminator = None

        if hostname is not None:
            self.hostname = hostname
        self.event_type = event_type
        self.timestamp = timestamp
        if tag_inventory_event is not None:
            self.tag_inventory_event = tag_inventory_event
        if antenna_connected_event is not None:
            self.antenna_connected_event = antenna_connected_event
        if antenna_disconnected_event is not None:
            self.antenna_disconnected_event = antenna_disconnected_event
        if inventory_status_event is not None:
            self.inventory_status_event = inventory_status_event
        if antenna_activation_event is not None:
            self.antenna_activation_event = antenna_activation_event
        if overflow_event is not None:
            self.overflow_event = overflow_event

    @property
    def hostname(self):
        """Gets the hostname of this ReaderEvent.  # noqa: E501

        The hostname of the reader that generated this event.  # noqa: E501

        :return: The hostname of this ReaderEvent.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ReaderEvent.

        The hostname of the reader that generated this event.  # noqa: E501

        :param hostname: The hostname of this ReaderEvent.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def event_type(self):
        """Gets the event_type of this ReaderEvent.  # noqa: E501

        The type of the event, should be the same as the name of the property that contains the event with the string \"Event\" stripped off.  For example an event with an eventType of \"tagInventory\" will contain the \"tagInventoryEvent\" property.  # noqa: E501

        :return: The event_type of this ReaderEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ReaderEvent.

        The type of the event, should be the same as the name of the property that contains the event with the string \"Event\" stripped off.  For example an event with an eventType of \"tagInventory\" will contain the \"tagInventoryEvent\" property.  # noqa: E501

        :param event_type: The event_type of this ReaderEvent.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def timestamp(self):
        """Gets the timestamp of this ReaderEvent.  # noqa: E501

        The UTC time at which the event was processed and queued for delivery.   # noqa: E501

        :return: The timestamp of this ReaderEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ReaderEvent.

        The UTC time at which the event was processed and queued for delivery.   # noqa: E501

        :param timestamp: The timestamp of this ReaderEvent.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def tag_inventory_event(self):
        """Gets the tag_inventory_event of this ReaderEvent.  # noqa: E501


        :return: The tag_inventory_event of this ReaderEvent.  # noqa: E501
        :rtype: TagInventoryEvent
        """
        return self._tag_inventory_event

    @tag_inventory_event.setter
    def tag_inventory_event(self, tag_inventory_event):
        """Sets the tag_inventory_event of this ReaderEvent.


        :param tag_inventory_event: The tag_inventory_event of this ReaderEvent.  # noqa: E501
        :type: TagInventoryEvent
        """

        self._tag_inventory_event = tag_inventory_event

    @property
    def antenna_connected_event(self):
        """Gets the antenna_connected_event of this ReaderEvent.  # noqa: E501


        :return: The antenna_connected_event of this ReaderEvent.  # noqa: E501
        :rtype: AntennaConnectedEvent
        """
        return self._antenna_connected_event

    @antenna_connected_event.setter
    def antenna_connected_event(self, antenna_connected_event):
        """Sets the antenna_connected_event of this ReaderEvent.


        :param antenna_connected_event: The antenna_connected_event of this ReaderEvent.  # noqa: E501
        :type: AntennaConnectedEvent
        """

        self._antenna_connected_event = antenna_connected_event

    @property
    def antenna_disconnected_event(self):
        """Gets the antenna_disconnected_event of this ReaderEvent.  # noqa: E501


        :return: The antenna_disconnected_event of this ReaderEvent.  # noqa: E501
        :rtype: AntennaDisconnectedEvent
        """
        return self._antenna_disconnected_event

    @antenna_disconnected_event.setter
    def antenna_disconnected_event(self, antenna_disconnected_event):
        """Sets the antenna_disconnected_event of this ReaderEvent.


        :param antenna_disconnected_event: The antenna_disconnected_event of this ReaderEvent.  # noqa: E501
        :type: AntennaDisconnectedEvent
        """

        self._antenna_disconnected_event = antenna_disconnected_event

    @property
    def inventory_status_event(self):
        """Gets the inventory_status_event of this ReaderEvent.  # noqa: E501


        :return: The inventory_status_event of this ReaderEvent.  # noqa: E501
        :rtype: InventoryStatusEvent
        """
        return self._inventory_status_event

    @inventory_status_event.setter
    def inventory_status_event(self, inventory_status_event):
        """Sets the inventory_status_event of this ReaderEvent.


        :param inventory_status_event: The inventory_status_event of this ReaderEvent.  # noqa: E501
        :type: InventoryStatusEvent
        """

        self._inventory_status_event = inventory_status_event

    @property
    def antenna_activation_event(self):
        """Gets the antenna_activation_event of this ReaderEvent.  # noqa: E501


        :return: The antenna_activation_event of this ReaderEvent.  # noqa: E501
        :rtype: AntennaActivationEvent
        """
        return self._antenna_activation_event

    @antenna_activation_event.setter
    def antenna_activation_event(self, antenna_activation_event):
        """Sets the antenna_activation_event of this ReaderEvent.


        :param antenna_activation_event: The antenna_activation_event of this ReaderEvent.  # noqa: E501
        :type: AntennaActivationEvent
        """

        self._antenna_activation_event = antenna_activation_event

    @property
    def overflow_event(self):
        """Gets the overflow_event of this ReaderEvent.  # noqa: E501


        :return: The overflow_event of this ReaderEvent.  # noqa: E501
        :rtype: OverflowEvent
        """
        return self._overflow_event

    @overflow_event.setter
    def overflow_event(self, overflow_event):
        """Sets the overflow_event of this ReaderEvent.


        :param overflow_event: The overflow_event of this ReaderEvent.  # noqa: E501
        :type: OverflowEvent
        """

        self._overflow_event = overflow_event

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
        if issubclass(ReaderEvent, dict):
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
        if not isinstance(other, ReaderEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReaderEvent):
            return True

        return self.to_dict() != other.to_dict()
