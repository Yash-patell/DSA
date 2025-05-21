# https://leetcode.com/problems/contains-duplicate/

arr = [1,2,3,4,5,6,17,22,18,22]

def check_duplicate(arr):
    
    seen = set()
    
    for i in arr:
        
        if i in seen:
            return True
        seen.add(i)
        
    return False

print(check_duplicate(arr))