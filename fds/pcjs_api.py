import json
from requests import get, post


class PCJsApi:
    def __init__(self, url):
        self.url = url
        self.System = json.loads(get(self.url, {"MM1_jc": "200"}).text)

    def getResolveBySystem(self, name, post_data=None):
        if post_data is None:
            post_data = {}

        def getUrl(url, get_data):
            data_get = []
            for key, value in get_data.items():
                data_get.append(key + "=" + value)
            return url + "?" + "&".join(data_get)
        resolve = post(getUrl(self.url, self.System[name]["GET"]), data=post_data)
        return resolve

    def getJsBySystem(self, name, post_data=None):
        resolve = self.getResolveBySystem(name, post_data)
        return json.loads(resolve.text)
