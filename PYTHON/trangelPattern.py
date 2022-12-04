"""
 Write 3 programs that prompts user for the size (a non-negative integer in int); and prints
the pattern as shown:
Enter the rows: 6

a)    #
    # # #
   # # # #
  # # # # #
# # # # # # #
# # # # # # # # 
"""
n = int(input("Enter the Number: "))
for x in range(0, n):
       for z in range(n-x):
        print(" ", end="")
       for y in range(x*2+1):
            print("#",end="")
       print("\n")

