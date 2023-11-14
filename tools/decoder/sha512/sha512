import hashlib

def sha512_encode(message, salt=None):
    sha512_hash = hashlib.sha512(salt.encode('utf-8')) if salt else hashlib.sha512()
    sha512_hash.update(message.encode('utf-8'))
    return sha512_hash.hexdigest()

def main():
    user_input = input("Enter the string to hash with SHA-512: ")
    use_salt = input("Do you want to use a salt? (yes/no): ").lower()

    if use_salt == 'yes':
        salt = input("Enter the salt: ")
        hashed_message = sha512_encode(user_input, salt)
    else:
        hashed_message = sha512_encode(user_input)

    print(f"\nOriginal string: {user_input}")
    print(f"Hashed SHA-512: {hashed_message}")

if __name__ == "__main__":
    main()
