arr = [0,1,2,2,1,0,1,2,0,2,0]

# we create 3 pointers
low = 0
mid = 1
high = len(arr) -1

while mid <= high:
# if mid = 0 then we swap it with low    
    if mid == 0:
        arr[low],arr[mid] = arr[mid],arr[low]
        low+=1
        mid+=1
        
# if mid = 1 then just move the pointer bcz mid is the position where 1 belongs
    elif mid == 1:
        mid+1
        
    else: #if mid ==2 then we swap it with high
        arr[mid],arr[high] = arr[high],arr[mid]
        mid+=1
        high -=1 # move the high pointer to the left
        
