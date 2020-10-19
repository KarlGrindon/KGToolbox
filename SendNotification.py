import requests
import argparse
import re
import configparser
import os

# Get slack secret URL from config file
# The config file should be in the same directory as the script
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "slackPyConfig.txt")

config = configparser.ConfigParser()
config.read(filename)
secretURL = config.get("configuration","slackURL")

# Class to describe colours, used for printing in the shell.
class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'

# Setup parser object
parser = argparse.ArgumentParser(description='A python script to send slack notifications')

# Add message arguement
parser.add_argument("--message", help="Message to be sent to slack")
arg = parser.parse_args()
message = arg.message

class request:
    url    = secretURL
    object = {'text':message}

slackRequest = requests.post(request.url, json=request.object)

if slackRequest.status_code == 200 :
    print(f"{bcolors.OKGREEN}OKAY: HTTP status code is " + str(x.status_code) + ". Proceeding")
else:
    print(f"{bcolors.FAIL}FAIL: HTTP status code is " + str(x.status_code) + ". Status code 200 expected." )
    print(f"{bcolors.FAIL}FAIL: Sending notification to Slack possibly did not work.")

if re.match(".*ok'$", str(x.content)) is not None :
    print(f"{bcolors.OKGREEN}OKAY: Response from Slack is 'ok'")
    print(f"{bcolors.OKGREEN}OKAY: Message '" + message + "' sent to Slack")
else:
    print(f"{bcolors.FAIL}FAIL: Unexpected response from Slack")