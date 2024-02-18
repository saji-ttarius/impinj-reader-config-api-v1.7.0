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


class TagInventoryEvent(object):
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
        'epc': 'Epc',
        'epc_hex': 'EpcHex',
        'tid': 'Tid',
        'tid_hex': 'TidHex',
        'xpc_hex': 'XpcHex',
        'antenna_port': 'AntennaPort',
        'antenna_name': 'AntennaName',
        'transmit_power_cdbm': 'TransmitPowerCdbm',
        'peak_rssi_cdbm': 'int',
        'frequency': 'int',
        'pc': 'str',
        'last_seen_time': 'datetime',
        'phase_angle': 'float',
        'tag_access_password_write_response': 'TagModificationResponse',
        'tag_security_modes_write_response': 'TagModificationResponse',
        'tag_authentication_response': 'TagAuthenticationResponse',
        'tag_memory_data': 'list[TagMemoryData]'
    }

    attribute_map = {
        'epc': 'epc',
        'epc_hex': 'epcHex',
        'tid': 'tid',
        'tid_hex': 'tidHex',
        'xpc_hex': 'xpcHex',
        'antenna_port': 'antennaPort',
        'antenna_name': 'antennaName',
        'transmit_power_cdbm': 'transmitPowerCdbm',
        'peak_rssi_cdbm': 'peakRssiCdbm',
        'frequency': 'frequency',
        'pc': 'pc',
        'last_seen_time': 'lastSeenTime',
        'phase_angle': 'phaseAngle',
        'tag_access_password_write_response': 'tagAccessPasswordWriteResponse',
        'tag_security_modes_write_response': 'tagSecurityModesWriteResponse',
        'tag_authentication_response': 'tagAuthenticationResponse',
        'tag_memory_data': 'tagMemoryData'
    }

    def __init__(self, epc=None, epc_hex=None, tid=None, tid_hex=None, xpc_hex=None, antenna_port=None, antenna_name=None, transmit_power_cdbm=None, peak_rssi_cdbm=None, frequency=None, pc=None, last_seen_time=None, phase_angle=None, tag_access_password_write_response=None, tag_security_modes_write_response=None, tag_authentication_response=None, tag_memory_data=None, _configuration=None):  # noqa: E501
        """TagInventoryEvent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._epc = None
        self._epc_hex = None
        self._tid = None
        self._tid_hex = None
        self._xpc_hex = None
        self._antenna_port = None
        self._antenna_name = None
        self._transmit_power_cdbm = None
        self._peak_rssi_cdbm = None
        self._frequency = None
        self._pc = None
        self._last_seen_time = None
        self._phase_angle = None
        self._tag_access_password_write_response = None
        self._tag_security_modes_write_response = None
        self._tag_authentication_response = None
        self._tag_memory_data = None
        self.discriminator = None

        if epc is not None:
            self.epc = epc
        if epc_hex is not None:
            self.epc_hex = epc_hex
        if tid is not None:
            self.tid = tid
        if tid_hex is not None:
            self.tid_hex = tid_hex
        if xpc_hex is not None:
            self.xpc_hex = xpc_hex
        if antenna_port is not None:
            self.antenna_port = antenna_port
        if antenna_name is not None:
            self.antenna_name = antenna_name
        if transmit_power_cdbm is not None:
            self.transmit_power_cdbm = transmit_power_cdbm
        if peak_rssi_cdbm is not None:
            self.peak_rssi_cdbm = peak_rssi_cdbm
        if frequency is not None:
            self.frequency = frequency
        if pc is not None:
            self.pc = pc
        if last_seen_time is not None:
            self.last_seen_time = last_seen_time
        if phase_angle is not None:
            self.phase_angle = phase_angle
        if tag_access_password_write_response is not None:
            self.tag_access_password_write_response = tag_access_password_write_response
        if tag_security_modes_write_response is not None:
            self.tag_security_modes_write_response = tag_security_modes_write_response
        if tag_authentication_response is not None:
            self.tag_authentication_response = tag_authentication_response
        if tag_memory_data is not None:
            self.tag_memory_data = tag_memory_data

    @property
    def epc(self):
        """Gets the epc of this TagInventoryEvent.  # noqa: E501


        :return: The epc of this TagInventoryEvent.  # noqa: E501
        :rtype: Epc
        """
        return self._epc

    @epc.setter
    def epc(self, epc):
        """Sets the epc of this TagInventoryEvent.


        :param epc: The epc of this TagInventoryEvent.  # noqa: E501
        :type: Epc
        """

        self._epc = epc

    @property
    def epc_hex(self):
        """Gets the epc_hex of this TagInventoryEvent.  # noqa: E501


        :return: The epc_hex of this TagInventoryEvent.  # noqa: E501
        :rtype: EpcHex
        """
        return self._epc_hex

    @epc_hex.setter
    def epc_hex(self, epc_hex):
        """Sets the epc_hex of this TagInventoryEvent.


        :param epc_hex: The epc_hex of this TagInventoryEvent.  # noqa: E501
        :type: EpcHex
        """

        self._epc_hex = epc_hex

    @property
    def tid(self):
        """Gets the tid of this TagInventoryEvent.  # noqa: E501


        :return: The tid of this TagInventoryEvent.  # noqa: E501
        :rtype: Tid
        """
        return self._tid

    @tid.setter
    def tid(self, tid):
        """Sets the tid of this TagInventoryEvent.


        :param tid: The tid of this TagInventoryEvent.  # noqa: E501
        :type: Tid
        """

        self._tid = tid

    @property
    def tid_hex(self):
        """Gets the tid_hex of this TagInventoryEvent.  # noqa: E501


        :return: The tid_hex of this TagInventoryEvent.  # noqa: E501
        :rtype: TidHex
        """
        return self._tid_hex

    @tid_hex.setter
    def tid_hex(self, tid_hex):
        """Sets the tid_hex of this TagInventoryEvent.


        :param tid_hex: The tid_hex of this TagInventoryEvent.  # noqa: E501
        :type: TidHex
        """

        self._tid_hex = tid_hex

    @property
    def xpc_hex(self):
        """Gets the xpc_hex of this TagInventoryEvent.  # noqa: E501


        :return: The xpc_hex of this TagInventoryEvent.  # noqa: E501
        :rtype: XpcHex
        """
        return self._xpc_hex

    @xpc_hex.setter
    def xpc_hex(self, xpc_hex):
        """Sets the xpc_hex of this TagInventoryEvent.


        :param xpc_hex: The xpc_hex of this TagInventoryEvent.  # noqa: E501
        :type: XpcHex
        """

        self._xpc_hex = xpc_hex

    @property
    def antenna_port(self):
        """Gets the antenna_port of this TagInventoryEvent.  # noqa: E501


        :return: The antenna_port of this TagInventoryEvent.  # noqa: E501
        :rtype: AntennaPort
        """
        return self._antenna_port

    @antenna_port.setter
    def antenna_port(self, antenna_port):
        """Sets the antenna_port of this TagInventoryEvent.


        :param antenna_port: The antenna_port of this TagInventoryEvent.  # noqa: E501
        :type: AntennaPort
        """

        self._antenna_port = antenna_port

    @property
    def antenna_name(self):
        """Gets the antenna_name of this TagInventoryEvent.  # noqa: E501


        :return: The antenna_name of this TagInventoryEvent.  # noqa: E501
        :rtype: AntennaName
        """
        return self._antenna_name

    @antenna_name.setter
    def antenna_name(self, antenna_name):
        """Sets the antenna_name of this TagInventoryEvent.


        :param antenna_name: The antenna_name of this TagInventoryEvent.  # noqa: E501
        :type: AntennaName
        """

        self._antenna_name = antenna_name

    @property
    def transmit_power_cdbm(self):
        """Gets the transmit_power_cdbm of this TagInventoryEvent.  # noqa: E501


        :return: The transmit_power_cdbm of this TagInventoryEvent.  # noqa: E501
        :rtype: TransmitPowerCdbm
        """
        return self._transmit_power_cdbm

    @transmit_power_cdbm.setter
    def transmit_power_cdbm(self, transmit_power_cdbm):
        """Sets the transmit_power_cdbm of this TagInventoryEvent.


        :param transmit_power_cdbm: The transmit_power_cdbm of this TagInventoryEvent.  # noqa: E501
        :type: TransmitPowerCdbm
        """

        self._transmit_power_cdbm = transmit_power_cdbm

    @property
    def peak_rssi_cdbm(self):
        """Gets the peak_rssi_cdbm of this TagInventoryEvent.  # noqa: E501

        The peak received power of the EPC backscatter in cdBm. We will give the client the opportunity to enable Impinj's high-precision mode to receive more accurate data.   # noqa: E501

        :return: The peak_rssi_cdbm of this TagInventoryEvent.  # noqa: E501
        :rtype: int
        """
        return self._peak_rssi_cdbm

    @peak_rssi_cdbm.setter
    def peak_rssi_cdbm(self, peak_rssi_cdbm):
        """Sets the peak_rssi_cdbm of this TagInventoryEvent.

        The peak received power of the EPC backscatter in cdBm. We will give the client the opportunity to enable Impinj's high-precision mode to receive more accurate data.   # noqa: E501

        :param peak_rssi_cdbm: The peak_rssi_cdbm of this TagInventoryEvent.  # noqa: E501
        :type: int
        """

        self._peak_rssi_cdbm = peak_rssi_cdbm

    @property
    def frequency(self):
        """Gets the frequency of this TagInventoryEvent.  # noqa: E501

        The frequency that was used to read the tag, in kHz.  # noqa: E501

        :return: The frequency of this TagInventoryEvent.  # noqa: E501
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this TagInventoryEvent.

        The frequency that was used to read the tag, in kHz.  # noqa: E501

        :param frequency: The frequency of this TagInventoryEvent.  # noqa: E501
        :type: int
        """

        self._frequency = frequency

    @property
    def pc(self):
        """Gets the pc of this TagInventoryEvent.  # noqa: E501

        The PC word (16-bits) backscattered by the inventoried tag.  # noqa: E501

        :return: The pc of this TagInventoryEvent.  # noqa: E501
        :rtype: str
        """
        return self._pc

    @pc.setter
    def pc(self, pc):
        """Sets the pc of this TagInventoryEvent.

        The PC word (16-bits) backscattered by the inventoried tag.  # noqa: E501

        :param pc: The pc of this TagInventoryEvent.  # noqa: E501
        :type: str
        """

        self._pc = pc

    @property
    def last_seen_time(self):
        """Gets the last_seen_time of this TagInventoryEvent.  # noqa: E501

        The UTC time at which the tag was last seen.   # noqa: E501

        :return: The last_seen_time of this TagInventoryEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._last_seen_time

    @last_seen_time.setter
    def last_seen_time(self, last_seen_time):
        """Sets the last_seen_time of this TagInventoryEvent.

        The UTC time at which the tag was last seen.   # noqa: E501

        :param last_seen_time: The last_seen_time of this TagInventoryEvent.  # noqa: E501
        :type: datetime
        """

        self._last_seen_time = last_seen_time

    @property
    def phase_angle(self):
        """Gets the phase_angle of this TagInventoryEvent.  # noqa: E501

        The phase angle in degrees of the tag that was read, accurate to two decimal places.   # noqa: E501

        :return: The phase_angle of this TagInventoryEvent.  # noqa: E501
        :rtype: float
        """
        return self._phase_angle

    @phase_angle.setter
    def phase_angle(self, phase_angle):
        """Sets the phase_angle of this TagInventoryEvent.

        The phase angle in degrees of the tag that was read, accurate to two decimal places.   # noqa: E501

        :param phase_angle: The phase_angle of this TagInventoryEvent.  # noqa: E501
        :type: float
        """
        if (self._configuration.client_side_validation and
                phase_angle is not None and phase_angle > 360):  # noqa: E501
            raise ValueError("Invalid value for `phase_angle`, must be a value less than or equal to `360`")  # noqa: E501
        if (self._configuration.client_side_validation and
                phase_angle is not None and phase_angle < 0):  # noqa: E501
            raise ValueError("Invalid value for `phase_angle`, must be a value greater than or equal to `0`")  # noqa: E501

        self._phase_angle = phase_angle

    @property
    def tag_access_password_write_response(self):
        """Gets the tag_access_password_write_response of this TagInventoryEvent.  # noqa: E501


        :return: The tag_access_password_write_response of this TagInventoryEvent.  # noqa: E501
        :rtype: TagModificationResponse
        """
        return self._tag_access_password_write_response

    @tag_access_password_write_response.setter
    def tag_access_password_write_response(self, tag_access_password_write_response):
        """Sets the tag_access_password_write_response of this TagInventoryEvent.


        :param tag_access_password_write_response: The tag_access_password_write_response of this TagInventoryEvent.  # noqa: E501
        :type: TagModificationResponse
        """

        self._tag_access_password_write_response = tag_access_password_write_response

    @property
    def tag_security_modes_write_response(self):
        """Gets the tag_security_modes_write_response of this TagInventoryEvent.  # noqa: E501


        :return: The tag_security_modes_write_response of this TagInventoryEvent.  # noqa: E501
        :rtype: TagModificationResponse
        """
        return self._tag_security_modes_write_response

    @tag_security_modes_write_response.setter
    def tag_security_modes_write_response(self, tag_security_modes_write_response):
        """Sets the tag_security_modes_write_response of this TagInventoryEvent.


        :param tag_security_modes_write_response: The tag_security_modes_write_response of this TagInventoryEvent.  # noqa: E501
        :type: TagModificationResponse
        """

        self._tag_security_modes_write_response = tag_security_modes_write_response

    @property
    def tag_authentication_response(self):
        """Gets the tag_authentication_response of this TagInventoryEvent.  # noqa: E501


        :return: The tag_authentication_response of this TagInventoryEvent.  # noqa: E501
        :rtype: TagAuthenticationResponse
        """
        return self._tag_authentication_response

    @tag_authentication_response.setter
    def tag_authentication_response(self, tag_authentication_response):
        """Sets the tag_authentication_response of this TagInventoryEvent.


        :param tag_authentication_response: The tag_authentication_response of this TagInventoryEvent.  # noqa: E501
        :type: TagAuthenticationResponse
        """

        self._tag_authentication_response = tag_authentication_response

    @property
    def tag_memory_data(self):
        """Gets the tag_memory_data of this TagInventoryEvent.  # noqa: E501

        This array will be provided if the tagMemoryReads parameter is specified for the `InventoryAntennaConfiguration` for the antenna generating this event.   # noqa: E501

        :return: The tag_memory_data of this TagInventoryEvent.  # noqa: E501
        :rtype: list[TagMemoryData]
        """
        return self._tag_memory_data

    @tag_memory_data.setter
    def tag_memory_data(self, tag_memory_data):
        """Sets the tag_memory_data of this TagInventoryEvent.

        This array will be provided if the tagMemoryReads parameter is specified for the `InventoryAntennaConfiguration` for the antenna generating this event.   # noqa: E501

        :param tag_memory_data: The tag_memory_data of this TagInventoryEvent.  # noqa: E501
        :type: list[TagMemoryData]
        """

        self._tag_memory_data = tag_memory_data

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
        if issubclass(TagInventoryEvent, dict):
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
        if not isinstance(other, TagInventoryEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TagInventoryEvent):
            return True

        return self.to_dict() != other.to_dict()