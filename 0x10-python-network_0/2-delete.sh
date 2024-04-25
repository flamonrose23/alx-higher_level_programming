#!/bin/bash
# Writing script sending DELETE request to URL passed as first argument and displaying body
curl -s -X DELETE "$1"
