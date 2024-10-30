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