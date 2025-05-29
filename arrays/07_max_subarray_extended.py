arr = [1,-2,-3,4,-1,5,-2,3,-1]

# assume that first element is the max we found so far
max_sum = arr[0]
current_sum = arr[0]

 # These will track the start and end indices of the max subarray
max_start_index = 0
max_end_index = 0
# This will track the start index of the current subarray
current_start_index = 0

for i in range(1,len(arr)):
    
    n = arr[i] # current element
   
# If adding the current element to current_sum results in a sum
# that is less than the current element itself, it means the
# previous 'current_sum' was dragging us down. So, it's better
# to start a new subarray from 'n'.
        
    if current_sum +n < n:
        current_sum = n
        current_start_index = i # start the new array from the current index
        
    else:
        current_sum += n
        
        
    
    if current_sum > max_sum:
        
        max_sum = current_sum
        max_start_index = current_start_index
        max_end_index = i

max_array = arr[max_start_index : max_end_index +1]
    
print(max_sum)
print(max_array)

