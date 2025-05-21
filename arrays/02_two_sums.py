
#Brute force approach 
# TC - O(n^2)
arr = [1,2,3,4,5,6,7,8,9]
target = 10

def twosum(arr):
    if len(arr) < 2:
        return
    else:
    
        for i in range (0,len(arr)):
            for j in range(i+1, len(arr)):
            
                if arr[i] + arr[j] == target:
                    return arr[i], arr[j]
            
        return None    

print(twosum(arr))



# optimized approach TC - O(n)
def op_twosum(arr):
    num_map = {}
 
   
    for index, num in enumerate(arr):
# calculate the compliment that added to num equals the target 
        compliment = target - num
        
        if compliment in num_map:
            return [num_map[compliment], index]
        
# we are adding num as key and its index as value to the dictonary(num_map)     
        num_map[num] = index
        
    return

print(op_twosum(arr))
        
        