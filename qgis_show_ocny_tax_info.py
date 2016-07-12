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

    url = 'http://propertydata.orangecountygov.com/imate/propdetail.aspx'

    # first 4 of PIN are town code:  str(pin)[0:4] 
    # search = '/'.join([BASE_URL, 'viewlist.aspx?sort=printkey&swis={tcode}'])

    # get cookie
    br.open('http://www.co.orange.ny.us/content/124/1368/4136.aspx')

    for link in br.links():
        if 'index.aspx' in link.url:
            br.follow_link(link)
            break

    swis = str(pin)[:6]
    printkey = str(pin)[6:]
    search_terms = 'swis={}&printkey={}'.format(swis, printkey)
    full_url = '?'.join([url, search_terms])

    response = br.open(full_url)
    return response.read()
