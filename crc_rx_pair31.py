from crc_tx_pair31 import XOR, crcCalc

def crcCheck(gen_pol, word):
    return int(crcCalc(gen_pol,word,reciver_side=True)) == 0

