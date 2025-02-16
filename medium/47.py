from itertools import permutations

def permutation(nums: list[int]) -> list[list[int]]:
    return [list(i) for i in set(permutations(nums))]

print(permutation(nums=[1]))