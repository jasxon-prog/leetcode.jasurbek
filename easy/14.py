strs = ["flower", "flow", "flight"]
def prefix(strs):
    if not strs:
        return ''

    result = ''
    min_strs = min(strs, key=len)

    for i in range(len(min_strs)):
        for j in strs:
            if j[i] != min_strs[i]:
                return result
        result += min_strs[i]
    return result
print(prefix(strs))