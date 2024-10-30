nums = [2,2,1,1]
def single_number(nums):
    num = []
    for i in nums:
        if not i in num:
            num.append(i)
        else:
            num.remove(i)
    return num[0] if num != [] else 0
print(single_number(nums))