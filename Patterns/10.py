'''
n =5

*
**
***
****
*****
****
***
**
*

                                                        '''
                                                        
n =5
for row in range(n):
    for col in range(row+1):
        print("*", end = " ")
    print()
    
    #2nd part
for row in range(n-1) :
    for col in range(n-1-row):
        print("*", end = " ")
        
    print()                                                 