#!/usr/bin/python3
"""
Writing script taking URL and email address, sending POST request
to passed URL with email as param and displaying body of response
"""
import sys
import requests


if __name__ == " __main__":
    url = argv[1]
    valour = {"email": argv[2]}
    req = requests.post(url, data=valour)
    print(req.text)
