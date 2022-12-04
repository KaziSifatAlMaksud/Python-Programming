
#give  you 2 array , you need tow join it
"""
l1 = [1,2,3]
l2 = [4,5,6]
l = []
for i in range(len(l)):
    l.append(l1[i])
    l.append(l2[i])
 print(l)
"""
l = [1,2,3,4,5,6]
l1 = []
l2 = []
for i in range (len(l)):
    if (i %2) == 0:
        l1.append(l[i])
    else:
        l2.append(l[i])
print(l1)
print(l2)
