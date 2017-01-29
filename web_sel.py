#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse


def show_tax_info():
    swis = args.swis[:4]
    browser = webdriver.Firefox()
    # browser = webdriver.PhantomJS()
    browser.implicitly_wait(10)  # seconds
    browser.get('http://www.co.orange.ny.us/content/124/1368/4136.aspx')
    enter = browser.find_element_by_class_name('ApplyClass')
    enter.send_keys(Keys.RETURN)

    select = Select(browser.find_element_by_name('ddlMunic'))
    select.select_by_value(swis)
    print_key = browser.find_element_by_name("txtTaxMapNum")
    print_key.send_keys(args.print_key)
    submit = browser.find_element_by_id("btnSearch")
    submit.send_keys(Keys.RETURN)
    WebDriverWait(browser, 10)
    print(browser.title)
    try:
        WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.ID, "pnlRTaxID"))
                )
        assert(EC.title_contains("Details"))
    finally:
        print(browser.page_source)
        browser.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search OC parcel database')
    parser.add_argument("swis")
    parser.add_argument("print_key")
    args = parser.parse_args()
    show_tax_info()
