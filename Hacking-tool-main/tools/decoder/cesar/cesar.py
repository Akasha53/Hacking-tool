message = input("Enter the message you want to encode: ")
shift = int(input("Enter the shift value (integer): "))
length = len(message)

encoded_message = ""

for x in range(length):
  char = message[x]
  if char.isalpha():
    unicode = ord(char)
    if char.islower():
      encoded_unicode = (unicode - 97 + shift) % 26 + 97
    else:
      encoded_unicode = (unicode - 65 + shift) % 26 + 65
    encoded_message += chr(encoded_unicode)
  else:
    encoded_message += char

print("Encoded message:", encoded_message)
