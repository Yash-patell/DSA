arr = [1,-2,-3,4,-1,5,-2,3,-1]

# assume that first element is the max we found so far
max_sum = arr[0]
current_sum = arr[0]

for i in range(1,len(arr)):
    
    n = arr[i] # current element
    if current_sum < 0:
        current_sum = n
        
    else:
        current_sum += n
        
    
    if current_sum > max_sum:
        
        max_sum = current_sum
    
print(max_sum)

