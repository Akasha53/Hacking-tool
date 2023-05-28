def main():
  surname = input("What is your surname? \n >> ")
  function = int(
    input(
      "Welcome, " + surname +
      "! What do you want to do today?\n 1: hack \n 2: osint \n 3: code & decode\n >>"
    ))
  if function == 1:
    hack()

  elif function == 2:
    osint()

  elif function == 3:
    decode()
  else:
    print("Please enter 1, 2 or 3.")


def hack():
  hack_type = int(
    input(
      "What type of attack do you want? \n 1: classical bruteforce \n 2: dictionary bruteforce \n 3: Specific bruteforce (depend on the target)\n >>",
      "Every bruteforce need a target, to give them one please read the README.md and follow the instructions."
    ))

  if hack_type == 1:
    exec(open("./bruteforce_c.py").read())

  if hack_type == 2:
    exec(open("./bruteforce_D.py").read())
    
  if hack_type == 3:
    exec(open("bruteforce_spe.py").read())


def osint():
  osint_type = int(input("What useful tools?\n 1: blabla\n >> "))
  if osint_type == 1:
    print("")


def decode():
  osint_type = int(
    input("What useful tools?\n 1:Cesar's code \n 2: Cesar's decode \n >> "))
  if osint_type == 1:
    exec(open("./cesar.py").read())
  if osint_type == 2:
    exec(open("./decesar.py").read())


main()
