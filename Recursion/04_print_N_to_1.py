def print_n_times(n):
    
    if n<1:
        return
    
    print(n,end=" ")
    print_n_times(n-1)
    
print_n_times(55)
    