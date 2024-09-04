def findMaxAverage(nums,k):
    i, total= 0, 0
    z=0
    ans = []
    while i < len(nums):
        if i<k:
            while i<k:
                total+=nums[i]
                i+=1
            val=total/k
            i-=1
            ans.append(val)
        elif i>=k:
            total=total-nums[z]
            total+=nums[i]
            val=total/k
            ans.append(val)
            z+=1
        i+=1
    return ans

nums=[1,12,-5,-6,50,3]
k=4
print(findMaxAverage(nums,k))