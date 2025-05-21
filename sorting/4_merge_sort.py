arr = [10,12,14,5,6,8,55,45,1,2,3]

n = len(arr)
def mergesort(arr,start,end):
    if start >= end:
        return
    
    mid = (start+end)//2
    
    mergesort(arr,start,mid) # left half
    mergesort(arr,mid+1, end) #right half
    merge(arr,start,mid,end)
    
def merge(arr,start,mid,end):
    
    left_half = arr[start:mid+1]
    right_half = arr[mid+1:end+1]
    
    i , j =0,0
    k =start

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i+=1
        
        else: #right_half[j] <= left_half[i]
            arr[k] = right_half[j]
            j+=1
            
        k +=1
        
    while i < len(left_half):
        arr[k] = left_half[i]
        i+=1
        k+=1
    
    while j < len(right_half):
        arr[k] = right_half[j]
        j+=1
        k+=1
        
mergesort(arr, 0, n-1)

print(arr)
            