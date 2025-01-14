'''
1        1
12      21
123    321
1234  4321
1234554321
'''

n =5 
# first triangle

for row in range(n):
    for col in range(row+1):
        print(col+1, end = "")


# blank spaces
    for col in range ((n-1-row)*2):
        print(" ", end =  '')
        
# reversed digits
    for col in range(row+1, 0, -1):
        print(col, end = "")
        
    print()