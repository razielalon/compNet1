

def hammingCalc(c):
    ascii_c = format(ord(c), '08b')
    left = ascii_c[:4]
    right = ascii_c[4:]
    to_return = []
    for i in range(2):
        if i == 0:
            s = left
        else:
            s = right

        if (int(s[0]) + int(s[1]) + int(s[3])) % 2 != 0:
            p1 = '1'
        else:
            p1 = '0'
        if (int(s[0]) + int(s[2]) + int(s[3])) % 2 != 0:
            p2 = '1'
        else:
            p2 = '0'
        if (int(s[1]) + int(s[2]) + int(s[3])) % 2 != 0:
            p3 = '1'
        else:
            p3 = '0'

        s = p1 + p2 + s[0] + p3 + s[1] + s[2] + s[3]
        print(s)
        to_return.append(s)
    return to_return


