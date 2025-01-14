'''
E
D E
C D E
B C D E
A B C D E
'''

n = 5
count = n-1
for row in range(n):
    
    
    for col in range (row+1):
        print(chr(count + col +65), end = " ")
    
    count -=1
    
    print()