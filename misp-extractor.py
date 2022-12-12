import requests
from pymisp import PyMISP
import urllib3
from collections import Counter
import argparse

urllib3.disable_warnings()

parser = argparse.ArgumentParser()
parser.add_argument('--misp-url', required=True, help='MISP URL')
parser.add_argument('--misp-key', required=True, help='MISP API Key')
parser.add_argument('--limit', default=2000, help='MISP Event limit')
args = parser.parse_args()

class MISPConnector:
    def __init__(self, misp_url, misp_key, limit):
        self.misp_url = misp_url
        self.misp_key = misp_key
        self.limit = limit
        self.misp = PyMISP(self.misp_url, self.misp_key, False)

    def run(self):
        network_set = set()
        hash_set = set()
        url_set = set()
        network_counter = Counter(network_set)

        events = self.misp.search(controller='events', pythonify=True, limit=self.limit, enforceWarninglist=True)
        for event in events:
            attributes = event['Attribute']
            for attribute in attributes:
                if attribute['type'] == 'ip-src' or attribute['type'] == 'ip-dst':
                    network_set.add(attribute['value'])
                if attribute['type'] == 'md5':
                    hash_set.add(attribute['value'])
                if attribute['type'] == 'url' or attribute['type'] == 'domain':
                    url = attribute['value']
                    if url.startswith("http://"):
                        url = url[7:]
                    elif url.startswith("https://"):
                        url = url[8:]
                    url_set.add(url)                            
    
        with open('network.txt', 'w',encoding="utf-8") as f:
            for network in network_set:
                f.write("{}\n".format(network))
            print(f"Wrote {len(network_set)} values to network.txt")
        with open('hash.txt', 'w',encoding="utf-8") as f:
            for hash in hash_set:
                f.write("{}\n".format(hash))
            print(f"Wrote {len(hash_set)} values to hash.txt")
        with open('url.txt', 'w',encoding="utf-8") as f:
            for url in url_set:
                f.write("{}\n".format(url))
            print(f"Wrote {len(url_set)} values to url.txt")

misp_connector = MISPConnector(args.misp_url, args.misp_key, args.limit)
misp_connector.run()
