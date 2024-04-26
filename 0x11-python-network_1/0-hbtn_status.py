#!/usr/bin/python3
"""
Writing script fetching https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        utf_body = body.decode('utf-8')
        resType = type(body)
        print(f"Body response:\n\t- type: {resType}\n\t\
- content: {body}\n\t- utf8 content: {utf_body}")
