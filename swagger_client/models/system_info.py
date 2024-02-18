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


class SystemInfo(object):
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
        'product_model': 'str',
        'manufacturer': 'str',
        'product_description': 'str',
        'product_sku': 'str',
        'product_hla': 'str',
        'pcba': 'str',
        'serial_number': 'str'
    }

    attribute_map = {
        'product_model': 'productModel',
        'manufacturer': 'manufacturer',
        'product_description': 'productDescription',
        'product_sku': 'productSku',
        'product_hla': 'productHla',
        'pcba': 'pcba',
        'serial_number': 'serialNumber'
    }

    def __init__(self, product_model=None, manufacturer=None, product_description=None, product_sku=None, product_hla=None, pcba=None, serial_number=None, _configuration=None):  # noqa: E501
        """SystemInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._product_model = None
        self._manufacturer = None
        self._product_description = None
        self._product_sku = None
        self._product_hla = None
        self._pcba = None
        self._serial_number = None
        self.discriminator = None

        self.product_model = product_model
        self.manufacturer = manufacturer
        self.product_description = product_description
        self.product_sku = product_sku
        self.product_hla = product_hla
        self.pcba = pcba
        self.serial_number = serial_number

    @property
    def product_model(self):
        """Gets the product_model of this SystemInfo.  # noqa: E501

        The model number of the reader.  # noqa: E501

        :return: The product_model of this SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._product_model

    @product_model.setter
    def product_model(self, product_model):
        """Sets the product_model of this SystemInfo.

        The model number of the reader.  # noqa: E501

        :param product_model: The product_model of this SystemInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and product_model is None:
            raise ValueError("Invalid value for `product_model`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                product_model is not None and len(product_model) > 32):
            raise ValueError("Invalid value for `product_model`, length must be less than or equal to `32`")  # noqa: E501

        self._product_model = product_model

    @property
    def manufacturer(self):
        """Gets the manufacturer of this SystemInfo.  # noqa: E501

        The reader manufacturer.  # noqa: E501

        :return: The manufacturer of this SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this SystemInfo.

        The reader manufacturer.  # noqa: E501

        :param manufacturer: The manufacturer of this SystemInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and manufacturer is None:
            raise ValueError("Invalid value for `manufacturer`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                manufacturer is not None and len(manufacturer) > 32):
            raise ValueError("Invalid value for `manufacturer`, length must be less than or equal to `32`")  # noqa: E501

        self._manufacturer = manufacturer

    @property
    def product_description(self):
        """Gets the product_description of this SystemInfo.  # noqa: E501

        A short, human-friendly description of the reader.  # noqa: E501

        :return: The product_description of this SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        """Sets the product_description of this SystemInfo.

        A short, human-friendly description of the reader.  # noqa: E501

        :param product_description: The product_description of this SystemInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and product_description is None:
            raise ValueError("Invalid value for `product_description`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                product_description is not None and len(product_description) > 64):
            raise ValueError("Invalid value for `product_description`, length must be less than or equal to `64`")  # noqa: E501

        self._product_description = product_description

    @property
    def product_sku(self):
        """Gets the product_sku of this SystemInfo.  # noqa: E501

        The official product SKU for the reader.  # noqa: E501

        :return: The product_sku of this SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._product_sku

    @product_sku.setter
    def product_sku(self, product_sku):
        """Sets the product_sku of this SystemInfo.

        The official product SKU for the reader.  # noqa: E501

        :param product_sku: The product_sku of this SystemInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and product_sku is None:
            raise ValueError("Invalid value for `product_sku`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                product_sku is not None and len(product_sku) > 32):
            raise ValueError("Invalid value for `product_sku`, length must be less than or equal to `32`")  # noqa: E501

        self._product_sku = product_sku

    @property
    def product_hla(self):
        """Gets the product_hla of this SystemInfo.  # noqa: E501

        The reader's high-level assembly code.  # noqa: E501

        :return: The product_hla of this SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._product_hla

    @product_hla.setter
    def product_hla(self, product_hla):
        """Sets the product_hla of this SystemInfo.

        The reader's high-level assembly code.  # noqa: E501

        :param product_hla: The product_hla of this SystemInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and product_hla is None:
            raise ValueError("Invalid value for `product_hla`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                product_hla is not None and len(product_hla) > 32):
            raise ValueError("Invalid value for `product_hla`, length must be less than or equal to `32`")  # noqa: E501

        self._product_hla = product_hla

    @property
    def pcba(self):
        """Gets the pcba of this SystemInfo.  # noqa: E501

        The assembly code for the reader's PCB.  # noqa: E501

        :return: The pcba of this SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._pcba

    @pcba.setter
    def pcba(self, pcba):
        """Sets the pcba of this SystemInfo.

        The assembly code for the reader's PCB.  # noqa: E501

        :param pcba: The pcba of this SystemInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and pcba is None:
            raise ValueError("Invalid value for `pcba`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                pcba is not None and len(pcba) > 32):
            raise ValueError("Invalid value for `pcba`, length must be less than or equal to `32`")  # noqa: E501

        self._pcba = pcba

    @property
    def serial_number(self):
        """Gets the serial_number of this SystemInfo.  # noqa: E501

        The serial number of the reader.  # noqa: E501

        :return: The serial_number of this SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this SystemInfo.

        The serial number of the reader.  # noqa: E501

        :param serial_number: The serial_number of this SystemInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                serial_number is not None and len(serial_number) > 32):
            raise ValueError("Invalid value for `serial_number`, length must be less than or equal to `32`")  # noqa: E501

        self._serial_number = serial_number

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
        if issubclass(SystemInfo, dict):
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
        if not isinstance(other, SystemInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemInfo):
            return True

        return self.to_dict() != other.to_dict()