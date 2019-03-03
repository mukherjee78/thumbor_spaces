#!/usr/bin/python
# -*- coding: utf-8 -*-

from thumbor.utils import logger
from thumbor.result_storages import BaseStorage, ResultStorageResult
from tornado.concurrent import return_future

import boto3
from botocore.client import Config
from io import BytesIO
import re
import magic
import mimetypes

class Storage(BaseStorage):
    def __init__(self, context):
        self.context = context

    @property
    def is_auto_webp(self):
        return self.context.config.AUTO_WEBP and self.context.request.accepts_webp

    @return_future
    def put(self, bytes, callback=None):
        logger.debug("INSIDE SPACES PUT")
        key = self.get_key_name(self.context.request.url)
        file_name = self.get_file_name(self.context.request.url)
        buff = BytesIO(bytes)
        session = boto3.session.Session()
        client = session.client('s3',
                                region_name=self.context.config.SPACES_REGION,
                                endpoint_url='https://'+self.context.config.SPACES_ENDPOINT+'.digitaloceanspaces.com',
                                aws_access_key_id=self.context.config.SPACES_KEY,
                                aws_secret_access_key=self.context.config.SPACES_SECRET)
        content_type = self.get_content_type(buff, file_name)
        client.upload_fileobj(buff, 
                                self.context.config.SPACES_BUCKET, 
                                key, 
                                ExtraArgs={
                                    'ACL':self.context.config.SPACES_ACL,
                                    'ContentType':content_type,
                                    'ContentDisposition':'inline',
                                    'CacheControl':'max-age=290304000, public',
                                    'Metadata': {
                                        'ContentType':content_type,
                                        'ContentDisposition':'inline',
                                        'CacheControl':'max-age=290304000, public',
                                    }
                                })

        if callback is None:
            def callback(key):
                logger.info("INSIDE SPACES PUT")

        callback(True)

    @return_future
    def get(self, callback):
        logger.debug("INSIDE SPACES GET")
        key = self.get_key_name(self.context.request.url)
        buff = BytesIO()
        session = boto3.session.Session()
        client = session.resource('s3',
                                    region_name=self.context.config.SPACES_REGION,
                                    endpoint_url='https://'+self.context.config.SPACES_ENDPOINT+'.digitaloceanspaces.com',
                                    aws_access_key_id=self.context.config.SPACES_KEY,
                                    aws_secret_access_key=self.context.config.SPACES_SECRET)
        try:
            objkey = client.Bucket(self.context.config.SPACES_BUCKET).Object(key)
            objkey.download_fileobj(buff)
            result = ResultStorageResult()
            result.buffer = buff
            result.metadata = objkey.get_metadata("Metadata")
            result.metadata.pop('Body')
            logger.debug(result.metadata)
            callback(result)
        except:
            callback(None)
        callback(None)

    def get_file_name(self, path):
        path_segments = path.lstrip('/').split("/")
        key = re.sub('[^0-9a-zA-Z]+', '_', path_segments[0])
        return path_segments[-1:][0]

    def get_key_name(self, path):
        path_segments = path.lstrip('/').split("/")
        key = re.sub('[^0-9a-zA-Z]+', '_', path_segments[0])
        key = '/'.join([self.context.config.SPACES_RESULT_FOLDER, key, path_segments[-1:][0]])
        return key

    def get_content_type(self, buff, name):
        try:
            return magic.from_buffer(buff, mime=True)
        except:
            name_segments = name.split(".")
            extn = '.'+'.'.join(name_segments[1:])
            mimetypes.init()
            return mimetypes.types_map[extn]