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
#
# d = {1:2,3:"abc"}
# import json
# s = json.dumps(d)
# open("data.txt","w").write(s)
# s2 = open("data.txt").read()
# x = json.loads(s2)
# for keys, i in x.items():
#     print(keys)
x=1
y=1
z=1
n=2


b = []
for i in range(0,x+1):
        for j in range(0, y+1):
            for k in range(0,z+1):
                sum = i +j + k
                print(sum)
                a = [0, 0, 0]
                if n != sum:
                  a[0]=i
                  a[1]=j
                  a[2]=k
                  b.append(a)
                sum=0


print(b)