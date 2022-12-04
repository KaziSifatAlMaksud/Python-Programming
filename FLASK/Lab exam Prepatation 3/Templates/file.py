g = {}
f = open("main.txt").readlines()

for line in f:
    line = line.replace("\n","")
    key, val = line.split(" ")
    g[key]= val
print(g)