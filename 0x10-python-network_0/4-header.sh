#!/bin/bash
# Writing script taking URL as argm, sending GET request to URL and displaying body
curl -s -X GET -H "X-School-User-Id: 98" "$1"
