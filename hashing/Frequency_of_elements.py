# Count the frequencies of elements in the array

arr = [10,10,18,42,33,24,5,9,11,9,13,5,5]

d = {}

for item in arr:
    d[item] = d.get(item,0)+1
    
print(d)