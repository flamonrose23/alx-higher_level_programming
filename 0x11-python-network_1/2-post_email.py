#!/usr/bin/python3
"""
Writing script taking URL and email, sending POST request with email
as parameter and displaying body of response
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    valour = {"email": email}
    utf_valour = urllib.parse.urlencode(valour).encode('utf-8')
    req = urllib.request.Request(url, data=utf_valour, method='POST')
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
