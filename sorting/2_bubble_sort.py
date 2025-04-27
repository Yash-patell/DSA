arr = [23,10,5,2,1,3,42]

n = len(arr)

#n-1 bcz last element will be in current position so we dont need to iterate till last element
for i in range(0,n-1):
    swapped = False #track if swapped happened or not
    
#n-1-i, bcz after i passes, the last i elements are already sorted, and we don’t need to check them again.    
    for j in range(0, n-1-i):
        
        #arr[j] is the current element
        #checks if current element is greater than next element
        if arr[j] > arr[j+1]:
            
            arr[j],arr[j+1] = arr[j+1],arr[j]
            
            swapped = True
        
    if not swapped :
            break
        


print(arr)
        

        
    