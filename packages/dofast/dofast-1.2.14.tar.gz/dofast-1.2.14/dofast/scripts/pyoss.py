#!/usr/bin/env python
from codefast.io.file import ProgressBar
from dataclasses import dataclass

import codefast as cf
import oss2
import os
from dofast.auth import auth


@dataclass
class AppInfo:
    id: str = auth.oss['access_id']
    secret: str = auth.oss['access_secret']
    region: str = auth.oss['region']


class Client(object):
    def __init__(self, appinfo=AppInfo(), bucket_name: str = "ali-oss-bucket-1"):
        self.appinfo = appinfo
        _id, _secret = self.appinfo.id, self.appinfo.secret
        self.oss_auth = oss2.Auth(_id, _secret)
        self.server = oss2.Service(self.oss_auth, self.appinfo.region)
        self.bucket = oss2.Bucket(
            self.oss_auth, self.appinfo.region, bucket_name)

    def upload(self, local_file_name: str, remote_dir: str = 'tmp') -> str:
        basename = cf.io.basename(local_file_name)
        remote_object_name = "{}/{}".format(remote_dir, basename)

        pb = ProgressBar()

        def progress_bar(*args):
            pb.run(args[0], args[1])
        self.bucket.put_object_from_file(
            remote_object_name, local_file_name, progress_callback=progress_bar)

        audio_url = self.bucket.sign_url('GET',
                                         remote_object_name,
                                         3600,
                                         slash_safe=True)
        return audio_url
