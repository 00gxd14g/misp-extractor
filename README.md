# MISP Extractor

This code connects to a given MISP (Malware Information Sharing Platform) server and parses a given number of events, writing the IP addresses, URLs, and MD5 hashes found in the events to three separate files.

# Usage

To use this script, you will need to provide the URL of your MISP instance and a valid API key. You can then call the MISPConnector.run() method to retrieve the attributes and save them to files.

To use the code, run the following command:

```python

python3 misp_connector.py --misp-url <MISP_URL> --misp-key <MISP_API_KEY> --limit <EVENT_LIMIT>

```
## Supported attribute types

The MISPConnector class currently supports the following attribute types:

- ip-src
- ip-dst
- md5
- url
- domain

If an attribute of one of these types is found in an event, it will be added to the appropriate set (for example, IP addresses will be added to the network_set) and written to the corresponding file (network.txt, hash.txt, or url.txt).

# Configuration

The code can be configured by passing arguments to the command-line script. The available arguments are:

- misp-url: The URL of the MISP server. This argument is required.
- misp-key: The API key for the MISP server. This argument is required.
- limit: The maximum number of events to parse. The default is 2000.


# Limitations

This script has the following limitations:
- It only retrieves attributes of specific types (as listed above).
- It only writes the retrieved attributes to files, without any further processing or analysis.
- It only retrieves a maximum of 2000 events, as specified by the limit parameter in the misp.search() method.

# License

This code is provided under the MIT License. See the LICENSE file for more details.

