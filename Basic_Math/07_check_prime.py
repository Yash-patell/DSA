# https://www.geeksforgeeks.org/problems/prime-number2314/0
import math
# Optimized code
# Input
N = int(input("Enter a number: "))

# Edge case: 1 is not prime

count = 0  # To count the divisors

# Iterate only up to the square root of N
for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        count += 1  # Count the divisor
        
        if i != N // i:  # If it's not a perfect square, count the pair divisor, check for self divisor
            count += 1

    # Check if the number has exactly two divisors
if count == 2:
    print("prime")
else:
    print("False")


# # why sqaure root - 
# Imagine N is 36. The square root of 36 is 6. So, instead of checking all numbers from 1 to 36 to see if they divide 36 evenly, we only check from 1 to 6. This is because:

# If a number larger than 6 divides 36 (like 12), there must be a smaller number (like 3) that also divides 36.

# So, by checking up to the square root, we make sure we don't miss any factors, and we reduce the number of checks, making the process faster.


# ---------------------------------------- brute force -----------------------------------------------------


num = int(input("enter NUM _"))
count_prime = 0

for i in range(1, num+1,1):
    
    if (num%i == 0):
        count_prime +=1

if count_prime == 2:
    print(True)
else:
    print(False)