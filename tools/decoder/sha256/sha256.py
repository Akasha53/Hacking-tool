import hashlib

def sha256_encode(message):
    sha256_hash = hashlib.sha256(message.encode()).hexdigest()
    return sha256_hash

# Exemple d'utilisation :
message_to_encode = input("Enter the message you want to encode: ")
sha256_encoded_message = sha256_encode(message_to_encode)
print("SHA-256 hash:", sha256_encoded_message)
