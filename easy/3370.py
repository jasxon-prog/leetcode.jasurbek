def smallestNumber(n: int) -> int:
    k = 1
    while (2 ** k) - 1 < n:
        k += 1
    return (2 ** k) - 1


print(smallestNumber(5))
print(smallestNumber(10))
print(smallestNumber(3))
print(smallestNumber(20))