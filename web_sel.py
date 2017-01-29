#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import argparse

def show_tax_info():
    swis = args.swis # str(args.pin)[:4]
    browser = webdriver.Firefox()
    browser.implicitly_wait(10) # seconds
    browser.get('http://www.co.orange.ny.us/content/124/1368/4136.aspx')
    enter = browser.find_element_by_class_name('ApplyClass')
    enter.send_keys(Keys.RETURN)

    select = Select(browser.find_element_by_name('ddlMunic'))
    select.select_by_value(swis)
    first = browser.find_element_by_name("txtFirstOwner")
    first.send_keys(args.first_name)
    last = browser.find_element_by_name("txtLastOwner")
    last.send_keys(args.last_name)
    first = browser.find_element_by_name("txtFirstOwner")
    submit = browser.find_element_by_id("btnSearch")
    submit.send_keys(Keys.RETURN)
    # more than 1? 
    # browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search OC parcel database')
    parser.add_argument("swis")
    # parser.add_argument("pin")
    parser.add_argument("last_name")
    parser.add_argument("first_name")
    args = parser.parse_args()
    show_tax_info()
