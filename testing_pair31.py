from crc_tx_pair31 import XOR, crcCalc
from crc_rx_pair31 import crcCheck
from hamming_tx_pair31 import hammingCalc
from hamming_rx_pair31 import hammingCheck
import random

def clean_all_the_hamming(word):
    return word[2] + word[4:]

def ass_a(word):
    # accepting a word(binary word - data only) and adding crc
    word_to_send = word + crcCalc("1101111",word)
    print(f"the word to send is: {word_to_send}")

    # noising random single bit:
    random_index = random.randint(0, len(word_to_send) - 1)
    if int(word_to_send[random_index]) == 1:
        dirty_bit = "0"
    else:
        dirty_bit = "1"


    noisy_word = word_to_send[:random_index] + dirty_bit + word_to_send[random_index+1:]
    print(f"the noisy word is: {noisy_word} after bit: {random_index} changed")

    print(f"does the accepted word has no errors: {crcCheck('1101111', noisy_word)}")


def ass_b(names):

    print("the coeded words are:")
    coded_word_to_send = []
    for char in names:
        coded_word_to_send.append(hammingCalc(char))

    # noising:
    print("the noisy word is:")
    recived_word = []
    for i, word in enumerate(coded_word_to_send):
        count = 0
        for j, miniword in enumerate(word):
            # block 1 - randomizing a single bit error
            random_index = random.randint(0, len(miniword) - 1)
            if int(miniword[random_index]) == 1:
                dirty_bit = "0"
            else:
                dirty_bit = "1"
            coded_word_to_send[i][j] = miniword[:random_index] + dirty_bit + miniword[random_index + 1:]
            print(miniword)
            # end block 1

    # fixing the recived word:

    recived_word = coded_word_to_send
    string_after_fix = ""
    for word in recived_word:
        count = 0
        for miniword in word:
            if count == 0:
                fixed_miniword1 = clean_all_the_hamming(hammingCheck(miniword))
                count += 1
            elif count == 1:
                fixed_miniword2 = clean_all_the_hamming(hammingCheck(miniword))
                string_after_fix = string_after_fix + chr(int(fixed_miniword1 + fixed_miniword2, 2))
                count = 0
    print(f"the string at the beginning: {names}")
    print("noise noise noise!!!")
    print(f"the string after fix is : {string_after_fix}")





ass_b("raziel and ilay")
