strs = ["eat","tea","tan","ate","nat","bat"]
result = {}
for i in strs:
    v = ''.join(sorted(i))
    if v in result:
        result[v].append(i)
    else:
        result[v] = [i]
l=  list(result.values())[::-1]
print(l)