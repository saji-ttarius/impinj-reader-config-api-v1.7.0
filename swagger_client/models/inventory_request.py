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


class InventoryRequest(object):
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
        'event_config': 'InventoryEventConfiguration',
        'antenna_configs': 'list[InventoryAntennaConfiguration]',
        'channel_frequencies_khz': 'list[int]',
        'start_triggers': 'list[InventoryStartTrigger]',
        'stop_triggers': 'list[InventoryStopTrigger]'
    }

    attribute_map = {
        'event_config': 'eventConfig',
        'antenna_configs': 'antennaConfigs',
        'channel_frequencies_khz': 'channelFrequenciesKHz',
        'start_triggers': 'startTriggers',
        'stop_triggers': 'stopTriggers'
    }

    def __init__(self, event_config=None, antenna_configs=None, channel_frequencies_khz=None, start_triggers=None, stop_triggers=None, _configuration=None):  # noqa: E501
        """InventoryRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._event_config = None
        self._antenna_configs = None
        self._channel_frequencies_khz = None
        self._start_triggers = None
        self._stop_triggers = None
        self.discriminator = None

        if event_config is not None:
            self.event_config = event_config
        self.antenna_configs = antenna_configs
        if channel_frequencies_khz is not None:
            self.channel_frequencies_khz = channel_frequencies_khz
        if start_triggers is not None:
            self.start_triggers = start_triggers
        if stop_triggers is not None:
            self.stop_triggers = stop_triggers

    @property
    def event_config(self):
        """Gets the event_config of this InventoryRequest.  # noqa: E501


        :return: The event_config of this InventoryRequest.  # noqa: E501
        :rtype: InventoryEventConfiguration
        """
        return self._event_config

    @event_config.setter
    def event_config(self, event_config):
        """Sets the event_config of this InventoryRequest.


        :param event_config: The event_config of this InventoryRequest.  # noqa: E501
        :type: InventoryEventConfiguration
        """

        self._event_config = event_config

    @property
    def antenna_configs(self):
        """Gets the antenna_configs of this InventoryRequest.  # noqa: E501


        :return: The antenna_configs of this InventoryRequest.  # noqa: E501
        :rtype: list[InventoryAntennaConfiguration]
        """
        return self._antenna_configs

    @antenna_configs.setter
    def antenna_configs(self, antenna_configs):
        """Sets the antenna_configs of this InventoryRequest.


        :param antenna_configs: The antenna_configs of this InventoryRequest.  # noqa: E501
        :type: list[InventoryAntennaConfiguration]
        """
        if self._configuration.client_side_validation and antenna_configs is None:
            raise ValueError("Invalid value for `antenna_configs`, must not be `None`")  # noqa: E501

        self._antenna_configs = antenna_configs

    @property
    def channel_frequencies_khz(self):
        """Gets the channel_frequencies_khz of this InventoryRequest.  # noqa: E501

        For non frequency hopping regions that allow the choice of operating frequency, this array contains the sequence of frequencies to use. Permissible values are region-dependent and will be included in the JSON schema produced by the reader.   # noqa: E501

        :return: The channel_frequencies_khz of this InventoryRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._channel_frequencies_khz

    @channel_frequencies_khz.setter
    def channel_frequencies_khz(self, channel_frequencies_khz):
        """Sets the channel_frequencies_khz of this InventoryRequest.

        For non frequency hopping regions that allow the choice of operating frequency, this array contains the sequence of frequencies to use. Permissible values are region-dependent and will be included in the JSON schema produced by the reader.   # noqa: E501

        :param channel_frequencies_khz: The channel_frequencies_khz of this InventoryRequest.  # noqa: E501
        :type: list[int]
        """

        self._channel_frequencies_khz = channel_frequencies_khz

    @property
    def start_triggers(self):
        """Gets the start_triggers of this InventoryRequest.  # noqa: E501

        This property contains an array of triggers that will start the inventory. If any triggers are specified, then the RFID operation will transition to the ARMED state.  When the reader is in the ARMED state, a trigger will transition the reader to the RUNNING state and begin the inventory.   # noqa: E501

        :return: The start_triggers of this InventoryRequest.  # noqa: E501
        :rtype: list[InventoryStartTrigger]
        """
        return self._start_triggers

    @start_triggers.setter
    def start_triggers(self, start_triggers):
        """Sets the start_triggers of this InventoryRequest.

        This property contains an array of triggers that will start the inventory. If any triggers are specified, then the RFID operation will transition to the ARMED state.  When the reader is in the ARMED state, a trigger will transition the reader to the RUNNING state and begin the inventory.   # noqa: E501

        :param start_triggers: The start_triggers of this InventoryRequest.  # noqa: E501
        :type: list[InventoryStartTrigger]
        """

        self._start_triggers = start_triggers

    @property
    def stop_triggers(self):
        """Gets the stop_triggers of this InventoryRequest.  # noqa: E501

        This property contains an array of triggers that will stop the inventory.  When the reader is in the RUNNING state, a trigger will transition the reader to the ARMED state and stop the inventory.   # noqa: E501

        :return: The stop_triggers of this InventoryRequest.  # noqa: E501
        :rtype: list[InventoryStopTrigger]
        """
        return self._stop_triggers

    @stop_triggers.setter
    def stop_triggers(self, stop_triggers):
        """Sets the stop_triggers of this InventoryRequest.

        This property contains an array of triggers that will stop the inventory.  When the reader is in the RUNNING state, a trigger will transition the reader to the ARMED state and stop the inventory.   # noqa: E501

        :param stop_triggers: The stop_triggers of this InventoryRequest.  # noqa: E501
        :type: list[InventoryStopTrigger]
        """

        self._stop_triggers = stop_triggers

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
        if issubclass(InventoryRequest, dict):
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
        if not isinstance(other, InventoryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InventoryRequest):
            return True

        return self.to_dict() != other.to_dict()
