"""

Write a web application that allows users to take a long URL and
convert it to a shortened URL similar to https://goo.gl/.

- The program should have a form that accepts the long URL
- The program should generate a short local URL like /abc1234
and store the short URL and the long URL together in a persistent
data store.
- The program should redirect visitors to the long URL when the short
URL is visited.
- The program should track the number of times the short URL is
visited
- The program should have a statistics page for the short URL, such
as /abc1234/stats. Visiting this URL should show the short URL,
the long URL, and the number of times the short URL was accessed.

___________________
Constraints
___________________

- The app must use a persistent data store that others can use. That
means a local, in-memory system isn't appropriate.
- Don't allow an invalid URL to be entered into the form

"""

import requests
import json
import datetime
import config
import string
from urllib.parse import urlparse


API_STRING = f"https://{config.fb_PROJECT_ID}.firebaseio.com/urllib.json"
URL_BASE = "rietz"

fb_CODE_VALUES = {
    ".":"%`p",
    "$":"%`d",
    "[":"%`l",
    "]":"%`r",
    "#":"%`h",
    "/":"%`s",
}

"""
NOTE:
Firebase does not allow the following characters in keys:
. (period)
$ (dollar sign)
[ (left square bracket)
] (right square bracket)
# (hash or pound sign)
/ (forward slash)

Will need to create an encoder or find another persistent store
"""

class URL_Store():
    def __init__(self):
        self.long_urls = {}
        self.short_urls = {}
        self.next_tag = 1

    def __str__(self):
        return "URL Store object"

    def key_encode(self, plain_key):
        encoded_key = plain_key
        for plain_text, encoded_value in fb_CODE_VALUES.items():
            encoded_key = encoded_key.replace(plain_text, encoded_value)
        return encoded_key

    def dict_encode(self, plain_dict):
        encoded_dict = {}
        for plain_key, value in plain_dict.items():
            encoded_dict[self.key_encode(plain_key)] = value
        return encoded_dict

    def key_decode(self, encoded_key):
        plain_key = encoded_key
        for plain_text, encoded_value in fb_CODE_VALUES.items():
            plain_key = plain_key.replace(encoded_value, plain_text)
        return plain_key

    def dict_decode(self, encoded_dict):
        plain_dict = {}
        for encoded_key, value in encoded_dict.items():
            plain_dict[self.key_decode(encoded_key)] = value
        return plain_dict

    def fetch(self):
        fetch_data = requests.get(API_STRING)
        if fetch_data.status_code != 200:
            return "Error fetching data from server. Please try again later."
        elif not fetch_data.json():
            return "No existing data"
        else:
            urls_stats = fetch_data.json()
            self.long_urls = self.dict_decode(urls_stats["long_urls"])
            self.short_urls = self.dict_decode(urls_stats["short_urls"])
            self.next_tag = urls_stats["next_tag"]
            return "Success"

    def push(self):
        url_data = {
            "long_urls":self.dict_encode(self.long_urls),
            "short_urls":self.dict_encode(self.short_urls),
            "next_tag":self.next_tag,
        }
        payload = json.dumps(url_data)
        print(json.dumps(url_data, indent = 4))
        post_data = requests.put(API_STRING, payload)
        if post_data.status_code != 200:
            return "Error fetching data from server. Please try again later."
        else:
            return "Success"

    def show_stats(self, short_url):
        long_url = self.short_urls[short_url]["long_url"]
        visits = self.short_urls[short_url]["visits"]
        return (long_url, short_url, visits)

    def increment_usage(self, short_url):
        visits = self.short_urls[short_url]["visits"] + 1
        self.short_urls[short_url]["visits"] = visits
        return(visits + 1)

    def check_url_valid(self, long_url):
        # We'll parse the URL into its six component parts using urlparse
        # URL components == scheme://netloc/path;parameters?query#fragment
        url_comps = urlparse(long_url)
        # We'll call the URL valid if:
        #  scheme is http or https
        #  netloc is comprised of only letter, numbers, hyphens, and periods
        valid_schemes = ["http", "https"]
        valid_netloc = set(string.ascii_letters + string.digits + "-.")

        if url_comps.scheme not in valid_schemes:
            print(f"Invalid scheme - perhaps you meant https://{long_url}")
            return False
        if set(url_comps.netloc) > valid_netloc:
            print("Invalid netloc - unexpected characters detected")
            return False
        return True

    def add_short_url(self, long_url):

        if long_url in self.long_urls.keys():
            return f"URL Already Exists. The shortened URL is: {self.long_urls[long_url]}"
        elif long_url in self.short_urls.keys():
            return f"URL Already Exists. The long URL is: {self.short_urls[short_url]}"

        short_url = URL_BASE + f"/{self.next_tag}"
        self.next_tag += 1

        self.long_urls[long_url] = short_url
        self.short_urls[short_url] = {
            "long_url" : long_url,
            "visits" : 0
        }
        return f"Success!\nThe short URL is:  {short_url}\n"


def main():
    print(API_STRING)
    local_url_store = URL_Store()
    print(local_url_store.fetch())
    while True:
        url = input("Enter a URL that you'd like to shorten (or 'QUIT'): \n")
        if url.upper() == "QUIT":
            break
        elif not local_url_store.check_url_valid(url):
            continue

        print(local_url_store.add_short_url(url))

    print(local_url_store.push())

main()
