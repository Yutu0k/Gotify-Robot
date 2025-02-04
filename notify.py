# coding=utf-8

import requests
import os

GOTIFY_APP_TOKEN = os.getenv("APP_TOKEN")
GOTIFY_INSTANCE_URL = os.getenv("INSTANCE_URL")


json = {
	"message": "popo提醒吃药药![蛙蛙](https://www.yutu0k.top/posts/11d3c1f7/image.png)。",
	"priority": 5,
	"title": "吃药药机器人发来消息",
	"extras": {
		"client::display": {
			"contentType": "text/markdown"
		}
	}

}

url = f"{GOTIFY_INSTANCE_URL}/message?token={GOTIFY_APP_TOKEN}"

# print(url)

response = requests.post(url, json=json)

print(response)

# "extras":
# {
# 	"client::display": 
# 	{
# 		"contentType": "text/markdown"
# 	}
# }
