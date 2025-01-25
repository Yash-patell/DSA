#Write a Python function push_zero(array) that rearranges an array so that all non-zero elements appear at the beginning of the array, while maintaining their original order, and all zeros are moved to the end.
def push_zero(array):

# Pointer to track the position for next non-zero element    
    count = 0
    

    for element in range (len(array)):

#If the current element is not zero
        if  array[element] != 0:
# swap the current element with the 0 at index count
            array[element], array[count] = array[count], array[element]
# move count pointer to next position
            count += 1
    
    return array
        
array = [1,2,3,65,4,0,5,0,7,14,0,55]


print(push_zero(array))    
    
    

        