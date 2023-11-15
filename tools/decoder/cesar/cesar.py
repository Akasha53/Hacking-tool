import hashlib

def md5_encode(message):
    md5_hash = hashlib.md5(message.encode()).hexdigest()
    return md5_hash

# Exemple d'utilisation :
message_to_encode = input("Enter the message you want to encode: ")
md5_encoded_message = md5_encode(message_to_encode)
print("MD5 hash:", md5_encoded_message)
