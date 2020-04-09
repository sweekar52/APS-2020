def subArray(l): 
    arr = [[]] 
    for i in range(len(l) + 1):  
        for j in range(i + 1, len(l) + 1):
            s = l[i:j] 
            arr.append(s) 
    return arr


a=[1,2,3]
print(subArray(a))
