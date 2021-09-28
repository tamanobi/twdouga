from fastapi import FastAPI
import requests
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = [
    "https://twdouga.pages.dev",
    "http://localhost",
    "http://localhost:5000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Twitter:
    _API_BASE = 'https://api.twitter.com/1.1/'
    headers = {}

    def __init__(self) -> None:
        self.headers.update({'x-guest-token': self.get_guest_token()})

    def _post(self, api: str, params: dict = {}):
        return requests.post(self._API_BASE + api, params=params, headers=self.headers).json()

    def _get(self, api: str, params: dict = {}) -> dict:
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

    def get_video_url(self, url) -> Optional[dict]:
        """usecase"""

        from twdouga.db import engine
        from twdouga.models import Request
        from sqlalchemy.orm import sessionmaker

        status = self._url_to_status_id(url)
        if not status:
            return None

        tweet = self._get('statuses/show.json', {'id': status})
        variants = tweet.get("extended_entities", {}).get("media", [{}])[0].get("video_info", {}).get("variants", [])
        mp4s = [v for v in variants if v.get("bitrate") and v.get("content_type") == "video/mp4"]
        if not mp4s:
            return None

        ret = sorted(mp4s, key=lambda x: -x.get("bitrate"))[0]
        session = sessionmaker(bind=engine)()
        r = Request(status=status, video_url=ret["url"], response=tweet)
        session.add(r)
        session.commit()

        return ret


@app.get("/")
async def root(url: str):
    tw = Twitter()
    return tw.get_video_url(url)


@app.get("/list")
async def list(offset: int = 0, limit: int = 100):
    from twdouga.db import engine
    from twdouga.models import Request
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import desc

    session = sessionmaker(bind=engine)()
    return [x.as_dict() for x in session.query(Request).order_by(desc(Request.created_at)).limit(100).offset(offset)]
