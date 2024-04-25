#!/bin/bash
# Writing script sending request to URL passed as argm, displaying only status code
curl -sI -o /dev/null -w "%{http_code}" "$1"
