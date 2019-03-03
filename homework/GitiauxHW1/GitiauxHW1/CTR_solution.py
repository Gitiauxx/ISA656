from Crypto.Cipher import AES
from Crypto import Random
import binascii
import sys



KEY_SIZE = AES.key_size[0]
key = Random.new().read(KEY_SIZE)
iv = Random.new().read(AES.block_size)
THIS_MODE = AES.MODE_CTR


def pad(s):
    """
    Take a string and pad it with 0 to match size of AES block 
    """
    return s + "\0" * (AES.block_size - len(s) % AES.block_size)

def unpad(s):
    """
    Remove trailing zeros"""
    return s.rstrip("\0")
     

def plus_five(cyphertext_filename, iv_filename):

    # open cyphertext
    cyphertext_file = open(cyphertext_filename, 'rb')
    cyphertext = cyphertext_file.read()
    cyphertext_file.close()

    #open iv
    iv_file = open(iv_filename, 'rb')
    iv = iv_file.read()
    iv_file.close()

    cyphertext = binascii.hexlify(cyphertext) 
    
    # each digit in the plaintext is an ascii character coded with 2 hexadecimal
    # characters, therefore the 8 first characteers of the cyphertext corresponds 
    # to the 4 digits multiple of 10. The rest is padding
    new_cyphertext = hex(int(cyphertext[0:8], 16) ^ int(binascii.hexlify("\0\0\0\05"), 16))
    new_cyphertext += cyphertext[8:]
    
    
    return new_cyphertext


if __name__ == "__main__":
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    c = plus_five(filename1, filename2)
    print("The new cyphertext is {}".format(c[2:]))


