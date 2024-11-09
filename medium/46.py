from itertools import permutations 
def permute(nums: list[int]) -> list[list[int]]: 
    result = []
    perm = permutations(nums)
    for i in list(perm):
        result.append(list(i))
    return result
nums = [1]
print(permute(nums))