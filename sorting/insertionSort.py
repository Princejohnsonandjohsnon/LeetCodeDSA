def insertion(nums):

    i=1
    while i<len(nums):
        key = nums[i]
        y=i-1
        #for x in range(y,-1,-1):
        while y>-1:
            if key < nums[y]:
                print('key', key)
                print('before nums', nums)
                print('y', y)
                nums[y + 1] = nums[y]
                print('nums', nums)
                y -= 1
            else:
                break

        print('y outside', y)
        nums[y+1] = key
        print('nums', nums)

        print('key',key)

        i+=1
        print('i is', i)
    return nums



#     5 4 3 2 1
nums=[5,4,3,2,1,7,8,9,0,0,0,1,2,3,-1,-2,-3,11]
print(insertion(nums))