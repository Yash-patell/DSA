def print_array(arr, n):
    
    print(" ")
    for i in range(n):
        print(arr[i], end = ' ')
    
    print()

def reversed_array(arr, start, end):
    
    if start<end:
        arr[start], arr[end] = arr[end],arr[start]
        reversed_array(arr, start+1, end -1) 
        

arr = [1,2,3,4,5,6,7,9]
n = len(arr)
reversed_array(arr, 0, n-1)
print_array(arr, n)   