'''

n = 5

    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *

'''


n = 5
# 1st triangle

for row in range(n):
    for col in range(n-1-row):
        print(" ", end = " ")
    
    for col in range(2*row+1):
        print("*", end = " ")
    
    print()

# 2nd part or bottom part

for row in range(n):
    for col in range(row):
        print(" ", end = " ")
    
    for col in range(2*(n-1-row)+1):
        print("*", end = " ")
    
    print()
