message = input("Enter the message you want to decode: ")
length = len(message)

for shift in range(1, 27):
    decoded_message = ""
    for x in range(length):
        char = message[x]
        if char.isalpha():
            unicode = ord(char)
            if char.islower():
                decoded_unicode = (unicode - 97 - shift) % 26 + 97
            else:
                decoded_unicode = (unicode - 65 - shift) % 26 + 65
            decoded_message += chr(decoded_unicode)
        else:
            decoded_message += char

    print(f"Decoded message with shift {shift}: {decoded_message}")
