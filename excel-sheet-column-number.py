# Given a column title as appear in an Excel sheet, return its corresponding column number.

# AA -> 27

def titleToNumber(s):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    out = 0
    for c in s:
        nums.append(alphabet.index(c) + 1)
    for index, i in enumerate(nums[::-1]):
        out += i * (26**index)
    return out

def titleToNumber2(s):
    s = s[::-1]
    sum = 0
    for exp, char in enumerate(s):
        sum += (ord(char) - 65 + 1) * (26 ** exp)
    return sum


print(titleToNumber2('C'))
    
