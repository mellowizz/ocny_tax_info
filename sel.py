#!/usr/bin/python2

''' sel.py
  Written by Niklas Moran
  niklas@niklasmoran.com
  Released under GPL.
'''

import sys
from seleniumrequests import Firefox
# from selenium import webdriver


swis = sys.argv[1]
pin = sys.argv[2]

BASE_URL = 'http://propertydata.orangecountygov.com/imate'

# http://propertydata.orangecountygov.com/imate/viewlist.aspx?sort=printkey&swis=3311

# get this cookie:
cookie_url = 'http://www.co.orange.ny.us/content/124/1368/4136.aspx'

towncode = str(swis)[0:4]
search = '/'.join([BASE_URL, 'viewlist..aspx?sort=printkey&swis={towncode}'])

# SWS = 332489; first four are town code
# 02200000090030000000

printkey = str(pin).strip(str(swis))
SEARCH_URL = ''.join([BASE_URL, '/propdetail.aspx?'])
prop_search = '&'.join(['swis={}'.format(swis),
                        'printkey={}'.format(printkey)])
full_url = SEARCH_URL + prop_search

# create driver
driver = Firefox()
driver.get(cookie_url)
link = driver.find_element_by_class_name('ApplyClass')
link.click()
response = driver.get(full_url)
response = driver.request('GET', full_url)
print(response)

# driver.save_screenshot(''.join([pin,'.png']))
# property_info = driver.find_element_by_id('pnlRTaxID')
# property_info.screenshot(''.join([pin,'.png']))
