# Given a positive integer num, The task is to find the value of Σi F(i) where i is from 1 to n and function F(i) is defined as the sum of all divisors of i.

    
    
import math
n = int(input("nummmmmm"))

total = 0

for i in range(1, int(math.isqrt(n))+1 ):
    
    if n % i == 0:
        total += i
        
        if i!=  n// i:
            total += n//i
        
print(total)