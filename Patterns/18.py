'''
E 
E D 
E D C 
E D C B 
E D C B A 
'''

n = 5

num = n-1  # when n = 5, num = 4

for row in range(n):
    for col in range(row +1, 0 , -1):
        print(chr(num + col + 64), end = " ")
        
    num -=1
    
    print()
    
    

          
    