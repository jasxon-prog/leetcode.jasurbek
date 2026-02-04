from typing import List


def isTrionic(nums: List[int]) -> bool:
    n = len(nums)
    if n < 3:
        return False

    i = 0

    while i + 1 < n and nums[i] < nums[i + 1]:
        i += 1
    if i == 0 or i == n - 1:
        return False

    while i + 1 < n and nums[i] > nums[i + 1]:
        i += 1
    if i == n - 1:
        return False

    while i + 1 < n and nums[i] < nums[i + 1]:
        i += 1

    return i == n - 1

print(isTrionic([2,1,3]))