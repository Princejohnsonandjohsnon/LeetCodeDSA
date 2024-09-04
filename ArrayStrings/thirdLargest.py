def thirdLargest(arr):
    arr.sort()
    s=set(arr)
    print(s)
    if len(s)<3:
        return arr[-1]
    
    return arr[len(s)-3]

arr=[2,4,1,5,3,6]
print(thirdLargest(arr))