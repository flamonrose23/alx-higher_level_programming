#!/usr/bin/python3
"""
Writing script taking URL, sending request to it
and displaying body of response(decoded in utf-8
"""
import sys
import urllib.request


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
