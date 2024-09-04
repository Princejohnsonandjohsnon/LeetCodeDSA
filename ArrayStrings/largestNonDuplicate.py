from collections import defaultdict


def nonDup(arr):
    arr.sort()
    max=0
    d=defaultdict(int)
    for x in arr:
        d[x]+=1
    for k,v in d.items():
        if d[k]==1:
            if k>max:
                max=k
    return max







arr=[4,3,2,7,2,4,8,8]
print(nonDup(arr))