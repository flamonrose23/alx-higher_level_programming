#!/usr/bin/python3
"""
Writing script fetching https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.text
    responseType = type(body)
    print(f"Body response:\n\t- type: {resType}\n\t\
- content: {body}")
