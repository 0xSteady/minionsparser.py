# Description

Python script to normalize the data contained in the file published by Binary Edge at https://api.binaryedge.io/v1/minions into a format that can be consumed as an EDL by the Palo Alto NGFW. The output is written to /tmp/minionsparser/minions.edl.txt.

# Updates

- 06-29-2023 - Initial Commit

# Requirements

python 3
pip
requests (python module)

# Usage

1. Install Python 3 (hhttps://www.python.org/downloads/)
2. Install Pip (https://pip.pypa.io/en/stable/installation/)
3. Install request module `pip install requests`
4. Run `./minionsparser.py`
5. Output will be in /tmp/minionsparser
    - minions-v4.edl.txt = IPv4 List
    - minions-v6.edl.txt = IPv6 List

# Support Policy

This script is provided under an **as-is, best effort,** support policy. This  code should be seen as community supported.  We will contribute our expertise as and when possible.

Palo Alto Networks **does not** provide technical support or help in using or troubleshooting the components of this project through its normal support options such as Palo Alto Networks support teams, or ASC (Authorized Support Centers) partners and backline support options. The underlying product(s) and product feature(s) used in conjunction with this container (Palo Alto Networks NGFW and EDLs) is supported by Palo Alto Networks according to support entitlements, but the support is only for the product functionality and not for help in deploying or using this container itself.

