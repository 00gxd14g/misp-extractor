# MISP Extractor

This is a simple Python script that connects to a MISP instance and retrieves attributes of specific types (such as IP addresses, URLs, and hashes). The retrieved attributes are then written to separate files.

# Usage

To use this script, you will need to provide the URL of your MISP instance and a valid API key. You can then call the MISPConnector.run() method to retrieve the attributes and save them to files.

Here is an example of how to use the MISPConnector class:

```python

from pymisp import PyMISP
from misp_connector import MISPConnector
# Provide the URL of your MISP instance and a valid API key

misp_url = "https://misp.example.com"
misp_key = "abc123"
# Create a new MISPConnector instance
misp_connector = MISPConnector(misp_url, misp_key)
# Retrieve the attributes and save them to files
misp_connector.run()
```
# Supported attribute types

The MISPConnector class currently supports the following attribute types:

```python
ip-src
ip-dst
md5
url
domain
```
If an attribute of one of these types is found in an event, it will be added to the appropriate set (for example, IP addresses will be added to the network_set) and written to the corresponding file (network.txt, hash.txt, or url.txt).

# Limitations

This script has the following limitations:
- It only retrieves attributes of specific types (as listed above).
- It only writes the retrieved attributes to files, without any further processing or analysis.
- It only retrieves a maximum of 2000 events, as specified by the limit parameter in the misp.search() method.

# License

This code is provided under the MIT License. See the LICENSE file for more details.

