from typing import List

def constructTransformedArray(nums: List[int]) -> List[int]:
    transformedArr = []
    n = len(nums)
    for i in range(len(nums)):
        if nums[i] > 0:
            new_index = (i + nums[i]) % n
        elif nums[i] < 0:
            new_index = (i + nums[i]) % n
        else:
            new_index = i
        transformedArr.append(nums[new_index])
    return transformedArr


print(constructTransformedArray([2,1,3]))