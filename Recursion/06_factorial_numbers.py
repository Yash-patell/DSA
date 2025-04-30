
#with recursion
# we have to return the factorial from the list of factorials that are lesser than n..simple
#basically we have to return the factorial numbers which are lesser than the n

# https://www.geeksforgeeks.org/problems/find-all-factorial-numbers-less-than-or-equal-to-n3548/0

def recursive_fact(n, factorial = 1, current_num =1 , result = None):

    if result is None:
        result = []
    
    if factorial > n:  # as soon as size of the factorial become larger than n it return result
        return result
    

    result.append(factorial) # appending factorial to the result
    

    return recursive_fact(n, factorial * (current_num + 1), current_num + 1, result)


# factorial * (current_num + 1) calculates the next factorial (it multiplies the current factorial by current_num + 1).
# current_num + 1 increments the current number to the next one
# result - continue to carry the results
    

print(recursive_fact(24))        



    
    

