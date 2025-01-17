def print_digit(n):
    if n==0:
        return
    
    print_digit(n-1) #base condition
    print(n,end = " ")  #print
    

print_digit(23)  #function call22
