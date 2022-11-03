'''
Write a program called SquarePattern that prompts user for the size (a non-negative
integer in int); and prints the following square pattern using two nested for-loops.
Enter the size: 5
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
'''

n = int(input("Enter the size:"))
print()
for x in range(n):
    for y in range(n):
        print("#", end=" ")
    print()