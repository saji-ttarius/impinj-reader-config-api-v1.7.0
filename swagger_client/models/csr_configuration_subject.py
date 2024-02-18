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


class CsrConfigurationSubject(object):
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
        'country': 'str',
        'state': 'str',
        'locality': 'str',
        'organization': 'str',
        'organizational_unit': 'str',
        'common_name': 'str'
    }

    attribute_map = {
        'country': 'country',
        'state': 'state',
        'locality': 'locality',
        'organization': 'organization',
        'organizational_unit': 'organizationalUnit',
        'common_name': 'commonName'
    }

    def __init__(self, country=None, state=None, locality=None, organization=None, organizational_unit=None, common_name=None, _configuration=None):  # noqa: E501
        """CsrConfigurationSubject - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._country = None
        self._state = None
        self._locality = None
        self._organization = None
        self._organizational_unit = None
        self._common_name = None
        self.discriminator = None

        if country is not None:
            self.country = country
        if state is not None:
            self.state = state
        if locality is not None:
            self.locality = locality
        if organization is not None:
            self.organization = organization
        if organizational_unit is not None:
            self.organizational_unit = organizational_unit
        self.common_name = common_name

    @property
    def country(self):
        """Gets the country of this CsrConfigurationSubject.  # noqa: E501

        The 2-letter country name.  # noqa: E501

        :return: The country of this CsrConfigurationSubject.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CsrConfigurationSubject.

        The 2-letter country name.  # noqa: E501

        :param country: The country of this CsrConfigurationSubject.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                country is not None and len(country) > 2):
            raise ValueError("Invalid value for `country`, length must be less than or equal to `2`")  # noqa: E501

        self._country = country

    @property
    def state(self):
        """Gets the state of this CsrConfigurationSubject.  # noqa: E501

        The state or province name.  # noqa: E501

        :return: The state of this CsrConfigurationSubject.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CsrConfigurationSubject.

        The state or province name.  # noqa: E501

        :param state: The state of this CsrConfigurationSubject.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                state is not None and len(state) > 64):
            raise ValueError("Invalid value for `state`, length must be less than or equal to `64`")  # noqa: E501

        self._state = state

    @property
    def locality(self):
        """Gets the locality of this CsrConfigurationSubject.  # noqa: E501

        The locality or city name.  # noqa: E501

        :return: The locality of this CsrConfigurationSubject.  # noqa: E501
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this CsrConfigurationSubject.

        The locality or city name.  # noqa: E501

        :param locality: The locality of this CsrConfigurationSubject.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                locality is not None and len(locality) > 64):
            raise ValueError("Invalid value for `locality`, length must be less than or equal to `64`")  # noqa: E501

        self._locality = locality

    @property
    def organization(self):
        """Gets the organization of this CsrConfigurationSubject.  # noqa: E501

        The organization associated with the certificate.  # noqa: E501

        :return: The organization of this CsrConfigurationSubject.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this CsrConfigurationSubject.

        The organization associated with the certificate.  # noqa: E501

        :param organization: The organization of this CsrConfigurationSubject.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                organization is not None and len(organization) > 64):
            raise ValueError("Invalid value for `organization`, length must be less than or equal to `64`")  # noqa: E501

        self._organization = organization

    @property
    def organizational_unit(self):
        """Gets the organizational_unit of this CsrConfigurationSubject.  # noqa: E501

        The organization unit associated with the certificate.  # noqa: E501

        :return: The organizational_unit of this CsrConfigurationSubject.  # noqa: E501
        :rtype: str
        """
        return self._organizational_unit

    @organizational_unit.setter
    def organizational_unit(self, organizational_unit):
        """Sets the organizational_unit of this CsrConfigurationSubject.

        The organization unit associated with the certificate.  # noqa: E501

        :param organizational_unit: The organizational_unit of this CsrConfigurationSubject.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                organizational_unit is not None and len(organizational_unit) > 64):
            raise ValueError("Invalid value for `organizational_unit`, length must be less than or equal to `64`")  # noqa: E501

        self._organizational_unit = organizational_unit

    @property
    def common_name(self):
        """Gets the common_name of this CsrConfigurationSubject.  # noqa: E501

        The common name or hostname for the certificate.  # noqa: E501

        :return: The common_name of this CsrConfigurationSubject.  # noqa: E501
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this CsrConfigurationSubject.

        The common name or hostname for the certificate.  # noqa: E501

        :param common_name: The common_name of this CsrConfigurationSubject.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and common_name is None:
            raise ValueError("Invalid value for `common_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                common_name is not None and len(common_name) > 64):
            raise ValueError("Invalid value for `common_name`, length must be less than or equal to `64`")  # noqa: E501
        if (self._configuration.client_side_validation and
                common_name is not None and len(common_name) < 2):
            raise ValueError("Invalid value for `common_name`, length must be greater than or equal to `2`")  # noqa: E501

        self._common_name = common_name

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
        if issubclass(CsrConfigurationSubject, dict):
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
        if not isinstance(other, CsrConfigurationSubject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CsrConfigurationSubject):
            return True

        return self.to_dict() != other.to_dict()
