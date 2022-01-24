# Incidents related functions
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import my_username, my_password, service_hub_url, incident_creation_url

# data set-up
def categories():
    # setting up
    sub_category = ""
    incident_type = ""
    num = 0
    categories = {
        "Access Accounts":"Accounts Accounts",
        "Applications and Software":{
            "Other Systems":['Hospital Portal', 'IG Mobile', 'PC Applications', 'Enterprise Correspondence (EC)', 'Citrix', 'Policy Management System', 'Share file'],
        },
        "Devices":["Computing Devices", "Printers, Scanners and Paper management equipment"],
        "Network and Communications":["Email", "Mobile", "Network"]

    }
    choice = input(
        "Enter a category:\n"
        "1 - Access Accounts\n"
        "2 - Application and software\n"
        "3 - Devices\n"
        "4 - Network\n"
    )

    if choice == "1":
        category = "Access Accounts"
        sub_category = "AD Account"
        return category, sub_category, incident_type
    
    elif choice == "2":
        category = "Applications and Software"
        sub_category = "Other Systems"
        for i in categories[category][sub_category]:
            print(f'{num} ', '-', i)
            num+=1
        choice = int(input("Enter incident type:\n"))
        incident_type = categories["Applications and Software"]["Other Systems"][choice]
        return category, sub_category, incident_type
    
    elif choice == "3":
        category = "Devices"
        for i in categories[category]:
            print(f'{num} ', '-', i)
            num+=1
        choice = int(input("Enter incident type:\n"))
        sub_category = categories[category][choice]
        return category, sub_category, incident_type

    elif choice == "4":
        category = "Network and Communications"
        for i in categories[category]:
            print(f'{num} ', '-', i)
            num+=1
        choice = int(input("Enter incident type:\n"))
        sub_category = categories[category][choice]
        return category, sub_category, incident_type



# incident functions
def self_incident():
    # Creating an incident for self credit
    # Set-up
    try:
        # Constants
        chrome_options = Options()
        chrome_options.add_argument('--log-level=3') #Getting rid of selenum logs
        # chrome_options.add_argument('headless')
        driver = webdriver.Chrome(options=chrome_options) #Chromium 
    except:
        print("Error: Chrome driver not matching Chrome version")
        quit()
    driver.implicitly_wait(20)
    driver.get(service_hub_url)
    driver.switch_to.frame('gsft_main')
    try:
        # Logging in 
        username_hub = driver.find_element(By.ID, 'user_name').send_keys(my_username)
        password_hub = driver.find_element(By.ID, 'user_password').send_keys(my_password)
        login = driver.find_element(By.XPATH, '//*[@id="login-body"]/div[2]/button').click()
    except:
        print('Invalid Username or Password or timed out')
        quit()
    driver.get(incident_creation_url)

    # Incident info
    user_id = input("Enter user ID\n")
    location_floor = input('Enter Floor: \n')
    location_room = input('Enter Room: \n')
    location_ext = input('Enter Ext: \n')
    location_building = input('Enter Building: \n')
    location_details = (
    f'Floor: {location_floor}\n'
    f'Room: {location_room}\n'
    f'Extension: {location_ext}\n'
    f'Building: {location_building}'
    )

    category, sub_category, incident_type = categories()
    short_description = input("Enter short description\n")
    description = input("Enter description\n")

    
    # userID
    create_id = driver.find_element(By.ID, 'sys_display.incident.caller_id')
    create_id.send_keys(user_id)
    create_id.send_keys(Keys.RETURN)

    # location input
    time.sleep(0.5)
    location = driver.find_element(By.XPATH, '//*[@id="incident.u_full_location"]')
    location.send_keys(Keys.CONTROL + 'a')
    location.send_keys(Keys.DELETE)
    location.send_keys(location_details)
    location.send_keys(Keys.RETURN)

    # contact type
    time.sleep(0.5)
    contact_type = Select(driver.find_element(By.XPATH, '//*[@id="incident.contact_type"]'))
    contact_type.select_by_visible_text("Phone")

    # category input
    time.sleep(0.5)
    create_category = driver.find_element(By.ID, 'sys_display.incident.u_category')
    create_category.send_keys(category)
    create_category.send_keys(Keys.RETURN)

    # sub-catagory input
    time.sleep(0.5)
    create_subcatg = driver.find_element(By.ID, 'sys_display.incident.u_subcategory')
    create_subcatg.send_keys(sub_category)
    create_subcatg.send_keys(Keys.RETURN)

    # incident type
    time.sleep(0.5)
    create_incident_type = driver.find_element(By.ID, 'sys_display.incident.u_incident_type')
    create_incident_type.send_keys(incident_type)
    create_incident_type.send_keys(Keys.RETURN)

    # assigned group
    time.sleep(0.5)
    create_assign = driver.find_element(By.XPATH, '//*[@id="sys_display.incident.assignment_group"]')
    create_assign.send_keys(Keys.CONTROL + 'a')
    create_assign.send_keys(Keys.DELETE)
    create_assign.send_keys("SERVICE DESK (Sec)-R")
    create_assign.send_keys(Keys.RETURN)

    # assigned to
    time.sleep(0.5)
    create_assigned_to = driver.find_element(By.XPATH, '//*[@id="sys_display.incident.assigned_to"]')
    create_assigned_to.send_keys(my_username)

    # short description
    time.sleep(0.5)
    create_short = driver.find_element(By.XPATH, '//*[@id="incident.short_description"]')
    create_short.send_keys(short_description)
    create_short.send_keys(Keys.RETURN)

    # long description
    time.sleep(0.5)
    create_long = driver.find_element(By.XPATH, '//*[@id="incident.description"]')
    create_long.send_keys(description)
    create_long.send_keys(Keys.RETURN)

    submit_status = input("Submit? (y)/(n)\n")
    if submit_status == 'y':
        submit_incident = driver.find_element(By.XPATH, '//*[@id="sysverb_insert_bottom"]').click()
        print('--- Ticket created ---\n')
        input('Press any button to close')
    if submit_status == 'n':
        input('Your ticket has not been created, press enter to end')
        quit()


    print(category)
    print(sub_category)
    print(incident_type)
    input()

