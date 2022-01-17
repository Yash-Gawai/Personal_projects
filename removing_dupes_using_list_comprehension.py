a = [1,1,3,4,5,6,4,2,5,6,6,5,4,3]
b = []
[b.append(x) for x in a if x not in b]
print(b)