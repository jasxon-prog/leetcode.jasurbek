def rome_integer(roman_number: str) ->int:
    r_a = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
    if not roman_number:
        return 0
    result = r_a[roman_number[0]]
    for i in range(1, len(roman_number)):
        result += r_a[roman_number[i]]
        if r_a[roman_number[i]] > r_a[roman_number[i-1]]:
            result -= 2*r_a[roman_number[i-1]] 
    return result

roman_numbers = 'IX'
print(rome_integer(roman_numbers))