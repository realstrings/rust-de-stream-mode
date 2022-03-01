import json

steamid=xxx

jesko=json.loads(open("RandomUsernames.json","r").read())["RandomUsernames"]

v = steamid % 2147483647

v = v % len(jesko)

print(jesko[v])