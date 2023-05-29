def main():
  surname = input("What is your surname?\n>> ")
  function = int(
    input(
      "Welcome, " + surname +
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
    exec(open("./tools/brutforce/classical").read())
  elif hack_type == 2:
    exec(open("./tools/brutforce/dictionary.py").read())
  elif hack_type == 3:
    exec(open("bruteforce_spe.py").read())
  elif hack_type == 4:
    exec(open("bruteforce_spe_smart.py").read())
  else:
    print("Invalid hack type.")


def osint():
  osint_type = int(input("What useful tools?\n 1: blabla\n>> "))
  if osint_type == 1:
    print("")


def decode():
  decode_type = int(
    input("What useful tools?\n 1: Caesar's code\n 2: Caesar's decode\n>> "))
  if decode_type == 1:
    exec(open("./cesar.py").read())
  elif decode_type == 2:
    exec(open("./decesar.py").read())
  else:
    print("Invalid decode type.")


if __name__ == "__main__":
  main()
