s = "anagram"
t = "nagaram"
def valid_anag(s, t):
    return True if sorted(s) == sorted(t) else False
    # x = set(s)
    # for i in x:
    #     if s.count(i) != t.count(i):
    #         return False
    # else:
    #     return True
print(valid_anag(s, t))