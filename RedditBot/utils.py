from HTMLParser import HTMLParser
import requests

headers = {'User-Agent': 'irc.gamesurge.net #redditmc/RedditBot'}
timeout = 5


def make_request_json(url, params={}):
    try:
        r = requests.get(url, params=params, headers=headers, timeout=timeout)
    except requests.exceptions.ConnectionError:
        return 'Connection error'
    except requests.exceptions.Timeout:
        return 'Request timed out ({} secs)'.format(timeout)
    except requests.exceptions.HTTPError:
        return 'HTTP Error'
    except requests.exceptions.TooManyRedirects:
        return 'Too many redirects'
    except:
        return 'Unhandled exception ({})'.format(r.status_code)
    return r.json


def unescape_html(string):
    return HTMLParser().unescape(string)
