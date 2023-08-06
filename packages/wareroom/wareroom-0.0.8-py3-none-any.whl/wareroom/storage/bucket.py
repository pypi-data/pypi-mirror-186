"""Bucket management."""

import tomllib


class Bucket:
    """Bucket class.

    :param name: Bucket name.
    :type name: str
    """

    def __init__(self, name):
        """Constructor method.
        """
        self._name = name

    @classmethod
    def from_file(cls, filepath, kind='obs'):
        """Initialize bucket from config file.

        :param filepath: config file path.
        :type filepath: str
        :param kind: config kind, only obs now.
        :type kind: str, optional

        :return: Credential object.
        :rtype: Credential
        """
        with open(filepath, 'rb') as file:
            config = tomllib.load(file)
            bucket= config["obs"]["bucket"]

            return \
                cls(bucket)

    @property
    def name(self):
        """Bucket name property.
        """
        return self._name

    def __str__(self):
        """String representation.
        """
        return \
            f"bucket name: {self._name}"
