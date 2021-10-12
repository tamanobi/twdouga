import os
import boto3
import requests
import hashlib
import os
import io

def get_bucket():
    s3 = boto3.resource('s3',
        endpoint_url = 'https://s3.ap-northeast-1.wasabisys.com',
        aws_access_key_id = os.environ["WASABI_KEY"],
        aws_secret_access_key = os.environ["WASABI_SECRET"]
    )
    return s3.Bucket('sabamiso')

def get_json(offset: int):
    ENDPOINT=os.environ["ENDPOINT"]
    assert ENDPOINT.endswith("/") and ENDPOINT.startswith("https://")
    API = ENDPOINT + "list?offset={}&limit=10"
    res = requests.get(API.format(offset))
    return res.json()

class MyVideo:
    def __init__(self, obj) -> None:
        self.obj = obj
        self._binary = None
    
    @property
    def url(self):
        return self.obj["video_url"]
    
    @property
    def binary(self):
        if self._binary is None:
            res = requests.get(self.url)
            self._binary = res.content
        return self._binary

    @property
    def filename(self):
        from pathlib import Path

        path = Path(self.url)
        suffix = path.suffix
        if suffix.find("?") != -1:
            suffix = suffix[0:suffix.find("?")]
        
        stem = hashlib.sha256(self.binary).hexdigest()
        return stem[0:2] + "/" + stem + suffix

bucket = get_bucket()

videos = [MyVideo(x) for x in get_json(0)]
for offset in range(0, 30, 10):
    for row in get_json(offset):
        vid = MyVideo(row)
        with io.BytesIO(vid.binary) as f:
            bucket.upload_fileobj(f, vid.filename)
