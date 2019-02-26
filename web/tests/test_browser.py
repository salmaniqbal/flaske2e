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

    driver.get('http://127.0.0.1:5000')
    time.sleep(2)

    #Fill name, email and phone in the example form
    page_heading = driver.find_element_by_id('pageheading')
    assert page_heading.text == 'Welcome to flask app' 

    if(page_heading.text == 'Welcome to flask app'):
        print ("Success: Heading of flask app is correct!")
        pass_check_counter += 1
    else:
        print ("Failed: Heading of flask app is correct!")
    total_checks += 1

    driver.quit() 
 
    #Assert if the pass and fail check counters are equal
    assert total_checks == pass_check_counter 
#---START OF SCRIPT
if __name__=='__main__':
    test_example_form()