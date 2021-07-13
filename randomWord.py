import requests
import argparse

# Setup argparse, so we can setup parameters for the script
parser = argparse.ArgumentParser(description='Script that gives you words!')

# Adding a single parameter called count, so we can easily control how many words we want to retrieve
parser.add_argument("-count", help="Specifies the amount of words to retrieve", default=1)
args = parser.parse_args()

# The request
r = requests.get("https://random-word-api.herokuapp.com/word?number=" + str(args.count))

# Return the result
print(r.text)