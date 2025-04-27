# Given an integer ‘num’, your task is to write a program that returns all the divisors of ‘N’ in ascending order.
# https://www.geeksforgeeks.org/problems/all-divisors-of-a-number/0
# num = int(input("enter......"))



# for i in range (1,num+1):
#     if num % i == 0:
#         print(i,end = " ")
        

# optimized approach ----------------------------------------------------------------
import math
def divisor(n):
    
    divisor_store = []
    
    for i in range (1, int(math.isqrt(n))+1 ):
        
        if n % i ==0:
            
            if i not in divisor_store:
                divisor_store.append(i)
                
            if i!= n//i :
                
                divisor_store.append(n//i)
    
    divisor_store.sort()
    return divisor_store

# num = 5
# result = divisor(num)

print(divisor(16))
    
    
