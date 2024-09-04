def consucutive(nums,k):
    l,r,zCount=0,0,0
    maxValue=0
    while r<len(nums):

        if nums[r]==1:
            maxValue=max(maxValue,r-l+1)
            print('ans,', r - l + 1)
            r += 1
        elif nums[r]==0:
            zCount+=1
            if zCount>k:
                while l<len(nums) and zCount>k:
                    if nums[l]==0:
                        l += 1
                        zCount-=1

                    else:
                        l+=1
            print('ans,', r - l + 1)
            maxValue=max(maxValue,r-l+1)
            r+=1
    return maxValue
#             l l
#               r r     r
nums=[1,1,1,0,0,0,1,1,1,1,0]
#     0 1 2 3 4 5 6 7 8 9 10
k=2
print(consucutive(nums,k))



