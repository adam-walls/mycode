#!/usr/bin/env python3

# Only import the CALL function from the subprocess module
# Keeps code from being too bloaty
from subprocess import call

# issue ip link show up to reveal interfaces that are currently in an up state
call(["ip", "link", "show", "up"])

print("This program will check your interfaces.")
interface = input("Enter an interface, like, ens3: ")

# uses above input from user to issue ip addr show dev to reveal IPv4 and IPv6 details
call(["ip", "addr", "show", "dev", interface])
# uses above input from user to issue ip route show dev to reveal IPv4 and IPv6 details
call(["ip", "route", "show", "dev", interface])


