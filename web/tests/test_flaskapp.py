"""
Qxf2 Services: Utility script to test example form
NOTE: This is a contrived example that was written up to make this blog post clear
We do not use this coding pattern at our clients
"""
 
from selenium import webdriver
import sys,time
import os
 
def test_example_form():
    "Test example form"
  
    driver_directory = os.getcwd()
    driver = webdriver.Chrome(driver_directory + '/chromedriver')
    #Create variables to keep count of pass/fail
    pass_check_counter = 0
    total_checks = 0
 
    #Visit the tutorial page
    driver.get('http://qxf2.com/selenium-tutorial-main') 
    #Check 1: Is the page title correct?
    if(driver.title=="Qxf2 Services: Selenium training main"):
        print ("Success: Title of the Qxf2 Tutorial page is correct")
        pass_check_counter += 1
    else:
        print ("Failed: Qxf2 Tutorial page Title is incorrect")
    total_checks += 1
 
    #Fill name, email and phone in the example form
    name_field = driver.find_element_by_xpath("//input[@type='name']")
    name_field.send_keys('Shivahari')
    email_field = driver.find_element_by_xpath("//input[@type='email']")
    email_field.send_keys('test@qxf2.com')
    phone_field = driver.find_element_by_xpath("//input[@type='phone']")
    phone_field.send_keys('9999999999')
    submit_button = driver.find_element_by_xpath("//button[@type='submit']") #Click on the Click me button
    submit_button.click()
    time.sleep(2)
    #Check 2: Is the page title correct?
    if(driver.title=="Qxf2 Services: Selenium training redirect"):
        print ("Success: The example form was submitted")
        pass_check_counter += 1
    else:
        print ("Failed: The example form was not submitted. Automation is not on the redirect page")
    total_checks += 1
    #Quit the browser window
    driver.quit() 
 
    #Assert if the pass and fail check counters are equal
    assert total_checks == pass_check_counter 
 
#---START OF SCRIPT
if __name__=='__main__':
    test_example_form()