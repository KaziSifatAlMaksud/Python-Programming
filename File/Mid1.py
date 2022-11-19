# f1 = open("data.txt","a")
# try:
#     f1.write("to day is sunny day! \n")
# except:
#     print("file error")
# finally:
#     f1.close()
#     f1 = open("data.txt")
#     y = f1.read()
#     print(y)

d = {1:2,3:"abc"}
import json
s = json.dumps(d)
open("data.txt","w").write(s)
s2 = open("data.txt").read()
x = json.loads(s2)
for keys, i in x.items():
    print(keys)
