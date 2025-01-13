'''
n = 5

*********
 *******
  *****
   ***
    *
                                                             '''
                                                             
n =5 

for row in range(n):
    # printing blank spaces
    for col in range(row):
        print(" ", end = " ")
    for col in range (2*(n-1-row)+1):
        print("*", end = " ")
    
    print()
                                                                 