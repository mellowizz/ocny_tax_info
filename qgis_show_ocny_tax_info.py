"""
Define new functions using @qgsfunction. feature and parent must always be the
last args. Use args=-1 to pass a list of values as arguments
"""

from qgis.core import *
from qgis.gui import *
import mechanize 
import cookielib

@qgsfunction(args='auto', group='Custom')
def show_tax_info(pin, feature, parent):

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

    BASE_URL = 'http://propertydata.orangecountygov.com/imate'

    towncode = str(pin)[0:4]
    # SWIS is 6 digits- 
    # first 4 are town code
    # get cookie
    search = '/'.join([BASE_URL, 'viewlist..aspx?sort=printkey&swis={towncode}'])

    br.open('http://www.co.orange.ny.us/content/124/1368/4136.aspx')

    for link in br.links():
        if 'index.aspx' in link.url:
            br.follow_link(link)
            break

    swis = str(pin)[0:6]
    printkey = str(pin).strip(str(swis))
    SEARCH_URL = ''.join([BASE_URL, '/propdetail.aspx?'])
    prop_search = '&'.join(['swis={}'.format(swis), 'printkey={}'.format(printkey)])
    full_url = SEARCH_URL + prop_search
    # print(full_url)

    response = br.open(full_url)
    # with open('.'.join([pin, 'html']), 'wb') as html:
    return response.read()