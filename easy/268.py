def missing_number(nums):
    n = len(nums)
    nums_sum = n * (n + 1) // 2
    sum_nums = sum(nums)
    return nums_sum - sum_nums

print(missing_number(nums=[3, 0, 1]))