'''
*                 *    # 1st half
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * *     * * * *     # 2nd half
* * *         * * * 
* *             * * 
*                 * 
'''


n = 5

for row in range(n):
    for col in range(row+1):
        print("*", end = " ")
        
    for col in range (2*(n - row  - 1)):
        print(" ",end = " ")
    
    for col in range (row+1):
        print("*", end = " ")
    
    
    print()

for row in range (n-1, 0, -1):
    
    for col in range (row):
        print("*", end = " ")
        
    for col in range (2* (n - row)):
        print(" ", end = " ")
    
    for col in range (row):
        print("*", end = " ")
    
    print()