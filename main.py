def main():
  function = int(
    input(
      "Welcome, "
      "! What do you want to do today?\n 1: hack\n 2: osint\n 3: code & decode\n>> "
    ))

  if function == 1:
    hack()
  elif function == 2:
    osint()
  elif function == 3:
    decode()
  else:
    print("Please enter 1, 2, or 3.")


def hack():
  hack_type = int(
    input(
      "What type of attack do you want?\n 1: classical bruteforce\n 2: dictionary bruteforce\n 3: Specific bruteforce (depend on the target)\n 4: Specific intelligent bruteforce attack (depend on the target, won't try every possibility but only the most intelligent)\n>> "
    ))

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
  osint_type = int(input("What useful tools?\n 1: blabla\n>> "))
  if osint_type == 1:
    print("")


def decode():
  decode_type = int(
    input("What useful tools?\n 1: Caesar encode\n 2: Caesar decode\n 3: MD5 encode \n 5: sha256 encode\n 7: sha512 encode\n>> "))
  if decode_type == 1:
    exec(open("tools\decoder\cesar\cesar.py").read())
  elif decode_type == 2:
    exec(open("tools\decoder\cesar\decesar.py").read())
  elif decode_type == 3:
    exec(open("tools\decoder\md5\md5.py").read())
  elif decode_type == 3:
    exec(open("tools\decoder\sha256\sha256.py").read())
  elif decode_type == 3:
    exec(open("tools\decoder\sha512\sha512.py").read())
  else:
    print("Invalid enter.")


if __name__ == "__main__":
  main()
