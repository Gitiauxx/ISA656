import tools
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import sys

def decrypt(key_pub, ctext, messagespace):
    key_pub = RSA.importKey(open(key_pub, 'r').read())
    cyphertext = eval(open(ctext, 'r').read())
    

    # read message sapce line by line
    with open (messagespace) as m:
        for line in m:
            
            line_int = tools.text_to_int(line.strip())
            c = key_pub.encrypt(line_int, None)
            
            if c == cyphertext:
                return line

    return 


if __name__ == "__main__":
    key_pub = sys.argv[1]
    ctext = sys.argv[2]
    messages = sys.argv[3]
    print("The message is: {}".format(decrypt(key_pub, ctext, messages)))
