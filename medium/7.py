x = 120
def reverse_num(x):
    y = str(abs(x))
    y = int(y[::-1]) if x > 0 else -int(y[::-1])
    if not pow(-2, 31) <= y <= pow(2, 31) - 1:
        return 0
    return y
print(reverse_num(x))