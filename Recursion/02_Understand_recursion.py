def fun(n):
    if n<1:
        return
    
    fun(n-1)
    print(f"XYZ..................... {n} times")
    

fun(10)