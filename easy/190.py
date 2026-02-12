def reverseBits(n: int) -> int:
    result  = 0

    for i in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

print(reverseBits(n=43261596))