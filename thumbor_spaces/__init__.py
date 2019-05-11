#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    from thumbor.config import Config
    Config.define('SPACES_KEY', 'xxxxxx', 'Spaces api key', 'SPACES')
    Config.define('SPACES_SECRET', 'xxxxxx', 'Spaces api secret', 'SPACES')
    Config.define('SPACES_REGION', 'xxxxxx', 'Spaces api region', 'SPACES')
    Config.define('SPACES_ENDPOINT', 'xxxxxx', 'Spaces api endpoint', 'SPACES')
    Config.define('SPACES_BUCKET', 'xxxxxx', 'Spaces api endpoint', 'SPACES')
    Config.define('SPACES_ACL', 'public-read', 'Spaces image acl', 'SPACES')
    Config.define('SPACES_RESULT_FOLDER', 'result_storage', 'Spaces result storage folder', 'SPACES')
    Config.define('SPACES_LOADER_FOLDER', 'storage', 'Spaces loader storage folder', 'SPACES')
    
except ImportError:
    #Thumbor isn't installed yet
    pass

__version__ = "2.2"