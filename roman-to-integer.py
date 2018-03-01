m = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

test = ['XXV', 'DCXIII', 'IX', 'DCXXI']

def roman_to_int(s):
    num, pre = 0, 'I'
    for c in s[::-1]:
        num, pre = num - m[c] if m[c] < m[pre] else num + m[c], c
    return num


if __name__ == '__main__':
    for num in test:
        print(f'{num} -> {roman_to_int(num)}')