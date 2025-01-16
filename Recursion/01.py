def func(n):
    if n==0:
        return
    
    print(" Asus ")
    func(n-1)  # func(n - 1) is used, each call reduces the value of n
                # The first call is func(5), which calls func(4).
                # func(4) calls func(3).
                # This continues until func(0) is reached.


func(5) 
