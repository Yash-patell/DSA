#normal code
# n = int(input("number =="))

# if n == 0 or n == 1:
#     print(1)
# else:
#     factorial = 1
#     while factorial<=n:
    
#         factorial = factorial*n
#         n -=1

# print(factorial)


#with recursion
# we have to return the factorial from the list of factorials that are lesser than n..simple


def recursive_fact(n, factorial = 1, current_num =1 , result = None):

    if result is None:
        result = []
    
    if factorial > n:
        return result
    

    result.append(factorial)
    

    return recursive_fact(n, factorial * (current_num + 1), current_num + 1, result)

    

print(recursive_fact(6))        



    
    

