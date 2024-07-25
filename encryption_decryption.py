# This Python code is implementing a simple encryption and decryption algorithm using a random key
# generated from a combination of punctuation, digits, and letters. Here's a breakdown of what the
# code does:
import random
import string

chars = ' ' +string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"key : {key}")
print(f"chars :{chars}")


# ENCRYPT

# This part of the code is responsible for encrypting a message entered by the user. Here's a
# breakdown of how it works:
plain_text = input("enter a massage to encrypt : ")
cipher_text = ""


for letter in plain_text: 
  index = chars.index(letter)
  cipher_text += key[index]
  
print(f"original maessage: {plain_text}")
print(f"encrypted message: {cipher_text}")


# decrypt

# This part of the code is responsible for decrypting a message that was previously encrypted using
# the generated key. Here's a breakdown of how the decryption process works:
cipher_text = input("enter a massage to decrypt : ")
plain_text = ""


for letter in cipher_text:
  index = key.index(letter)
  plain_text += chars[index]
  
print(f"original maessage: {cipher_text}")
print(f"encrypted message: {plain_text}")
