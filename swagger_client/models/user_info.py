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


class UserInfo(object):
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
        'user_id': 'int',
        'username': 'str'
    }

    attribute_map = {
        'user_id': 'userId',
        'username': 'username'
    }

    def __init__(self, user_id=None, username=None, _configuration=None):  # noqa: E501
        """UserInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_id = None
        self._username = None
        self.discriminator = None

        self.user_id = user_id
        self.username = username

    @property
    def user_id(self):
        """Gets the user_id of this UserInfo.  # noqa: E501

        A unique identifier for the user. This identifier does not persist across reboots, but will not change as long as the reader is up and running.   # noqa: E501

        :return: The user_id of this UserInfo.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserInfo.

        A unique identifier for the user. This identifier does not persist across reboots, but will not change as long as the reader is up and running.   # noqa: E501

        :param user_id: The user_id of this UserInfo.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                user_id is not None and user_id < 0):  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._user_id = user_id

    @property
    def username(self):
        """Gets the username of this UserInfo.  # noqa: E501

        The name of the user.  # noqa: E501

        :return: The username of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserInfo.

        The name of the user.  # noqa: E501

        :param username: The username of this UserInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                username is not None and len(username) > 64):
            raise ValueError("Invalid value for `username`, length must be less than or equal to `64`")  # noqa: E501
        if (self._configuration.client_side_validation and
                username is not None and len(username) < 1):
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

        self._username = username

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
        if issubclass(UserInfo, dict):
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
        if not isinstance(other, UserInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserInfo):
            return True

        return self.to_dict() != other.to_dict()
