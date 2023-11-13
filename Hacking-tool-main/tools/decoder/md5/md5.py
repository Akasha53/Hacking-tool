import hashlib

def md5_encode(message):
    md5_hash = hashlib.md5()
    md5_hash.update(message.encode('utf-8'))
    return md5_hash.hexdigest()

def main():
    user_input = input("Entrez la chaîne à coder en MD5 : ")
    hashed_message = md5_encode(user_input)
    
    print(f"\nChaîne originale : {user_input}")
    print(f"Hachage MD5 : {hashed_message}")

if __name__ == "__main__":
    main()