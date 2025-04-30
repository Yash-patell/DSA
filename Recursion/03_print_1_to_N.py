def digit(n):
    if n==0: #base condition
        return
    
    digit(n-1)  #- we are using n-1 bcz when n=0 the function will stop calling itself
    
    
    print(n,end = " ")  #print
    

digit(23)  #function call22

# https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops3621/1