#!/usr/bin/python3
"""
Writing script taking URL, sending request to it
and displaying body of response
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if (response.status_code >= 400):
        print(f"Error code: {response.status_code}")
        exit()
    print(response.text)
