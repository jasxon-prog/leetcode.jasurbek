# leetcode 58 - misol
s = 'Hello world'
a = s.split()
b = len(a[-1])
print(b)

# 28 - misol
def strStr(haystack: str, needle: str) -> int:
    l = len(haystack)
    l1 = len(needle)
    for i in range(l):
        if haystack[i:i+l1] == needle:
            return i
    return -1
    

haystack = 'sadbutsad'
needle = ''
print(strStr(haystack, needle))

# 66 - misol
digits = [1,2,3]
nums = str(int(''.join(str(i) for i in digits)) + 1)
x = lambda i: int(i)
result = list(map(x, nums))
print(result)

# 125 - misol
import re
s = "A man, a plan, a canal: Panama"
a = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
if a == a[::-1]:
    print(True)
else: 
    print(False) 

# 67 - misol
a = '11'
b = '1'
summa = int(a, 2) + int(b, 2)
print(bin(summa)[2:])