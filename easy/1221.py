def string_split(s: str) -> int:
    count = 0
    count1 = 0
    for i in s:
        if i == 'R':
            count += 1
        elif i == 'L':
            count -= 1
        if count == 0:
            count1 += 1
    return count1
    
s = "LLLLRRRR"  
print(string_split(s))