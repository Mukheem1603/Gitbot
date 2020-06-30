import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

user = input("Enter your Github Email/Github Username:")
passcode = getpass.getpass("Enter password:")
repo = input("Repository to be named as(make sure you give a unique name :) ):")
desc = input("Description(if any or press enter):")
access = input("Public/Private???: ")
driver = webdriver.Chrome()
driver.get('https://github.com/')
time.sleep(2)
driver.maximize_window()
time.sleep(2)
signin = driver.find_element_by_link_text('Sign in')
signin.click()
time.sleep(2)
username = driver.find_element_by_xpath('//*[@id="login_field"]')
username.send_keys(user)
pwd = driver.find_element_by_xpath('//*[@id="password"]')
pwd.send_keys(passcode)
sbtn = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
time.sleep(2)
sbtn.click()
# checking status
def create_repo():
    new = driver.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/summary')
    new.click()
    print('Sign in successful!!!')
    # driver.minimize_window()
    time.sleep(3)
    # driver.maximize_window()
    new.send_keys(Keys.DOWN)
    time.sleep(2)
    cnr = driver.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/details-menu/a[1]')
    cnr.click()
    time.sleep(2)
    rinp = driver.find_element_by_xpath('//*[@id="repository_name"]')
    rinp.send_keys(repo)
    time.sleep(2)
    d = driver.find_element_by_xpath('//*[@id="repository_description"]')
    d.send_keys(desc)
    time.sleep(2)
    if access=="Public" or access=="public":
        pub = driver.find_element_by_xpath('//*[@id="repository_visibility_public"]')
        pub.click()
        time.sleep(2)
        create = driver.find_element_by_xpath('//*[@id="new_repository"]/div[5]/button')
        create.click()
        time.sleep(2)
        print("A public repository named "+repo+" has been created successfully!!!")
        # driver.minimize_window()
        time.sleep(3)
        # driver.maximize_window()
    else:
        pri = driver.find_element_by_xpath('//*[@id="repository_visibility_private"]')
        pri.click()
        time.sleep(2)
        create = driver.find_element_by_xpath('//*[@id="new_repository"]/div[5]/button')
        create.click()
        time.sleep(2)
        print("A private repository named "+repo+" has been created successfully!!!")
        # driver.minimize_window()
        time.sleep(3)
        # driver.maximize_window()
# fail = driver.find_element_by_xpath('//*[@id="js-flash-container"]/div/div')
try:
    
    create_repo()
    time.sleep(3)
    driver.minimize_window()
    ans = input("Sign out??? Yes/No:")
    if ans=="yes" or ans=="Yes":
        driver.quit()
        
    else:
        driver.maximize_window()

    
except NoSuchElementException as e: 
    print('Incorrect Username/Password!!!!') 
    print(e)
    driver.quit()
