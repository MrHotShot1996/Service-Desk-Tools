# request related functions
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import my_username, my_password, service_hub_url, app_inst_req_url, email_add_url, update_access_url

def set_up():
    '''Setup'''
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
        return driver
    except:
        print('Invalid Username or Password or timed out')
        quit()

def app_inst_request():
    # application installation requests
    driver = set_up()
    driver.get(app_inst_req_url)
    user_id = input("Enter UserID:\n")
    tag_id = input('Enter the tag number: \n')
    app_to_install = Select(driver.find_element(By.ID, 'IO:4f4b04cdf8c74b406cc7ee131c2d8638'))
    
    time.sleep(0.5)
    # Getting the options for the applications
    i = 0
    for option in app_to_install.options:
        print(f'[{i}] - {option.text}')
        i+=1
    try:
        option = input('Choose an Application: \n')
        app_to_install.select_by_index(int(option))
    except:
        print('The entered option is not a number or a valid number')

    # requested for
    time.sleep(0.5)
    requested_for = driver.find_element(By.ID, 'sys_display.IO:8625965cf8c30b406cc7ee131c2d866b')
    requested_for.send_keys(Keys.CONTROL + 'a') 
    requested_for.send_keys(Keys.DELETE)
    requested_for.send_keys(user_id)
    requested_for.send_keys(Keys.RETURN)

    # extention
    time.sleep(0.5)
    extension = driver.find_element(By.ID, 'IO:366cde10f8070b406cc7ee131c2d8649').send_keys('00000')
    
    #  pc tag number
    time.sleep(0.5)
    pc_tag = driver.find_element(By.ID, 'sys_display.IO:b77d4401f80b4b406cc7ee131c2d86b1').send_keys(tag_id)
   
    option = input('Submit? [y]/[n]\n')
    if option == 'y':
            submit = driver.find_element(By.ID, 'oi_order_now_button').click()
            ritm = driver.find_element(By.XPATH, '//*[@id="sc_cart_view"]/table/tbody/tr/td[1]/a').click()

            # To close the ticket
            catalog_task = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/span[4]/span/span[2]').click()
            cata_link = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[4]/span/div[2]/div[4]/table/tbody/tr/td/div/table/tbody/tr[1]/td[3]/a').click()
            assigned_to = driver.find_element(By.NAME, 'sys_display.sc_task.assigned_to')
            assigned_to.send_keys(Keys.CONTROL + 'a')
            assigned_to.send_keys(Keys.DELETE)
            time.sleep(0.5)
            assigned_to.send_keys(username)
            assigned_to.send_keys(Keys.RETURN)
            check_box = driver.find_element(By.XPATH, '//*[@id="e9f9d08fd08817006cc7db7b2539014c"]/div/div/div[3]/table/tbody/tr/td/div[1]/div/div/div/div[1]/div/div/div[3]/div/span/span/span').click()
            time.sleep(0.5)
            notes = driver.find_element(By.XPATH, '//*[@id="activity-stream-work_notes-textarea"]')
            notes.send_keys('Done')
            submit = driver.find_element(By.XPATH, '//*[@id="closed_complete_sc_task_bottom"]').click()


def email_config_request():
    # email configuration on phone

    driver = set_up()
    driver.get(email_add_url)
    user_id = input("Enter UserID:\n")

    device = Select(driver.find_element(By.ID, 'IO:f4f59e91419413006cc744a6f62bf3d4'))
    # Getting the options for the applications
    i = 0
    for option in device.options:
        print(f'[{i}] - {option.text}')
        i+=1
    try:
        option = input('Choose a Device: \n')
        device.select_by_index(int(option))
    except:
        print('The entered option is not a number or a valid number')

    # request for 
    requested_for = driver.find_element(By.ID, 'sys_display.IO:8625965cf8c30b406cc7ee131c2d866b')
    requested_for.send_keys(Keys.CONTROL + 'a') 
    requested_for.send_keys(Keys.DELETE)
    requested_for.send_keys(user_id)
    requested_for.send_keys(Keys.RETURN)

    # Extension
    time.sleep(0.5)
    extension = driver.find_element(By.ID, 'IO:366cde10f8070b406cc7ee131c2d8649').send_keys('00000')

    option = input('Submit? [y]/[n]\n')
    if option == 'y':
            submit = driver.find_element(By.ID, 'oi_order_now_button').click()
            ritm = driver.find_element(By.XPATH, '//*[@id="sc_cart_view"]/table/tbody/tr/td[1]/a').click()

            # To close the ticket
            catalog_task = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/span[4]/span/span[2]').click()
            cata_link = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[4]/span/div[2]/div[4]/table/tbody/tr/td/div/table/tbody/tr[1]/td[3]/a').click()
            assigned_to = driver.find_element(By.NAME, 'sys_display.sc_task.assigned_to')
            assigned_to.send_keys(Keys.CONTROL + 'a')
            assigned_to.send_keys(Keys.DELETE)
            time.sleep(0.5)
            assigned_to.send_keys(username)
            assigned_to.send_keys(Keys.RETURN)
            check_box = driver.find_element(By.XPATH, '//*[@id="e9f9d08fd08817006cc7db7b2539014c"]/div/div/div[3]/table/tbody/tr/td/div[1]/div/div/div/div[1]/div/div/div[3]/div/span/span/span').click()
            time.sleep(0.5)
            notes = driver.find_element(By.XPATH, '//*[@id="activity-stream-work_notes-textarea"]')
            notes.send_keys('Done')
            submit = driver.find_element(By.XPATH, '//*[@id="closed_complete_sc_task_bottom"]').click()

def clarvia_reset_request():
    # Clarvia password reset

    driver = set_up()
    driver.get(update_access_url)
    user_id = input("Enter UserID:\n")


    time.sleep(0.5)
    requested_for = driver.find_element(By.ID, 'sys_display.IO:8625965cf8c30b406cc7ee131c2d866b')
    requested_for.send_keys(Keys.CONTROL + 'a')
    requested_for.send_keys(Keys.DELETE)
    requested_for.send_keys(user_id)
    requested_for.send_keys(Keys.RETURN)
    
    time.sleep(0.5)
    extension = driver.find_element(By.ID, 'IO:366cde10f8070b406cc7ee131c2d8649').send_keys('00000')
    
    time.sleep(0.5)
    service_type = Select(driver.find_element(By.ID, 'IO:44180b68f80f0b406cc7ee131c2d8659'))
    service_type.select_by_visible_text('Reset Password')
    password_type = Select(driver.find_element(By.ID, 'IO:55e4ed2641d0d3006cc744a6f62bf3e4'))
    password_type.select_by_visible_text('Clairvia password reset and unlock account')
    reset_through = Select(driver.find_element(By.ID, 'IO:af85e96641d0d3006cc744a6f62bf3bb'))
    reset_through.select_by_visible_text('Over the phone')
    
    option = input('Submit? [y]/[n]\n')
    if option == 'y':
        submit = driver.find_element(By.ID, 'oi_order_now_button').click()
        ritm = driver.find_element(By.XPATH, '//*[@id="sc_cart_view"]/table/tbody/tr/td[1]/a').click()

        # To close the ticket
        catalog_task = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/span[4]/span/span[2]').click()
        cata_link = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[4]/span/div[2]/div[4]/table/tbody/tr/td/div/table/tbody/tr[1]/td[3]/a').click()
        assigned_to = driver.find_element(By.NAME, 'sys_display.sc_task.assigned_to')
        assigned_to.send_keys(Keys.CONTROL + 'a')
        assigned_to.send_keys(Keys.DELETE)
        time.sleep(0.5)
        assigned_to.send_keys(username)
        assigned_to.send_keys(Keys.RETURN)
        check_box = driver.find_element(By.XPATH, '//*[@id="e9f9d08fd08817006cc7db7b2539014c"]/div/div/div[3]/table/tbody/tr/td/div[1]/div/div/div/div[1]/div/div/div[3]/div/span/span/span').click()
        time.sleep(0.5)
        notes = driver.find_element(By.XPATH, '//*[@id="activity-stream-work_notes-textarea"]')
        notes.send_keys('Done')
        submit = driver.find_element(By.XPATH, '//*[@id="closed_complete_sc_task_bottom"]').click()


