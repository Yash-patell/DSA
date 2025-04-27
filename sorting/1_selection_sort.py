arr = [23,10,5,2,1,3,42]

n = len(arr)
for i in range (0,n):

#assume current element is min element    
    min_index = i
    
    for j in range(i+1, n): #iterates through the array
        
        if arr[j] < arr[min_index]: #checks if current element is smaller than the minimum element
            
# if there is any element 'j' smaller than the current minimum element 'min_index' then make the j, minimum element            
            min_index = j #min element changes from i to j

# i is the current position and min_index is the min element            
    arr[i],arr[min_index] = arr[min_index],arr[i]
        
print(arr)