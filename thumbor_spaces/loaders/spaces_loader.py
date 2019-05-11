from os import fstat
from datetime import datetime
from os.path import join, exists, abspath

from six.moves.urllib.parse import unquote
from tornado.concurrent import return_future

from thumbor.loaders import http_loader
from thumbor.loaders import LoaderResult

from thumbor.utils import logger

import boto3
from botocore.client import Config


@return_future
def load(context, path, callback):
    logger.debug("INSIDE SPACES LOADER")
    logger.debug(path)
    logger.debug(context.request.url)
    chker1 = context.config.SPACES_BUCKET+'.'+context.config.SPACES_ENDPOINT+'.digitaloceanspaces.com'
    chker2 = '/storage/'
    if chker1 not in context.request.url and chker2 not in context.request.url:
        logger.debug(path)
        http_loader.load(context, path, callback)
    else:
        key = get_key_name(context, context.request.url)
        session = boto3.session.Session()
        client = session.client('s3',
                                    region_name=context.config.SPACES_REGION,
                                    endpoint_url='https://'+context.config.SPACES_ENDPOINT+'.digitaloceanspaces.com',
                                    aws_access_key_id=context.config.SPACES_KEY,
                                    aws_secret_access_key=context.config.SPACES_SECRET)
        url = client.generate_presigned_url(ClientMethod='get_object', 
                                                Params={
                                                    'Bucket': context.config.SPACES_BUCKET,
                                                    'Key': key
                                                }, ExpiresIn=300)
        logger.debug(url)
        def noop(url):
            return url
        http_loader.load_sync(context, url, callback, normalize_url_func=noop)

def get_key_name(context, path):
    path_segments = path.lstrip('/').split("/")
    storage_index = index_containing_substring(path_segments, 'storage')
    return '/'.join(path_segments[storage_index:])

def index_containing_substring(the_list, substring):
    for i, s in enumerate(the_list):
        if substring in s:
              return i
    return -1