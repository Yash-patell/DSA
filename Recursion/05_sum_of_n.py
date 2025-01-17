# Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.

def series(n):
    
    if n ==0:
        return 0

    return n**3 + series(n-1)

result = series(8)
print(result)