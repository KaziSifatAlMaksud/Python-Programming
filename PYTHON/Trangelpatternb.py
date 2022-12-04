"""
Write 3 programs that prompts user for the size (a non-negative integer in int); and prints
the pattern as shown:
Enter the rows: 6

b) # # # # # # # # # # #
     # # # # # # # # #
       # # # # # # #
        # # # #
         # # #5
           #
"""

n = int(input("Enter the rows: "))

for x in range(n):
    for z in range(x):
        print(" ", end="")
    for y in range(n*2-x*2-1):
        print("#",end="")
    print("\n")