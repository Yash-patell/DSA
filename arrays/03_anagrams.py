string1 = 'god'
string2 = 'dog'

def anagrams(string1, string2):
    
    charcount = {}
    
#count the frequency of each character in a string1    
    for char in string1:
        charcount[char] = charcount.get(char,0) + 1
        
# this returns the value of the key (char) otherwise default value that you specify(0)
# key are the characters and values are the frequency = {'d':1, 'O':1, 'g':1}
# for ex - charCount['d'] = 1

#count the frquency of each character in string 2

    for char in string2:
        charcount[char] = charcount.get(char, 0) - 1
        
        
    for value in charcount.values():
        if value != 0:
            return False
        
        
    # if all conditions are satisfied return TRUE
    
    return True

print(anagrams(string1,string2))




