def remove_element(nums: list[int], val: int) -> int:
    new_nums = []

    for i in range(len(nums)):
        if nums[i] != val:
            new_nums.append(nums[i])
    
    nums[:] = new_nums

    return len(new_nums)



nums = [0,1,2,2,3,0,4,2]
val = 2

print(remove_element(nums, val))