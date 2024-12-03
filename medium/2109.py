def spaces_str(s, spaces):
    result = []
    space_index = 0
    for i in range(len(s)):
        if space_index < len(spaces) and i == spaces[space_index]:
            result.append(' ')
            space_index += 1
        result.append(s[i])
    return ''.join(result)

s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]
print(spaces_str(s, spaces))