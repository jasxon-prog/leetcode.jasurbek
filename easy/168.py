def convertTitle(n):
    result = ''
    while n > 0:
        n = n - 1
        result = chr(n % 26 + ord('A')) + result
        n //= 26
    return result
   
print(convertTitle(n = 28))