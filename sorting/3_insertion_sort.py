arr = [23,10,5,2,1,3,42]

n = len(arr)

for i in range (1,n):
    
    key = arr[i] # current element
    j = i-1   # j is an index that points to the last element in the sorted portion of the array (the portion to the left of i)
    
    while j >= 0 and arr[j] > key:
        
        arr[j+1] = arr [j] #shift the element right
        
        j = j-1 
        
    arr[j+1] = key #After the inner loop finishes, j + 1 is the correct position where the key should be inserted.
    
print(arr)
        
        