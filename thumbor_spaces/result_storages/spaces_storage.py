#!/usr/bin/python
# -*- coding: utf-8 -*-

from thumbor.utils import logger
from thumbor.result_storages import BaseStorage, ResultStorageResult
from tornado.concurrent import return_future

import boto3
from botocore.client import Config
from io import BytesIO

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
        buff = BytesIO(bytes)
        session = boto3.session.Session()
        client = session.client('s3',
                                region_name=self.context.config.SPACES_REGION,
                                endpoint_url='https://'+self.context.config.SPACES_ENDPOINT+'.digitaloceanspaces.com',
                                aws_access_key_id=self.context.config.SPACES_KEY,
                                aws_secret_access_key=self.context.config.SPACES_SECRET)
        client.upload_fileobj(buff, self.context.config.SPACES_BUCKET, key, ExtraArgs={'ACL':self.context.config.SPACES_ACL})

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
            client.Bucket(self.context.config.SPACES_BUCKET).Object(key).upload_fileobj(buff)
            result = ResultStorageResult()
            result.buffer = buff
            callback(result)
        except:
            callback(None)
        callback(None)

    def get_key_name(self, path):
        path_segments = path.lstrip('/').split("/")
        return '/'.join(['result_storage', path_segments[0], path_segments[-1:][0]])
