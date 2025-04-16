def dublicate_element(nums: list[int]) -> int:
    new_nums = [nums[0]]

    j = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j = i
            new_nums.append(nums[i])

    nums[:] = new_nums
    return len(new_nums)


nums = [1,1,2]

print(dublicate_element(nums))