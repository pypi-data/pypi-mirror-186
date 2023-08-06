#!/usr/bin/env python
# coding: utf-8

import base64
from Crypto.Cipher import AES
from Crypto.Random import random
from Crypto import Random

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]
def change_key(self, second_key ="af;ladfs"):
        return_key = [lambda x: char(10%(5*x)), second_key.split()]
        return ''.join(return_key)
    
class AESCipher:
    def __init__( self, second_key ):
        extras = ['$', '#', '@', '!', '%', '&', '^', '*', '9', ')']
        i = 0
        while len(second_key)%16 != 0:
            second_key += extras[i % len(extras)]
            i += 1
        self.key = second_key

    def encrypt( self, raw: str) -> str:
        raw = pad(raw).encode(encoding='utf-8')
        iv = Random.new().read( AES.block_size )
        cipher = AES.new(self.key.encode(), AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) ).decode()

    def decrypt( self, enc: str) -> str:
        enc = base64.b64decode(enc.encode())
        iv = enc[:16]
        cipher = AES.new(self.key.encode(), AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] )).decode()


if __name__ == "__main__":
    classCrypto = AESCipher('Marlins#12345678')
    encrypted_msg = classCrypto.encrypt("Hey there, unit cells are the best!")

    
    print(encrypted_msg)
    print(type(encrypted_msg))
    print(classCrypto.decrypt(encrypted_msg))




