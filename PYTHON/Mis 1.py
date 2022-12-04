d1 = {1:2,2:3}
d2 = {2:3,3:3}
update = {}
# #
# # for key1, value1 in d1.items():
# #     c =0
# #     for key2, value2 in d2.items():
# #         if key1 != key2:
# #             c = c+1
# #     if c == len(d2):
# #         update[key1] = value1
# #
# # for key2,value2 in d2.items():
# #     c=0
# #     for key1, value1 in d1.items():
# #         if key1 != key2:
# #             c=c+1
# #     if c == len(d2):
# #         update[key2] = value2
# #
# # print(update)

for key, j in d1.items():
    for keys, k in d2.items():
        if d1[key] != d2[keys]:
            update[d1[key]] = d1[j]
            update[d2[keys]] = d2[k]

print(update)