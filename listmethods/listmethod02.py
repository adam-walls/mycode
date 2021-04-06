#!/usr/bin/python3

# Source data
issnow = {"message": "success", "timestamp": 1617722828, "iss_position": {"longitude": "-163.7676", "latitude": "-50.4155"}}

# Display contents of issnow
for stuff in issnow:
    print(issnow.get(stuff))


