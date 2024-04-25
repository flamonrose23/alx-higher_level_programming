#!/bin/bash
# Writing script taking URL and displaying all HTTP methods that server will accept
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
