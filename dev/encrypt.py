#BORROWED AND MODIFIED FROM CNOX.PY AVAILABLE AT:
#https://github.com/nafscript/cnox/blob/master/cnox.py

import os
import struct

from Crypto.Cipher import AES
from Crypto import Random

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

block = AES.block_size #16


# Encryption
def Encrypt(in_file, key, out_file=None, chunksize=8192):
    if not out_file:
        out_file = in_file + '.enc'

    iv = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_file)

    with open(in_file, 'rb') as infile:
        with open(out_file, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    add = b' ' * (16 - len(chunk)%16)
                    chunk = chunk + add

                outfile.write(encryptor.encrypt(chunk))
    #os.remove(in_file)

# Decryption
def Decrypt(in_file, key, out_file=None, chunksize=8192):

    if not out_file:
        #remove .enc
        out_file = os.path.splitext(in_file)[0]
        #find last/only period, and remove everything after _
        o = out_file.rsplit('.',1)
        #get string after period but before _
        if '_' in o[-1]:
            out_file = o[0] + "." + o[1].rsplit('_',1)[0]
        else:
            out_file = o[0] + "." + o[1]
        print(out_file)

    with open(in_file, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_file, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(origsize)


def main():
    aesKey = Random.new().read(16)
   #print(aesKey)
    rsaKey = RSA.generate(1024, Random.new().read)
    cipher = PKCS1_OAEP.new(rsaKey.publickey())
    ciphertext = cipher.encrypt(aesKey)
    #print(ciphertext)
    uncipher = PKCS1_OAEP.new(rsaKey)
    uncipherText = uncipher.decrypt(ciphertext)
    #print(uncipherText)

    print(rsaKey.publickey())
    export = rsaKey.publickey().exportKey()
    print(str(export))
    print(len(export))
    newKey = RSA.importKey(export)
    print(newKey)

if __name__ == '__main__':
    main()