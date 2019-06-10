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

class URL_Store():
    def __init__(self):
        self.long_urls = {}
        self.short_urls = {}
        self.next_tag = 1

    def __str__(self):
        return "URL Store object"

    def fetch(self):
        fetch_data = requests.get(API_STRING)
        if fetch_data.status_code != 200:
            return "Error fetching data from server. Please try again later."
        elif not fetch_data.json():
            return "No existing data"
        else:
            urls_stats = fetch_data.json()
            self.long_urls = urls_stats["long_urls"]
            self.short_urls = urls_stats["short_urls"]
            self.next_tag = urls_stats["next_tag"]
            return "Success"

    def push(self):
        url_data = {"urllib":{
            "long_urls":self.long_urls,
            "short_urls":self.short_urls,
            "next_tag":self.next_tag,
            }
        }
        # print(url_data)
        payload = json.dumps(url_data)
        payload = json.dumps({
            "test":{
                "var1":1,
                "var2":2,
            }
        })
        print(json.dumps(url_data, indent = 4))
        print(json.dumps({"test":{"var1":1,"var2":2,}},indent = 4))
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
            print("Invalid scheme")
            return False
        if set(url_comps.netloc) > valid_netloc:
            print("Invalid netloc")
            return False

        return True

    def format_url(self, long_url):
        pass

    def add_short_url(self, long_url):

        if long_url in self.long_urls.keys():
            return "URL Already Exists (long)"
        elif long_url in self.short_urls.keys():
            return "URL Already Exists (short)"

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
