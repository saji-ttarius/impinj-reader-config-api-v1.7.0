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


class TagMemoryData(object):
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
        'memory_bank': 'TagMemoryBank',
        'word_offset': 'int',
        'tag_data_hex': 'str'
    }

    attribute_map = {
        'memory_bank': 'memoryBank',
        'word_offset': 'wordOffset',
        'tag_data_hex': 'tagDataHex'
    }

    def __init__(self, memory_bank=None, word_offset=None, tag_data_hex=None, _configuration=None):  # noqa: E501
        """TagMemoryData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._memory_bank = None
        self._word_offset = None
        self._tag_data_hex = None
        self.discriminator = None

        self.memory_bank = memory_bank
        self.word_offset = word_offset
        self.tag_data_hex = tag_data_hex

    @property
    def memory_bank(self):
        """Gets the memory_bank of this TagMemoryData.  # noqa: E501


        :return: The memory_bank of this TagMemoryData.  # noqa: E501
        :rtype: TagMemoryBank
        """
        return self._memory_bank

    @memory_bank.setter
    def memory_bank(self, memory_bank):
        """Sets the memory_bank of this TagMemoryData.


        :param memory_bank: The memory_bank of this TagMemoryData.  # noqa: E501
        :type: TagMemoryBank
        """
        if self._configuration.client_side_validation and memory_bank is None:
            raise ValueError("Invalid value for `memory_bank`, must not be `None`")  # noqa: E501

        self._memory_bank = memory_bank

    @property
    def word_offset(self):
        """Gets the word_offset of this TagMemoryData.  # noqa: E501

        The offset, in 16-bit words, relative to the start of the specified memory bank, from where the memory was read.   # noqa: E501

        :return: The word_offset of this TagMemoryData.  # noqa: E501
        :rtype: int
        """
        return self._word_offset

    @word_offset.setter
    def word_offset(self, word_offset):
        """Sets the word_offset of this TagMemoryData.

        The offset, in 16-bit words, relative to the start of the specified memory bank, from where the memory was read.   # noqa: E501

        :param word_offset: The word_offset of this TagMemoryData.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and word_offset is None:
            raise ValueError("Invalid value for `word_offset`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                word_offset is not None and word_offset > 65535):  # noqa: E501
            raise ValueError("Invalid value for `word_offset`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self._configuration.client_side_validation and
                word_offset is not None and word_offset < 0):  # noqa: E501
            raise ValueError("Invalid value for `word_offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._word_offset = word_offset

    @property
    def tag_data_hex(self):
        """Gets the tag_data_hex of this TagMemoryData.  # noqa: E501

        The hex-encoded contents of the tag's memory. An empty string is sent by the device if the tag memory read was not successful.   # noqa: E501

        :return: The tag_data_hex of this TagMemoryData.  # noqa: E501
        :rtype: str
        """
        return self._tag_data_hex

    @tag_data_hex.setter
    def tag_data_hex(self, tag_data_hex):
        """Sets the tag_data_hex of this TagMemoryData.

        The hex-encoded contents of the tag's memory. An empty string is sent by the device if the tag memory read was not successful.   # noqa: E501

        :param tag_data_hex: The tag_data_hex of this TagMemoryData.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and tag_data_hex is None:
            raise ValueError("Invalid value for `tag_data_hex`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                tag_data_hex is not None and not re.search(r'^[0-9A-F]*$', tag_data_hex)):  # noqa: E501
            raise ValueError(r"Invalid value for `tag_data_hex`, must be a follow pattern or equal to `/^[0-9A-F]*$/`")  # noqa: E501

        self._tag_data_hex = tag_data_hex

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
        if issubclass(TagMemoryData, dict):
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
        if not isinstance(other, TagMemoryData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TagMemoryData):
            return True

        return self.to_dict() != other.to_dict()
