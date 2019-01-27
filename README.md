Thumbor-Spaces

## DigitalOcean Spaces adapter for thumbor

Provides a [Thumbor](https://github.com/thumbor/thumbor) result storage adapter for Spaces that stores files in DigitalOcean.

### Installing

Thumbor-Spaces can be easily installed using `pip install thumbor_spaces=='2.0'`.

### Configuration

Use spaces for result storage.
For more info on result storage: https://thumbor.readthedocs.io/en/latest/result_storage.html



/etc/thumbor.conf

    RESULT_STORAGE = 'thumbor_spaces.result_storages.spaces_storage'

    SPACES_REGION='xxx'

    SPACES_ENDPOINT='xxx'

    SPACES_KEY='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    SPACES_SECRET='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    SPACES_BUCKET='your-bucket-name'

    SPACES_ACL='public'