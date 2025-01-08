#Given a positive integer n, count the number of digits in n that divide n evenly (i.e., without leaving a remainder). Return the total number of such digits.

n = int(input("Enter num : "))

orignal_num = n
count = 0

while n>0:
    last_digit = n%10  #Extracting the last digit
    
    #checking if last digit is not equal to zero and extracted digit divides the orignal number evenly
    if last_digit != 0 and orignal_num % last_digit == 0:  
        count += 1 
    
    n = n// 10  #remove the last digit so that we can extract the second digit then third.....and so on ....
    
print(count)


#note - The // operator is used for floor division, which divides the numbers and truncates the decimal part to return the largest integer less than or equal to the result.
#It is particularly useful when you want to work with integers and ignore the fractional part of the division.
