def isPalindorm(x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return True
    return False
    
print(isPalindorm(122))