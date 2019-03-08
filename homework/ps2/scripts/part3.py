from tools import find_root, int_to_text
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import sys

def decrypt(ctext):
    
    cyphertext = eval(open(ctext, 'r').read())
    m = find_root(cyphertext[0], 3)

    return int_to_text(m)


if __name__ == "__main__":
    ctext = sys.argv[1]
    print("The message is: {}".format(decrypt(ctext)))