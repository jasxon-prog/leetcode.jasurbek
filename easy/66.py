digits = [1,2,3]
nums = str(int(''.join(str(i) for i in digits)) + 1)
x = lambda i: int(i)
result = list(map(x, nums))
print(result)