"""Credential management."""

import tomllib


class Credential:
    """Credential class.

    :param access_key_id: Access key ID.
    :type access_key_id: str
    :param secret_access_key: Secret access key.
    :type secret_access_key: str
    :param endpoint: Endpoint URL.
    :type endpoint: str
    :param kind: Storage type. As "obs" "s3" "minio" "gcs" "azure"
    :type kind: str
    """

    def __init__(self, access_key_id, secret_access_key, endpoint, kind):
        """Constructor method.
        """
        self._access_key_id = access_key_id
        self._secret_access_key = secret_access_key
        self._endpoint = endpoint
        # kind is storage type. like "obs" "s3" "minio" "gcs" "azure"
        self._kind = kind

    @classmethod
    def from_file(cls, filepath, kind='obs'):
        """Initialize credential from config file.

        :param filepath: config file path.
        :type filepath: str
        :param kind: config kind, only obs now.
        :type kind: str, optional

        :return: Credential object.
        :rtype: Credential
        """
        with open(filepath, 'rb') as file:
            config = tomllib.load(file)

            access_key_id = config["obs"]["access_key_id"]
            secret_access_key = config["obs"]["secret_access_key"]
            endpoint = config["obs"]["endpoint"]

            return \
                cls(access_key_id, secret_access_key, endpoint, kind)

    @property
    def access_key(self):
        """Access key property.
        """
        return self._access_key_id

    @property
    def secret_key(self):
        """Secret key property.
        """
        return self._secret_access_key

    @property
    def endpoint(self):
        """Endpoint url property.
        """
        return self._endpoint

    def __str__(self):
        """String representation.
        """
        return \
            f"access_key_id: {self._access_key_id}, " \
            f"secret_access_key: {self._secret_access_key}, " \
            f"endpoint: {self._endpoint}, " \
            f"kind: {self._kind}"