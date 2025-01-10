a = int(input("enter a "))
b = int(input("enter b "))

ans = []
hcf =1
for i in range (1, min(a,b)+1):
    if a%i == 0 and b%i == 0:
        hcf = i
        
    
lcm = a*b//hcf
ans.append(lcm)
ans.append(hcf)

print("LCM and HCF =",ans)
