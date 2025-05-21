arr = ['flower', 'flow', 'foat']

def longest_prefix(arr):
    
    result = ''
    
    for i in range(len(arr[0])):
        
        for s in arr:
            
            if i == len(s) or s[i] != arr[0][i]:

                return result
            
        result += arr[0][i]
        
    return result

print(longest_prefix(arr))

print(arr[0][4])

