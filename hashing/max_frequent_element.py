# you have to return most frequent element by doing k operations 
# basically we have to return how frequent an element can be in the array by doing max K operations
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/submissions/1624393835/
k = 10
arr = [10,11,12,13,14,15,14,17,22,21,20,21,30,21]
def max_freq(arr,k):
    
    arr.sort()
    
    # create left and right pointer
    right, left = 0,0
    result, total = 0,0
#result will store max frequency that we are going to return, and total will contain total sum of the current window    
    
    while right < len(arr):
        total += arr[right] # Expand the window with the right pointer
        
        while arr[right] * (right - left +1) > total + k:

# arr[right] * (right - left +1) - means - cost  to make all numbers in the window equal to the num which is at the right pointer

            total -= arr[left]
            left += 1
# If the cost is too high, we shrink the window from the left until the window is valid again.
            
        result = max(result, right - left +1) 
        right +=1  #Move to the next element and repeat.
        
    return result


print(max_freq(arr, k))