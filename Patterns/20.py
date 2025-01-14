''' 

* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 

'''

n = 5

for row in range (2*n):
    if row < n:
        
        for col in range(n-row):
            print("*", end = "")
            
        for col in range (2*row):
            print(" ", end = "")
        
        for col in range (n-row):
            print("*", end = "")
    
    else :
        for col in range (row - n +1):
            print("*", end = "")
        
        for col in range ((2 * n - row -1)*2):
            print(" ",end = "")
        
        for col in range(row - n +1):
            print("*", end = "")
        
    print()