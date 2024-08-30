def maxOperations(nums,k):
    i = 0
    # j=1
    ans = 0
    nums.sort()
    while i < len(nums):
        j = i+1
        print(nums)
        while j < len(nums):
            if nums[i] + nums[j] == k:
                print('i', i)
                print('j', j)
                ans += 1
                nums.pop(j)
                nums.pop(i)
                # nums=nums[:i]
                i = -1
                break
            else:
                j+=1


        i += 1

    return ans

nums=[3,1,3,4,3]
k=6
print(maxOperations(nums,k))