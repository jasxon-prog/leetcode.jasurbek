from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    #number = ()
    # for i in nums:
    #     if i in number:
    #         return True
    #     number += (i,)
    # return False
    return len(nums) != len(set(nums))
nums = [1,2,3,1]

print(containsDuplicate(nums))