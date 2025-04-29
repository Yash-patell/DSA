def print_reverse(n):
    
    if n < 1:  # base condition
        return
        
    print(n, end = " ") # first we will print n
        
    print_reverse(n-1) # then decrease the value of n by 1 - to reverse the count

print_reverse(10) # calling the function

# https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1    