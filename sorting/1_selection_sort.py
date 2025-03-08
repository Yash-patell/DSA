arr = [23,10,5,2,1,3,42]

n = len(arr)
for i in range (n):

#assume current element is min element    
    min_index = i
    
    for j in range(i+1, n): #iterates through the array
        
        if arr[j] < arr[min_index]: #checks if current element is smaller than the minimum element
            
            min_index = j #min element chnages from i to j
            
    arr[i],arr[min_index] = arr[min_index],arr[i]
        
print(arr)