# return fibonnaci number
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fib(n-1) + fib(n-2)
    
print(fib(9))


#Optimized code 
# using memmory

def fibonnaci_number( n, memo = {}):
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 0
    
    if n ==1:
        return 1
    
    memo[n] = fibonnaci_number(n-1, memo) + fibonnaci_number(n-2, memo)
    return memo[n]

print(fibonnaci_number(7))



