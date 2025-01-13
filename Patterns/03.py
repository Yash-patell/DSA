'''
n = 4

1
12
123
1234
'''

n = 4

for row in range (n):
    for col in range(row+1):
        print(col+1, end = " ")
    print()