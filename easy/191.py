def hammingWeight(n: int) -> int:
    return bin(n).count('1')

print(hammingWeight(n=11))