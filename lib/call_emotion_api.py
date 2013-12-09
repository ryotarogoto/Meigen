#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json

dislike = "生は永久の闘いである。 自然との闘い、社会との闘い、他との闘い、永久に解決のない闘いである。 闘え。闘いは生の花である。"
fear = "人生は恐れなければ、とても素晴らしいものなんだよ。人生に必要なもの。それは勇気と想像力、そして少しのお金だ。"
sad = "何でも謝って済むことではないけれど 謝れない人間は最低だ"

text = sys.argv[1]
url = "http://ap.mextractr.net/ma9/emotion_analyzer"
query = {
        "out" : "json",
        "apikey" : "YOURAPIKEY",
        "text" : text
        }

res = requests.get("http://ap.mextractr.net/ma9/emotion_analyzer",
    params=query)

data = json.loads(res.text)
rank_like = data["likedislike"]
rank_anger = data["angerfear"]
rank_joy = data["joysad"]

if(rank_like <= rank_anger and rank_like <= rank_joy):
    result = dislike
elif(rank_anger <= rank_like and rank_joy <= rank_like):
    result = fear
else:
    result = sad

print("あなたにピッタリの名言は : %s" % result)
