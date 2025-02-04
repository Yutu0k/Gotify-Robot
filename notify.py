# coding=utf-8

import requests
import os

GOTIFY_APP_TOKEN = os.getenv("APP_TOKEN")
GOTIFY_INSTANCE_URL = os.getenv("INSTANCE_URL")

json = {
	"title": "Md Test",
	"message": "Hello: ![](https://gotify.net/img/logo.png)",
	"priority": "5",	
	"extras": {
		"client::display": {
			"contentType": "text/markdown"
		}
	}
}

url = f"{GOTIFY_INSTANCE_URL}/message?token={GOTIFY_APP_TOKEN}"

response = requests.post(url, json=json)

# "extras":
# {
# 	"client::display": 
# 	{
# 		"contentType": "text/markdown"
# 	}
# }
