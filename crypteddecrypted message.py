import random
import base64

def generate_key(length):
    key = ''
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for _ in range(length):
        key += random.choice(characters)
    return key

def encrypt_message(message, key):
    encrypted_message = ''
    for i, char in enumerate(message):
        if char != ' ':
            char_bytes = char.encode('utf-8')
            key_char = key[i % len(key)]
            key_bytes = key_char.encode('utf-8')
            encrypted_bytes = bytes(b1 ^ b2 for b1, b2 in zip(char_bytes, key_bytes))
            encrypted_char = base64.b64encode(encrypted_bytes).decode('utf-8')
        else:
            encrypted_char = ' '  # Preserve spaces as is
        encrypted_message += encrypted_char
    return encrypted_message

def decrypt_message(encrypted_message, key):
    decrypted_message = ''
    char_index = 0
    for char in encrypted_message:
        if char != ' ':
            encrypted_char = encrypted_message[char_index:char_index+4]
            if encrypted_char != '====':  # Skip padding
                encrypted_bytes = base64.b64decode(encrypted_char)
                key_char = key[char_index % len(key)]
                key_bytes = key_char.encode('utf-8')
                decrypted_bytes = bytes(b1 ^ b2 for b1, b2 in zip(encrypted_bytes, key_bytes))
                decrypted_char = decrypted_bytes.decode('utf-8')
                decrypted_message += decrypted_char
            char_index += 4
        else:
            decrypted_message += ' '  # Preserve spaces as is
    return decrypted_message

choice = input("Enter 'encode' to encrypt a message or 'decode' to decrypt a message: ")

if choice == "encode":
    message = input("Enter the message to encrypt: ")
    key = generate_key(len(message))
    encrypted_message = encrypt_message(message, key)
    print("Encrypted message:", encrypted_message)
    print("Key:", key)
elif choice == "decode":
    encrypted_message = input("Enter the message to decrypt: ")
    key = input("Enter the key: ")
    decrypted_message = decrypt_message(encrypted_message, key)
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid choice. Please enter either 'encode' or 'decode'.")
