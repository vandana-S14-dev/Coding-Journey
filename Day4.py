# Day 4 - Roman To Integer
# Platform: LeetCode

def romanToInt(s):
    roman = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    total = 0

    for i in range(len(s)):
        if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]

    return total


# Input
s = input("Enter Roman Numeral: ").upper()

try:
    print("Integer value:", romanToInt(s))
except KeyError:
    print("Invalid Roman Numeral! Please enter only I, V, X, L, C, D, M.")
# To save program from kerError