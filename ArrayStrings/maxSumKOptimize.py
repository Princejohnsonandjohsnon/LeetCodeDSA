def ans(nums,k):
    map = {}

    for i in range(len(nums)):
        if nums[i] not in map:
            map[nums[i]] = []
        map[nums[i]].append(i)
    print(map)

nums=[1,2,2,2,2,3,3,4,5,6]
k=5
print(ans(nums,k))
