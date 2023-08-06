# wareroom
cloud object storage wrapper

## Usage
```bash
pip install wareroom
```

set cloud storage credentials in config file
```toml
[obs]
access_key_id = "xxxx"
secret_access_key = "xxxx"
endpoint="https://obs.cn-north-4.myhuaweicloud.com"
bucket="image"
```
replace access_key_id and secret_access_key with your own credentials


```python
from wareroom import Client

import tomllib


def read_config(filepath, kind='storage'):
    """Read storage config from toml file.
    
    :param filepath: path to config file
    :type filepath: str
    
    :param kind: kind of config, default is storage
    :type kind: str
    
    :return: return config keys
    :rtype: tuple, (str, str, str, str): access_id, secret_key, endpoint, bucket.
    """
    with open(filepath, "rb") as f:
        config = tomllib.load(f)

        access_key_id = config["storage"]["access_key_id"]
        secret_access_key = config["storage"]["secret_access_key"]
        endpoint = config["storage"]["endpoint"]
        bucket = config["storage"]["bucket"]
        return access_key_id, secret_access_key, endpoint, bucket

config_file = "config.toml"

# read access key from config file
access_key_id, secret_access_key, endpoint, bucket = read_config(config_file)

# create client
client = Client(access_key_id, secret_access_key, endpoint, bucket)

# upload file
filename = "test.jpg"
bucket = "image"

with open(filename, "rb") as file:
    result, content = client.add(bucket, filename, "image/jpeg", file)

# download file
result, content, buffer = client.get(bucket, filename)

# delete file
result, content = client.delete(bucket, filename)
```

## api

### read_config
read cloud storage credentials from config file

    Read obs config from toml file.

    Args:
        filepath (str): toml config file path.
        kind (str): config kind, only obs now.
    Returns:
        (str, str, str, str): access_id, secret_key, endpoint, bucket.

### Client.add
upload file to cloud storage

if upload success, return True and url, else return False and reason

    Args:
        bucket (str): OBS bucket name.
        filename (str): filename.
        content_type (str): image MIME type / media type e.g. image/png or text/markdown.
        file (File) :  A SpooledTemporaryFile (a file-like object).
        This is the actual Python file that you can pass directly to other functions
        or libraries that expect a "file-like" object.

    Returns:
        (bool, str): (True/False, url/reason)


### Client.get
download file from cloud storage

if download success, return True, content type, file buffer, 
else return False ,reason and ""

    Args:
        bucket (str): OBS bucket name.
        filename (str): filename.

    Returns:
        (bool, str, File): (True/False, reason, file buffer)

        Args:
            bucket (str): OBS bucket name.
            filename (str): filename
        
        Returns:
            (bool, str, str): (True/False, content_type/reason, buffer/"")


### Client.delete
delete file from cloud storage

if delete success, return True and success message, else return False and reason

        Args:
            bucket (str): OBS bucket name.
            filename (str): filename
        Returns:
            (bool, str): (True/False, message/reason)


