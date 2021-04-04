#!/usr/bin/env python3

# open file in read mode
dnsfile = open("dnsservers.txt", "r")

# create list from each line in txt file
dnslist = dnsfile.readlines()

# loop over lines
for svr in dnslist:
    #print and end without a newline
    print(svr, end="")
# close your file
dnsfile.close()

