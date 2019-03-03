from Crypto.Cipher import AES
from Crypto import Random


KEY_SIZE = AES.key_size[0]
key = Random.new().read(KEY_SIZE)
iv = Random.new().read(AES.block_size)


def pad(s):
    """
    Take a string and pad it with 0 to match size of AES block 
    """
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def unpad(s):
    """
    Remove trailing zeros"""
    return s.rstrip(b"\0")

# get image
input_file = open("../minilab_data/tux6.ppm", 'rb')
input_data = input_file.read()
input_file.close()

# get ppm header: {P6}\n {width} {height} \n{color} \n
splits = input_data.split(b"\n", 3)
data_for_encryption = splits[3]
style = splits[0]
size = splits[1]
color = splits[2]

# encryt with ECB
THIS_MODE = AES.MODE_ECB
ecb_cipher = AES.new(key, THIS_MODE)
encrypt_data_ecb =ecb_cipher.encrypt(pad(data_for_encryption))

# save file after adding ppm_header P6}\n {width} {height} \n{color} \n
output_file = open("../results/ECB_image.ppm", "wb")
output_file.write(b"\n".join([style, size, color, encrypt_data_ecb]))
output_file.close()

# encryt with CBC
THIS_MODE = AES.MODE_CBC
cbc_cipher = AES.new(key, THIS_MODE, iv)
encrypt_data_cbc = cbc_cipher.encrypt(pad(data_for_encryption))

# save file after adding ppm_header P6}\n {width} {height} \n{color} \n
output_file = open("../results/CBC_image.ppm", "wb")
output_file.write(b"\n".join([style, size, color, encrypt_data_cbc]))
output_file.close()


