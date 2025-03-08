# basic 
arry = [2,3,4,5,6,7,2,9,0,5]

freq = {}

for i in arry:
    
    if i in freq:
        freq[i] += 1
    
    else:
        freq[i] =1
    

print(freq)





# Count the frequencies of elements in the array

arr = [10,10,18,42,33,24,5,9,11,9,13,5,5]

d = {}

for item in arr:
    d[item] = d.get(item,0)+1
    
print(d)