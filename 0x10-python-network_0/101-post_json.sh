#!/bin/bash
# Writing script that sends JSON POST request to URL passed as first argument, and displaying  body of response
curl -s -X "POST" -H "Content-Type: application/json" -d @"$2" "$1"
