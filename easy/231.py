def power_two(n):
    if n == 0 :
        return False
    if n==1:
        return True
    while n % 2 == 0:
        n = n / 2 
        if n == 1:
            return True
    else:
        return False
print(power_two(16))