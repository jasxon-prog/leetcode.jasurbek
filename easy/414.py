def third_max(nums):
    nums = list(set(nums))
    if len(nums) < 3:
        return max(nums)
    nums.sort()
    return nums[-3]
        
print(third_max(nums=[3, 2,1]))