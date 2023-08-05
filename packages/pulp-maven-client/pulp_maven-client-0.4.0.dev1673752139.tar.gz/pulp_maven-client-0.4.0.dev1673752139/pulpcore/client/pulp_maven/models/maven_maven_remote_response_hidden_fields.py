# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_maven.configuration import Configuration


class MavenMavenRemoteResponseHiddenFields(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'is_set': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'is_set': 'is_set'
    }

    def __init__(self, name=None, is_set=None, local_vars_configuration=None):  # noqa: E501
        """MavenMavenRemoteResponseHiddenFields - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._is_set = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if is_set is not None:
            self.is_set = is_set

    @property
    def name(self):
        """Gets the name of this MavenMavenRemoteResponseHiddenFields.  # noqa: E501


        :return: The name of this MavenMavenRemoteResponseHiddenFields.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MavenMavenRemoteResponseHiddenFields.


        :param name: The name of this MavenMavenRemoteResponseHiddenFields.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_set(self):
        """Gets the is_set of this MavenMavenRemoteResponseHiddenFields.  # noqa: E501


        :return: The is_set of this MavenMavenRemoteResponseHiddenFields.  # noqa: E501
        :rtype: bool
        """
        return self._is_set

    @is_set.setter
    def is_set(self, is_set):
        """Sets the is_set of this MavenMavenRemoteResponseHiddenFields.


        :param is_set: The is_set of this MavenMavenRemoteResponseHiddenFields.  # noqa: E501
        :type: bool
        """

        self._is_set = is_set

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MavenMavenRemoteResponseHiddenFields):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MavenMavenRemoteResponseHiddenFields):
            return True

        return self.to_dict() != other.to_dict()
