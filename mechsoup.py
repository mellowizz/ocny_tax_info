#!/usr/bin/python

""" Python3 compatible """

import argparse
import mechanicalsoup

def has_class_but_no_id(tag):
        return tag.has_attr('class') and not tag.has_attr('id')

def show_tax_info():

    br = mechanicalsoup.Browser()

    page = br.get('http://www.co.orange.ny.us/content/124/1368/4136.aspx')
    # page = br.get('http://propertydata.orangecountygov.com/search.aspx')
    # form.find("select", {"name": "ddlMunic"})["value"] = swis
    # swis = str(args.pin)[:4]
    # printkey = str(args.pin)[6:]
    # print(printkey)
    # print(swis)
    # form.find("a", {"class": "ApplyClass"})["value"
    # form.find("select", {"name": "ddlMunic"})["value"] = swis
    # form.find("input", {"name": "txtTaxMapNum"})["value"] = printkey
    # "option", text="Transaction Statement")["value"]`
    form = None
    for tag in page.soup.find_all(has_class_but_no_id):
        if tag.get('href') and 'cty=33' in tag.get('href'):
            page = br.get(tag.get('href'))
    form = page.soup.form
    if form:
        form.find("select", {"name": "ddlMunic"}).option["value"] = args.swis
        form.find("input", {"name": "txtLastOwner"})["value"] = args.last_name
        form.find("input", {"name": "txtFirstOwner"})["value"] = args.first_name
 
    response = br.submit(form, page.url)
    print(response.content)
    '''
    json = response.json()
    data = json["form"]
    assert data["txtLastOwner"] == "Moran"
    assert data["txtFirstOwner"] == "John"
    assert data["ddlMunic"] == "3324"
    '''


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search OC parcel database')
    # parser.add_argument("pin")
    parser.add_argument("swis")
    parser.add_argument("last_name")
    parser.add_argument("first_name")
    args = parser.parse_args()
    show_tax_info()
