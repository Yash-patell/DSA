'''
A
A B
A B C
A B C D
A B C D E
'''

n = 5
for row in range(n):
    for col in range(row+1):
        print(chr(col + 65), end = " ")  # 65 is the unicode point for the uppercase letter A
    
    print()