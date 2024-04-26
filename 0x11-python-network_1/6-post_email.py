#!/usr/bin/python3
"""
Writing script taking URL and email address, sending POST request
to passed URL with email as param and displaying body of response
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    valours = {"email": email}
    res = requests.post(url, data=valours)
    print(res.text)
