def titleColumn(columnTitle):
    result = 0
    for i in columnTitle:
        result = result * 26 + (ord(i)-ord('A') + 1)
    return result

print(titleColumn(columnTitle='A'))
print(titleColumn(columnTitle='AB'))