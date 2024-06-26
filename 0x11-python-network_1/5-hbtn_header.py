#!/usr/bin/python3
"""
Writing script taking URL, sending to it and
displaying value of variable X-Request-Id in reponse header
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
