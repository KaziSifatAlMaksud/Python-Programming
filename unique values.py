"""
20. Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""
"""
21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd
"""

d = {'1':['a','b'], '2':['c','d']}
a1 =[]
print(len(d))
for key in range(len(d)+1):
  a1.append(key)

print(a1)