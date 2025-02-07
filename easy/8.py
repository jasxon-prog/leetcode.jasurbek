def str_int(s: str) -> int:
    s = s.strip()

    sign = 1
    index = 0 # 1

    if s[0] == '-':
        sign = -1
        index += 1

    elif s[0] == '+':
        index += 1

    result = 0
    while index < len(s) and s[index].isdigit(): 
        result = result * 10 + int(s[index])                             
        index += 1                              
    return result * sign  
    
print(str_int(s='-111kjvgc555'))