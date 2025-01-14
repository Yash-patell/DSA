'''
A B C D E
A B C D
A B C
A B
A
'''

n = 5

for row in range(n):
    for col in range(n):
        
        print(chr(col + 65), end = " ")
        
    n -=1
    print()