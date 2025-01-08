
# using extracting the last digit method --------------------------------------------------
# approach 1 - optimised


x =121

absolute_x = abs(x)

reversed_digit =0
while (x>0):
    
    last_digit = x % 10

    reversed_digit = reversed_digit * 10 + last_digit

    x//=10

    print("rversed digit =",reversed_digit)
    print("absolute of x = ",absolute_x)
if reversed_digit == absolute_x:
    print (True)
else: 
    print(False)
        

#approach -2 Brute force------------ using string slicing method---------------------------------

print("\n -------- approach - 2 ---------------------")
        
num = str(x)
reversed_num = num[::-1]

        
if num == reversed_num:
    print (True)
else : print(False)