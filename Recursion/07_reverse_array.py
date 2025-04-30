# https://www.geeksforgeeks.org/problems/reverse-an-array/0
arr = [1,2,3,4,5]
def reverse_array(arr):
    
    def reversing(arr, start, end):
        
        if start >= end:
            return
        
        arr[start],arr[end] = arr[end], arr[start]
        
        return reversing(arr, start+1, end-1)
    
    return reversing(arr, 0, len(arr)-1)
    
reverse_array(arr)
print(arr)    