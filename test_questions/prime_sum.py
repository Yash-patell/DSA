# question - we have a bill amount from that bill amount check the prime digits and sum them, now that summision of prime digits is the discount on the total bill

#-------------------------brute force-------------------------------------------------------
amount = int(input(' '))

discounted_amount = 0

#extract digits

while amount > 0:
    last_digit = amount %10 
    
    #check prime for that digit

    count_prime = 0

    for i in range(1, amount+1,1 ):
    
        if last_digit % i == 0:
            count_prime +=1
    
    if count_prime ==2:
        
        discounted_amount += last_digit
        
    
    amount //=10 # remove last digit from the amount

print(discounted_amount)





# ----------------------------------------optimised code 

amount = int(input("Enter the amount "))

org_amount = amount

discount = 0

prime_digits = [2,3,5,7]

while amount>0:
    
    last_digit = amount % 10 #extract the digit from orignal amount
    
    if last_digit in prime_digits:
        discount += last_digit
    
    amount //= 10  #remove the last digit from orignal amount to iterate every digit

    discounted_price = org_amount - discount

print('orignal amount = ', org_amount)    
print('discount applicable = ',discount)
print('final price price of the item = ',discounted_price)