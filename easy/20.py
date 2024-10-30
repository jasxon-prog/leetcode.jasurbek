s = '() [] {}'
while True:
    if '()' in s:
        s =  s.replace('()', '')
    elif '[]' in s:
        s = s.replace('[]', '')
    elif '{}' in s:
        s = s.replace('{}', '')
    else:
        print(not s)
        break
