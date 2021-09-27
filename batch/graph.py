import requests

def getTwitterFollowers(username):
    res = requests.options('https://api.twitter.com/1.1/guest/activate.json',
    headers={
        'access-control-request-method': 'POST',
        'origin': 'https://twitter.com',
        'user-agent':'Mozilla/5.0'
        })

    headers = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'user-agent': 'Mozilla/5.0',
    }
    res = requests.post(
        'https://api.twitter.com/1.1/guest/activate.json', headers=headers, data={})

    headers['x-guest-token'] = res.json()['guest_token']

    res = requests.get('https://twitter.com/i/api/graphql/jMaTS-_Ea8vh9rpKggJbCQ/UserByScreenName?variables=%7B%22screen_name%22%3A%22' +
                       username + '%22%2C%22withHighlightedLabel%22%3Atrue%7D', headers=headers)

    # return int(res.json()['data']['user']['legacy']['normal_followers_count'])
    return res.json()


print(getTwitterFollowers('twitterjp'))