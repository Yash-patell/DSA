# Given a positive integer num, The task is to find the value of Σi F(i) where i is from 1 to n and function F(i) is defined as the sum of all divisors of i.


num = int(input("Enter Num : "))

sum_count = 0

for i in range(1, num+1):
    
    sum_count = sum_count + i * (num//i)
    
print(sum_count)
    