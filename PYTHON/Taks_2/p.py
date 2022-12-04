n = 9
v=0
a = [2,3,9,5,7,8,9,6,5]
for j in range(n):
    for i in range(0, n-1):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
        temp = 0
for k in range(n):
    if a[n-1] > a[k]:
        v = a[k]
print(v)
