import hashlib

def sha512_encode(message):
    sha512_hash = hashlib.sha512(message.encode()).hexdigest()
    return sha512_hash

# Exemple d'utilisation :
message_to_encode = input("Enter the message you want to encode: ")
sha512_encoded_message = sha512_encode(message_to_encode)
print("SHA-512 hash:", sha512_encoded_message)
