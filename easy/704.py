def binary_search(nums: list[int], target: int) -> int:

    low = 0
    high = len(nums) - 1 # 5

    while low <= high:
        mid = (low + high)//2 # 2
        guess = nums[mid] # [2]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

nums = [-1,0,3,5,9,12]
target = 9

print(binary_search(nums, target))