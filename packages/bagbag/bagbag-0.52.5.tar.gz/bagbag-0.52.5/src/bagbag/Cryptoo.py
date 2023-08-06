from Crypto.Cipher import AES as AAAES
from Crypto import Random
import base64
import hashlib

class AES():
    def __init__(self, key:str, mode:str="cfb"): 
        """
        The function takes a key and a mode as arguments, and sets the block size, key, and mode of the
        cipher
        
        :param key: The key to use for the encryption
        :type key: str
        :param mode: The mode of operation for the cipher object; must be one of "ecb", "cbc", "cfb",
        "ofb", defaults to cfb
        :type mode: str (optional)
        """
        self.bs = AAAES.block_size
        self.key = hashlib.sha256(key.encode()).digest()
        self.mode = {
            "cfb": AAAES.MODE_CFB, 
            "cbc": AAAES.MODE_CBC,
            "ecb": AAAES.MODE_ECB, 
            "ofb": AAAES.MODE_OFB,
        }[mode]

    def Encrypt(self, raw:str) -> str:
        raw = self._pad(raw)
        iv = Random.new().read(AAAES.block_size)
        if self.mode == AAAES.MODE_ECB:
            cipher = AAAES.new(self.key, self.mode)
        else:
            cipher = AAAES.new(self.key, self.mode, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode())).decode('utf-8')

    def Decrypt(self, enc:str) -> str:
        enc = base64.b64decode(enc)
        iv = enc[:AAAES.block_size]
        if self.mode == AAAES.MODE_ECB:
            cipher = AAAES.new(self.key, self.mode)
        else:
            cipher = AAAES.new(self.key, self.mode, iv)
        return self._unpad(cipher.decrypt(enc[AAAES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

if __name__ == "__main__":

    for mode in ["ecb", "cbc", "cfb", "ofb"]:
        print(mode)
        a = AES("1685pXjF(2IPucuKl23D[YZuIKd95zkmb2", mode)

        e = a.Encrypt("enc = base64.b64decode(enc)")
        print(e)

        c = a.Decrypt(e)
        print(c)