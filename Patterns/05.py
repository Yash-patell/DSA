'''
n = 5

*****
****
***
**
*


'''

n = 5
for row in range(n):
    for col in range(n):
        print("*", end = " ")
    n -=1
    print()