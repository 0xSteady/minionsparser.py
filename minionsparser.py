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
v4ofile = "/tmp/minionsparser/minions-v4.edl.txt"
if os.path.isfile(v4ofile):
    os.remove(v4ofile)
    print("Stale Minions-v4 File Deleted, Proceeding with Download")
else:
    print("Minions-v4 File Did Not Exist, Proceeding with Download")

# Retrieve contents of the v4 file and store as a string in a buffer 
v4link = "https://api.binaryedge.io/v1/minions"
v4data = requests.get(v4link)

# Sanitize the file to be IPv4 Addresses, one per line
v4data2 = v4data.text.replace("{\"scanners\": [\"", "\n")
v4data3 = v4data2.replace("\"]}", "\n")
v4newdata = (v4data3.replace("\", \"", "\n")) 

# Open the file minions.edl.txt in the tmp directory and write the newly formatted data.  
output = open("/tmp/minionsparser/minions-v4.edl.txt", "w")
output.writelines(v4newdata)

# Sort the file by the first octet of the IP Addresses

v4file = Path("/tmp/minionsparser/minions.edl.txt")
v4file.write_text(
    "\n".join(
        sorted(
            v4file.read_text().split("\n")
        )
    )
)
# Close the file
output.close()
print("New IPv4 EDL can be found in /tmp/minionsparser/minions-v4.edl.txt")


# If the output file currently exists, delete it
v6ofile = "/tmp/minionsparser/minions-v6.edl.txt"
if os.path.isfile(v6ofile):
    os.remove(v6ofile)
    print("Stale Minions-v6 File Deleted, Proceeding with Download")
else:
    print("Minions-v6 File Did Not Exist, Proceeding with Download")

# Retrieve contents of the v6 IP file and store as a string in a buffer 
v6link = "https://api.binaryedge.io/v1/minions-ipv6"
v6data = requests.get(v6link)

# Sanitize the file to be IPv4 Addresses, one per line
v6data2 = v6data.text.replace("{\"scanners\": [\"", "\n")
v6data3 = v6data2.replace("\"]}", "\n")
v6newdata = (v6data3.replace("\", \"", "\n")) 

# Open the file minions.edl.txt in the tmp directory and write the newly formatted data.  
v6output = open("/tmp/minionsparser/minions-v6.edl.txt", "w")
v6output.writelines(v6newdata)

# Sort the file by the first octet of the IP Addresses

v6file = Path("/tmp/minionsparser/minions.edl.txt")
v6file.write_text(
    "\n".join(
        sorted(
            v6file.read_text().split("\n")
        )
    )
)
# Close the file
output.close()
print("New IPv4 EDL can be found in /tmp/minionsparser/minions-v6.edl.txt")