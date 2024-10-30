import re
s = "A man, a plan, a canal: Panama"
a = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
if a == a[::-1]:
    print(True)
else: 
    print(False)