def print_digit(n):
    if n==0:
        return
    
    
    print_digit(n-1)
    print(n,end = " ")
    


print_digit(23)
