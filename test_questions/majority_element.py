# Given an array of numbers and length n, find the majority element. A majority element is an element that appears more than half of the times in the array. If no such element exists, return 0.


# time complexity - O(n^2) - outer loop runs n times and for each iteration of outer loop, inner loop also runs n times
def majority_element(arr): 
    
    n = len(arr)
    
    for i in range(n): #iterate through every element in the array,The variable i represents the current index in the list.
        count = 0
        
        for j in range (n):
            # his inner loop goes through the entire list again to compare each element (arr[j]) with the current element (arr[i]).
            
            if arr[i] == arr[j]:
                count +=1
            
            # This inner loop goes through the entire list again to compare each element (arr[j]) with the current element (arr[i]).
            # Every time it finds an element that is the same as arr[i], it increments the count by 1.
            
        if count >  n//2:
            return arr[i]

    return 0


user_array = (input('')) 

print("majortiy element is ",majority_element(user_array) )




#---------------------------------optimise code----------------------------------------------------
# time complexity - O(n)



def majorityElement(nums):
       
        
    # Phase 1: Find the candidate
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num  # Set a new candidate
            
        if num == candidate:

            count += 1
        else :
            count -=1
    
    return candidate

user_input = (input(''))

print(majorityElement(user_input))