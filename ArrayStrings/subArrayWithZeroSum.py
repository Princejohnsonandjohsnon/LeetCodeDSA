def ZeroSum(arr):
    ans=[]
    for x in range(len(arr)-1):
        l=[]
        sum=arr[x]
        for y in range(x+1,len(arr)):
            if sum+ arr[y]==0:
                l.append(arr[x:y+1])
                sum+=arr[y]

            else:
                sum+=arr[y]
        if l:
            ans.append(l)
    return ans

arr=[1,2,-3,3,-1,-1]
print(ZeroSum(arr))
