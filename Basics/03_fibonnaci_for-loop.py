# The n-th term of Fibonacci series F(n), where F(n) is a function, is calculated using the following formula -

#     F(n) = F(n - 1) + F(n - 2), 
#     Where, F(1) = 1, F(2) = 1


# Provided 'n' you have to find out the n-th Fibonacci Number. Handle edges cases like when 'n' = 1 or 'n' = 2 by using conditionals like if else and return what's expected.

# "Indexing is start from 1"

from math import *
from collections import *
from sys import *
from os import *

n = int(input("enter num :    ")) #we can change 

def fibonacci(n):
    if n ==1 and n ==2:
        return 1
    
    first_num, second_num = 1,1   #Intialize the first 2 fibonnaci num
    
    for k in range (3, n+1):      # Loop starts from 3 upto n
        next_num = first_num + second_num #Calculate the next fibonacci num
        first_num = second_num   #update first number to the previous 'second number'
        second_num = next_num   #update second_num to the new fibonacci number
    
    return second_num

result = fibonacci(n)


print(result)
