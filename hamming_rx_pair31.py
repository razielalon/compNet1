from hamming_tx_pair31 import hammingCalc

def hammingCheck(coded_word):
    # checks hamming(7,4), coded word is 8 bits binary
    p1, p2, p3 = 0, 0, 0
    if (int(coded_word[0]) + int(coded_word[2]) + int(coded_word[4]) + int(coded_word[6])) % 2 != 0:
        p1 = 1
    if (int(coded_word[1]) + int(coded_word[2]) + int(coded_word[5]) + int(coded_word[6])) % 2 != 0:
        p2 = 1
    if (int(coded_word[3]) + int(coded_word[4]) + int(coded_word[5]) + int(coded_word[6])) % 2 != 0:
        p3 = 1
    if not p1 and not p2 and not p3:
        print('word is great, miawule!')
    else:  # fixing the word, given only one error
        errorInd = (p1 + 2*p2 + 4*p3) - 1
        if int(coded_word[errorInd]) == 1:
            coded_word = coded_word[:errorInd] + "0" + coded_word[errorInd+1:]
        else:
            coded_word = coded_word[:errorInd] + "1" + coded_word[errorInd+1:]
        print(coded_word)
        return coded_word

