#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

url = "https://api.librepcb.org/api/v1/libraries/v0.1"
content = json.loads(requests.get(url).content.decode("UTF-8"))
assert content["next"] is None

libraries = content["results"]
symbols = 0
packages = 0
components = 0
devices = 0
for library in libraries:
    symbols += int(library["symbols"])
    packages += int(library["packages"])
    components += int(library["components"])
    devices += int(library["devices"])

print("Libraries: {}".format(len(libraries)))
print("Symbols: {}".format(symbols))
print("Packages: {}".format(packages))
print("Components: {}".format(components))
print("Devices: {}".format(devices))
print("Total: {}".format(symbols + packages + components + devices))
