import rsa
from cryptography.fernet import Fernet


import rsa

# Open key file and return key data
def file_open(file):
    key_file = open(file, 'rb')
    key_data = key_file.read()
    key_file.close()
    return key_data


# Open public key file and load in key
pubkey = rsa.PublicKey.load_pkcs1(file_open('publickey.key'))

message = file_open('mytextfile.txt')
signature = file_open('signature_file')

# Verify the signature to show if successful or failed
try:
    rsa.verify(message,signature,pubkey)
    print("Signature successfully verified")
    
    
    # load the private key to decrypt the public key
    prkey = open('privkey.key','rb')
    pkey = prkey.read()
    private_key = rsa.PrivateKey.load_pkcs1(pkey)

    e = open('encrypted_key','rb')
    ekey = e.read()

    dpubkey = rsa.decrypt(ekey,private_key)

    cipher = Fernet(dpubkey)

    encrypted_data = open('encrypted_file','rb')
    edata = encrypted_data.read()


    decrypted_data = cipher.decrypt(edata)

    print(decrypted_data.decode())



except:
    print("Warning!!!! Signature could not be verified")