def large(nums: list[int]) -> int:
    a = max(nums)
    b = nums.index(a)
    for i in range(len(nums)):
        if a < 2*nums[i] and i != b:
            return -1
    return b
nums = [3,6,1,0]
print(large(nums))