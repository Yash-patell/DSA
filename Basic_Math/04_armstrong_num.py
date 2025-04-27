# You are given an integer ‘NUM’ . Your task is to find out whether this number is an Armstrong number or not.
#https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1
num = int(input("enter num : "))

abs_num = abs(num)
stack = 0

#count the number of digits in input
count = len(str(num))

while num>0:
    last_digit = num % 10 #extracting the last digit
    multiplied_val = last_digit ** count  # exponentiation last digit by count
    stack += multiplied_val #adding the exponetiated value
    
    num //=10 #removing the last digit
    
if abs_num == stack:
    print("Armstrong number ")
else: print(f"False - {abs_num} not a armstrong number")
    
    