__author__ = 'Mike'
from Crypto.PublicKey import RSA
from Crypto import Random

def encode(str1, public_key):
    return public_key.encrypt(str1.encode(),32)[0]

def decrypt_string(enc_str1, key):
    b_str = key.decrypt(enc_str1)
    return b_str.decode()

def gen_keys():
    random_gen = Random.new().read
    return RSA.generate(1024, random_gen)

def enc_file(fname, public_key):
    with open(fname, 'r+') as orig_file:
        with open(fname + '.enc', 'wb') as enc_file:
            enc_file.write(encode(orig_file.read(),public_key))
        enc_file.closed
    orig_file.closed

    return True

def dec_file(fname, priv_key):
    with open(fname, 'rb+') as enc_file:
        fname2 = 'dec_' + fname[0:len(fname)-3]
        with open(fname2, 'w') as new_file:
            dec_string = decrypt_string(enc_file.read(), priv_key)
            new_file.write(dec_string)
        new_file.closed
    enc_file.closed
    return True


