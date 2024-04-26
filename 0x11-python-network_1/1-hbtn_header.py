#!/usr/bin/python3
"""
Writing script taking URL, sending request to it and displaying value
This value refers to X-Request-Id which is variable found in header of response
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.info()["X-Request-Id"])
