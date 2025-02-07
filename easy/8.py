def str_int(s: str) -> int:
    s = s.strip()

    sign = 1
    index = 0 

    if not s:
        return 0

    if s[0] == '-':
        sign = -1
        index += 1

    elif s[0] == '+':
        index += 1

    result = 0
    while index < len(s) and s[index].isdigit(): 
        result = result * 10 + int(s[index])                             
        index += 1                              
    result = result * sign  

    int_min, int_max = -2**31, 2**31 - 1
    if result < int_min:
        return int_min
    if result > int_max:
        return int_max 
    
    return result
    
print(str_int(s=''))