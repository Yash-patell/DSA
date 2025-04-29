# Sum of n natural numbers

# without recusrion

def series_sum(n):
    
    total = 0
    if n ==0:
        return 0
    else:
        
        for i in range(1, n+1):
        
            total +=i
            
        return total
            
print(series_sum(5))


# with recusrion

def recursive_series(k):
    
    if k ==0:
        return 0
    else:
        
        return k + recursive_series(k-1) # we are doing nothing but n+(n-1) simple
    
print(recursive_series(6))
    
            
        