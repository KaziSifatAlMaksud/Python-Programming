"""
let,
String s = "abc_1-def_2"
to
dictionary
d = {
 "abc" : 1,
 "def" : 2
}



"""
s = "abc_1-def_2"
a = []
b = []
d = {}
for i in s.split("-"):
    a.append(i)
for j in range(len(a)):
    for k in a[j].split("_"):
        b.append(k)

for i in range (len(b)):
    if i % 2 == 0:
        d[b[i]] = int(b[i+1])
print(d)