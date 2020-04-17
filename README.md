This package implements function for reading config file from S3.
Example:
```
import os
import avanan_config_utils
config_file = os.environ['CONFIG_FILE']
config_bucket = os.environ.get('CONFIG_BUCKET')
config_dict = avanan_config_utils.get_config_dict(config_file, config_bucket)
```
