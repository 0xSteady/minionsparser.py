#!/usr/bin/env python3
# 
# Description: This script normalizes the data contained in the file published by 
# Binary Edge at https://api.binaryedge.io/v1/minions into a format that can be 
# consumed as an EDL by the Palo Alto NGFW
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
# or using the template or script itself. 

import requests
import os
from pathlib import Path

# If the output file currently exists, delete it
ofile = "/tmp/minionsparser/minions.edl.txt"
if os.path.isfile(ofile):
    os.remove(ofile)
    print("Stale Minions File Deleted, Proceeding with Download")
else:
    print("Minions File Did Not Exist, Proceeding with Download")

# Retrieve contents of the file and store as a string in a buffer 
link = "https://api.binaryedge.io/v1/minions"
data = requests.get(link)

# Sanitize the file to be IPv4 Addresses, one per line
data2 = data.text.replace("{\"scanners\": [\"", "\n")
data3 = data2.replace("\"]}", "\n")
newdata = (data3.replace("\", \"", "\n")) 

# Open the file minions.edl.txt in the tmp directory and write the newly formatted data.  
output = open("/tmp/minionsparser/minions.edl.txt", "w")
output.writelines(newdata)

# Sort the file by the first octet of the IP Addresses

file = Path("/tmp/minionsparser/minions.edl.txt")
file.write_text(
    "\n".join(
        sorted(
            file.read_text().split("\n")
        )
    )
)
# Close the file
output.close()

print("New EDL can be found in /tmp/minionsparser/minions.edl.txt")