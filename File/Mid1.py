import json

s1 = []
f1 = open("data.txt","r")

s = f1.read()
res = json.load(s)
print(s)
