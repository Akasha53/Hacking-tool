import hashlib

def main():
    print("Welcome! What do you want to do today?")
    print("1: Bruteforce")
    print("2: OSINT")
    print("3: Code & Decode")
    choice = int(input(">> "))
    
    if choice == 1:
        hack()
    elif choice == 2:
        osint()
    elif choice == 3:
        decode()
    else:
        print("Please enter 1, 2, or 3.")

def hack():
    print("What type of attack do you want?")
    print("1: Classical Bruteforce")
    print("2: Dictionary Bruteforce")
    print("3: Specific Bruteforce (depends on the target)")
    print("4: Specific Intelligent Bruteforce Attack (depends on the target, won't try every possibility but only the most intelligent)")
    hack_type = int(input(">> "))
    
    if hack_type == 1:
        exec(open("./tools/bruteforce/classical.py").read())
    elif hack_type == 2:
        exec(open("./tools/bruteforce/dictionary.py").read())
    elif hack_type == 3:
        exec(open("./tools/bruteforce/special.py").read())
    elif hack_type == 4:
        exec(open("./tools/bruteforce/special_smart.py").read())
    else:
        print("Invalid hack type.")

def osint():
    print("What useful tools?")
    print("1: OSINT book (with a huge number of websites)")
    print("2: ")
    osint_type = int(input(">> "))
    
    if osint_type == 1:
        print_osint_book()

def print_osint_book():
    with open("tools/osint/OSINT_Handbook_June-2018_Final.pdf", "rb") as file:
        pdf_document = fitz.open("pdf", file.read())
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text = page.get_text()
            print(text)

def decode():
    print("What useful tools?")
    print("1: Caesar encode")
    print("2: Caesar decode")
    print("3: MD5 encode")
    print("4: SHA256 encode")
    print("5: SHA512 encode")
    decode_type = int(input(">> "))
    
    if decode_type == 1:
        exec(open("tools/decoder/cesar/cesar.py").read())
    elif decode_type == 2:
        exec(open("tools/decoder/cesar/decesar.py").read())
    elif decode_type == 3:
        md5_input = input("Enter the string to be hashed with MD5: ")
        md5_hash = hashlib.md5(md5_input.encode()).hexdigest()
        print(f"MD5 hash: {md5_hash}")
    elif decode_type == 4:
        exec(open("tools/decoder/sha256/sha256.py").read())
    elif decode_type == 5:
        exec(open("tools/decoder/sha512/sha512.py").read())
    else:
        print("Invalid enter.")

if __name__ == "__main__":
    main()
