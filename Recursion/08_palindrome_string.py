# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# https://leetcode.com/problems/valid-palindrome/
def is_palindrome(s):
    
    new_string = ''.join(c.lower() for c in s if c.isalnum())
    
    def palindorme_check(start, end):
        
        if start >= end:
            
            return True #base case if pointer has met or crossed it is a palindrome
        
        if new_string[start] != new_string[end]:
            return False 
        
        return palindorme_check(start +1, end -1 )   #move the pointers
    
    return palindorme_check(0, len(new_string)-1)    # initial values 

print(is_palindrome('acb'))      