def happy_number(n: int) -> bool:
    nums = set()
    while n != 1 and n not in nums:
        nums.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1
print(happy_number(n=19))
print(happy_number(n=2))