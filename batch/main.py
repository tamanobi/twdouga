import requests
from bs4 import BeautifulSoup
import urllib.parse
import logging
logger = logging.getLogger(__package__)
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    url = "https://www.twidouga.net/realtime_t.php"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    tweet_list = [anchor['href'] for anchor in soup.select('div.saisei > a')]
    for url in tweet_list:
        endpoint = "https://safe-sands-65135.herokuapp.com/"
        logger.info("will register: %s", url)
        res = requests.get(f"{endpoint}?url={urllib.parse.quote(url)}")
        if res.status_code == 200:
            logger.info("success: %s", url)
