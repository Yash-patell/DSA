'''
4444444
4333334
4322234
4321234
4322234
4333334
4444444
'''
n = 5

for row in range (2*n-1):
    for col in range(2*n-1):
        
        row = min (row, 2*n - 2 - row)
        col = min (col, 2*n - 2 - col)
        ans = min (row, col)
    
        print(n -ans, end = " ")
    
    print()