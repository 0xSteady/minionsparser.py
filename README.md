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
5. Output will be in /tmp/minionsparser/minions.edl.txt



