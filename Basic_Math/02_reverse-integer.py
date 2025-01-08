class Solution(object):
    
    def reverse(self):
        
        x = (input("Enter num : "))
        x = int(x)
        
        # Store the sign of a number 
        sign = -1 if x < 0 else 1

        x = abs(x) #absolute value of x 
        
# - abs function is used to find the absolute value of integer regardless of its sign(-5=5 and +5 =5)

        reversed_num = 0

        while x>0 :
            last_digit = x % 10 #extract the last digit
            # this modulo operator returns the remainder
            reversed_num = reversed_num * 10 + last_digit #append the last digit to reversed_num

            #This operation appends the last_digit to the end of the number being built (reversed_num), effectively reversing the order of digits as you iterate through the original number.
            
            
            x //= 10 #remove the last digit
            #perform integer division and return quotient
        
        #restore the sign
        reversed_num *= sign

        #handle overflow of 32 bit integer

        if reversed_num < -2**31 or reversed_num > 2**31 -1:
            return 0

        return reversed_num
    
    
    
    
if __name__ == "__main__":
    # Create an object of the Solution class
    sol = Solution()

    # Call the reverse method
    result = sol.reverse()

    # Print the result
    print(f"Reversed number: {result}")




           