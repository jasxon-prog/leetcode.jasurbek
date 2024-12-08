# from collections import Counter
# def majorityElement(nums) -> int:
#         count = Counter(nums)
#         return max(count, key = count.get)

# nums = [3, 3, 2]
# print(majorityElement(nums))

def majorityElement(nums):
    nums.sort()
    return nums[len(nums) // 2]
    
print(majorityElement(nums=[3, 2, 3]))