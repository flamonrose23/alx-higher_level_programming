#!/bin/bash
# Writing script taking URL, sending request to it and displaying size of body
curl -si "$1" | grep Content-Length | tail -c 4
