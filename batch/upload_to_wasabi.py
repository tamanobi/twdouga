import os
import boto3
import requests
import hashlib
import os
import io
from abc import ABC, abstractmethod
from pathlib import Path
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)


class Uploader(ABC):
    @abstractmethod
    def upload(self, body: io.BytesIO, name: str):
        pass


class S3Uploader(Uploader):
    def __init__(self, s3_client) -> None:
        self.client = s3_client

    def upload(self, body: io.BytesIO, name: str):
        path = name[0:2] + "/" + name  # 分散のために名前の先頭二文字をフォルダとする
        self.client.upload_fileobj(body, path)


def get_bucket():
    s3 = boto3.resource(
        's3',
        endpoint_url = 'https://s3.ap-northeast-1.wasabisys.com',
        aws_access_key_id = os.environ["WASABI_KEY"],
        aws_secret_access_key = os.environ["WASABI_SECRET"]
    )
    return s3.Bucket('sabamiso')


class Crawler:
    def __init__(self, endpoint: str) -> None:
        assert endpoint.endswith("/") and endpoint.startswith("https://")
        self.endpoint = endpoint

    def get(self, offset: int) -> dict:
        url = self.endpoint + "list?offset={}&limit=10"
        res = requests.get(url.format(offset))
        return res.json()


class VideoInfoExtractor:
    def __init__(self, obj) -> None:
        self.obj = obj
        self._binary = None
    
    @property
    def url(self) -> str:
        return self.obj["video_url"]
    
    @property
    def binary(self) -> bytes:
        if self._binary is None:
            res = requests.get(self.url)
            self._binary = res.content
        return self._binary

    @property
    def filename(self) -> str:
        path = Path(self.url)
        suffix = path.suffix
        if suffix.find("?") != -1:
            suffix = suffix[0:suffix.find("?")]
        
        stem = hashlib.sha256(self.binary).hexdigest()
        return stem + suffix


if __name__ == "__main__":
    uploader = S3Uploader(get_bucket())
    crawler = Crawler(os.environ["ENDPOINT"])

    for offset in range(0, 200, 10):
        for row in crawler.get(offset):
            vid = VideoInfoExtractor(row)
            logger.info(vid.filename)
            with io.BytesIO(vid.binary) as f:
                uploader.upload(f, vid.filename)
