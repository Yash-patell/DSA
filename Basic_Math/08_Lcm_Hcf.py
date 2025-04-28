# a = int(input("enter a "))
# b = int(input("enter b "))

# ans = []
# hcf =1
# for i in range (1, min(a,b)+1):
#     if a%i == 0 and b%i == 0:
#         hcf = i
        
    
# lcm = a*b//hcf
# ans.append(lcm)
# ans.append(hcf)

# print("LCM and HCF =",ans)


def hcf_lcm(a,b):
    ans = []
    org_a =a
    org_b = b
    
    while a>0 and b>0:
        
        if a>b:
            a = a %b
        
        else : # b>a
            b = b%a
        
    if a ==0:
        hcf = b
        
    else:   # b == 0

        hcf = a
        
    
    lcm = org_a * org_b// hcf
    
    
    ans.append(f"lcm is {lcm}")
    ans.append(f"hcf is {hcf}")

    print(ans)
    
hcf_lcm(5,9)
        
