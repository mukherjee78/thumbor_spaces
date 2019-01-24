#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    from thumbor.config import Config
    Config.define('SPACES_KEY', 'xxxxxx', 'Spaces api key', 'SPACES')
    Config.define('SPACES_SECRET', 'xxxxxx', 'Spaces api secret', 'SPACES')
    Config.define('SPACES_REGION', 'xxxxxx', 'Spaces api region', 'SPACES')
    Config.define('SPACES_ENDPOINT', 'xxxxxx', 'Spaces api endpoint', 'SPACES')
    Config.define('SPACES_BUCKET', 'xxxxxx', 'Spaces api endpoint', 'SPACES')
    
except ImportError:
    #Thumbor isn't installed yet
    pass

__version__ = "0.4"