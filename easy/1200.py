def min_farq(arr):
    if not arr:
        return []
    result = []
    arr.sort()
    min_dif = arr[1] - arr[0]
    for index in range(2, len(arr)):
        min_dif = min(min_dif, (arr[index] - arr[index-1]))
    for index in range (1, len(arr)):
        if arr[index] - arr[index-1] == min_dif:
            result.append([arr[index-1], arr[index]])
    return result
arr = [-3,-2,1,0]
print(min_farq(arr))