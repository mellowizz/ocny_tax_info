#!/usr/bin/python2

import sys
import mechanize 
import cookielib
import io
import shutil

br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
swis = sys.argv[1]
pin = sys.argv[2]

BASE_URL = 'http://propertydata.orangecountygov.com/imate'

# http://propertydata.orangecountygov.com/imate/viewlist.aspx?sort=printkey&swis=3311

# get cookie
towncode = str(swis)[0:4]

search = '/'.join([BASE_URL, 'viewlist..aspx?sort=printkey&swis={towncode}'])

br.open('http://www.co.orange.ny.us/content/124/1368/4136.aspx')

for link in br.links():
    if 'index.aspx' in link.url:
        br.follow_link(link)
        print("FOUND")
        break
    else:
        print("ERROR! Could not find link!")

# SWS = 332489; first four are town code
# 02200000090030000000

printkey = str(pin).strip(str(swis))
SEARCH_URL = ''.join([BASE_URL, '/propdetail.aspx?'])
prop_search = '&'.join(['swis={}'.format(swis), 'printkey={}'.format(printkey)])
full_url = SEARCH_URL + prop_search
print(full_url)

response = br.open(full_url)
#print(response.read())

with open('.'.join([pin, 'html']), 'wb') as html:
    html.write(response.read())
#if sys.version < '3':
#    infile = io.open('.'.join([pin, 'html']), 'w+')
#else:
#    infile = io.open('.'.join([pin, 'html']), 'w+')

# with infile as html:
    # html.write(response.read())
    # response.raw.decode_content = True
    # shutil.copyfileobj(response.read(), html)
