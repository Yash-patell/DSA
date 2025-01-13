'''
n = 5

12345
1234
123
12
1

'''
n = 5
for i in range (n):
    for col in range(n):
        print(col+1, end = " ")
    
    n -=1
    
    print()
    