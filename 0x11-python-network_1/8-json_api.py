#!/usr/bin/python3
"""
Writing script taking in letter and sending POST request
to http://0.0.0.0:5000/search_user with letter as parameter
letter must be sent in the variable q
and If no argument is given, set q=""
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    letters = {"q": q}
    response = requests.post(url, data=letters)
    try:
        responsejson = response.json()
        if responsejson:
            print(f'[{responsejson["id"]}] {responsejson["name"]}')
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
