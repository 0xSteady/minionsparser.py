#!/usr/bin/env python3
# 
# Description: This script normalizes the data contained in the file published by 
# Binary Edge at https://api.binaryedge.io/v1/minions and https://api.binaryedge.io/v1/minions-ipv6
# into a format that can be consumed as an EDL by the Palo Alto NGFW
#
# SUPPORT POLICY
# 
# This script is provided under an AS-IS, best effort, support policy. 
# These scripts should be seen as community supported and Palo Alto Networks will 
# contribute our expertise as and when possible. We do not provide technical support 
# or help in using or troubleshooting the components of the project through our 
# normal support options such as Palo Alto Networks support teams, or ASC (Authorized 
# Support Centers) partners and backline support options. 
#
# The underlying product used (the NGFW and EDLs) by the scripts is still supported, 
# but the support is only for the product functionality and not for help in deploying 
# or using the template or script itself. import requests

import requests
import os
from pathlib import Path

v4file = Path("./minions-v4.edl.txt")
v6file = Path("./minions-v6.edl.txt")
files = [(v4file) , (v6file)]
for file in files:
    if os.path.isfile(file):
        os.remove(file)
    print("Stale ", (file), "Deleted, Proceeding with Download")


v4url = "https://api.binaryedge.io/v1/minions"
v6url = "https://api.binaryedge.io/v1/minions-ipv6"
urls = [(v4url) , (v6url)]

for url in urls:
    urldata = requests.get(url)
    # datalist = [urldata.text]

    # Sanitize the file to be IPv4 Addresses, one per line
    urldata2 = urldata.text.replace("{\"scanners\": [\"", "\n")
    urldata3 = urldata2.replace("\"]}", "\n")
    cleandata = (urldata3.replace("\", \"", "\n")) 

    if url == v4url:
        output = open("./minions-v4.edl.txt", "w")
        output.writelines(cleandata)
    elif url == v6url:
        output = open("./minions-v6.edl.txt", "w")
        output.writelines(cleandata)
