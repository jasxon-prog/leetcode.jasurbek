def str_sum(word: str):
    result = ""
    count = 1
    if len(word) ==1:
        return 
    for i in range(1,len(word)):
        if word[i-1]==word[i] and count !=9:
            count+=1
        else:
            result =result + f"{count}{word[i-1]}"
            count = 1
    result =result + f'{count}{word[i]}'
    return result

print(str_sum('d'))