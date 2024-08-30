def bubbleSort(nums):
    for x in range(len(nums)-1):
        for y in range(0,len(nums)-x-1):
            if nums[y]>nums[y+1]:
                nums[y],nums[y+1]=nums[y+1],nums[y]
    return  nums




nums=[5,4,3,2,1,0,0,0,7,8,9]
print(bubbleSort(nums))