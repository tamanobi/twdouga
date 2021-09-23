from fastapi import FastAPI
import requests
from typing import Optional

app = FastAPI()

class Twitter:
    _API_BASE = 'https://api.twitter.com/1.1/'
    headers = {}

    def __init__(self) -> None:
        self.headers.update({'x-guest-token': self.get_guest_token()})

    def _post(self, api: str, params: dict = {}):
        return requests.post(self._API_BASE + api, params=params, headers=self.headers).json()

    def _get(self, api: str, params: dict = {}):
        return requests.get(self._API_BASE + api, params=params, headers=self.headers).json()

    def get_guest_token(self) -> str:
        """副作用あり"""
        self.headers.update({'Authorization':  'Bearer AAAAAAAAAAAAAAAAAAAAAPYXBAAAAAAACLXUNDekMxqa8h%2F40K4moUkGsoc%3DTYfbDKbT3jJPCEVnMYqilB28NHfOPqkca3qaAxGfsyKCs0wRbw'})  # cspell:disable-line
        return self._post('guest/activate.json')['guest_token']
    
    def _url_to_status_id(self, url: str) -> Optional[str]:
        import re
        if m := re.search("status/([0-9]+)", url):
            return m[1]
        return None

    def get_tweet(self, url: str) -> dict:
        if id_ := self._url_to_status_id(url):
            return self._get('statuses/show.json', {'id': id_})

        return {}
    
    def get_video_url(self, url) -> Optional[dict]:
        variants = self.get_tweet(url).get("extended_entities", {}).get("media", [{}])[0].get("video_info", {}).get("variants", [])
        mp4s = [v for v in variants if v.get("bitrate") and v.get("content_type") == "video/mp4"]
        if mp4s:
            return sorted(mp4s, key=lambda x: -x.get("bitrate"))[0]
        
        return None



@app.get("/")
async def root(url: str):
    tw = Twitter()
    return tw.get_video_url(url)
