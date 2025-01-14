'''

      A
    A B A
  A B C B A
A B C D C B A
'''

n = 5

# spaces

for row in range (n):
    for col in range (n -1 -row):
        print(" ", end = " ")
    
# Letters
    for col in range (row+1):
        print(chr(col + 65), end = " ")

# Reverse alphabets
    for col in range (row, 0,  -1):
        print(chr(col+64), end = " ")
    
    print()