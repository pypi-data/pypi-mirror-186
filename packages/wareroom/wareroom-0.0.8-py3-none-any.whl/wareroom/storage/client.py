"""Cloud Object Based Storage backend."""
from obs import ObsClient, PutObjectHeader
from .credential import Credential
from .bucket import Bucket


class Client:
    """Cloud Storage Backend.

    :param credentials: Cloud Storage credentials.
    :type credentials: :class:`Credential`
    """

    def __init__(self, credentials):
        """Initialize the cloud storage backend.
        """
        self._client = ObsClient(credentials.access_key,
                                 credentials.secret_key,
                                 server=credentials.endpoint)
        self._bucket = None

    @property
    def bucket(self) -> Bucket:
        """Get bucket name.

        :return: bucket name
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket: Bucket):
        """Set bucket name.

        :param bucket: bucket name
        :type Bucket: bucket object
        """
        self._bucket = bucket

    def add(self, filename, content_type, file, bucket=None):
        """Add file to cloud storage.

        :param filename: filename.
        :type filename: str
        :param content_type: image MIME type / media type e.g. image/png or text/markdown.
        :type content_type: str
        :param file: A SpooledTemporaryFile (a file-like object).
            This is the actual Python file that you can pass directly to other functions
            or libraries that expect a "file-like" object.
        :type file: File
        :param bucket: bucket name. If bucket is None, use default bucket.
        :type bucket: str, optional

        :return: if success return (True, url), else return (False, reason)
        :rtype: (bool, str)
        """
        # set bucket_name
        bucket = bucket if bucket else self._bucket
        if bucket.name is None:
            return False, "bucket name is None"

        # check is has same file
        result = self._client.getObjectMetadata(bucket.name, filename)
        if result.status < 300:
            # has same file
            return False, "has same file"

        # upload file to storage
        headers = PutObjectHeader(contentType=content_type)
        result = self._client.putContent(bucket.name, filename, file, headers)

        # upload success
        if result.status < 300:
            # return true and file url
            return True, result.body.objectUrl

        # upload failed, return false and error message
        return False, result.reason

    def delete(self, filename, bucket=None):
        """Delete file from cloud storage.

        :param filename: filename
        :type filename: str
        :param bucket: bucket name. If bucket is None, use default bucket.
        :type bucket: str, optional

        :return: if success return (True, message), else return (False, reason)
        :rtype: (bool, str)
        """
        # set bucket_name
        bucket = bucket if bucket else self._bucket
        if bucket.name is None:
            return False, "bucket name is None"

        # delete object
        result = self._client.deleteObject(bucket.name, filename)

        # delete success
        if result.status < 300:
            return True, "delete success"

        # delete failed
        return False, result.reason

    def get(self, filename, bucket=None):
        """Get file from cloud storage.

        :param filename: filename
        :type filename: str
        :param bucket: bucket name. if bucket is None, use default bucket.
        :type bucket: str, optional

        :return: if success return (True, filetype, buffer),
            else return (False, reason, "")
        :rtype: (bool, str, str/bytes)
        """
        # set bucket_name
        bucket = bucket if bucket else self._bucket
        if bucket.name is None:
            return False, "bucket name is None", ""

        # get object from cloud
        result = self._client.getObject(bucket.name, filename,
                                        loadStreamInMemory=True)

        if result.status < 300:
            return True, result.body["contentType"], result.body.buffer

        return False, result.reason, ""
