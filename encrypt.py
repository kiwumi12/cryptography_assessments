from cryptography.fernet import Fernet
import rsa
# open the symmetric key file
skey = open('symmetric.key','rb')
key = skey.read()

# create the cipher
cipher = Fernet(key)

# open file for encrypting

myfile = open('mytextfile.txt','rb')
myfiledata= myfile.read()

# encrypt the data
encrypted_data = cipher.encrypt(myfiledata)
edata = open('encrypted_file','wb')
edata.write(encrypted_data)

print(encrypted_data)

# open the public key file
pkey = open('publickey.key','rb')
pkdata = pkey.read()

# load the file
pubkey = rsa.PublicKey.load_pkcs1(pkdata)

# encrypt the symmetric key file with the public key
encrypted_key = rsa.encrypt(key,pubkey)

ekey = open('encrypted_key','wb')
ekey.write(encrypted_key)

print(encrypted_key)
