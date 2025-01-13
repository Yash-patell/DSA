
n = 5
'''
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1


'''
# tip - print 0 where row is odd or column is odd, and elsewhere print 1

for row in range(n):
    for col in range(row+1):
        
        if (row+col) % 2 == 0:
            print(1, end = " ")
        else :
            print(0, end = " ")
    
    print()
    
    