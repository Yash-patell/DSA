'''
A
B B
C C C
D D D D
E E E E E
'''

n = 5

for row in range (n):
    for col in range(row+1):
        print(chr(row+65), end = " ")
    
    print()