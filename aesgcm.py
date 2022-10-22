#第三方加密库pyca/cryptography 
#pip install cryptography
import os
import uuid
import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (Cipher, algorithms, modes)

def encrypt(key, plaintext):
  iv = os.urandom(12)
  encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=default_backend()
  ).encryptor()
  ciphertext = encryptor.update(plaintext) + encryptor.finalize() + encryptor.tag #将tag直接追加在最后，即可和java解密代码兼容
  return ciphertext.hex().upper()

if __name__ =='__main__':
    key = os.urandom(32)
    requestId = str(uuid.uuid4())
    payload = {
        "appId":"036",
        "msgName":"userEvent",
        "requestId":requestId,
        "traceId":requestId,
        "payload":"security"
    }
    plaintext = json.dumps(payload).encode()
    ciphertext = encrypt(key, plaintext)
    print(ciphertext)
