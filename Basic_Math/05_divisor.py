# Given an integer ‘num’, your task is to write a program that returns all the divisors of ‘N’ in ascending order.

num = int(input("enter......"))



for i in range (1,num+1):
    if num % i == 0:
        print(i,end = " ")
        

    
    