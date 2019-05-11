import os
from os.path import exists
from tornado.concurrent import return_future

from thumbor.loaders import LoaderResult
from thumbor.engines import BaseEngine

class LoaderResult(object):

    ERROR_NOT_FOUND = 'not_found'
    ERROR_UPSTREAM = 'upstream'
    ERROR_TIMEOUT = 'timeout'

    def __init__(self, buffer=None, successful=True, error=None, metadata=dict()):
        '''
        :param buffer: The media buffer
        :param successful: True when the media has been loaded.
        :type successful: bool
        :param error: Error code
        :type error: str
        :param metadata: Dictionary of metadata about the buffer
        :type metadata: dict
        '''

        self.buffer = buffer
        self.successful = successful
        self.error = error
        self.metadata = metadata