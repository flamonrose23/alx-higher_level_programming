#!/bin/bash
# Writing script taking URL sending POST request to URL and displaying body
curl -sX POST $1 -d "email=test@gmail.com&subject=I will always be here for PLD" -L
