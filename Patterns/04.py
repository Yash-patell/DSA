'''
n =4
1
22
333
4444
'''

n = 5

for row in range(n):
    for col in range(row + 1):
        print(row +1, end = " ")
    
    print()