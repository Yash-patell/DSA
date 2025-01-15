a = int(input("enter a "))
b = int(input("enter b "))

ans = []

# save orignal value of a and b
org_a = a
org_b = b

while a>0 and b>0:   
        # check whether a or b is greater, (greater % smaller = 0) if one of them is 0 remaining will be GCD
    
    if a>b:
        a = a%b
    else: #b>a
        b = b%a
            
if a==0:
    gcd = b
            
else:      #b==0
    gcd = a
                
lcm = (org_a * org_b) //gcd

ans.append(lcm)
ans.append(gcd)

print("lcm and gcd = ",ans)
            