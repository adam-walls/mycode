#!/usr/bin/env python3

import urllib.request
# RegEx library
import re

print("Where should we search?")
url = input()
print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")
searchFor = input()

# parse URL entered by user
searchMe = urllib.request.urlopen(url).read().decode("utf-8")

# If searchFor pattern matches searchMe string
if re.search(searchFor, searchMe):
    print("Found a match!")
else:
    print("No match!")

