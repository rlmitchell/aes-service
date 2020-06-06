import os
import binascii
import struct
from Crypto.Cipher import AES

class AESUtil(object):
    __module__       = 'aes-service/aesutil.py'
    __author__       = 'Rob Mitchell'
    __maintainer__   = 'Rob Mitchell'
    __email__        = 'rlmitchell@gmail.com'
    __version__      = '1.0.1'
    __version_date__ = '2020.06.06.1539ct'
    __status__       = 'personal use release'
    __description__  = 'AES wrapper that handles padding.'

    def __init__(self,key=None):
        self.key = self.check_key(key)

    def check_key(self,key):
        if len(key) < 32:
            raise Exception('32 byte/256 bit key required')
        return key[:32]

    def encrypt(self,plaintext):
        iv = os.urandom(16)
        aes = AES.new(self.key,AES.MODE_CBC,iv)
        plaintext_size = len(plaintext)
        while( (len(plaintext)%16) != 0 ):
            plaintext = plaintext + '0'
        dif = binascii.b2a_hex(struct.pack('H',(len(plaintext)-plaintext_size)))
        ciphertext = aes.encrypt(plaintext)
        return dif+iv+ciphertext

    def decrypt(self,ciphertext):
        (dif,iv,ciphertext) = (ciphertext[:4],ciphertext[4:20],ciphertext[20:]) 
        aes = AES.new(self.key,AES.MODE_CBC,iv)
        dif = binascii.a2b_hex(dif)
        dif = struct.unpack('H',dif)[0]
        plaintext = aes.decrypt(ciphertext)
        plaintext = plaintext[:len(plaintext)-dif]
        return plaintext

