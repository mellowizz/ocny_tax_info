#!/usr/bin/python2
#from qgis.core import *
#from qgis.gui import *
from __future__ import print_function
import mechanize
import cookielib
import sys

def eprint(*args, **kwargs):
        print(*args, file=sys.stderr, **kwargs)

#def show_tax_info(pin):
def show_tax_info(last, first):

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

    #url = 'http://propertydata.orangecountygov.com/imate/propdetail.aspx'
    url ='http://propertydata.orangecountygov.com/imate/viewlist.aspx?sort=prinkey&swis=all'

    # first 4 of PIN are town code:  str(pin)[0:4]
    # search = '/'.join([BASE_URL, 'viewlist.aspx?sort=printkey&swis={tcode}'])

    # get cookie

    useragent = [('User-agent',
                  ("Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 "
                   "Firefox/49.0"))]
    br.addheaders = useragent
    br.open('http://www.co.orange.ny.us/content/124/1368/4136.aspx')

    for link in br.links():
        #print("br links: {}".format(''.join(br.links())))
        if 'index.aspx' in link.url:
            br.follow_link(link)
            break

    #swis = str(pin)[0:6]
    #printkey = str(pin)[6:]
    #printkey = str(pin).strip(str(swis))
    #search_terms = 'swis={}&printkey={}'.format(swis, printkey)
    search_terms = '&ownernamel={}&ownernamef={}'.format(last,
                                                                         first)
    full_url = ''.join([url, search_terms])
    #eprint("full url: {}".format(full_url))

    response = br.open(full_url)
    return response.read()

if __name__ == "__main__":
    print(show_tax_info(sys.argv[1],sys.argv[2]))
