# https://leetcode.com/problems/fibonacci-number/submissions/1621776562/

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

def fibonnaci_calc( n, memo = {}):
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 0
    
    if n ==1:
        return 1
    # calculate fibonnaci num - f(n-1) + f(n-2) and store it in memory
    memo[n] = fibonnaci_calc(n-1, memo) + fibonnaci_calc(n-2, memo)
    
    return memo[n]

print(fibonnaci_calc(7))



