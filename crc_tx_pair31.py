
def XOR(word1, word2):
    int1 = int(word1, 2)
    int2 = int(word2, 2)
    xor_result = int1 ^ int2
    # Convert the result back to a binary string
    return str(bin(xor_result)[2:])


# calculating CRC given gen poly and word to send
def crcCalc(gen_poly, word, reciver_side=False):
    if not reciver_side:
        padded_word = word + "0" * (len(gen_poly)-1)
    else:
        padded_word = word
    compliment = padded_word[len(gen_poly):]
    xor_res = XOR(padded_word[:len(gen_poly)], gen_poly)

    finished = False
    flag = False
    while not finished:
        # more numbers going dowm
        if len(compliment) > 0:
            while len(xor_res) < len(gen_poly) :
                xor_res = xor_res + compliment[0]
                compliment = compliment[1:]
                if len(compliment) == 0 and len(xor_res) < len(gen_poly):
                    flag = True
                    break
            if not flag:
                xor_res = XOR(xor_res, gen_poly)
        else:
            finished = True
    xor_res = "0"*(len(gen_poly)-1 - len(xor_res)) + xor_res
    return xor_res

