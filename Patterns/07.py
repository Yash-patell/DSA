
n = 5
for row in range (n):
    # printing blank spaces
    for col in range(n-1-row):
        print(" ", end = " ")
    
    #print stars
    for col in range (2*row +1):
        print("*", end = " ")
    
    print()
        
