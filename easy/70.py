def clim_stair(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    step = 1
    step1 = 2
    for i in range(2, n):
        result = step1
        step1 = step + step1
        step = result
    return step1
n = 4
print(clim_stair(n))