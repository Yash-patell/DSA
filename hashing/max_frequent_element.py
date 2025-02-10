#count the max and less frequent element from the array

arr = [10,11,12,13,14,15,14,17,22,21,20,21,30,21]

d = {}

for item in arr:
    d[item] = d.get(item,0)+1
    

#max
maxcount = 0
maxvalue = -1

mincount = len(arr)+1
minvalue = None

for key,count in d.items():
    
    if maxcount<count:
        maxvalue = key
        maxcount = count
        
    if mincount>count:
        minvalue = key
        mincount = count
        
print(maxcount, maxvalue)
print("-------------------")
print(mincount,minvalue)